---
name: portfolio-human-voice
description: >-
  Enforces Jesse van den Hoven's authentic, grounded, human writing style and eliminates AI-characteristic phrasing, clichés, and punctuation (such as em-dashes and en-dashes). Use whenever drafting, editing, or reviewing copy, bios, job descriptions, cover letters, or portfolio sections.
---

# Portfolio Human Voice & Style Guide

This skill guides the agent in writing and editing copy that matches Jesse van den Hoven's personal voice, while systematically stripping out telltale AI markers.

## The Core Rule: Zero AI Dashes

Never use em-dashes (`—`) or en-dashes (`–`) in prose, headings, bullet points, or dates.
- **Why**: AI models default to em-dashes as a dramatic pause crutch. Real human writing uses commas, colons, parentheses `( )`, or simply two clear sentences.
- **Dates**: Use `tot` or `tot heden` in Dutch (e.g. `September 2026 tot heden`), and `to` or `to present` in English (`September 2026 to present`).
- **Separators**: Use vertical bars `|` or centered dots `·` for page titles and footers.

## Tone & Vocabulary (Modeled on Jesse's Motivational Letter & CV)

Jesse writes with a down-to-earth, pragmatic, and confident tone. He focuses on practical realities rather than abstract corporate buzzwords.

### Preferred Expressions
- *"Verbinding leggen tussen mens, organisatie en IT"*
- *"De schakel tussen de IT-inrichting, leveranciers en de dagelijkse praktijk van medewerkers"*
- *"Met beide benen in de praktijk staan"*
- *"Requirements ophalen en werkprocessen vertalen naar concrete oplossingen"*
- *"Planning en leveranciersafspraken in de gaten houden"*
- *"Mensen van begin tot eind meenemen bij een verandering"*
- *"Makkelijk schakelen tussen management, technici en adviseurs"*
- *"Weten hoe de techniek onder de motorkap werkt"*

### Banned AI Cliches
Do NOT use:
- *"Aanjagen van..."* (overused AI buzzword; use *begeleiden*, *uitvoeren*, *bevorderen*, *in kaart brengen*)
- *"Cruciale synergie"*, *"krachtige impuls"*, *"deze dynamische rol"*
- *"Use-case discovery"* (use *praktische mogelijkheden ontdekken*)
- *"Adoption, not demos"* or formulaic slogans
- *"Dat pad is het punt: ..."* or theatrical one-liners
- Hollow philosophical quotes like *"Technologie heeft pas waarde wanneer..."*

## Step-by-Step Writing Workflow

1. **Draft in First-Person**: Keep sentences active and direct (*"Ik help..."*, *"Ik zorg voor..."*, *"Ik heb gewerkt aan..."*).
2. **Read Aloud Test**: If a sentence sounds like an AI generated an elevator pitch, simplify it to plain Dutch or English.
3. **Punctuation Check**: Run a search for `\u2014` (`—`) and `\u2013` (`–`). If any are found, replace with a comma, parentheses, or rewrite into a clean sentence.
4. **Validation**: Run the automated check:
   ```bash
   python3 tools/validate.py
   ```
