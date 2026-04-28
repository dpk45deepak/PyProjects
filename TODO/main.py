import os

from flask import Flask, send_file, jsonify, request
from markupsafe import escape

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "name": "Learn Tailwind CSS",
        "description": "Go through the Tailwind CSS documentation and practice styling components."
    },
    {
        "id": 2,
        "name": "Build To-Do App",
        "description": "Create a functional to-do list app with add and delete features."
    },
    {
        "id": 3,
        "name": "Study Flask",
        "description": "Learn how to create routes, handle requests, and build APIs using Flask."
    }
]
# Find the highest existing ID to avoid collisions
if tasks:
    next_task_id = max(task['id'] for task in tasks) + 1
else:
    next_task_id = 1


@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/hello", methods=['GET'])
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

# get all tasks
@app.route("/task", methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# get a specific task
@app.route("/task/<int:task_id>", methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@app.route("/task", methods=['POST'])
def create_task():
    global next_task_id
    if not request.is_json or "name" not in request.get_json():
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json()
    new_task = {
        "id": next_task_id,
        "name": data["name"],
        "description": data.get("description", "")
    }
    tasks.append(new_task)
    next_task_id += 1
    return jsonify(new_task), 201

@app.route("/task/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task_found = any(task['id'] == task_id for task in tasks)
    if not task_found:
        return jsonify({"error": "Task not found"}), 404
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

def main():
    app.run(debug=True, port=int(os.environ.get("PORT", 80)))
    
if __name__ == "__main__":
    main()
