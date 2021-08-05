from getNews import Samakal, Politico
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/samakal')
def somokal():
    q = request.args.get('q')
    result = Samakal(q)
    if result == []:
        result = "No result Found"
    return jsonify(result)

@app.route('/politico')
def politico():
    q = request.args.get('q')
    result = Politico(q)
    if result == []:
        result = "No result Found"
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)