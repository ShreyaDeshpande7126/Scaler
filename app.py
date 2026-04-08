from flask import Flask, render_template
from environment import SupportEnv
from logic import decide_action
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

env = SupportEnv("tickets.json")

@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/dashboard")
def dashboard():
    state = env.reset()
    action = decide_action(state)
    _, reward, _, _ = env.step(action)

    steps, avg = env.get_metrics()

    return render_template(
        "index.html",
        ticket=state,
        action=action,
        reward=reward,
        steps=steps,
        avg=avg
    )


@app.route("/next")
def next_step():
    state = env.tickets[env.index]
    action = decide_action(state)
    _, reward, done, _ = env.step(action)

    steps, avg = env.get_metrics()

    return render_template(
        "index.html",
        ticket=state,
        action=action,
        reward=reward,
        steps=steps,
        avg=avg,
        done=done
    )


@app.route("/auto")
def auto_run():
    env.reset()

    results = []
    state = env.tickets[0]
    done = False

    while not done:
        action = decide_action(state)
        next_state, reward, done, _ = env.step(action)

        results.append(reward)
        state = next_state

    steps, avg = env.get_metrics()

    # create graph
    os.makedirs("static", exist_ok=True)

    plt.figure()
    plt.plot(results)
    plt.title("Reward per Ticket")
    plt.xlabel("Steps")
    plt.ylabel("Reward")
    plt.savefig("static/graph.png")
    plt.close()

    return render_template("auto.html", avg=avg)


if __name__ == "__main__":
    app.run(debug=True)