from flask import Flask, request, jsonify

app = Flask(__name__)

users=[]
@app.route('/create', methods=['POST'])
def create_user_data():
    data = request.get_json()
    username = data.get("username")
    emailid = data.get("emailid")
    new_user = {
        "id": len(users) + 1,
        "username": username,
        "emailid": emailid
    }

    return jsonify(new_user), 201
@app.route('/read',methods=['GET'])
def get_data():
    return jsonify(users)

# Update User
@app.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    new_username = data.get('username')
    new_emailid = data.get('emailid')
    for user in users:
        if user['id'] == user_id:
            user['username'] = new_username
            user['emailid'] = new_emailid
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# Delete User
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            del users[index]
            return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)
