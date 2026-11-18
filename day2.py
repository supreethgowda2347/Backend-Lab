from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/register', methods =['POST'])
def register():
    data = request.get_json()
    name = data.get('name',' ')
    email = data.get('email',' ')
   

    if not name:
        return jsonify({"success": False , "message": "Name is Required"}), 404

    if not email:
            return jsonify({"success": False, "message": "Email is Required"}), 404

    if not is_valid_email(email):
            return jsonify({"success": False, "message": "Invalid email format"}), 404

    
    return jsonify({"success": True, "message": f"User {name} registered successfully with email {email}"})

if __name__ == "__main__":
     app.run(debug = True)

