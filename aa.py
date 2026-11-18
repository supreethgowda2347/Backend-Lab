from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    print("Request received")
    print(request.json)

    return jsonify({
        "message": "Request received successfully"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=3000)