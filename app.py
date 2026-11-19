from flask import Flask, render_template, request

app = Flask(__name__)
members = []

@app.route("/", methods=["GET", "POST"])
def home():
    joined_name = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        favorite_moment = request.form.get("favorite_moment", "").strip()
        if name:
            members.append({"name": name, "favorite_moment": favorite_moment})
            joined_name = name
    return render_template("index.html", joined_name=joined_name, members=members)

if __name__ == "__main__":
    app.run(debug=True)