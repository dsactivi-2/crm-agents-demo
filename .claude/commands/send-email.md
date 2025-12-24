---
description: Follow-up Email senden
allowed-tools: Read, Bash(curl:*)
---

# Email Agent

Sende Email an Lead: $ARGUMENTS

## Templates

- follow-up: Nach Anruf
- nurture: Für kalte Leads
- reminder: Termin-Erinnerung
- thank-you: Nach Meeting

## Output

```json
{
  "lead_id": 123,
  "email_id": "xyz789",
  "template": "follow-up",
  "status": "sent"
}
```
