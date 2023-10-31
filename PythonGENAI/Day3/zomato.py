import  json
import random
def load_data():
    try:
        with open('menu.json', 'r') as file:
            data = json.load(file)
        return data
      
    except FileNotFoundError:
        return []
menu = load_data()
def load_data_order():
    try:
        with open('orders.json', 'r') as file:
            data = json.load(file)
        return data
      
    except FileNotFoundError:
        return []
order = load_data_order()
# print(order)
# Save menu data to JSON file
def save_data(menu):
    with open('menu.json', 'w') as file:
        json.dump(menu, file)
# Save order data to JSON file
def save_data_oder(order):
    with open('orders.json', 'w') as file:
        json.dump(order, file)


def add_dish(menu):

    dish_name=input("Enter dish_name:")
    price=input("Enter price:")
    availability=input("Enter availability yes/no:")
    menu.append({"dish_id":len(menu)+1,"dish_name":dish_name,"price":price,"availability":availability})
    save_data(menu)
    




def remove_dish(menu):
    for item in menu:
        print(f"Dish ID: {item['dish_id']}, Dish Name: {item['dish_name']}")
    
    enter_id=input("Enter the order_id of the dish you want to remove:")
    for dish in menu:
        if(int(enter_id)==dish["dish_id"]):
            menu.remove(dish)
            save_data(menu)
            print(f"Dish with dish_id {enter_id} has been removed.")
            return

          
            



def update_availability(menu):
        for menu_item in menu:
            print(f"Dish ID: {menu_item['dish_id']}, Dish Name: {menu_item['dish_name']},Availability: {menu_item['availability']}")
        enter_id=input("Enter the dish_id of the dish you want to updata:")
        
        found=False
        for dish in menu:
            if (int(enter_id)==dish["dish_id"]):
                new_availability = input("Enter the new availability (yes/no): ")
                dish["availability"]=new_availability
                save_data(menu)
                print(f"Dish with dish_id {enter_id} has been updated.")
                found=True
                break

        if not found:
            print("please check dish_id once")
               
# remove_dish(menu)
# add_dish(menu)

# update_availability(menu)

def order_dish(menu,order):
    for menu_item in menu:
        print(f"Dish ID: {menu_item['dish_id']}, Dish Name: {menu_item['dish_name']}")
    found = False
   
    order_item=input("Place order through by dish name or id:")

    for menu_dish in menu:
        if str(menu_dish["dish_name"])==order_item or str(menu_dish["dish_id"])==order_item:
            dish_id= menu_dish["dish_id"]
            dish_name=menu_dish["dish_name"]
            order_id=random.randint(1,1000)

            order.append({"order_id":order_id,"status":"recieved","dishs":[{"dish_id":dish_id,"dish_name":dish_name,}]})
            save_data_oder(order)
            found=True
            return
    if not found:
        print("Dish not found in the menu.")




# order_dish(menu,order)

def status_update(order):
    for order_item in order:
        print(f"Order ID: {order_item['order_id']}, Order Status: {order_item['status']}")
    status_input =input("which order status update through by dish name or id:")
    for dish in order:
        if str(dish["order_id"])==status_input   :
            new_status=input("Updata the order status preparing/reviewed/ready for pickup/delivered:")
            dish["status"]=new_status
            save_data_oder(order)
            print(f" order status {new_status} has been updated.")
            break

# status_update(order)
def remove_order(order):
    for order_item in order:
        print(f"Dish ID: {order_item['order_id']}, Dish Name: {order_item['status']}")
    
    enter_id=input("Enter the order_id of the dish you want to remove:")
    for dish in order:
        if(int(enter_id)==dish["order_id"]):
            order.remove(dish)
            save_data_oder(order)
            print(f"Dish with dish_id {enter_id} has been removed.")
            return


def review_orders(order):
    print(order)
    

# review_orders(order)
flag=True
while flag:
    print("\nOptions:")
    print("1. Add a dish")
    print("2. Remove a dish")
    print("3. Update the availability")
    print("4. Place an order")
    print("Enter any other number t0 exit")

   
    choice = input("Enter your choice: ")

    if choice == "1":
        add_dish(menu)
    elif choice == "2":
        remove_dish(menu)
    elif choice == "3":
        update_availability(menu)
    elif choice == "4":
        print("\nOptions:")
        print("1. Place an order")
        print("2. Remove a dish")
        print("3. Update order status")
        print("4. Review all orders")
        choice2 = input("Enter your choice: ")
        if choice2 == "1":
            order_dish(menu,order)
        elif choice2 == "2":
            remove_order(order)
        elif choice2 == "3":
            status_update(order)
        elif choice2 == "4":
            review_orders(order)
        else:
            print("Invalid choice. Please try again.")
            break
    else:
        print("Invalid choice. Please try again and exited")
        flag=False
        break

