from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
import output

app = Flask(__name__)
app.debug = True
# app.secret_key = "super secret key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["file"]
        model = request.form.get("model")
        output_file = "./uploaded_imgs/" + f.filename
        f.save(output_file)
        out = output.run(model, output_file)
        if out > 0.5:  # Change cutoff depending on the model
            resultval = "Adenocarcinoma Positive"
        else:
            resultval = "Adenocarcinoma Negative - i.e. Adenoma"
        return render_template("value.html", value=out, valuetext=resultval)
    return render_template("home.html")

@app.route("/outputs")
def outputs():
    return render_template("outputs.html")

# connect and run the python backend
@app.route("/code", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f = request.files["file"]
        model = request.form.get("model")
        output_file = "./uploaded_imgs/" + f.filename
        f.save(output_file)
        out = output.run(model, output_file)
        if out > 0.5:  # Change cutoff depending on the model
            resultval = "Adenocarcinoma Positive"
        else:
            resultval = "Adenocarcinoma Negative - i.e. Adenoma"
        return render_template("value.html", value=out, valuetext=resultval)
    return render_template("code.html")


if __name__ == "__main__":
    app.run()
