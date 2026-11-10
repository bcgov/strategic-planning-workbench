#!/usr/bin/env python3
"""Regression checks for the investment scoring scripts.

Run after changing generate_investment_quadrant.py, interactive_investment_app.py or the ledger templates:
    python scripts/test_investment_scripts.py
Covers lossless CSV round trips, null-safe commitment evidence, the Q1 safeguard, zero scores,
HTML escaping, JavaScript syntax (needs node) and saved scoring weights.
"""
import sys, os, json, csv, subprocess, time, urllib.request, shutil, importlib.util, re, tempfile
skill=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode=True
S=os.path.join(skill,'scripts'); T=os.path.join(skill,'assets','templates')
sp=tempfile.mkdtemp(prefix='investment-test-')
def load(name,fn):
    spec=importlib.util.spec_from_file_location(name,os.path.join(S,fn)); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
g=load('gen','generate_investment_quadrant.py')
app=load('app','interactive_investment_app.py')
ok=True
def check(label,cond,detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ')+label+(' '+str(detail) if detail and not cond else '')); ok=ok and bool(cond)

items=json.load(open(os.path.join(T,'investment-scoring-ledger.json'),encoding='utf-8'))
fw=json.load(open(os.path.join(T,'investment-scoring-framework.json'),encoding='utf-8'))
framework=g.copy.deepcopy(g.DEFAULT_FRAMEWORK)
scored=g.calculate_scores(items,framework)
by={x['id']:x for x in scored}

# 1 lossless CSV round trip incl. history (generator)
for x in scored: g.add_snapshot(x,'2026-11-10','Tester',framework)
p=os.path.join(sp,'rt.csv'); g.export_csv(scored,p)
back=g.calculate_scores(g.load_data(p),framework); bb={x['id']:x for x in back}
check('generator CSV round trip keeps composite', all(abs(bb[i]['composite_score']-by[i]['composite_score'])<0.01 for i in by), {i:(bb[i]['composite_score'],by[i]['composite_score']) for i in by})
check('generator CSV round trip keeps history', all(len(bb[i].get('score_history',[]))==1 for i in by))
check('generator CSV round trip keeps lifecycle fields', bb['INV-001']['owner']==by['INV-001']['owner'] and bb['INV-001']['related_idea_id']=='IDEA-012')

# 2 interactive app CSV round trip + framework persistence
ap=os.path.join(sp,'app-rt.json'); json.dump(scored,open(ap,'w',encoding='utf-8'))
fwx=app.load_framework(ap); fwx['value_weights']['drivers']=40.0; fwx['version']='custom-test'
app.save_dataset(ap,scored,fwx)
reloaded=app.load_dataset(ap.replace('.json','.csv')); rr={x['id']:x for x in g.calculate_scores(reloaded,framework)}
check('app CSV round trip keeps composite', all(abs(rr[i]['composite_score']-by[i]['composite_score'])<0.01 for i in by))
check('app CSV round trip keeps history', all(len(rr[i].get('score_history',[]))==1 for i in by))
f2=app.load_framework(ap)
check('app persists and reloads weights', f2['value_weights']['drivers']==40.0 and f2.get('version')=='custom-test', f2)

# 3 null / placeholder evidence is not evidence
bad={'sponsor':None,'approval_date':None,'owner':None,'capacity_confirmed':True,'capacity_source':None}
check('null evidence is not committable', g.commitment_status(bad)[0]!='Committable', g.commitment_status(bad))
bad2={'sponsor':'Director','approval_date':'2026-10-01','owner':'TBD','capacity_confirmed':'true','capacity_source':'None'}
check('placeholder owner and source are not evidence', g.commitment_status(bad2)[0]!='Committable', g.commitment_status(bad2))
good={'sponsor':'Director','approval_date':'2026-10-01','owner':'A. Owner','capacity_confirmed':'true','capacity_source':'ASG-007'}
check('complete evidence is committable', g.commitment_status(good)[0]=='Committable')

# 4 stale recommendation cannot override the safeguard
it=json.loads(json.dumps(items[0])); it['capacity_confirmed']='false'; it['capacity_source']=''
r=g.calculate_scores([it],framework)[0]
check('Q1 without capacity holds as decision gate', r['commitment_status']=='Capacity unconfirmed' and 'Hold as a decision gate' in r['recommended_action'], r['recommended_action'])
check('human note preserved separately', r['recommendation']==items[0]['recommendation'] and 'Planning note' in r['recommended_action'])
md=g.render_markdown([r],framework)
check('markdown shows the safeguard, not the stale note alone', 'Hold as a decision gate' in md)

# 5 JS: zero scores, escaping, syntax
html=app.HTML_DASHBOARD
check('no "|| 5.0" score defaults left', '|| 5.0' not in html)
check('nullish defaults used', html.count('?? 5.0')>=9)
raw=[m for m in re.findall(r'\$\{item\.(?:name|id|sponsor|quadrant)\b[^}]*\}',html) if not m.startswith('${esc(')]
unsafe=[m for m in raw if 'toFixed' not in m]
innerhtml_lines=[l for l in html.split('\n') if re.search(r'\$\{item\.(name|id|sponsor|quadrant)\b',l)]
check('item text interpolations are escaped', all('esc(' in l or 'item.name + ' in l or 'matchText' in l or '.toLowerCase()' in l for l in innerhtml_lines), [l.strip()[:80] for l in innerhtml_lines if 'esc(' not in l][:3])
m=re.search(r'<script>(.*?)</script>',html,re.S)
jsfile=os.path.join(sp,'dash.js'); open(jsfile,'w',encoding='utf-8').write(m.group(1))
if shutil.which('node'):
    res=subprocess.run(['node','--check',jsfile],capture_output=True,text=True)
    check('dashboard JavaScript parses', res.returncode==0, res.stderr[:300])
else:
    print('SKIP dashboard JavaScript syntax check (node not installed)')

# 6 end to end server: framework survives restart; save requires nothing else
led=os.path.join(sp,'srv-ledger.json'); shutil.copy(os.path.join(T,'investment-scoring-ledger.json'),led)
for ext in ('.framework.json','.csv'):
    q=led.replace('.json',ext)
    if os.path.exists(q): os.remove(q)
def start(port):
    p=subprocess.Popen([sys.executable,'-B',os.path.join(S,'interactive_investment_app.py'),'-i',led,'-p',str(port),'--no-browser'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for _ in range(40):
        try: return p,json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/api/data',timeout=2))
        except Exception: time.sleep(0.25)
    p.kill(); raise SystemExit('server did not start')
p1,d1=start(8793)
try:
    d1['framework']['value_weights']['drivers']=10.0
    req=urllib.request.Request('http://127.0.0.1:8793/api/save',data=json.dumps({'items':d1['items'],'framework':d1['framework']}).encode(),headers={'Content-Type':'application/json'})
    st=json.load(urllib.request.urlopen(req,timeout=3))
finally:
    p1.terminate(); p1.wait(timeout=3)
p2,d2=start(8794)
try:
    check('weights survive a server restart', d2['framework']['value_weights']['drivers']==10.0, d2['framework']['value_weights'])
finally:
    p2.terminate(); p2.wait(timeout=3)
# ---- second review round: evidence types, dashboard logic, framework schema ----
bool_bad={'sponsor':False,'approval_date':False,'owner':False,'capacity_confirmed':True,'capacity_source':False}
check('boolean false is not evidence', g.commitment_status(bool_bad)[0]!='Committable', g.commitment_status(bool_bad))
bad_date={'sponsor':'Director','approval_date':'sometime soon','owner':'A. Owner','capacity_confirmed':'true','capacity_source':'ASG-007'}
check('invalid approval date is not evidence', g.commitment_status(bad_date)[0]!='Committable', g.commitment_status(bad_date))
check('impossible calendar date is not evidence', g.commitment_status(dict(bad_date,approval_date='2026-02-31'))[0]!='Committable')

# generator reads the flat framework schema that the dashboard saves
flat=app.framework_path(ap)
fw_loaded=g.load_framework_file(flat)
check('generator honours dashboard-saved weights', fw_loaded['value_weights']['drivers']==40.0 and fw_loaded.get('version')=='custom-test', fw_loaded)
fw_axes=g.load_framework_file(os.path.join(T,'investment-scoring-framework.json'))
check('generator still reads the axes template', abs(sum(fw_axes['value_weights'].values())-100)<0.01)

# invalid framework files are reported, not silently replaced
for label,content in [('null','null'),('array','[]'),('malformed','{not json')]:
    q=os.path.join(sp,f'bad-{label}.json'); open(q,'w').write('[]')
    open(app.framework_path(q),'w').write(content)
    try:
        app.load_framework(q); check(f'invalid framework ({label}) is rejected', False)
    except ValueError:
        check(f'invalid framework ({label}) is rejected', True)

# dashboard logic executed in node
if shutil.which('node'):
    def grab(name):
        m=re.search(r'        function '+name+r'\(.*?\n        \}\n',html,re.S); assert m,name; return m.group(0)
    funcs=''.join(grab(n) for n in ['hasValue','validDate','isTrue','weightsHash','applySaveSnapshots','commitmentStatus','recommendedAction'])
    js=funcs+r'''
const out = {};
out.badDate = commitmentStatus({sponsor:'Director', approval_date:'not a date', owner:'A', capacity_confirmed:'true', capacity_source:'ASG-1'});
out.boolOwner = commitmentStatus({sponsor:'Director', approval_date:'2026-10-01', owner:false, capacity_confirmed:true, capacity_source:'ASG-1'});
out.good = commitmentStatus({sponsor:'Director', approval_date:'2026-10-01', owner:'A', capacity_confirmed:'true', capacity_source:'ASG-1'});
const q1 = {qCode:'Q1', recommendation:'Fund now', commitment_status:'Capacity unconfirmed', commitment_missing:['confirmed capacity with source']};
out.action = recommendedAction(q1);
out.actionOk = recommendedAction({qCode:'Q2', recommendation:'', commitment_status:'Committable', commitment_missing:[]});
const base = [{id:'A', scores:{drivers:8}, scored_on:'2026-01-01', scored_by:'X', value_score:8, delivery_score:6, composite_score:7, quadrant:'Q1'}];
const items = [{id:'A', scores:{drivers:5}, value_score:3.43, composite_score:3.43}];
applySaveSnapshots(items, base, {fwChanged:true, loadedVersion:'default', loadedWeights:{value_weights:{drivers:25}}, today:'2026-11-10'});
out.snap = items[0].score_history;
const items2 = [{id:'A', scores:{drivers:8}}];
applySaveSnapshots(items2, base, {fwChanged:false, loadedVersion:'default', loadedWeights:{}, today:'2026-11-10'});
out.noChange = items2[0].score_history || null;
out.h1 = weightsHash({overall_weights:{value_weight:50}, value_weights:{drivers:25}, delivery_weights:{}, threshold_x:5, threshold_y:5});
out.h2 = weightsHash({overall_weights:{value_weight:50}, value_weights:{drivers:30}, delivery_weights:{}, threshold_x:5, threshold_y:5});
console.log(JSON.stringify(out));
'''
    jp=os.path.join(sp,'logic.js'); open(jp,'w',encoding='utf-8').write(js)
    r=subprocess.run(['node',jp],capture_output=True,text=True)
    if r.returncode!=0:
        check('dashboard logic runs in node', False, r.stderr[:300])
    else:
        o=json.loads(r.stdout)
        check('JS: invalid date is not evidence', 'sponsor approval date' in o['badDate']['missing'], o['badDate'])
        check('JS: boolean owner is not evidence', 'owner' in o['boolOwner']['missing'], o['boolOwner'])
        check('JS: complete evidence is committable', o['good']['status']=='Committable', o['good'])
        check('JS: Q1 without capacity recomputes the safeguarded action', 'Hold as a decision gate' in o['action'] and 'Planning note: Fund now' in o['action'], o['action'])
        check('JS: action default used when no note', o['actionOk']=='Fund phased discovery & de-risking', o['actionOk'])
        sn=o['snap']
        check('JS: weights plus score edit gives one snapshot of the OLD values and framework', len(sn)==1 and sn[0]['framework']=='default' and sn[0]['composite_score']==7 and sn[0]['value_score']==8 and 'weights' in sn[0], sn)
        check('JS: no change, no snapshot', o['noChange'] is None, o['noChange'])
        check('JS: different weights get different version hashes', o['h1']!=o['h2'], (o['h1'],o['h2']))

print('ALL PASS' if ok else 'SOME FAILED')
sys.exit(0 if ok else 1)
