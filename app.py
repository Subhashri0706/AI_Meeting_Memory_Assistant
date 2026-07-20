from utils.summarizer import summarize
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        notes = request.form["meeting_notes"]
        result = summarize(notes)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)