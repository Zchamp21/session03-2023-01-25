from flask import *

app = Flask(__name__)

# @app.route("/") # Python annotation. This returns a function
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/hi', methods=['GET'])
# def hi():
#   user_name = request.args.get("userName", "unknown")
#   return render_template('main.html', user=user_name) 

cur_entries = [("Zach Champlin (me)", "The Connection")]

@app.route("/")
def load_site():
    return render_template("index.html", entries=cur_entries)

@app.route("/add_guest", methods=["POST"])
def add_guest():
    if request.method == "POST":
        guest = request.form["guest"]
        album = request.form["record"]
        newEntry = (guest, album)
        cur_entries.append(newEntry)

    return redirect("/")