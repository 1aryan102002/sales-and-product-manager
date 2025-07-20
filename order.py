from db import get_connection
conn = get_connection()
cursor = conn.cursor()

def place_new_order():
    p_name = input("enter the name of the product ")
    coustomer = input("enter the coustomer id")
    cursor.execute("SELECT * FROM coustomer WHERE coustomer_id  = %s",(coustomer,))
    c_results = cursor.fetchone()
    if not c_results:
        print("coustomer is not logged in please login in first then came back to order")
        return
    else:
        cursor.execute("SELECT * FROM Product WHERE product_name = %s",(p_name,))
        p_results = cursor.fetchall()
        if not p_results:
            print("product is not listed ")
            return
        elif len(p_results)>1:
            print("multiple searches found ")
            for row in p_results:
                print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock: {row[3]}")
            p_id= input("enter the product id to proced")
            cursor.execute("SELECT * FROM Product WHERE product_id = %s", (p_id,))
            selected_product = cursor.fetchone()

            if not selected_product:
                print("invalid product id")
                return
            else:
                selected_product = p_results[0]
                p_id = selected_product[0]
                
            price = selected_product[2]

            cursor.execute("INSERT INTO orders (product_id, price, coustomer_id) VALUES (%s, %s, %s)",
                   (p_id, price, coustomer))
            conn.commit()
            print("order placed")

def view_all_orders():
    coustomer = input("enter the coustomer id")
    cursor.execute("SELECT * FROM coustomer WHERE coustomer_id  = %s",(coustomer,))
    c_results = cursor.fetchone()
    if not c_results:
        print("coustomer is not logged in please login in first then came back")
        return
    else:
        cursor.execute("SELECT * FROM orders WHERE coustomer_id = %s",(coustomer,))
        orders_results = cursor.fetchall()
        if not orders_results:
            print("you havent place any orders")
        else:
            print("orders")
            for row in orders_results:
                print(f"ID: {row[0]},  coustomer_id{row[1]}, product_id: {row[2]}, orderd_at: {row[3],}, price: ₹{row[4]}")     

def view_order_details():
    try:
        order_id = int(input("Enter Order ID: "))
    except ValueError:
        print("invalid input")
        return

    cursor.execute("SELECT * FROM orders WHERE id = %s",(order_id,))
    vod_results = cursor.fetchone()
    if not vod_results:
        print("the orderid is either incorrect or DOES NOT EXIST")
        return
    else:
        cursor.execute("SELECT o.id, o.price, o.orderd_at, c.id, c.coustomer_name, " \
        "p.product_id, p.product_name, p.price AS product_price FROM orders o " \
        "INNER JOIN coustomer c ON o.coustomer_id = c.id " \
        "INNER JOIN Product p ON o.product_id = p.product_id WHERE o.id =%s",(order_id,)) 
        details = cursor.fetchone()

    if details:
        print("\nOrder Details:")
        print(f"Order ID      : {details[0]}")
        print(f"Order Price   : ₹{details[1]}")
        print(f"Ordered At    : {details[2]}")
        print(f"\nCustomer Details:")
        print(f"Customer ID   : {details[3]}")
        print(f"Customer Name : {details[4]}")
        print(f"\nProduct Details:")
        print(f"Product ID    : {details[5]}")
        print(f"Product Name  : {details[6]}")
        print(f"Product Price : ₹{details[7]}")
    else:
        print("no details found for this order.")

def cancel_order():
    try:
        order_id = int(input("enter order id to cancel: "))
    except ValueError:
        print("invalid input. please enter a valid order id.")
        return
    cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
    order_can_results = cursor.fetchone()
    if not order_can_results:
        print("Order not found or invalid Order ID.")
        return
    confirm = input(f"are you sure you want to cancel Order {order_id}? (yes/no): ")
    if confirm.lower() == 'yes':
        cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        conn.commit()
        print(f"Order {order_id} has been cancelled.")
    else:
        print("Cancellation aborted.")


def order_menu():
    while True:
        print("\n--- ORDER MENU ---")
        print("1. Place New Order")
        print("2. View All Orders")
        print("3. View Order Details")
        print("4. Cancel Order")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            place_new_order()
        elif choice == "2":
            view_all_orders()
        elif choice == "3":
            view_order_details()
        elif choice == "4":
            cancel_order()
        elif choice == "5":
            break
        else:
            print("Invalid input.")
