---
name: gemini-json-persona
description: Create a reusable personal context package from a Gemini compact JSON export. Use this skill when the user wants to infer a person's profile, memory, meta document, LLM context, or TELOS-style personal context from a standardized JSON export produced from Gemini activity/conversation history.
metadata:
  short-description: Extract persona docs from Gemini JSON
---

# Gemini Json Persona

## Overview

Use this skill to turn a standardized Gemini compact JSON export into three reusable artifacts:

- `meta-moi.md`: structured profile with confidence levels
- `llm-context-<name>.md`: compact context for future LLMs
- `personal_telos_<name>.md`: TELOS-style personal context

This skill assumes the input JSON follows the structure produced by `gemini_activity_to_json.py`, with fields such as `stats`, `conversation_groups`, and `items`.

## Workflow

1. Inspect the JSON with `scripts/inspect_compact_json.py`.
2. Read only the most relevant slices of the JSON:
   - `stats`
   - selected `conversation_groups`
   - selected `items` tied to recurring themes
3. Infer only what is stable or strongly repeated.
4. Separate:
   - high-confidence facts
   - medium-confidence inferences
   - low-confidence hypotheses
5. Produce the three output documents using the templates in `references/output-templates.md`.

## Input Contract

Expect a JSON file with this general shape:

```json
{
  "stats": {},
  "conversation_groups": [],
  "items": []
}
```

Important expected item fields:

- `datetime_utc`
- `conversation_group_id`
- `prompt`
- `response`
- `preview`

If the JSON shape differs materially from this format, say so and adapt carefully instead of pretending compatibility.

## Inference Rules

- Do not overclaim.
- Treat repeated direct self-statements as stronger than topical curiosity.
- Distinguish stable traits from temporary moods, exploratory questions, or one-off opinions.
- Treat political, cultural, medical, and emotional interpretations with extra caution.
- Prefer wording like `semble`, `probablement`, `à confirmer` when confidence is not high.
- If the user wants a context file for LLMs, optimize for helpful defaults, not psychoanalysis.

## Output Rules

### `meta-moi.md`

Use this for the richest, most explicit profile.

Include:

- confidence scale
- work identity
- personal context
- technical preferences
- cognitive style
- collaboration preferences
- things to avoid
- open questions
- source conversation IDs

### `llm-context-<name>.md`

Use this as the most practical artifact.

Include:

- language preferences
- who the person is
- stable defaults
- project/work context
- how to help best
- what to avoid
- compact summary

Keep it short and operational.

### `personal_telos_<name>.md`

Map the profile into a TELOS-like structure:

- History
- Problems
- Mission
- Narratives
- Goals
- Challenges
- Strategies
- Projects
- Wisdom
- Metrics
- Log / Journal

Do not fabricate deeply personal details that are not grounded in the source.

## Recommended Process

- Run `python3 scripts/inspect_compact_json.py <file.json>` first.
- Use the keyword/theme output to find high-signal groups.
- Open only the relevant JSON passages rather than loading the whole file into context.
- Quote source conversation IDs in the output when useful.

## Resources

### scripts/

- `inspect_compact_json.py`: summarize the JSON, top keywords, top groups, likely themes, and selected example prompts.

### references/

- `output-templates.md`: compact templates and writing guidance for the three standard outputs.
