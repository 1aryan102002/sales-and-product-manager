from db import get_connection

conn = get_connection()
cursor = conn.cursor()
def add_new_coustomer():
    try:
        conn
        cursor
        print("enter the details")
        name = (input("enter the name"))
        phone = (input("enter the phone number"))
        address = (input("enter tthe address"))
        while True:
            email = (input("enter the email"))
            cursor.execute("SELECT * FROM coustomer WHERE email = %s", (email,))
            if cursor.fetchone():
                print("email already taken. please enter a different one")
            else:
                query = ("INSERT INTO coustomer (coustomer_name, phone, email, address) VALUES (%s, %s, %s, %s)")
                values = (name, phone, email, address)
                cursor.execute(query,values)
                conn.commit()
                print("customer added")
                break
    
    except Exception as e:
        print(f"error:{e}")

    finally:
        cursor.close()
        conn.close()

def view_coustomer():
    try:
        conn
        cursor

        query1 = "SELECT * FROM coustomer"
        cursor.execute(query1)
        results = cursor.fetchall()

        print("\n Customer List:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}, Address: {row[4]}")

    except Exception as e:
        print(f" Error: {e}")
    finally:
        cursor.close()
        conn.close()

def search_coustomer():
    try:
        conn
        cursor

        coustomer_name = (input("enter the coustomer name"))
        coustomer_id = (input("enter the coustomer id"))

        query2 = "SELECT * FROM coustomer WHERE id =(%s) AND coustomer_name = (%s)"
        cursor.execute(query2, (coustomer_id, coustomer_name))
        result = cursor.fetchone()

        if result:
            print("\n Customer Details:")
            print(f"ID: {result[0]}, Name: {result[1]}, Phone: {result[2]}, Email: {result[3]}, Address: {result[4]}")
        else:
            print(" No matching customer found.")


    except Exception as e:
        print(f" Error: {e}")

    finally:
        cursor.close()
        conn.close()

def update_coustomer():
        conn
        cursor
        try:
            c_name = print(input("enter the name for updation   = "))

            cursor.execute("SELECT id, coustomer_name FROM coustomer WHERE coustomer_name = %s", (c_name,))
            results = cursor.fetchall()
            if not results:
                print("no one found")
                return
            elif len(results)> 1:
                print(f"mutiple users found {c_name}:")
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}")
                c_id = input("Enter your Customer ID to proceed with update: ")
            else:
                c_id = results[0][0]
                print(f"match found with id {c_id}")

            while True:
                
                print("choose the options to update your details\n")

                print("1. name")
                print("2. phone")
                print("3. email")
                print("4. address")
                print("5. exit update menu")

                choice = input("enter your choice \n")

                if choice == "1":
                    while True:
                        
                        replacing_name  = input("enter the new name\n")
                        cursor.execute("SELECT * FROM coustomer WHERE coustomer_name = %s", (replacing_name,))
                        if cursor.fetchone():
                            print(" Username already taken.")
                        else:
                            cursor.execute ("UPDATE coustomer SET coustomer_name = %s WHERE id = %s", (replacing_name,c_id)) 
                            conn.commit()
                            print("update secessfull")
                            break
                elif choice =="2":
                        
                        replacing_phone = input("enter the new phone number\n")
                        cursor.execute("UPDATE coustomer SET phone = %s WHERE id = %s", (replacing_phone, c_id)) 
                        conn.commit()
                        print("phone number is updated ")
                elif choice =="3":
                        while True:
                            
                            replacing_email = input("enter the new email\n")
                            cursor.execute("SELECT * FROM coustomer WHERE email = %s", (replacing_email,))
                            if cursor.fetchone():
                                print("email already taken. please enter a different one")
                            else:
                                cursor.execute("UPDATE coustomer SET email = %s WHERE ID = %s",(replacing_email,c_id))
                                conn.commit()
                                print("email updated sucessfully")
                                break

                elif choice == "4":
                    print("enter the new adress")
                    replacing_address = input()
                    cursor.execute("UPDATE coustomer SET address = %s WHERE id = %s",(replacing_address,c_id))
                    conn.commit()
                    print("address is updated sucessfully")

                elif choice == "5":
                    print("exiting update menu. thank you!")
                    break

                else:
                    print("invalid choice ")
        except Exception as e:
            print(f"error ocurred {e}")
        
        finally:
            cursor.close()
            conn.close()

def delete_customer():
    try:
        conn 
        cursor 

        name = input("enter the customer name to delete: ")
        query = "SELECT id, coustomer_name FROM customer WHERE coustomer_name = %s"
        cursor.execute(query, (name,))
        results = cursor.fetchall()

        if not results:
            print("no customer found with that name.")
            return

        print("\nMatching customers:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}")

        delete_id = input("enter the id you want to delete: ")

        confirm = input(f"Are you sure you want to delete customer ID {delete_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("cancelled.")
            return

        delete_query = "DELETE FROM customer WHERE id = %s"
        cursor.execute(delete_query, (delete_id,))
        conn.commit()

        print("deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")
        
    finally:
            cursor.close()
            conn.close()

def coustomer_menu():
        while True:
            print("\nCustomer Menu:")
            print("1. Add New Customer")
            print("2. View All Customers")
            print("3. Search Customer")
            print("4. Update Customer")
            print("5. Delete Customer")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                add_new_coustomer()
            elif choice == '2':
                view_coustomer()
            elif choice == '3':
                search_coustomer()
            elif choice == '4':
                update_coustomer()
            elif choice == '5':
                delete_customer()
            elif choice == '6':
                print("Exiting customer menu.")
                break
            else:
                print("Invalid choice. Try again.")


