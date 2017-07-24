import csv
import re
file_name = "data/products.csv"

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
print("There are", int(count), "products in the database")
print("")
print("Operation  |  Description")
print("---------- | ----------------------")
print(" 'List'    | Display a list of product identifiers and names.")
print(" 'Show'    | Show information about a product.")
print(" 'Create'  | Add a new product.")
print(" 'Update'  | Edit an existing product.")
print(" 'Destroy' | Delete an existing product.")
print(" 'End'     | Close and write to file.")
print("")

#user_input = "Please choose an operation from the list above: "
#user_op = input(user_input).title()

#def list_prod(): print("LISTING PRODUCTS")
#def show_prod(): print("SHOWING PRODUCTS")
#def edit_list(): print("CREATING PRODUCTS")
#def updt_list(): print("UPDATING PRODUCTS")
#def term_prod(): print("DESTROYING PRODUCTS")

if user_op == "List": list_prod()
elif user_op == "Show": show_prod()
elif user_op == "Create": edit_list()
elif user_op == "Update": updt_list()
elif user_op == "Destroy": term_prod()
else: print("Invalid input. Please try again.")

# print the entire contents of the inventory CSV file

file_name = "data/products.csv"

with open(file_name, "r") as file:
    prod_ct = file.read()
    lines = prod_ct.split("\n")
    print(prod_ct)

# loop through each product in the inventory and print the name of each

with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])

# print the number of products in the inventory

with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        count += 1
    print(count)

# Write some random content to a temporary file

test = "data/test_me.csv"
with open(test, "w") as file:
    content = "Hello, World!"
    file.write(content)

# Read the existing inventory and write to a separate, temporary file

write_test = "data/write-me.csv"
with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    with open(write_test, "w") as file:
        for row in reader:
            file.write(row["name"] + "\n")

# Read existing inventory and overwrite that file with its original contents

column = ["id", "name", "aisle", "department", "price"]
with open(file_name, "r+") as file:
    text = file.read()
    text = re.sub(text, text, text)
    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()
