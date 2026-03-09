---
name: engineering-quality-guardrails
description: Design, implement, refactor, or review code with explicit engineering guardrails focused on reuse, neutrality, object-oriented design, SOLID, Objects Calisthenics, YAGNI, DRY, KISS, semantic versioning, and testability. Use when Codex must turn quality requirements into a concrete architecture, challenge an over-engineered approach, document tradeoffs before coding, or evaluate whether an implementation is rigid, fragile, opaque, viscous, or hard to reuse.
---

# Engineering Quality Guardrails

## Overview

Apply a compact architecture and review workflow for tasks where code quality matters more than raw speed of delivery.
Keep the solution reusable and explicit, but reject ceremony that does not improve maintainability or correctness.

## Workflow

### 1. Frame the problem before coding

Write a short architecture note before editing code when the task is non-trivial.

Include:
- goal and scope
- core domain objects or modules
- dependency direction
- chosen patterns and why they fit
- expected complexity and resource profile
- semantic versioning impact if public behavior changes

If the current request pushes toward overengineering, say so and propose the smaller design first.

### 2. Prefer the simplest viable object model

Model the problem with explicit names and narrow responsibilities.

Prefer:
- small classes or components with one reason to change
- dependencies injected through constructors or explicit interfaces
- value objects instead of loose primitives when a concept has rules
- composition over inheritance unless substitution is genuinely required
- standard library and established framework features before custom abstractions

Avoid:
- speculative extension points
- generic managers, helpers, or utils with mixed responsibilities
- boolean flag APIs that hide multiple behaviors
- public mutable state without a strong reason
- abbreviations that obscure the domain

### 3. Apply guardrails during implementation

Use this checklist while coding:
- Keep control flow shallow. Extract intention-revealing methods instead of stacking conditionals.
- Minimize `else` branches by returning early or splitting responsibilities.
- Keep one level of abstraction per function.
- Keep object interactions narrow; avoid long call chains.
- Keep data and behavior together when the behavior belongs to the concept.
- Make invalid states harder to represent.
- Remove duplication of knowledge, not just duplication of syntax.
- Add tests around behavior and seams, not around private implementation details.

### 4. Review with failure modes, not slogans

When reviewing code, explicitly check whether the change introduces:
- rigidity: a small change forces edits across many modules
- fragility: unrelated areas can break after a local change
- immobility: useful parts cannot be reused elsewhere
- viscosity: hacks are easier than respecting the intended design
- opacity: intent is hard to understand from names and structure

If one of these appears, describe the concrete mechanism and propose the smallest corrective change.

### 5. Make performance and versioning explicit

Do not claim performance without a concrete argument.

State:
- dominant time complexity for the critical path when it matters
- meaningful memory or I/O costs
- whether the change affects API shape, persistence format, or external behavior
- whether the versioning impact is patch, minor, or major, with justification

Prefer a simple and measurable implementation over a clever optimization without evidence.

## References

Read [principles.md](references/principles.md) when the task needs the detailed rationale behind SOLID, Objects Calisthenics, YAGNI, KISS, DRY, semantic versioning, or the code smell taxonomy.

## Output Expectations

For non-trivial tasks, structure the answer in this order:
1. architecture decision
2. tradeoffs and rejected simpler or heavier alternatives
3. implementation
4. tests
5. versioning impact if relevant

For small tasks, compress the same reasoning into a short paragraph but keep the tradeoff visible.
