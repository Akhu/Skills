#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


STOPWORDS = {
    "alors", "au", "aucun", "aussi", "autre", "avant", "avec", "avoir", "bon",
    "car", "ce", "cela", "ces", "ceux", "chaque", "comme", "comment", "dans",
    "des", "du", "dedans", "dehors", "depuis", "devrait", "doit", "donc", "dos",
    "droite", "début", "elle", "elles", "en", "encore", "essai", "est", "et",
    "eu", "fait", "faites", "fois", "font", "force", "haut", "hors", "ici", "il",
    "ils", "je", "juste", "la", "le", "les", "leur", "là", "ma", "maintenant",
    "mais", "mes", "mine", "moins", "mon", "mot", "même", "ni", "nommés", "notre",
    "nous", "nouveaux", "ou", "où", "par", "parce", "parole", "pas", "personnes",
    "peut", "peu", "pièce", "plupart", "pour", "pourquoi", "quand", "que", "quel",
    "quelle", "quelles", "quels", "qui", "sa", "sans", "ses", "seulement", "si",
    "sien", "son", "sont", "sous", "soyez", "sujet", "sur", "ta", "tandis", "tellement",
    "tels", "tes", "ton", "tous", "tout", "trop", "très", "tu", "valeur", "voie",
    "voient", "vont", "votre", "vous", "vu", "ça", "c", "d", "j", "l", "m", "n", "s", "t",
    "estce", "peux", "peut", "faut", "faire", "a", "ai", "as", "y", "on", "de", "un", "une",
}

THEME_PATTERNS = {
    "famille": r"\bfamille|enfant|bébé|poussette|vacances|camping|voiture|fanny|canapé|maison|garage\b",
    "dev-produit": r"\bapp|application|android|ios|mac|swift|swiftui|react|node|docker|api|site|store|ux|ui\b",
    "ia-agents": r"\bia|llm|agent|agents|mcp|modèle|model|openai|claude|ollama|rag|vllm\b",
    "souverainete": r"\bprivacy|vie privée|souverain|local|linux|homelab|backup|auto-h[eé]berg|self-host\b",
    "positionnement": r"\boffre|positionnement|profil|site|article|livre|écrire|rédige|structurer\b",
}


def tokenize(text: str):
    text = text.lower()
    return re.findall(r"[a-zà-ÿ0-9][a-zà-ÿ0-9'_-]*", text)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def top_keywords(items, limit=40):
    counter = Counter()
    for item in items:
        text = " ".join(filter(None, [item.get("prompt"), item.get("entry_title"), item.get("content"), item.get("preview")]))
        for tok in tokenize(text):
            if len(tok) < 3 or tok in STOPWORDS:
                continue
            counter[tok] += 1
    return counter.most_common(limit)


def theme_matches(groups):
    results = defaultdict(list)
    for group in groups:
        title = group.get("title_inferred", "")
        for theme, pattern in THEME_PATTERNS.items():
            if re.search(pattern, title, re.IGNORECASE):
                results[theme].append(group)
    return results


def select_examples(items, theme, limit=5):
    pattern = THEME_PATTERNS[theme]
    out = []
    for item in items:
        text = " ".join(filter(None, [item.get("prompt"), item.get("entry_title"), item.get("preview")]))
        if re.search(pattern, text, re.IGNORECASE):
            out.append(item)
        if len(out) >= limit:
            break
    return out


def main():
    parser = argparse.ArgumentParser(description="Inspect a Gemini compact JSON export for persona extraction.")
    parser.add_argument("json_file", help="Path to compact JSON export")
    parser.add_argument("--top-groups", type=int, default=20, help="Number of conversation groups to show")
    args = parser.parse_args()

    path = Path(args.json_file)
    data = load_json(path)
    stats = data.get("stats", {})
    groups = data.get("conversation_groups", [])
    items = data.get("items", [])

    print(f"file: {path}")
    print(f"items: {len(items)}")
    print(f"groups: {len(groups)}")
    if stats:
        print(f"range: {stats.get('first_datetime_utc')} -> {stats.get('last_datetime_utc')}")
    print()

    print("top_keywords:")
    for word, count in top_keywords(items):
        print(f"- {word}: {count}")
    print()

    print("top_groups:")
    for group in groups[: args.top_groups]:
        print(
            f"- {group.get('id')} | {group.get('start_datetime_utc')} | "
            f"{group.get('item_count')} items | {group.get('title_inferred')}"
        )
    print()

    print("themes:")
    themed = theme_matches(groups)
    for theme, matched_groups in themed.items():
        print(f"- {theme}: {len(matched_groups)} groups")
        for group in matched_groups[:5]:
            print(f"  - {group.get('id')} | {group.get('title_inferred')}")
    print()

    print("example_items:")
    for theme in THEME_PATTERNS:
        print(f"[{theme}]")
        for item in select_examples(items, theme):
            prompt = item.get("prompt") or item.get("entry_title") or item.get("preview") or ""
            print(f"- {item.get('conversation_group_id')} | {item.get('datetime_utc')} | {prompt[:180]}")
        print()


if __name__ == "__main__":
    main()
