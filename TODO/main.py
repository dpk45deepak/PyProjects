import os
from flask import Flask, send_file, jsonify, request
from markupsafe import escape

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "name": "Learn Tailwind CSS",
        "description": "Go through the Tailwind CSS documentation."
    }
]

next_task_id = max(task["id"] for task in tasks) + 1 if tasks else 1


@app.route("/")
def index():
    return send_file("src/index.html")


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"


@app.route("/task", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/task", methods=["POST"])
def create_task():
    global next_task_id

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name required"}), 400

    new_task = {
        "id": next_task_id,
        "name": data["name"],
        "description": data.get("description", "")
    }

    tasks.append(new_task)
    next_task_id += 1

    return jsonify(new_task), 201


@app.route("/task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)