from environment import SupportEnv
from logic import decide_action

env = SupportEnv("tickets.json")

state = env.reset()
total_reward = 0
count = 0
done = False

while not done:
    action = decide_action(state)
    state, reward, done, _ = env.step(action)
    total_reward += reward
    count += 1

print("Final Score:", total_reward / count)
