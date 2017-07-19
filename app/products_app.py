file_name = "c:/users/andrew/desktop/crud-practice/data/products.csv"
with open(file_name, "r") as file:
    prod_ct = file.read()
    lines = prod_ct.split("\n")
    # print(prod_ct)

print("----------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------")
print("Welome @aeg486!")
print("")
print("There are ", len(lines) - 2, " products in the database")
print("")
print("Operation  |  Description")
print("---------- | ----------------------")
print(" 'List'    | Display a list of product identifiers and names.")
print(" 'Show'    | Show information about a product.")
print(" 'Create'  | Add a new product.")
print(" 'Update'  | Edit an existing product.")
print(" 'Destroy' | Delete an existing product.")
print("")

user_input = "Please choose an operation from the list above: "
user_op = input(user_input)

if user_op.title() == "List":
    print("LISTING PRODUCTS")
elif user_op.title() == "Show":
    print("SHOWING PRODUCTS")
elif user_op.title() == "Create":
    print("CREATING PRODUCTS")
elif user_op.title() == "Update":
    print("UPDATING PRODUCTS")
elif user_op.title() == "Destroy":
    print("DESTROYING PRODUCTS")
else:
    print("Invalid input. Please try again.")
