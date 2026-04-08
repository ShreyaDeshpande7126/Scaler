class SupportEnv:
    def __init__(self, file):
        import json
        with open(file) as f:
            self.tickets = json.load(f)
        self.index = 0

    def reset(self):
        self.index = 0
        return self.tickets[self.index]

    def step(self, action):
        ticket = self.tickets[self.index]

        reward = 1 if action["priority"] == ticket["priority"] else 0

        self.index += 1
        done = self.index >= len(self.tickets)

        next_state = self.tickets[self.index] if not done else None

        return next_state, reward, done, {}

    def state(self):
        return self.tickets[self.index]
