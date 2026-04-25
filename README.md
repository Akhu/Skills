# Skills Repository

Repository Git pour versionner et partager mes skills Codex personnalisées.

## Structure

```text
.
├── README.md
└── skills/
    ├── engineering-quality-guardrails/
    ├── gemini-json-persona/
    └── security-best-practices/
```

## Index des skills

| Skill | Description | Chemin |
| --- | --- | --- |
| `engineering-quality-guardrails` | Design, implement, refactor, or review code with explicit engineering guardrails focused on reuse, neutrality, object-oriented design, SOLID, Objects Calisthenics, YAGNI, DRY, KISS, semantic versioning, and testability. | [`skills/engineering-quality-guardrails`](./skills/engineering-quality-guardrails/) |
| `gemini-json-persona` | Extract a reusable persona/context package from a Gemini compact JSON export, including a structured meta profile, an operational LLM context file, and a TELOS-style personal context document. | [`skills/gemini-json-persona`](./skills/gemini-json-persona/) |
| `security-best-practices` | Perform language and framework specific security best-practice reviews and suggest improvements for Python, JavaScript/TypeScript, and Go stacks. | [`skills/security-best-practices`](./skills/security-best-practices/) |

## Convention

Chaque dossier de skill conserve sa structure native:

- `SKILL.md` pour la définition de la skill
- `agents/` pour la configuration agent
- `references/` pour la documentation de support
- fichiers additionnels éventuels comme `LICENSE.txt`

## Ajouter une nouvelle skill

1. Créer un nouveau dossier sous `skills/`.
2. Y copier la structure complète de la skill.
3. Ajouter l'entrée correspondante dans la section `Index des skills` de ce README.
