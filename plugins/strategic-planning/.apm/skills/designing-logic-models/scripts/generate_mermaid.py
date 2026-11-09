#!/usr/bin/env python3
"""
Generate accessible, B.C. Government Design System-compliant Mermaid flowcharts
for logic models, results chains, and theories of change.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class LogicStage:
    """Represents a single stage in a logic model."""
    id: str
    title: str
    subtitle: str
    items: List[str]
    css_class: str


@dataclass
class LogicModel:
    """Complete logic model definition."""
    layout: str = "TB"  # 'TB' or 'LR'
    style_mode: str = "classDef"  # 'classDef' or 'style'
    wrapping_width: Optional[int] = None
    min_node_width: Optional[int] = None
    need: Optional[LogicStage] = None
    inputs: Optional[LogicStage] = None
    activities: Optional[LogicStage] = None
    outputs: Optional[LogicStage] = None
    immediate_outcomes: Optional[LogicStage] = None
    intermediate_outcomes: Optional[LogicStage] = None
    long_term_outcomes: Optional[LogicStage] = None


BC_GOV_PALETTE = {
    "need": {"fill": "#F4F4F4", "stroke": "#555555", "color": "#111111"},
    "input": {"fill": "#E8F1FA", "stroke": "#2B6EA6", "color": "#111111"},
    "activity": {"fill": "#E5F3F3", "stroke": "#258080", "color": "#111111"},
    "output": {"fill": "#E9F4E4", "stroke": "#518A3A", "color": "#111111"},
    "immediate": {"fill": "#FFF4D6", "stroke": "#C49102", "color": "#111111"},
    "intermediate": {"fill": "#FCE8D5", "stroke": "#C76B19", "color": "#111111"},
    "longterm": {"fill": "#F3E5F5", "stroke": "#7B4B94", "color": "#111111"},
}


def sanitize_label(text: str) -> str:
    """Escape characters that break Mermaid syntax and normalize quotes."""
    return text.replace('"', "'").strip()


def format_node_label(stage: LogicStage) -> str:
    """Format node label with title, subtitle, and items separated by HTML breaks."""
    lines: List[str] = [f"<b>{sanitize_label(stage.title)}</b>"]
    if stage.subtitle:
        lines.append(f"<i>{sanitize_label(stage.subtitle)}</i>")
    if stage.items:
        lines.append("")
        for item in stage.items:
            lines.append(sanitize_label(item))
    return "<br/>".join(lines)


def generate_mermaid(model: LogicModel) -> str:
    """Generate clean Mermaid flowchart syntax with configurable node widths."""
    wrap_w = model.wrapping_width or (450 if model.layout == "TB" else 260)
    min_w = model.min_node_width or (350 if model.layout == "TB" else 220)
    init_directive = f'%%{{init: {{"flowchart": {{"wrappingWidth": {wrap_w}, "minNodeWidth": {min_w}}}}} }}%%'
    out: List[str] = [init_directive, f"flowchart {model.layout}", ""]

    stages: List[LogicStage] = []
    if model.need:
        stages.append(model.need)
    if model.inputs:
        stages.append(model.inputs)
    if model.activities:
        stages.append(model.activities)
    if model.outputs:
        stages.append(model.outputs)
    if model.immediate_outcomes:
        stages.append(model.immediate_outcomes)
    if model.intermediate_outcomes:
        stages.append(model.intermediate_outcomes)
    if model.long_term_outcomes:
        stages.append(model.long_term_outcomes)

    # 1. Node definitions
    for s in stages:
        label = format_node_label(s)
        out.append(f'{s.id}["{label}"]')
        out.append("")

    # 2. Transition links
    transitions = [
        ("N", "I", "justifies"),
        ("I", "A", "enables"),
        ("A", "O", "produces"),
        ("O", "IO", "leads to"),
        ("IO", "MO", "contributes to"),
        ("MO", "LO", "contributes to"),
    ]
    stage_ids = {s.id for s in stages}
    for src, dst, verb in transitions:
        if src in stage_ids and dst in stage_ids:
            out.append(f'{src} -->|"{verb}"| {dst}')
    out.append("")

    # 3. Styling definitions
    if model.style_mode == "classDef":
        for name, col in BC_GOV_PALETTE.items():
            out.append(f'classDef {name} fill:{col["fill"]},stroke:{col["stroke"]},color:{col["color"]}')
        out.append("")
        for s in stages:
            out.append(f"class {s.id} {s.css_class}")
    else:
        for s in stages:
            col = BC_GOV_PALETTE.get(s.css_class, {"fill": "#FFFFFF", "stroke": "#333333"})
            out.append(f'style {s.id} fill:{col["fill"]},stroke:{col["stroke"]},stroke-width:2px')

    return "\n".join(out)


def get_preset_need_driven() -> LogicModel:
    """Top-to-bottom court modernization logic model driven by Program Need."""
    return LogicModel(
        layout="TB",
        style_mode="classDef",
        need=LogicStage(
            id="N",
            title="PROGRAM NEED",
            subtitle="Current operational bottlenecks",
            items=[
                "Court processes remain manual,",
                "high-touch and fragmented.",
                "Validation often occurs late.",
                "Digital evidence is hard to manage.",
                "Policy changes require manual effort.",
            ],
            css_class="need",
        ),
        inputs=LogicStage(
            id="I",
            title="INPUTS",
            subtitle="What we invest",
            items=[
                "Program funding",
                "Court policy and expertise",
                "CSO and CEIS services",
                "BC Court Assistant",
                "CITZ shared IDP capability",
                "Azure and OpenShift platforms",
                "Verified credentials",
                "Security and privacy controls",
            ],
            css_class="input",
        ),
        activities=LogicStage(
            id="A",
            title="ACTIVITIES",
            subtitle="What we do",
            items=[
                "Encode policy rules",
                "Build pre-flight validation",
                "Configure data extraction",
                "Set confidence thresholds",
                "Integrate results with CEIS",
                "Enable self-service authoring",
                "Digitize exhibit management",
                "Expose governed APIs",
                "Implement credential access",
            ],
            css_class="activity",
        ),
        outputs=LogicStage(
            id="O",
            title="OUTPUTS",
            subtitle="What we produce",
            items=[
                "Validation portal and API",
                "Machine-readable rule schemas",
                "Validation tokens",
                "Extracted fields and scores",
                "Human-review routing",
                "Form-authoring tools",
                "Digital-exhibit service",
                "External filing APIs",
                "Credential-based access",
            ],
            css_class="output",
        ),
        immediate_outcomes=LogicStage(
            id="IO",
            title="IMMEDIATE OUTCOMES",
            subtitle="What changes first",
            items=[
                "Earlier client feedback",
                "Problems detected sooner",
                "Structured registry data",
                "Faster rule updates",
                "Secure digital access",
                "Less removable-media handling",
                "More traceable decisions",
            ],
            css_class="immediate",
        ),
        intermediate_outcomes=LogicStage(
            id="MO",
            title="INTERMEDIATE OUTCOMES",
            subtitle="What changes next",
            items=[
                "Fewer rejected filings",
                "Better first-time accuracy",
                "Less manual processing",
                "Faster service delivery",
                "More consistent enforcement",
                "Lower vendor dependence",
                "Fewer counter visits",
                "Safer information handling",
            ],
            css_class="intermediate",
        ),
        long_term_outcomes=LogicStage(
            id="LO",
            title="LONG-TERM OUTCOMES",
            subtitle="Ultimate impact",
            items=[
                "More accessible court services",
                "More timely court services",
                "Reliable court administration",
                "Sustainable digital delivery",
                "Protected judicial information",
                "Improved access to justice",
                "Fully digital court processes",
            ],
            css_class="longterm",
        ),
    )


def get_preset_canonical_lr() -> LogicModel:
    """Left-to-right public service digital transformation logic model."""
    return LogicModel(
        layout="LR",
        style_mode="style",
        inputs=LogicStage(
            id="I",
            title="INPUTS",
            subtitle="What we invest",
            items=["Program funding", "Staff and expertise", "Technology platform", "Existing service data"],
            css_class="input",
        ),
        activities=LogicStage(
            id="A",
            title="ACTIVITIES",
            subtitle="What we do",
            items=["Map current services", "Redesign processes", "Build digital services", "Train staff"],
            css_class="activity",
        ),
        outputs=LogicStage(
            id="O",
            title="OUTPUTS",
            subtitle="What we produce",
            items=["New online services", "Redesigned processes", "Staff trained", "Guidance and tools published"],
            css_class="output",
        ),
        immediate_outcomes=LogicStage(
            id="IO",
            title="IMMEDIATE OUTCOMES",
            subtitle="What changes first",
            items=[
                "Staff gain new capabilities",
                "Services are easier to access",
                "More transactions are digital",
                "Better service data is available",
            ],
            css_class="immediate",
        ),
        intermediate_outcomes=LogicStage(
            id="MO",
            title="INTERMEDIATE OUTCOMES",
            subtitle="What changes next",
            items=[
                "Faster service delivery",
                "Fewer manual processes",
                "Lower administrative effort",
                "Improved client experience",
                "Better evidence-based decisions",
            ],
            css_class="intermediate",
        ),
        long_term_outcomes=LogicStage(
            id="LO",
            title="LONG-TERM OUTCOMES",
            subtitle="Ultimate impact",
            items=[
                "More accessible public services",
                "Better outcomes for citizens",
                "More efficient government",
                "Sustainable digital services",
            ],
            css_class="longterm",
        ),
    )


def parse_json_input(data: Dict[str, Any]) -> LogicModel:
    """Parse a dictionary or JSON payload into a LogicModel."""
    layout = data.get("layout", "TB")
    style_mode = data.get("style_mode", "classDef")

    def make_stage(key: str, default_id: str, default_title: str, default_class: str) -> Optional[LogicStage]:
        raw = data.get(key)
        if not raw:
            return None
        return LogicStage(
            id=raw.get("id", default_id),
            title=raw.get("title", default_title),
            subtitle=raw.get("subtitle", ""),
            items=raw.get("items", []),
            css_class=raw.get("css_class", default_class),
        )

    return LogicModel(
        layout=layout,
        style_mode=style_mode,
        need=make_stage("need", "N", "PROGRAM NEED", "need"),
        inputs=make_stage("inputs", "I", "INPUTS", "input"),
        activities=make_stage("activities", "A", "ACTIVITIES", "activity"),
        outputs=make_stage("outputs", "O", "OUTPUTS", "output"),
        immediate_outcomes=make_stage("immediate_outcomes", "IO", "IMMEDIATE OUTCOMES", "immediate"),
        intermediate_outcomes=make_stage("intermediate_outcomes", "MO", "INTERMEDIATE OUTCOMES", "intermediate"),
        long_term_outcomes=make_stage("long_term_outcomes", "LO", "LONG-TERM OUTCOMES", "longterm"),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate B.C. Gov Design System Mermaid Logic Model diagrams.")
    parser.add_argument("--preset", choices=["need-driven", "canonical-lr"], help="Use built-in reference preset.")
    parser.add_argument("--input", type=Path, help="Path to JSON file defining the logic model.")
    parser.add_argument("--layout", choices=["TB", "LR"], default=None, help="Override flowchart direction (TB or LR).")
    parser.add_argument("--style", choices=["classDef", "style"], default=None, help="Styling syntax mode.")
    parser.add_argument("--wrapping-width", type=int, default=None, help="Maximum text wrapping width in pixels (e.g., 450).")
    parser.add_argument("--min-node-width", type=int, default=None, help="Minimum node box width in pixels (e.g., 350).")
    parser.add_argument("--output", type=Path, help="Write output to file instead of stdout.")
    parser.add_argument("--raw", action="store_true", help="Omit ```mermaid markdown code fence.")

    args = parser.parse_args()

    if args.preset == "need-driven":
        model = get_preset_need_driven()
    elif args.preset == "canonical-lr":
        model = get_preset_canonical_lr()
    elif args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
        model = parse_json_input(data)
    else:
        # Default fallback to need-driven preset
        model = get_preset_need_driven()

    if args.layout:
        model.layout = args.layout
    if args.style:
        model.style_mode = args.style
    if args.wrapping_width:
        model.wrapping_width = args.wrapping_width
    if args.min_node_width:
        model.min_node_width = args.min_node_width

    diagram = generate_mermaid(model)
    rendered = diagram if args.raw else f"```mermaid\n{diagram}\n```"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Generated Mermaid diagram saved to {args.output}")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
