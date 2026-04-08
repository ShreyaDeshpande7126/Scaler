def decide_action(ticket):
    if ticket["urgency"] == "high":
        return {"priority": "high", "department": "tech", "escalate": True}
    elif ticket["urgency"] == "medium":
        return {"priority": "medium", "department": "support", "escalate": False}
    else:
        return {"priority": "low", "department": "general", "escalate": False}
