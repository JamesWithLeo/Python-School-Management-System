import mysql.connector

school_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="schoolsys_db"
)
mycursor = school_db.cursor(buffered=True, dictionary=True)
def commit_transact():
    school_db.commit()


def cursor_exe(sql_code:str,target):
    mycursor.execute(sql_code,target)

sql_get_all_info = "SELECT * FROM student WHERE gmail_account = (%s)"
sql_get_student_gmail = "SELECT gmail_account,passwrd FROM student WHERE gmail_account = (%s)"
# sql_get_student_password = "SELECT passwrd FROM student WHERE gmail_account = (%s)"

sql_get_name = "SELECT name FROM student WHERE gmail_account = (%s)"
sql_get_middle_name = "SELECT middle_name FROM student WHERE gmail_account = (%s)"
sql_get_last_name = "SELECT last_name FROM student WHERE gmail_account = (%s)"

insert_new_student = (
    "INSERT INTO enrollee" # 20 columns
    "(gmail_account,phone_no,passwrd,name,middle_name,last_name,suffix_name,\
gender,date_birth,age,street,barangay,municipality,zipcode,civil_status,religion,\
nationality,birth_place,course,year_level,good_moral,grade_f138)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
)

insert_old_student = (
    "INSERT INTO student" # 20 columns
    "(gmail_account,phone_no,passwrd,name,middle_name,last_name,suffix_name,\
gender,date_birth,age,street,barangay,municipality,zipcode,civil_status,religion,\
nationality,birth_place,course,year_level)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
)



# for profesional job position e.g: security guard, admin staff,& professor 
insert_applicant_with_cert = (
    "INSERT INTO applicant"
    "(gmail,phone_no,password,role,name,middle_name,last_name,suffix_name,\
college_degree,street,municipality,barangay,contact_no,resume,certificate)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            )

insert_applicant = (
    "INSERT INTO applicant"
    "(gmail,phone_no,password,role,name,middle_name,last_name,suffix_name,\
college_degree,street,municipality,barangay,contact_no,resume)" 
"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
)




sql_get_staff_gmail = "SELECT role, gmail_role FROM staff WHERE gmail_role = (%s)"
get_password_in_admin = "SELECT password FROM ADMIN WHERE gmail = (%s)"

# sql_get_staff_password = "SELECT password FROM (%s) WHERE gmail = (%s)"
# sql_get_staff_role = "SELECT role FROM staff WHERE gmail = (%s)"
password_in_table = "SELECT password FROM (%s) WHERE gmail = (%s)"


