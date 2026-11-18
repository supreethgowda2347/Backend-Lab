from flask import Flask, request, jsonify
app = Flask(__name__)

orders = []

@app.route('/addOrders', methods = ['POST'])
def add_orders():
    data = request.get_json()
    orders.append(data)
    return jsonify({"message" : "order added successfully", "order" : data})

@app.route('/showOrders', methods = ['GET'])
def show_order():
    return jsonify(orders)

if __name__=='__main__':
    app.run(debug = True)
