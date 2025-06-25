from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_filename = None
    if request.method == "POST":
        data = request.form["data"]
        if data:
            img = qrcode.make(data)
            qr_filename = "static/qr_code.png"
            img.save(qr_filename)
    return render_template("index.html", qr_filename=qr_filename)

if __name__ == "__main__":
    app.run(debug=True)
