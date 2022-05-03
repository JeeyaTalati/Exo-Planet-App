from flask import Flask,jsonify,request
from data import data
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "exoPlanetData":data,
        "message":"Success"
    })
@app.route("/planet")
def planet():
    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"]== name)
    return jsonify({
        "exoPlanetData":planet_data,
        "message":"Success"
    })
if __name__ == "__main__":
    app.run(debug=True)