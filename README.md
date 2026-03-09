# Skills Repository

Repository Git pour versionner et partager mes skills Codex personnalisées.

## Structure

```text
.
├── README.md
└── skills/
    ├── engineering-quality-guardrails/
    └── security-best-practices/
```

## Index des skills

| Skill | Description | Chemin |
| --- | --- | --- |
| `engineering-quality-guardrails` | Design, implement, refactor, or review code with explicit engineering guardrails focused on reuse, neutrality, object-oriented design, SOLID, Objects Calisthenics, YAGNI, DRY, KISS, semantic versioning, and testability. | [`skills/engineering-quality-guardrails`](./skills/engineering-quality-guardrails/) |
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
