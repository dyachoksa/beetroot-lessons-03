from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    # print(request.method)

    if request.method == "POST":
        email = request.form["email"]
        content = request.form["message"]

        message = f"""
        <strong>Email:</strong> {email} <br/> 
        <strong>Message:</strong> {content}
        """

        return render_template("index.html", message=message)

    return render_template("index.html", message=message)
