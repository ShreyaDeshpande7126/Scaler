def decide_action(state):
    text = state["text"].lower()

    priority = "high" if state["urgency"] == "high" else "low"
    escalate = state["sentiment"] == "angry"

    if "refund" in text or "payment" in text:
        department = "billing"
    elif "bug" in text or "crash" in text:
        department = "technical"
    else:
        department = "support"

    confidence = 0.95 if escalate else 0.7

    return {
        "priority": priority,
        "department": department,
        "escalate": escalate,
        "request_info": False,
        "confidence": confidence
    }