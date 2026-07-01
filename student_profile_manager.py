interests=["singing","music"]
profile={"name":"Dua","class":"10th","age":int(16),"interests":interests}
# Function for viewing profile
def view_profile():
    print(profile)
# Function for updating age
def update_age(new_age):
    profile["age"]=new_age
# Function for updating name
def update_name(new_name):
    profile["name"]=new_name
# Function for adding interest
def add_interest(new_interest):
    interests.append(new_interest)
# Function for removing interest
def remove_interest(particular_interest):
    interests.remove(particular_interest)
# Actual Code
user_input=int(input("Enter your choice: \n 1- View profile,\n 2- Updating age,3 for updating name,4 for adding interest,5 for removing interest and 6 for exit:"))
while True:
    match user_input:
        case 1:
            view_profile()
        case 2:
            update_age(input("Enter the updated age:"))
        case 3:
            update_name(input("Enter the new name:"))
        case 4:
            add_interest(input("Enter the interest which you want to add:"))
        case 5:
            remove_interest(input("Enter the interest which you want to remove:"))
        case 6:
         print("Exit")
         break 
        case _:
            print("Invalid Input")
    user_input=int(input("Enter 1 for viewing profile,2 for updating age,3 for updating name,4 for adding interest,5 for removing interest and 6 for exit:"))    