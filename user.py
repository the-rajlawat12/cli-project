# cool
#git init 
#git add .
#git commit -m "your message.."\
#copied from github repository
#git remote add origin https://github.com/the-rajlawat12/cli-project.git
# git branch -M main
#git push -u origin main 

#After changing any file: git status(checks what happend)
#git diff (file bhitra kk change bhako cha tyo hercha)
#press q to get out ..agadi ko check garna :f and back:b
#git add .
#git commit -m "your message.."
#git push -u origin main
import sqlite3

def create_con():
    try:
        con=sqlite3.connect("Users.sqlite")
        return con
    except Exception as e:
        print(f"Error:,{e}")



Input_string="""
Enter the options:
1.CREATE TABLE
2.DUMP user from csv INTO users TABLE
3.ADD new user INTO users TABLE
4.QUERY all users from TABLE
5.QUERY user by id from table
6.QUERY specified no. of records from table
7.DELETE all users
8.DELETE user by Id
9.UPDATE user
10.PRESS any key to EXIT
"""

def create_table(con):
    table_query="""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name CHAR(255) NOT NULL,
        last_name CHAR(255) NOT NULL,
        company_name CHAR(255) NOT NULL,
        address CHAR(255) NOT NULL,
        city CHAR(255) NOT NULL,
        county CHAR(255) NOT NULL,
        state CHAR(255) NOT NULL,
         zip REAL NOT NULL,
        phone1 CHAR(255) NOT NULL,
        phone2 CHAR(255) NOT NULL,
        email CHAR(255) NOT NULL,
        web text
        );
    """
    cur=con.cursor()
    cur.execute(table_query)
    print("user table successfully created..")
  #2  
import csv
def read_csv():
    users=[]
    with open("sample_users.csv","r") as f: 
        data=csv.reader(f)
        for user in data:
            users.append(tuple(user))
    # print(user)
    return users[1:] #since the first list is of columns of headings

def insert(con,users):
    insert_query= """
        INSERT INTO  users
    (
            
        first_name ,
        last_name ,
        company_name ,
        address ,
        city,
        county ,
        state ,
        zip ,
        phone1 ,
        phone2 ,
        email,
        web 
                
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
    """
    cur=con.cursor()
    cur.executemany(insert_query,users)
    con.commit()
        
    print(f"{len(users)} user were imported successfully..")
    #3
# def taking_input():
#     fn=input("Enter the first name:")
#     ls=input("Enter the last  name:")
#     cn=input("Enter the company name:")
#     add=input("Enter the address :")
#     city=input("Enter the city name:")
#     county=input("Enter the county :")
#     state=input("Enter the state:")
#     zip=input("Enter the zip:")
#     phone1=input("Enter number:")
#     phone2=input("Enter number:")
#     email=input("Enter email:")
#     web=input("Enter web:")
#     return fn,ls,cn,add,city,county,state,zip,phone1,phone2,email,web
    
# def add_user(con,userData):
   
#     # fn,ls,cn,add,city,county,state,zip,phone1,phone2,email,web=userData #tuple unpacking


#     add_query="""
#     INSERT INTO  users
#     (
            
#         first_name ,
#         last_name ,
#         company_name ,
#         address ,
#         city,
#         county ,
#         state ,
#         zip ,
#         phone1 ,
#         phone2 ,
#         email,
#         web 
                
#     )
#     VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
#     """
#     cur=con.cursor()
#     cur.execute(add_query,userData)
#     con.commit()
#     print("user data inserted successfully.")
columns=("first_name","last_name","company_name","address","city","county","state","zip","phone1","phone2","email","web")
        
    
    #4
def select_user(con):
    cur=con.cursor()
    users=cur.execute("SELECT * FROM users")
    for user in users:
     print(user)
#5
def select_user_by_id(con,user_id):
    cur=con.cursor()
    users=cur.execute("SELECT * FROM users WHERE id=?;",(user_id,))
    for user in users:
        print(user)
#6
def select_specified_records(con,no_of_users=0):
    cur=con.cursor()
    if no_of_users: #boolean value checking
        users=cur.execute("SELECT * FROM users LIMIT ? ",(no_of_users,))
    # else:
    #     users=cur.execute("SELECT * FROM users")
    for user in users:
        print(user)
        
#7DELETE all users
def delete_all(con):
    cur=con.cursor()
    cur.execute("DELETE FROM users ")
    con.commit()
    print("All records deleted successfully")
# 8.DELETE user by Id
def delete_by_id(con,id):
    cur=con.cursor()
    cur.execute("DELETE FROM users WHERE id=?;",(id,))
    con.commit()
    print(f"[{id}] has been deleted successfully")
# 9.UPDATE user
# def data():
#     id=int(input("Enter the id record you want to update:"))
#     fn=input("Enter the first name you want to update:")
#     return id,fn
   
def update(con,user_id,col_name,col_value):

    cur=con.cursor()
    cur.execute(f"UPDATE users SET {col_name} = ? WHERE id = ?",(col_value,user_id))
    con.commit()
    print(f"[{col_name}] was updated successfully with value[{col_value}] of user id [{user_id}]")
    


def main():
    con=create_con()
    user_input=input(Input_string)
    if user_input =="1":
        create_table(con)
    elif user_input=="2":
        users=read_csv()
        insert(con,users)
    elif user_input=="3":
    #    user=taking_input()
    #    add_user(con,user)
        data=[]
        for column in columns:
            col_value=input(f"Enter the value  of {column}:")
            data.append(col_value)
        insert(con,[tuple(data)]) #list bhitra tuple:execute many
    elif user_input=="4":
        select_user(con)
    elif user_input=="5":
        user_id=input("Enter the id you want to see the details of:")
        if user_id.isnumeric():
            select_user_by_id(con,user_id)
    elif user_input=="6":
        # select_user(con)
       user=input("Enter no. of users:")
       if user.isnumeric() and int(user)>0:
        select_specified_records(con,user)
    elif user_input=="7":
        confirm=input("ARE YOU SURE ? (Y/N):")
        if confirm=="Y":
            delete_all(con)
    elif user_input=="8":
        # select_user(con)
        user_id=input("Enter the id you want to remove from the table:")
        if user_id.isnumeric():
            delete_by_id(con,user_id)
    elif user_input=="9":
        # select_user(con)
        # inp=data()
        # update(con,inp)
        id=input("Enter the id record you want to update:")
        if id.isnumeric():
            col_name=input(f"Enter column name.Make sure it in is {columns}:")
        if col_name in columns:
            col_value=input(f"Enter the value of {col_name}:")
            update(con,id,col_name,col_value)
        
    else :
        print("ENter any key to exit:")
        exit()
       

        
main()