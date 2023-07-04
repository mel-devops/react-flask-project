from flask import flask 

app = Flask(__name__)

# members APi route
@app.route("/members")

def members():
    return {"members": ["membr1", "member2", "member3"]}


if __name__ == "__main__":
    app.run(debug=True)