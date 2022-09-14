from UserDao import UserDao
from User import User

def menu():
    try:
        option = 0
        while option != 5:
            print("""
                    1_Select all users
                    2_Insert user
                    3_Delete user
                    4_Update user
                    5_Exit
                    """)
            option = int(input("select an option: "))
            if option == 1:
                UserDao.selectAll()
            elif option == 2:
                id = int(input("enter the user id: "))
                name = input("user name: ")
                password = input("password: ")
                UserDao.insertUser(User(id, name, password))
            elif option == 3:
                id = int(input("enter the user id: "))
                UserDao.deleteUser(id)
            elif option == 4:
                id = int(input("enter the user id to update: "))
                name = input("User name: ")
                password = input("Password: ")
                UserDao.updateUser(User(id, name, password))
            elif option == 5:
                print("Goodbye")
            else:
                print("Invalid option")
    except Exception as ex:
        print(f"An exception ocurred: {ex}")

menu()

