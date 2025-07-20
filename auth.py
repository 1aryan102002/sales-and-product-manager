from db import get_connection
current_user = {"username": None, "role": None}
def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    # check if user is already in the database 
    cursor.execute("SELECT *  FROM user WHERE user_name = %s",(username,))#usename,   the ',' is very imp beacause it is a tuple
    if cursor.fetchone():
        print("user is laready in the database try using an different username")
        return
    #register new user 
    else:
        cursor.execute("INSERT INTO user (user_name,password_user) VALUES (%s, %s)",(username, password))
        conn.commit()
        print("user seccessfuklly registered ")
        cursor.close()
        conn.close()# always remember to close it 


def login_user():
    print("login required to proced")
    
    
    while True:
        conn = get_connection()
        cursor = conn.cursor()
        username = input("enter username")
        password = input("enter password")
        cursor.execute("SELECT * FROM user WHERE user_name = %s AND password_user = %s",(username, password))
        user  = cursor.fetchone()
        cursor.close()
        conn.close()

        if user :
            current_user["username"]=user[0]
            current_user["role"]= user[1]
            print("login secuessfull")
            break
        return True
    print("invalid username or password try again")
    return False



