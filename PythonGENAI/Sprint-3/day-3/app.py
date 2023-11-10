from flask import Flask, request, jsonify
from db import create_connection

app = Flask(__name__)

# Get the database connection
connection = create_connection()
# API endpoint for Menu Management
@app.route('/menu', methods=['GET', 'POST',"PATCH","DELETE"])
def menu():
    if request.method == 'GET':
        # Implement logic to retrieve menu items
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM menu_items")
        menu_items = cursor.fetchall()
        cursor.close()
      
        return jsonify({"menu_items": menu_items,"total_items":len(menu_items)})

    elif request.method == 'POST':
        # Implement logic to add a new menu item
        data = request.json
        # Extract item attributes from data dictionary
        item_name = data.get("name")
        item_description = data.get("description")
        item_price = data.get("price")
        item_availability = data.get("availability")

        # Insert into the database
        cursor = connection.cursor()
        insert_query = "INSERT INTO menu_items (name, description, price, availability) VALUES (%s, %s, %s, %s)"
        values = (item_name, item_description, item_price, item_availability)
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()

        return jsonify({"message": "Add new menu item", "data": data})
# API endpoint for updating and deleting a menu item using ID in URL parameters
@app.route('/menu/<int:item_id>', methods=['PATCH', 'DELETE'])
def update_or_delete_menu_item(item_id):
    if request.method == 'PATCH':
        # Implement logic to update a menu item
        data = request.json
       

        cursor = connection.cursor()
        update_query = "UPDATE menu_items SET name = %s, description = %s, price = %s, availability = %s WHERE id = %s"
        values = (data.get("name"), data.get("description"), data.get("price"), data.get("availability"), item_id)
       
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()

        return jsonify({"message": "Update menu item", "data": data})

    elif request.method == 'DELETE':
        # Implement logic to delete a menu item
        cursor = connection.cursor()
        delete_query = "DELETE FROM menu_items WHERE id = %s"
        values = (item_id,)
        cursor.execute(delete_query, values)
        connection.commit()
        cursor.close()

        return jsonify({"message": "Delete menu item", "item_id": item_id})



# API endpoint for Order Handling
@app.route('/orders', methods=['GET', 'POST', 'PUT'])
def orders():
    if request.method == 'GET':
        # Implement logic to retrieve orders based on criteria
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        cursor.close()
      
        return jsonify({"orders": orders,"total_items":len(orders)})
        
    
    elif request.method == 'POST':
        # Implement logic to accept new orders
        data = request.json
        customer_name = data.get("customer_name")
        item_ids = data.get("item_ids")

        # Insert order details into the database
        insert_order_query = "INSERT INTO orders (customer_name) VALUES (%s)"
        cursor.execute(insert_order_query, (customer_name,))
        order_id = cursor.lastrowid

        # Insert order items into the database
        insert_order_item_query = "INSERT INTO order_items (order_id, item_id) VALUES (%s, %s)"
        for item_id in item_ids:
            cursor.execute(insert_order_item_query, (order_id, item_id))

        connection.commit()
        cursor.close()

        return jsonify({"message": "Order accepted", "order_id": order_id})
    elif request.method == 'PUT':
        # Update order statuses
        data = request.json
        order_id = data.get("order_id")
        new_status = data.get("new_status")

        # Update order status in the database
        update_order_query = "UPDATE orders SET status = %s WHERE id = %s"
        cursor.execute(update_order_query, (new_status, order_id))
        connection.commit()
        cursor.close()

        return jsonify({"message": "Order status updated", "order_id": order_id, "new_status": new_status})



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
