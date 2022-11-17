from flask import Flask, jsonify
app = Flask(_name_)


@app.route('/')
def home():
    return "HOME"


@app.route("/result", methods=["GET"])
def similar_to(volH, volS, N):
    res = (volH*N*50*1000)/(volS)
    res = jsonify(res)
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res


if _name_ == "_main_":
    app.run(debug=True)
