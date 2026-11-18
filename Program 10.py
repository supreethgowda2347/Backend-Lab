from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Running. Send POST request to /n8n webhook"

@app.route('/n8n-webhook', methods=['POST'])
def n8n_webhook():
    data = request.get_json()
    print("Recieved from n8n:",data)
    return jsonify({"status" : "recieved", "data" : data})

if __name__=='__main__':
    app.run(debug = True, port = 5000)
    