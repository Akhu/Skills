# Engineering Principles Reference

## Core objective

Produce code that is reusable, neutral, understandable, object-oriented, testable, and maintainable in open-source or private contexts.
Prefer standards and broadly transferable patterns over project-specific shortcuts unless the project constraints require otherwise.

## Design priorities

- reuse across projects when the same domain problem exists
- explicit intent over implicit magic
- small responsibilities and explicit dependencies
- technologies chosen for project fit, not habit
- test seams that allow injecting inputs and dependencies
- simple designs that cover the common case without speculative complexity

## SOLID

### Single Responsibility Principle

Keep one reason to change per class, module, or function.
Split orchestration, domain rules, persistence, and presentation when they evolve at different rates.

### Open/Closed Principle

Extend behavior through composition, strategies, or polymorphism when the variation is real and recurring.
Do not add extension points before the second concrete need.

### Liskov Substitution Principle

Subtypes must preserve the expectations of the abstraction.
Do not force inheritance when subclasses weaken guarantees, add preconditions, or remove supported behavior.

### Interface Segregation Principle

Expose narrow contracts shaped by real consumers.
Prefer several focused interfaces over a broad contract that pushes unused methods onto callers.

### Dependency Inversion Principle

Depend on stable abstractions at boundaries.
Keep infrastructure behind interfaces or ports when that boundary improves substitution, tests, or long-term coupling.

## Objects Calisthenics

- keep one indentation level per method when possible
- avoid `else` by using early returns, guards, or separate objects
- wrap primitives when they represent a domain concept with validation or behavior
- keep at most one object navigation per line
- avoid abbreviations in names
- grow small classes rather than god objects
- limit instance fields to what the class truly owns
- avoid first-class collection wrappers unless they add real domain behavior
- minimize public getters and setters when behavior can stay inside the object

These are guardrails, not absolute laws. Break them only with a concrete reason.

## Simplicity rules

### YAGNI

Do not build a capability before a real use case needs it.
Favor deleting future-proof scaffolding over maintaining it indefinitely.

### KISS

Start from the clearest design that can satisfy the current requirement.
Optimize only after the simple version is correct and measurable.

### DRY

Keep one authoritative representation of each rule or piece of knowledge.
Do not merge code just because it looks similar if the underlying reasons to change differ.

## Quality failure modes

### Rigidity

A local change requires touching many dependent modules.

### Fragility

A local change breaks behavior in unrelated modules.

### Immobility

Useful code cannot be reused without excessive risk or effort.

### Viscosity

Bypassing the design is easier than following it.

### Opacity

The code does not clearly communicate its purpose.

## Performance expectations

Justify performance with concrete reasoning:
- time complexity on the critical path
- memory, allocation, or I/O costs
- expected usage profile and scaling limits

Do not over-optimize for rare edge cases when a simpler design correctly serves most use cases.

## Semantic versioning

Assess whether the change is:
- patch: bug fix without breaking public contracts
- minor: backward-compatible capability added
- major: incompatible change in public behavior, contracts, data format, or integration expectations

If the project is private, still reason with the same discipline at public boundaries such as APIs, persisted models, or shared modules.

## Architecture note template

Use this template before non-trivial implementation:

1. Problem statement
2. Scope and non-goals
3. Domain objects and responsibilities
4. Dependency direction
5. Pattern choice and rejected alternatives
6. Complexity and resource profile
7. Test strategy
8. Versioning impact
