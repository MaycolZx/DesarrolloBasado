from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("formulario.html")

@app.route("/cv")
def curr():
    return render_template("curriculum.html")


if __name__ == '__main__':
    app.run(debug=True,port=5000)