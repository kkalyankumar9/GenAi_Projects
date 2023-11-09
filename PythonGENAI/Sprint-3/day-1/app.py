from flask import Flask, jsonify, request, abort
import json
import unittest



app = Flask(__name__)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

menu_filename = 'menu.json'
orders_filename = 'orders.json'

menu = load_data(menu_filename)
orders = load_data(orders_filename)

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route('/add', methods=['POST'])
def add_dish():
    data = request.get_json()

    # Validate input
    if 'name' not in data or 'price' not in data or 'availability' not in data:
        abort(400, 'Invalid input data. Please provide name, price, and availability.')

    new_dish = {
        "id": len(menu) + 1,
        "name": data['name'],
        "price": float(data['price']),  # Assuming price is a float
        "availability": bool(data["availability"])  # Assuming availability is a boolean
    }

    menu.append(new_dish)
    save_data(menu, menu_filename)
    return jsonify(message='Dish added successfully', id=new_dish['id']), 201

@app.route('/remove/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    global menu
    menu = [dish for dish in menu if dish['id'] != dish_id]
    save_data(menu, menu_filename)
    return jsonify(message='Dish was removed'), 200

@app.route('/update_availability/<int:dish_id>', methods=['PATCH'])
def update_availability(dish_id):
    data = request.get_json()

    # Validate input
    if 'availability' not in data:
        abort(400, 'Invalid input data. Please provide availability.')

    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = bool(data['availability'])
            save_data(menu, menu_filename)
            return jsonify(message='Dish updated successfully'), 200

    abort(404, 'Dish not found')

@app.route("/place_order", methods=['POST'])
def place_order():
    data = request.get_json()

    # Validate input
    customer_name = data.get('customer_name')
    dish_ids = data.get('dish_ids')

    if not customer_name or not dish_ids:
        abort(400, 'Invalid input data. Please provide customer_name and dish_ids.')

    order_id = len(orders) + 1
    ordered_dishes = []

    for dish_id in dish_ids:
        for dish in menu:
            if dish['id'] == dish_id and dish['availability']:
                ordered_dishes.append({
                    "id": dish['id'],
                    "name": dish['name'],
                    "price": dish['price']
                })
                break
        else:
            abort(400, f'Dish with id {dish_id} not available.')

    order = {
        "id": order_id,
        "customer_name": customer_name,
        "dishes": ordered_dishes,
        "status": "received"
    }

    orders.append(order)
    save_data(orders, orders_filename)
    return jsonify(message=f'Order placed successfully with ID {order_id}'), 201
@app.route("/update_order/<int:order_id>", methods=['PATCH'])
def update_order(order_id):
    data = request.get_json()

    # Validate input
    new_status = data.get('status')
    if not new_status:
        abort(400, 'Invalid input data. Please provide status.')

    for order in orders:
        if order['id'] == order_id:
            order['status'] = new_status
            save_data(orders, orders_filename)
            return jsonify(message=f'Order {order_id} status updated to {new_status}'), 200

    abort(404, f'Order with id {order_id} not found.')




if __name__ == '__main__':
    unittest.main()
    app.run(debug=True)
 