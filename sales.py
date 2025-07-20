from db import get_connection
from auth import current_user

conn = get_connection()
cursor = conn.cursor()

def view_all_sales():
    try:
        if current_user["role"] == "sales_manager":
            cursor.execute("SELECT * FROM sales")
            sales_results = cursor.fetchall()
            if not sales_results:
                print("No sales records found.")
            else:
                print("Sales Records:")
                for row in sales_results:
                    print(f"ID: {row[0]}, coustomer_id: {row[1]}, product_id: {row[2]}, quanty: {row[3]}, sale_date: {row[4]}, price: ₹{row[5]}")
        else:
            print("You do not have permission to view sales records.")
    except Exception as e:
        print(f"Error: {e}")

def view_sales_by_date():
    try:
        if current_user["role"] == "sales_manager":
            date = input("Enter the date (YYYY-MM-DD): ")
            cursor.execute("SELECT * FROM sales WHERE sale_date = %s", (date,))
            sales_results = cursor.fetchall()
            if not sales_results:
                print("No sales records found for that date.")
            else:
                print(f"Sales Records for {date}:")
                for row in sales_results:
                    print(f"ID: {row[0]}, coustomer_id: {row[1]}, product_id: {row[2]}, quanty: {row[3]}, sale_date: {row[4]}, price: ₹{row[5]}")
        else:
            print("You do not have permission to view sales records.")
    except Exception as e:
        print(f"Error: {e}")

def sales_summary():
    try:
        if current_user["role"] == "sales_manager":
            cursor.execute("SELECT SUM(price) FROM sales")
            total_sales = cursor.fetchone()[0] or 0
            cursor.execute("SELECT COUNT(*) FROM sales")
            total_orders = cursor.fetchone()[0]
            print(f"Total Sales: ₹{total_sales}, Total Orders: {total_orders}")
        else:
            print("You do not have permission to view sales summary.")
    except Exception as e:
        print(f"Error: {e}")

def search_sales():
    try:
        if current_user["role"] == "sales_manager":
            search_term = input("Enter the search term (coustomer_id, product_id, or quanty): ")
            if not search_term.isdigit():
                print("Please enter a valid number.")
                return
            cursor.execute(
                "SELECT * FROM sales WHERE coustomer_id = %s OR product_id = %s OR quanty = %s",
                (search_term, search_term, search_term)
            )
            sales_results = cursor.fetchall()
            if not sales_results:
                print("No sales records found for that search term.")
            else:
                print("Search Results:")
                for row in sales_results:
                    print(f"ID: {row[0]}, coustomer_id: {row[1]}, product_id: {row[2]}, quanty: {row[3]}, sale_date: {row[4]}, price: ₹{row[5]}")
        else:
            print("You do not have permission to search sales records.")
    except Exception as e:
        print(f"Error: {e}")

def sales_manager():
    while True:
        print("\n--- SALES MANAGER MENU ---")
        print("1. View all sales")
        print("2. View sales by date")
        print("3. Sales summary")
        print("4. Search sales")
        print("5. Exit Sales Manager Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_sales()
        elif choice == "2":
            view_sales_by_date()
        elif choice == "3":
            sales_summary()
        elif choice == "4":
            search_sales()
        elif choice == "5":
            print("Exiting Sales Manager Menu.")
            break
        else:
            print("Invalid input.")