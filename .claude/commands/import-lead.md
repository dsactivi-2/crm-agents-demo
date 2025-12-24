---
description: Lead automatisch ins CRM importieren
allowed-tools: Read, Write, Bash(python:*), Bash(curl:*)
---

# Lead Import Agent

Importiere Lead: $ARGUMENTS

## Ablauf

1. Validiere Daten
2. Prüfe Duplikate
3. Speichere in DB
4. Berechne initialen Score
5. Trigger nächsten Agent

## Output

```json
{
  "status": "success",
  "lead_id": 123,
  "name": "...",
  "score": 50,
  "next_action": "qualify"
}
```
