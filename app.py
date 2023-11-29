import sqlite3
import random
from flask import Flask, session, render_template, request, g

## Basic Flask App
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
app.config["SESSION_COOKIE_NAME"] = "myCOOKIE_monSTER528"

@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["task_items"] = get_db()
    return render_template("index.html", all_items=session["all_items"],
                                         task_items=session["task_items"])

@app.route("/add_items", methods=["post"])
def add_items():
    session["task_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", all_items=session["all_items"],
                                         task_items=session["task_items"])

@app.route("/remove_items", methods=["post"])
def remove_items():
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["task_items"]:
            idx = session["task_items"].index(item)
            session["task_items"].pop(idx)
            session.modified = True

    return render_template("index.html", all_items=session["all_items"],
                                         task_items=session["task_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("select name from task")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        task_list = all_data.copy()
        random.shuffle(task_list)
        task_list = task_list[:5]
    return all_data, task_list

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()