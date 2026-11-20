# Guided interaction

How this skill talks to the user. The user may not know the planning vocabulary, so guide them one step at a time instead of asking for a finished input.

## Contents

- [Turn pattern](#1-turn-pattern)
- [Question types](#2-question-types)
- [Pacing and progress](#3-pacing-and-progress)
- [When the user does not know](#4-when-the-user-does-not-know)
- [Confirmation before writing](#5-confirmation-before-writing)
- [Ending a turn](#6-ending-a-turn)

## 1. Turn pattern

1. Say in one sentence where we are and what this step is for.
2. Ask one or two questions, in plain language, with an example.
3. When there is a clear best choice, make it the first option and mark it `(Recommended)`.
4. Use the host's structured question tool if it has one; otherwise show the same numbered options in text.
5. Wait for the answer. Do not answer your own questions or assume the default silently.

## 2. Question types

| Use | When | Rules |
|---|---|---|
| Numbered menu | 3–6 clear options | Recommended option first; always end with `Other (describe)` |
| Open question | Facts only the user knows | One at a time, with an example: "e.g., the registry clerks and the sheriffs" |
| Smart default | One obvious answer | "I suggest X. Keep it? (yes / change)" |
| Yes or no | A real two-way choice, such as a write | Only when there are exactly two options |
| Table choice | Options differ on several points | Compare briefly, then ask which one |

Introduce any technical term (for example, a TOGAF phase or a plateau) with a one-line plain meaning the first time it appears.

## 3. Pacing and progress

- Never ask more than two questions in a turn, and never present a form.
- Show progress in long flows: "Step 2 of 5: who is affected".
- If the user pastes a lot, summarize what you understood in a short table and ask only about the gaps.
- Let the user jump: if they answer a later question early, take it and move on.
- Keep each turn short enough to read in a minute.

## 4. When the user does not know

"I don't know" is a valid answer. Record it as an open item (`Unvalidated assumption`, `Baseline needed`, `Capacity unconfirmed`, or an open question), say what would resolve it and who could answer, and continue. Do not invent a value to fill the gap, and do not block the flow.

## 5. Confirmation before writing

Before any write, change, promotion, deletion or commitment, show a recap and ask:

```text
Here is what I will save:
[short table of the records and changes]

1. Yes, save it (Recommended)
2. Adjust something
3. Show me the full preview first
```

Only a clear yes proceeds. Anything else returns to the step. After saving, say what changed and where.

## 6. Ending a turn

End every turn with the next question or a numbered choice of next steps. When a flow completes, offer a short menu: continue to the next step, work on something else, or stop here. Never end with a statement that leaves the user wondering what to do.
