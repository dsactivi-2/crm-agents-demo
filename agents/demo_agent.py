#!/usr/bin/env python3
"""
CRM Demo Agent - Zeigt wie die Automatisierung funktioniert
"""

import json
import random
from datetime import datetime

# Simulierte Datenbank
LEADS_DB = []

def import_lead(name: str, email: str, phone: str = None, company: str = None) -> dict:
    """Agent 1: Lead importieren"""
    print(f"\n🤖 AGENT 1: Lead Import")
    print(f"   Importiere: {name} ({email})")
    
    # Validierung
    if not name or not email:
        return {"status": "error", "message": "Name und Email erforderlich"}
    
    # Duplikat-Check
    for lead in LEADS_DB:
        if lead["email"] == email:
            print(f"   ⚠️ Duplikat gefunden!")
            return {"status": "duplicate", "lead_id": lead["id"]}
    
    # Speichern
    lead = {
        "id": len(LEADS_DB) + 1,
        "name": name,
        "email": email,
        "phone": phone,
        "company": company,
        "status": "new",
        "score": 0,
        "created_at": datetime.now().isoformat()
    }
    LEADS_DB.append(lead)
    
    print(f"   ✅ Lead #{lead['id']} gespeichert")
    return {"status": "success", "lead_id": lead["id"], "next_action": "qualify"}


def qualify_lead(lead_id: int) -> dict:
    """Agent 2: Lead bewerten"""
    print(f"\n🤖 AGENT 2: Lead Qualifier")
    print(f"   Bewerte Lead #{lead_id}")
    
    # Lead finden
    lead = next((l for l in LEADS_DB if l["id"] == lead_id), None)
    if not lead:
        return {"status": "error", "message": "Lead nicht gefunden"}
    
    # Score berechnen
    score = 0
    reasons = []
    
    if lead["name"] and lead["email"]:
        score += 20
        reasons.append("Vollständige Daten")
    
    if lead["email"] and not any(x in lead["email"] for x in ["gmail", "yahoo", "hotmail"]):
        score += 15
        reasons.append("Firmen-Email")
    
    if lead["phone"]:
        score += 10
        reasons.append("Telefon vorhanden")
    
    if lead["company"]:
        score += 15
        reasons.append("Firma angegeben")
    
    # Zufällig weitere Punkte für Demo
    score += random.randint(10, 30)
    
    # Priorität
    if score >= 70:
        priority = "HOT 🔴"
        next_action = "voice-call"
    elif score >= 50:
        priority = "WARM 🟡"
        next_action = "voice-call"
    elif score >= 30:
        priority = "COLD 🔵"
        next_action = "send-email"
    else:
        priority = "DISQUALIFIED ⚫"
        next_action = "archive"
    
    # Update Lead
    lead["score"] = score
    lead["priority"] = priority
    
    print(f"   📊 Score: {score}/100")
    print(f"   🎯 Priorität: {priority}")
    print(f"   ➡️ Nächste Aktion: {next_action}")
    
    return {
        "status": "success",
        "lead_id": lead_id,
        "score": score,
        "priority": priority,
        "reasons": reasons,
        "next_action": next_action
    }


def voice_call(lead_id: int) -> dict:
    """Agent 3: Automatischer Anruf"""
    print(f"\n🤖 AGENT 3: Voice AI")
    print(f"   Starte Anruf für Lead #{lead_id}")
    
    lead = next((l for l in LEADS_DB if l["id"] == lead_id), None)
    if not lead:
        return {"status": "error", "message": "Lead nicht gefunden"}
    
    print(f"   📞 Wähle {lead.get('phone', 'Nummer nicht vorhanden')}...")
    print(f"   🗣️ 'Guten Tag {lead['name']}, hier ist der KI-Assistent...'")
    
    # Simuliere Call-Ergebnis
    outcomes = ["termin_vereinbart", "interesse", "kein_interesse", "mailbox"]
    outcome = random.choice(outcomes)
    
    if outcome == "termin_vereinbart":
        print(f"   ✅ Termin vereinbart!")
    elif outcome == "interesse":
        print(f"   👍 Interesse bekundet")
    elif outcome == "kein_interesse":
        print(f"   👎 Kein Interesse")
    else:
        print(f"   📭 Mailbox - später erneut versuchen")
    
    return {
        "status": "success",
        "lead_id": lead_id,
        "outcome": outcome,
        "duration": f"{random.randint(1,5)}:{random.randint(10,59):02d}",
        "next_action": "send-email"
    }


def send_email(lead_id: int, template: str = "follow-up") -> dict:
    """Agent 4: Email senden"""
    print(f"\n🤖 AGENT 4: Email Agent")
    print(f"   Sende '{template}' Email an Lead #{lead_id}")
    
    lead = next((l for l in LEADS_DB if l["id"] == lead_id), None)
    if not lead:
        return {"status": "error", "message": "Lead nicht gefunden"}
    
    print(f"   📧 An: {lead['email']}")
    print(f"   📝 Template: {template}")
    print(f"   ✅ Email gesendet!")
    
    return {
        "status": "success",
        "lead_id": lead_id,
        "template": template,
        "email": lead["email"]
    }


def daily_report() -> dict:
    """Agent 5: Täglicher Report"""
    print(f"\n🤖 AGENT 5: Report Agent")
    print(f"   Erstelle Daily Report...")
    
    total = len(LEADS_DB)
    hot = len([l for l in LEADS_DB if l.get("priority", "").startswith("HOT")])
    warm = len([l for l in LEADS_DB if l.get("priority", "").startswith("WARM")])
    
    report = f"""
    ═══════════════════════════════════════
    📊 DAILY REPORT - {datetime.now().strftime('%d.%m.%Y')}
    ═══════════════════════════════════════
    
    LEADS:
    • Total: {total}
    • HOT 🔴: {hot}
    • WARM 🟡: {warm}
    
    TOP LEADS:
    """
    
    for lead in sorted(LEADS_DB, key=lambda x: x.get("score", 0), reverse=True)[:3]:
        report += f"    • {lead['name']} - Score: {lead.get('score', 0)}\n"
    
    print(report)
    return {"status": "success", "leads_total": total}


def run_demo():
    """Komplette Demo der Agent-Kette"""
    print("=" * 50)
    print("🚀 CRM AGENTS DEMO")
    print("=" * 50)
    
    # Agent 1: Lead Import
    result1 = import_lead(
        name="Max Müller",
        email="max.mueller@techfirma.de",
        phone="+49 176 12345678",
        company="TechFirma GmbH"
    )
    
    if result1["status"] == "success":
        lead_id = result1["lead_id"]
        
        # Agent 2: Qualify
        result2 = qualify_lead(lead_id)
        
        if result2["next_action"] == "voice-call":
            # Agent 3: Voice Call
            result3 = voice_call(lead_id)
            
            # Agent 4: Email
            result4 = send_email(lead_id, "follow-up")
    
    # Noch ein Lead
    import_lead("Anna Schmidt", "anna@startup.io", company="Startup.io")
    qualify_lead(2)
    
    # Agent 5: Report
    daily_report()
    
    print("\n" + "=" * 50)
    print("✅ DEMO ABGESCHLOSSEN")
    print("=" * 50)


if __name__ == "__main__":
    run_demo()
