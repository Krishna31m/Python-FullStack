from databse import insert_user, get_user, update_user, get_user_by_id, delete_user


while True:
    print("Enter the Option: ")
    print("1: Create User")
    print("2: Update User")
    print("3: Delete User")
    print("4: Get All Users")
    print("5: Get User by ID")
    print("6: Exit")
    options = int(input("Options: "))

    if options == 1:
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        insert_user(name, email)
        print("User Added Successfully.")
        print(get_user())

    elif options == 2:
        user_id = int(input("Enter user ID: "))
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        update_user(user_id, name, email)
        print("User Updated Successfully.")

    elif options == 3:
        user_id = int(input("Enter user ID to delete: "))
        delete_user(user_id)
        print("Deleted Successfully.")

    elif options == 4:
        users = get_user()
        print("All users:")
        for user in users:
            print(user)

    elif options == 5:
        user_id = int(input("Enter user ID: "))
        user = get_user_by_id(user_id)
        print("User by given ID:")
        print(user if user else "User not found.")

    elif options == 6:
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again.")

 
