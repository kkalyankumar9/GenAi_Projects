import snack_inventory
import record

def add_snack():
    snack_name = input("Enter the snack name: ")
    snack_price = float(input("Enter the snack price: ₹"))
    current_inventory = snack_inventory.snack_inventory
    snack_id = max(current_inventory.keys(), default=0) + 1
    current_inventory[snack_id] = {"name": snack_name, "price": snack_price, "availability": True}
    print(f"{snack_name} has been added to the inventory with ID: {snack_id}")

    with open("snack_inventory.py", "w") as file:
        file.write("snack_inventory = " + repr(current_inventory))

    # Adding record
    record_entry = f"Added: {snack_name} (ID: {snack_id})"
    record.record.append(record_entry)

def remove_snack():
    current_inventory = snack_inventory.snack_inventory
    print("Current Inventory:")
    for snack_id, snack_details in current_inventory.items():
        print(f"ID: {snack_id}, Name: {snack_details['name']}, Price: ₹{snack_details['price']}, Availability: {snack_details['availability']}")
    snack_id_to_remove = int(input("Enter the ID of the snack to remove: "))
    if snack_id_to_remove in current_inventory:
        removed_snack_name = current_inventory.pop(snack_id_to_remove)['name']
        print(f"{removed_snack_name} with ID {snack_id_to_remove} has been removed from the inventory.")
        with open("snack_inventory.py", "w") as file:
            file.write("snack_inventory = " + repr(current_inventory))

        # Adding record
        record_entry = f"Removed: {removed_snack_name} (ID: {snack_id_to_remove})"
        record.record.append(record_entry)
    else:
        print("Invalid snack ID. No snack removed.")

def update_snack_availability():
    current_inventory = snack_inventory.snack_inventory
    print("Current Inventory:")
    for snack_id, snack_details in current_inventory.items():
        print(f"ID: {snack_id}, Name: {snack_details['name']}, Price: ₹{snack_details['price']}, Availability: {snack_details['availability']}")
    snack_id_to_update = int(input("Enter the ID of the snack to update: "))
    if snack_id_to_update in current_inventory:
        new_availability = input("Enter the new availability (True or False): ").capitalize()
        if new_availability == "True":
            new_availability = True
        elif new_availability == "False":
            new_availability = False
        else:
            print("Invalid availability status. Please enter True or False.")
            return
        current_inventory[snack_id_to_update]['availability'] = new_availability
        print(f"Availability of snack with ID {snack_id_to_update} has been updated to {new_availability}.")
        with open("snack_inventory.py", "w") as file:
            file.write("snack_inventory = " + repr(current_inventory))

        # Adding record
        record_entry = f"Updated availability: Snack ID: {snack_id_to_update} - New Availability: {new_availability}"
        record.record.append(record_entry)
    else:
        print("Invalid snack ID. No snack updated.")

# Main program
inputdata = int(input("Enter which operation you want: 1 for add, 2 for remove, 3 for update: "))
if inputdata == 1:
    add_snack()
elif inputdata == 2:
    remove_snack()
elif inputdata == 3:
    update_snack_availability()
else:
    print("Invalid choice.")

# Print records after operations
print("Records:")
for entry in record.record:
    print(entry)
