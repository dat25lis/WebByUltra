from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Главная",
        ai_logo_path="images/ai_logo.png"
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="Информация",
        ai_logo_path="images/ai_logo.png"
    )

@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False
    if request.method == "POST":
        phone = request.form.get("phone")
        message = request.form.get("message")
        sent = True
    return render_template(
        "contact.html",
        title="Предложения",
        sent=sent,
        ai_logo_path="images/ai_logo.png"
    )

if __name__ == "__main__":
    app.run(debug=True)

