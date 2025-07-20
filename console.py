from auth import login_user, current_user, register_user
from coustomer import coustomer_menu
from product import product_menu
from order import order_menu
from sales import sales_manager


def main_console():
    while True:
        print("Welcome to the Sales and Product Management Console")
        print("1. login")
        print("2. Customers")
        print("3. Products")
        print("4. Orders")
        print("5. sales")
        print("5. Exit")

        choice = input("enter the choice")

        if choice == "1":
            login_user()
        elif choice == "2":
            coustomer_menu()
        elif choice == "3":
            product_menu()
        elif choice == "4":
            order_menu()
    
        elif choice == "5":
            sales_manager()
        elif choice == "6":
            print("Exiting the console. Goodbye!")
            break
        else:
            print("invaild choice")


if __name__ == "__main__":
    main_console()           


            