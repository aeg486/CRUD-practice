file_name = "data/products.csv"
with open(file_name, "r") as file:
    prod_ct = file.read()
    lines = prod_ct.split("\n")
    # print(prod_ct)

print("----------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------")
print("Welome @aeg486!")
print("")
print("There are", len(lines) - 2, "products in the database")
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
user_op = input(user_input).title()

def list_prod():
    print("LISTING PRODUCTS")
def show_prod():
    print("SHOWING PRODUCTS")
def edit_list():
    print("CREATING PRODUCTS")
def updt_list():
    print("UPDATING PRODUCTS")
def term_prod():
    print("DESTROYING PRODUCTS")

if user_op == "List": list_prod()
elif user_op == "Show": show_prod()
elif user_op == "Create": edit_list()
elif user_op == "Update": updt_list()
elif user_op == "Destroy": term_prod()
else:
    print("Invalid input. Please try again.")
