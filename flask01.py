from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("frontend.html", result="")
@app.route("/calculate", methods=["POST"])
def solve():
    function = request.form["function"]
    try:
        result = eval(function)
    except Exception as e:
        result = f"Error: {e}"
    return render_template("frontend.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)