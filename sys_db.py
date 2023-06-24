import mysql.connector


school_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="user password",
    database="name of database"
)
mycursor = school_db.cursor(buffered=True, dictionary=True)

def commit_transact():
    school_db.commit()


def cursor_exe(sql_code:str,target):
    mycursor.execute(sql_code,target)

sql_get_all_info = "SELECT * FROM student WHERE gmail_account = (%s)"
sql_get_gmail = "SELECT gmail_account FROM student WHERE gmail_account = (%s)"
sql_get_password = "SELECT passwrd FROM student WHERE gmail_account = (%s)"

sql_get_name = "SELECT name FROM student WHERE gmail_account = (%s)"
sql_get_middle_name = "SELECT middle_name FROM student WHERE gmail_account = (%s)"
sql_get_last_name = "SELECT last_name FROM student WHERE gmail_account = (%s)"
