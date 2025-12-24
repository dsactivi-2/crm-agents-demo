---
description: Lead bewerten und Score berechnen
allowed-tools: Read, Bash(python:*), WebSearch
---

# Lead Qualifier Agent

Bewerte Lead: $ARGUMENTS

## Score-Kriterien (0-100)

+20: Vollständige Daten
+15: Firmen-Email
+10: Telefon vorhanden
+15: Firma > 10 Mitarbeiter
+10: Branche passt
+10: Budget vorhanden
+10: Dringlichkeit
+10: Entscheider

## Priorität

- 70-100: 🔴 HOT → Sofort anrufen
- 50-69: 🟡 WARM → 24h
- 30-49: 🔵 COLD → Nurture
- 0-29: ⚫ DISQUALIFIED

## Output

```json
{
  "lead_id": 123,
  "score": 75,
  "priority": "HOT",
  "next_action": "voice-call"
}
```
