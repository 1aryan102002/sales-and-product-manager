from db import get_connection
from auth import current_user

conn = get_connection()
cursor = conn.cursor()

def add_product():
    try:
        print("enter the product details")

        product_name = input("enter the product name: ")
        price = input("enter the price of the product: ")
        stock = input("enter the stock quantity: ")

        cursor.execute("INSERT INTO product(product_name, price, stock) VALUES (%s, %s, %s)",
            (product_name, price, stock))
        conn.commit()
        print("product added successfully")
    except Exception as e:
        print(f"error: {e}")

def view_products():
    try:
        cursor.execute("SELECT * FROM product")
        results = cursor.fetchall()

        if results:
            print("\nproduct List:")
            for row in results:
                print(f"Product_ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock: {row[3]}")
        else:
            print("no products found")
    except Exception as e:
        print(f"error: {e}")

def update_product():
    try:
        while True:
            print("\nwhat do you want to update")
            print("1. Product Name")
            print("2. Price")
            print("3. Stock")
            print("4. Back to Product Menu")

            update_choice = input("enter your choice: ")

            if update_choice == "1":
                old_name = input("enter the current product name: ")

                cursor.execute("SELECT * FROM product WHERE product_name = %s", (old_name,))
                results = cursor.fetchall()

                if not results:
                    print("no product found with that name")
                else:
                    print("matching products:")
                    for row in results:
                        print(f"ID: {row[0]}, Name: {row[1]}")

                    p_id = input("enter the Product ID to update: ")
                    new_name = input("enter the new product name: ")
                    cursor.execute("UPDATE product SET product_name = %s WHERE product_id = %s", (new_name, p_id))
                    conn.commit()
                    print("product name updated")

            elif update_choice == "2":
                p_id = input("enter the Product ID to update price: ")
                new_price = input("enter the new price: ")
                cursor.execute("UPDATE product SET price = %s WHERE product_id = %s", (new_price, p_id))
                conn.commit()
                print("price updated")

            elif update_choice == "3":
                p_id = input("enter the Product ID to update stock: ")
                new_stock = input("enter the new stock quantity: ")
                cursor.execute("UPDATE product SET stock = %s WHERE product_id = %s", (new_stock, p_id))
                conn.commit()
                print("stock updated")

            elif update_choice == "4":
                break
            else:
                print(" invalid choice")

    except Exception as e:
        print(f"⚠️ Error: {e}")

def delete_product():
    try:
        p_name = input("enter the product name to delete: ")
        cursor.execute("SELECT * FROM product WHERE product_name = %s", (p_name,))
        results = cursor.fetchall()

        if not results:
            print("no product found")
            return

        print("matching products:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock: {row[3]}")

        delete_id = input("enter the Product ID to delete: ")
        confirm = input(f"are you sure you want to delete product ID {delete_id}? (yes/no): ")

        if confirm.lower() == 'yes':
            cursor.execute("DELETE FROM product WHERE product_id = %s", (delete_id,))
            conn.commit()
            print("product deleted.")
        else:
            print("deletion cancelled.")

    except Exception as e:
        print(f"error: {e}")

def product_menu():
    if current_user["role"] != "product_manager":
        print("access Denied:--Only product managers can access this menu.")
        return

    while True:
        print("\nProduct Menu ")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")

        choice = input("enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            print("returning to main menu.")
            break
        else:
            print("invalid option. try again.")
