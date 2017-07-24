import csv

file_name = "data/products.csv"
inventory = []

def get_total(product): return int(product["id"])

def auto_id():
    new_id = map(get_total, inventory)
    return max(new_id) + 1


#program interface

with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        count += 1

print("----------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------")
print("Welome @aeg486!")
print("")
print("There are", int(count), "products in the database.")
print("")
print("Operation  |  Description")
print("---------- | ----------------------")
print(" 'List'    | Display a list of product identifiers and names.")
print(" 'Show'    | Show information about a product.")
print(" 'Create'  | Add a new product.")
print(" 'Update'  | Edit an existing product.")
print(" 'Destroy' | Delete an existing product.")
print(" 'End'     | Complete changes and update inventory.")
print("")

# read data from csv file and input into inventory list

with open(file_name, "r") as file:
    prod_library = csv.DictReader(file)
    for clean in prod_library:
        inventory.append(dict(clean))

# function implementation

def item_list():
    print("Below is the current list of products in the database:")
    for x in range(0,len(inventory)):
        print("+", inventory[x]["id"], ":", inventory[x]["name"], ":", inventory[x]["aisle"], ":", inventory[x]["department"], ":", inventory[x]["price"])

def show_prod():
    while True:
        try:
            id_num = input("Input Product ID #:")
            if any (d['id'] == id_num for d in inventory):
                print("Product Retrieved! - ", inventory[int(id_num)])
            else:
                print('Input error. Please try again.')
                continue
        except:
            if id_num.upper() == 'DONE':
                break

def edit_list():
    print('Please enter new product information:')
    new_products = {"id": auto_id() }
    new_products['name'] = input('Name: ').title()
    new_products['aisle'] = input('Aisle: ').title()
    new_products['department'] = input('Department: ').title()
    new_products['price'] = input('Price: ')
    print('Product Created!')
    print("Name:", new_products['name'], ";", "Aisle:", new_products['aisle'],";", "Department:", new_products['department'],";","Price:", new_products['price'])
    return inventory.append(new_products)



def updt_list():
    while True:
        current_id = input("Enter the product identifier for the item you wish to UPDATE: ")
        try:
            if any (d['id'] == current_id for d in inventory):
                print("Product Retrieved! - ", inventory[int(current_id)-1])
                inventory[int(current_id)]['name'] = input('Name: ')
                inventory[int(current_id)]['aisle'] = input('Aisle: ')
                inventory[int(current_id)]['department'] = input('Department: ')
                inventory[int(current_id)]['price'] = input('Price: ')
                print('Product Updated!')
                print(inventory[int(current_id)])
            else:
                print("Input error. Please try again.")
                continue
        except:
            if current_id.upper() == 'DONE':
                break
        return inventory

def term_prod():
    term_id = input("Enter the product identifier for the item you wish to DELETE: ")
    if any (d['id'] == term_id for d in inventory):
        print("Product removed from inventory!", inventory[int(term_id)-1])
        del inventory[int(term_id)-1]
    else:
        print("Input error. Please try again.", term_id)
    return inventory

while True:
    user_input = "Please choose an operation from the list above:"
    user_op = input(user_input).title()
    try:
        if user_op == "List":
             item_list()
        elif user_op == "Show":
             show_prod()
        elif user_op == "Create":
            edit_list()
        elif user_op == "Update":
            updt_list()
        elif user_op == "Destroy":
            term_prod()
        elif user_op == "End":
            break
    except:
        print("Invalid input. Please try again.")

with open(file_name, "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for product in inventory:
        writer.writerow(product)
