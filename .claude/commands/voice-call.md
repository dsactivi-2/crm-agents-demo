---
description: Automatischen Anruf starten
allowed-tools: Read, Bash(curl:*)
---

# Voice AI Agent

Starte Anruf für Lead: $ARGUMENTS

## Provider
- Vapi.ai (Standard)
- Retell.ai (Alternative)
- Bland.ai (Sales)

## Call Script

1. Begrüßung
2. Qualifizierungsfragen
3. Bei Interesse → Termin
4. Bei Ablehnung → Höflich beenden

## Output

```json
{
  "lead_id": 123,
  "call_id": "abc123",
  "status": "completed",
  "duration": "3:45",
  "outcome": "termin_vereinbart",
  "next_action": "send-email"
}
```
