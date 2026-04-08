import json

class SupportEnv:
    def __init__(self, file):
        with open(file) as f:
            self.tickets = json.load(f)
        self.index = 0
        self.total_reward = 0
        self.steps = 0

    def reset(self):
        self.index = 0
        self.total_reward = 0
        self.steps = 0
        return self.tickets[self.index]

    def step(self, action):
        ticket = self.tickets[self.index]
        reward = 0

        # urgency rule
        if ticket["urgency"] == "high" and action["priority"] == "high":
            reward += 1
        elif ticket["urgency"] == "low" and action["priority"] == "low":
            reward += 1
        else:
            reward -= 1

        # sentiment rule
        if ticket["sentiment"] == "angry" and action["escalate"]:
            reward += 1
        elif ticket["sentiment"] != "angry" and not action["escalate"]:
            reward += 1
        else:
            reward -= 1

        # department rule
        text = ticket["text"].lower()
        if ("refund" in text or "payment" in text) and action["department"] == "billing":
            reward += 1
        elif ("bug" in text or "crash" in text) and action["department"] == "technical":
            reward += 1
        elif action["department"] == "support":
            reward += 1
        else:
            reward -= 1

        reward = max(0, min(1, reward / 3))

        self.total_reward += reward
        self.steps += 1

        self.index += 1
        done = self.index >= len(self.tickets)
        next_state = None if done else self.tickets[self.index]

        return next_state, reward, done, {}

    def get_metrics(self):
        avg = self.total_reward / self.steps if self.steps else 0
        return self.steps, round(avg, 2)