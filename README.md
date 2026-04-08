🤖 AI Customer Support Simulator:

🚀 Overview: This project is an AI-powered customer support simulation system that automates decision-making for handling customer tickets. It analyzes ticket data and determines the appropriate priority, department routing, and escalation strategy.

🧠 Motivation In real-world platforms, customer support teams handle large volumes of tickets daily. Efficient triaging and routing is critical to reduce response time and improve customer satisfaction. This project simulates that process using a rule-based AI system inspired by reinforcement learning concepts.

How It Works: The system processes customer tickets based on:

Urgency
Sentiment
Customer Tier
Ticket Content
It then decides:

✅ Priority (high / low)
✅ Department (billing / technical / support)
✅ Escalation (True / False)
Reward System: Each decision is evaluated using a reward function:

Correct priority → +1
Correct escalation → +1
Correct department → +1
Incorrect decisions → penalty
Final reward is normalized between 0 and 1

Simulation:

Each click processes the next ticket
Displays decision and reward
Simulates real-world ticket handling workflow
Tasks: We simulate 3 levels of task complexity:

Easy

Low urgency, neutral sentiment
Simple routing (support)
Medium

Medium urgency, frustrated users
Requires correct priority and routing
Hard

High urgency, angry enterprise users
Requires escalation + correct department + priority
Observation Space: Each ticket contains:

{
  "text": "string",
  "urgency": "low | medium | high",
  "customer_tier": "free | pro | enterprise",
  "sentiment": "happy | neutral | frustrated | angry"
}
