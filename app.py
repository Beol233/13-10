from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'clave_secreta'
@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)