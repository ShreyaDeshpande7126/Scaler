import gradio as gr
from fastapi import FastAPI
import uvicorn
from environment import SupportEnv
from logic import decide_action

env = SupportEnv("tickets.json")

app = FastAPI()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    state, reward, done, _ = env.step(action)
    return {"state": state, "reward": reward, "done": done}

@app.get("/state")
def state():
    if env.index < len(env.tickets):
        return env.tickets[env.index]
    return {"message": "done"}

def run_ai():
    if env.index >= len(env.tickets):
        return "🎉 All tickets processed!"

    state = env.tickets[env.index]
    action = decide_action(state)
    _, reward, _, _ = env.step(action)

    return f"""
Ticket: {state['text']}

Priority: {action['priority']}
Department: {action['department']}
Escalate: {action['escalate']}

Reward: {reward}
"""

demo = gr.Interface(fn=run_ai, inputs=[], outputs="text")

app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
