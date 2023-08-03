# import json
import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from time import sleep
from datetime import date
from login import *
from signUp import *
from userType import *
# if user is logged this is where user information can be located.
#   this frame can toggle to hide or show .
class Profile:
    def __init__(self,parentFrame,account,accountType) -> None:
        profile_menu_frame = ttk.Frame(
            master=parentFrame,bootstyle='secondary')
        # profile_menu_frame.place(anchor='nw',relheight=1,relwidth=.3)    
        self.frame = profile_menu_frame
        
        def profile_menu_row_col():
            profile_menu_frame.columnconfigure(0,weight=1)
            profile_menu_frame.columnconfigure(1,weight=1)
            profile_menu_frame.columnconfigure(2,weight=1)
            profile_menu_frame.columnconfigure(3,weight=1)
            profile_menu_frame.columnconfigure(4,weight=1)
            profile_menu_frame.rowconfigure(0,weight=1)
            profile_menu_frame.rowconfigure(1,weight=1)
            profile_menu_frame.rowconfigure(2,weight=1)
            profile_menu_frame.rowconfigure(3,weight=1)
            profile_menu_frame.rowconfigure(4,weight=1)
            profile_menu_frame.rowconfigure(5,weight=1)
            profile_menu_frame.rowconfigure(6,weight=1)
            profile_menu_frame.rowconfigure(7,weight=1)
            profile_menu_frame.rowconfigure(8,weight=1)
            profile_menu_frame.rowconfigure(9,weight=1)
            profile_menu_frame.rowconfigure(10,weight=1)
            profile_menu_frame.rowconfigure(11,weight=15)
        profile_menu_row_col()
            
            
        if accountType == 'ADMIN':
            hamburger_hide_bttn = ttk.Frame(
                profile_menu_frame, bootstyle='secondary')
            hamburger_hide_bttn.place(
                relheight=.08,relwidth=.14,relx=.03,rely=.02)
            label_hide_bttn = ttk.Label(borderwidth=0,background='#4e5d6c',
                master=hamburger_hide_bttn)
            label_hide_bttn.place(relheight=1,relwidth=1,relx=.5,rely=.4,anchor='center')
            self.hide_profile_bttn = label_hide_bttn
        else:
            name = ttk.Label(
                profile_menu_frame, text=account.full_name,
                font=('helvetica',12))
            name.grid(column=2,row=4,sticky=tk.W)
            
            stu_id = ttk.Label(
                profile_menu_frame, text=account.stud_id,
                font=('helvetica',12))
            stu_id.grid(column=2,row=5,sticky=tk.W)
            
            course = ttk.Label(
                profile_menu_frame, text=account.course,
                font=('helvetica',12))
            course.grid(column=2,row=6,sticky=tk.W)
            
            gender_and_age = ttk.Label(
                profile_menu_frame, text=account.gender,
                font=('helvetica',12))
            gender_and_age.grid(column=2,row=7,sticky=tk.W)
            
            address = ttk.Label(
                profile_menu_frame, text=account.address,
                font=('helvetica',12))
            address.grid(column=2,row=8,sticky=tk.W)

            hamburger_hide_bttn = ttk.Frame(
                profile_menu_frame, bootstyle='secondary')
            hamburger_hide_bttn.place(
                relheight=.08,relwidth=.14,relx=.03,rely=.02)
            label_hide_bttn = ttk.Label(borderwidth=0,background='#4e5d6c',
                master=hamburger_hide_bttn)
            label_hide_bttn.place(relheight=1,relwidth=1,relx=.5,rely=.4,anchor='center')
            self.hide_profile_bttn = label_hide_bttn
            
    def hide_frame(self):
        self.frame.place_forget()
        
    
    def show_frame(self):
        self.frame.place(anchor='nw',relheight=1,relwidth=.3)

# This class will be the connector to datebase and will communicate -
#   with mainMenu class. to do the fetching and updating .
class databaseAccountConnect:
    def __init__(self,gmail,passw,accountType) -> None:
        if accountType == 'ADMIN':
            return None
        else:
            self.gmail = gmail.get().strip()
            self.password = passw
            
            sys_db.cursor_exe(
                sql_code=sys_db.sql_get_all_info,
                target=[self.gmail,])
            account_row = sys_db.mycursor.fetchone()
            
            name = account_row.get('name')
            middle_name = account_row.get('middle_name')[0]
            last_name = account_row.get('last_name')
            self.full_name = f'{name} {middle_name[0]}. {last_name}'.title()
            
            stu_id = account_row.get('id')
            self.stud_id = stu_id
            
            age = account_row.get('age')
            gender = account_row.get('gender')
            if gender.upper() == 'M':
                self.gender = f'{age} years old, Male'
            else:
                self.gneder = f'{age} years old, Female'
            
            self.course = 'Bachelor of Bsit major in pindot'
            
            
            street = account_row.get('street')
            barangay = account_row.get('barangay')
            municipality = account_row.get('municipality')
            self.address = f'{street} {barangay} {municipality}'.title()
        
        
        
    def fetch_fullname(self):
        self.gmail


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('School System')
        self.style = ttk.Style()
        self.style.configure('.',font=('System 20'))
        # self.iconbitmap('PyclassProject\graduation.ico')
        def app_geometry():
            scrn_w = int((self.winfo_screenwidth()-1000) / 2)
            scrn_h = int((self.winfo_screenheight()-700) / 2)
            self.geometry(f'1000x700+{scrn_w}+{scrn_h}')
            # self.minsize(1000,700)
        app_geometry()
        ttk.Style(theme='superhero')

class Home(ttk.Frame):
    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.root = parent # parent is instance of class App
        self.configure(bootstyle='default')
        self.place(relx=.994,rely=.5,anchor='e',relheight=.98,relwidth=.4)
        # the button reference as bg_design served as border design only .
        bg_design = ttk.Button(
            master=parent, bootstyle='primary-outline',state='disabled')
        bg_design.place(
            relheight=.98, relwidth=.59 , relx=.3,rely=.5, anchor='center')
        # import any picture of school facade .
        image_background = Image.open(
            r'C:\Users\james\OneDrive\Python codes\ecsr.jpg')
        resized_img = image_background.resize((1400,900))
        final_img = ImageTk.PhotoImage(image=resized_img)
        image_cnvs = ttk.Label(
            master=bg_design,bootstyle='secondary')
        image_cnvs.place(
            relx=.5, rely=.5 , relheight=.98, relwidth=.98, anchor='center',)
        image_cnvs.configure(image=final_img)
        
        
        header_login = ttk.Label(
            master=self,bootstyle="default",
            text='LOGIN',font='system 20',)
        header_login.place(
            relx=.5,rely=.12,anchor='center')

        account = accountLogin(self)
        
        def focus_password(event):
            """from gmail_entry focus to password_entry"""
            # clicking enter while the type cursor in gmail entry will move the
            #   cursor to password entry , only if its not whitespace . 
            if account.my_gmail.get() != '':
                account.password_entry.focus_set()
                print('p focus')

        # Once enter key is pressed type cursor will
        #   moves to password entry widget . 
        account.gmail_entry.bind("<Return>",func=focus_password)


        def str_var_gmail_password(click_enter):
            """Login verification"""
            if account.my_gmail.get().strip() == '' and \
                account.my_password.get().strip() == '' :
                account.gmail_entry.configure(bootstyle='danger')
                account.password_entry.configure(bootstyle='danger')
                return None
            elif account.my_gmail.get().strip() == '' and \
                account.my_password.get().strip() != '' :
                account.password_entry.configure(bootstyle='default')
                account.gmail_entry.configure(bootstyle='danger')
                return None
            elif account.my_password.get().strip() == '' and \
                account.my_gmail.get().strip() != '':
                account.gmail_entry.configure(bootstyle='default')
                account.password_entry.configure(bootstyle='danger')
                return None
            
            account.gmail_entry.configure(bootstyle='default')
            account.password_entry.configure(bootstyle='default')
            
            
            # Check account existence/ get the gmail from user then 
            #  match it to database .
            try:
                role = 'STUDENT' # set as default.
                # check the gmail if its student acc, return None in var 
                #   if it doesn't exist there.
                gmail = account.my_gmail.get().strip()
                sys_db.cursor_exe(
                    sql_code=sys_db.sql_get_student_gmail,
                    target=[gmail]
                )
                request_gmail = sys_db.mycursor.fetchone()
                if request_gmail is None:
                    # Now find it in the staff/role table .
                    sys_db.cursor_exe(
                        sql_code=sys_db.sql_get_staff_gmail,
                        target=[gmail]
                    )
                    request_gmail_staff = sys_db.mycursor.fetchone()
                    #  raise error since end user entered account that doesn't.
                    #   -exist in any table in the database .
                    if request_gmail_staff is None:
                        print('account doesnt exist')
                        warn_no_acc_gmail.place(
                        relx=.5 , rely=.564 ,anchor='center')
                        account.border_frame.configure(bootstyle='danger')
                        raise FileNotFoundError
                    else: # get the specific role/position .
                        role = request_gmail_staff.get('role')
                        print(role)
                else:pass
                account.gmail_entry.configure(bootstyle='default')
                account.border_frame.configure(bootstyle='primary')
                warn_no_acc_gmail.place_forget()
            except FileNotFoundError:
                return None 
            else:
                # role is now a specifier for every role/position table.
                if role == 'STUDENT':
                    if account.my_password.get() == request_gmail.get('passwrd'):
                        pass
                        # print(request_gmail)
                    else:
                        account.password_entry.configure(bootstyle='danger')
                        warn_incorrect_pass.place(relx=.41,rely=.4,)
                        return None
                
                elif role == 'ADMIN':
                    sys_db.cursor_exe(
                    sql_code=sys_db.get_password_in_admin,
                    target=[gmail])
                    request_password_staff = sys_db.mycursor.fetchone()
                    if account.my_password.get() == request_password_staff.get('password'):
                        pass
                        # print(request_gmail_staff)
                        # print(request_password_staff)
                    else:
                        account.password_entry.configure(bootstyle='danger')
                        warn_incorrect_pass.place(relx=.41,rely=.4,)
                        return None
                
                elif role == 'TEACHER':pass
                elif role == 'UTILITY':pass
                elif role == 'SECURITY':pass
                else:return None
                
                # if account exist and the password is correct .
                self.account_type = role
                self.my_gmail = account.my_gmail          
                self.my_password = account.my_password
                bg_design.place_forget()
                self.quit()
                # account.gmail_entry.configure(bootstyle='danger')
                account.password_entry.configure(bootstyle='danger')
                # warn_incorrect_pass.place(relx=.41,rely=.4,)
                
                
        # Once enter key pressed, typed gmail and password will be submitted
        #   to  check its existence, authority, and to veritfy .
        # Basically its like loggin_button but it doesn't need mouse to work.
        account.password_entry.bind(
            "<Return>", func=str_var_gmail_password)

        # Following labels is for entries, 
        #   it will only show depending on condition .
        warn_no_entry_gmail = ttk.Label(
            master=account.border_frame,
            text='INVALID GMAIL',
            bootstyle='danger-inversed',justify='center',
            font=('helveltica',10))

        warn_no_acc_gmail = ttk.Label(
            master=self,
            text='Account doesnt\'t exist',
            bootstyle='danger-inversed',justify='right',
            font=('arial',10))

        warn_incorrect_pass = ttk.Label(
            master=account.border_frame,
            text='INCORRECT PASSWORD',
            bootstyle='danger-inversed',justify='center',
            font=('helveltica',8))

        # Main button to check entries then proceed to mainMenu
        loggin_button = ttk.Button(
                account.border_frame, text='LOG IN',
                bootstyle='primary')
        loggin_button.place(
            relx=.5, rely=.83,
            relheight=.15, relwidth=.3, anchor='center')
        loggin_button.bind("<Button-1>",func=str_var_gmail_password,add='+')


        def change_label_onhover(label):
            """Only Reserved for forget account label"""
            label.bind(
                "<Enter>",
                func=lambda l:label.configure(bootstyle='warning'),
                add=True)
            label.bind(
                "<Leave>",
                func=lambda l:label.configure(bootstyle='primary'),
                add=True)


        forget_acc_label = ttk.Label(
            master=self, text='Forgot password?',
            bootstyle='primary',padding=8)
        forget_acc_label.place(
            relx=.5 , rely=.6,anchor='center',
            relheight=.04)
        change_label_onhover(forget_acc_label)
        # forget_acc_label.bind("<ButtonPress>",func=)


        # grab the location for later use .
        pos_x = self.place_info()['relx']
        pos_y = self.place_info()['rely']
        pos_w = self.place_info()['relwidth']
        pos_h = self.place_info()['relheight']
        
        def back_to_log(func,x,y,h,w,target):
            enroll_button.place(
                anchor='center', relx=.5, rely=.9, relheight=.05, relwidth=.2)
            # show back the Login Frame and its child widget then
            #  the hide the enroll frame .
            self.place(relx=x, rely=y, relheight=h, relwidth=w,anchor='e')
            # adjust the canvas .
            bg_design.place_configure(relwidth=.59,relx=.3)
            target.place_forget()
            func()
            


        upload_image_raw = Image.open(r"C:\Users\james\Downloads\upload.png")
        upload_resume_image = upload_image_raw.resize((30,30))
        upload_image = ImageTk.PhotoImage(image=upload_resume_image)
        # func for creating account
        def enroll():
            enroll_button.place_forget()
            self.place_forget() # temporary hides it & place it back again if 
            #   the back_bttn was clicked.
            
            # adjust the canvas(school in the background) to fit the screen .
            bg_design.place_configure(relwidth=.99,relx=.5)
            
            
            enroll_frame = ttk.Frame( # Frame for  creating account .
                master=parent, bootstyle='default')
            enroll_frame.place(
                relx=.5,rely=.5,
                relheight=.8,relwidth=.7,anchor='center')
            
            # use the lambda to pass the arguments .
            # button for exiting creating account/enroll .
            exit_enroll_bttn = ttk.Button(
                enroll_frame,bootstyle='danger',text='EXIT',
                command=lambda:back_to_log(student_widgets.hide_frame,
                    x=pos_x, y=pos_y, 
                    h=pos_h, w=pos_w,target=enroll_frame))
            exit_enroll_bttn.place(
                relx=.932, rely=.05,
                relheight=.06, relwidth=.11, anchor='center')
            
            
            # prompt the enroll_frame with widgets .
            student_widgets = getStudents(enroll_frame,upload_image)
            # ready the guardian frame and its child widgets 
            # place it, if next button is clicked .
            guardian_widgets = getGuardian(enroll_frame)

            def to_save_all():
                """func for placing frame for guardian/parents \n
                and verifying entries"""
                def back_prev_entry(event):
                    # if prev_bttn was clicked remove itself .
                    prev_bttn.place_forget()
                    save_bttn.place_forget()
                    next_bttn.place(
                        relx=.5, rely=.93,relheight=.06,
                        relwidth=.15, anchor='center')
                    student_widgets.display_frame()
                    guardian_widgets.hide_frame()


                def overview():
                    def back_using_prev_bttn(event):
                        to_save_all()
                        verify_button.place_forget()
                        overview_frame.place_forget()
                        prev_bttn.bind(
                            "<Button-1>", func=back_prev_entry)
                    
                    
                    prev_bttn.bind(
                        "<Button-1>", func=back_using_prev_bttn,add='+')
                    
                    save_bttn.place_forget()
                    guardian_widgets.hide_frame()
                    overview_frame = ttk.Frame(enroll_frame)
                    overview_frame.place(
                        relheight=.6,relwidth=.5,
                        relx=.5,rely=.4,anchor='center')
                    
                    
                    
                    
                    student_widgets.verify_gmail(overview_frame)
                    student_widgets.verify_name(overview_frame)
                    student_widgets.verify_bday(overview_frame)
                    student_widgets.verify_gender(overview_frame)
                    student_widgets.verify_status(overview_frame)
                    student_widgets.verify_address(overview_frame)
                    student_widgets.verify_edu(overview_frame)
                    
                    
                    def save_to_database(frame_to_destroy):
                        # the format of the bday should be the same as format
                        #   in mysql ; year-month-day, so switching the index
                        #   of the bday will result some error .
                        bday = [
                            student_widgets.my_year.get(),
                            student_widgets.my_month.get(),
                            student_widgets.my_day.get(),
                        ]
                        YEAR_TODAY = str(date.today())[:4]
                        bday = '-'.join(bday)
                        age = str(int(YEAR_TODAY) - int(bday[:4]))
                        
                        student_datas = [
                            student_widgets.my_gmail.get(),
                            student_widgets.my_phone_no.get(),
                            student_widgets.my_password.get(),
                            student_widgets.my_name.get(),
                            student_widgets.my_middle_name.get(),
                            student_widgets.my_last_name.get(),
                            student_widgets.my_suffix.get(),
                            student_widgets.my_gender.get(),
                            bday,
                            age,
                            student_widgets.my_street.get(),
                            student_widgets.my_barangay.get(),
                            student_widgets.my_municipality.get(),
                            student_widgets.my_zipcode.get(),
                            student_widgets.my_civil_status.get(),
                            student_widgets.my_religion.get(),
                            student_widgets.my_nationality.get(),
                            student_widgets.my_birth_place.get(),
                            student_widgets.my_course.get(),
                            student_widgets.my_college_level.get()
                        ]
                        if (student_widgets.transferee_bool.get() is True):
                            student_datas.append(student_widgets.good_moral)
                            student_datas.append(student_widgets.grade)
                            sys_db.cursor_exe(
                                sql_code=sys_db.insert_new_student,
                                target=student_datas
                            )
                        else:
                            sys_db.cursor_exe(
                                sql_code=sys_db.insert_old_student,
                                target=student_datas
                            )
                        sys_db.commit_transact()
                        frame_to_destroy.place_forget()
                        
                    def verify_question():
                        enroll_frame.place_forget()
                        save_question_f = ttk.Frame(parent)
                        save_question_f.place(
                            relx=.5,rely=.5,
                            relheight=.4,relwidth=.4,anchor='center')
                        label = ttk.Label(
                            save_question_f,text='Confirm to Enroll',
                            font=('helveltica', 20))
                        label.place(
                            relx=.59,rely=.4,
                            relheight=.15,relwidth=.6,anchor='center')
                        
                        yes_bttn = ttk.Button(
                            save_question_f,text='Confirm',
                            bootstyle='success',
                            command=lambda:save_to_database(
                                frame_to_destroy=save_question_f
                            ))
                        yes_bttn.place(
                            relx=.75,rely=.7,
                            relheight=.1,relwidth=.3,anchor='center')
                        
                        def back_to_beginning(event):
                            save_question_f.place_forget()
                            verify_button.place_forget()
                            overview_frame.place_forget()
                            enroll_frame.place(
                                relx=.5,rely=.5,
                                relheight=.8,relwidth=.7,anchor='center')
                            back_prev_entry(event)
                            
                            
                        no_bttn = ttk.Button(
                            save_question_f,text='Cancel',
                            bootstyle='danger')
                        no_bttn.place(
                            relx=.25,rely=.7,
                            relheight=.1,relwidth=.3,anchor='center')
                        no_bttn.bind(
                            "<Button-1>",func=back_to_beginning)
                        
                    verify_button = ttk.Button(
                        enroll_frame,text='VERIFY',
                        command=verify_question,bootstyle='danger',)
                    verify_button.place(
                    relx=.7, rely=.93,relheight=.06,
                    relwidth=.15, anchor='center')
                    
                    

                def submit():
                    guardian = guardian_widgets.get_all_data()
                    if guardian is False:
                        print(False, 'Guardian widget contains empty entry')
                    else:
                        overview()


                student = student_widgets.get_all_data()
                if student is False:
                    print(False, 'Student entries should be filled')
                    return None
                
                student_widgets.hide_frame()
                guardian_widgets.display_frame()
                
                # Remove, then replace it with save button .
                next_bttn.place_forget()
                save_bttn = ttk.Button(
                    enroll_frame, text='SAVE',
                    bootstyle='primary',command=submit)
                save_bttn.place(
                    relx=.7, rely=.93,relheight=.06,
                    relwidth=.15, anchor='center')
                
                # place the back button for going back to student widgets .
                prev_bttn = ttk.Button(
                    master=enroll_frame, text='Back', bootstyle='warning')
                prev_bttn.place(
                    relx=.3, rely=.93,
                    relheight=.06, relwidth=.15, anchor='center')
                prev_bttn.bind(
                    "<Button-1>", func=back_prev_entry)



            next_bttn = ttk.Button(
                master=enroll_frame, text='NEXT', bootstyle='primary',
                command=to_save_all)
            next_bttn.place(
                relx=.5, rely=.93,
                relheight=.06, relwidth=.15, anchor='center')

        def hide_enroll_show():
            """This func is for effect only"""
            account.border_frame.bind(
                "<Enter>",func=lambda b:enroll_button.place_forget())
            account.border_frame.bind(
                "<Leave>",
                func=lambda b:enroll_button.place(
                    anchor='center', relx=.5, rely=.9, 
                    relheight=.05, relwidth=.2))


        enroll_button = ttk.Button(
            image_cnvs, text='ENROLL NOW', bootstyle='success',command=enroll,)
        enroll_button.place(
            anchor='center', relx=.5, rely=.9, relheight=.05, relwidth=.2)
        hide_enroll_show()


        email_icon_raw = Image.open(
            r"C:\Users\james\Downloads\Icons&bg\contact.png")
        email_icon_resized = email_icon_raw.resize((25,25))
        email_icon = ImageTk.PhotoImage(image=email_icon_resized)
        email_frame = ttk.Label(self,image=email_icon,background='#4e5d6c',anchor='center')
        email_frame.place(relheight=.05,relwidth=.08,relx=.95,rely=.028,anchor='center')
        
        contact_us = ttk.Label(
            self,text='Contact no. : 09123456789 | EMAIL: NameOfUni@fb.com',
            bootstyle='secondary-inversed',anchor='center')
        
        def place_on_hover(label,target):
            label.bind(
                "<Enter>", 
                func=lambda l:target.place(
                    relheight=.05,relwidth=.95,
                    relx=.51,rely=.028,anchor='center'))
            label.bind(
                "<Leave>", func=lambda l:target.place_forget())
        
        
        place_on_hover(email_frame,contact_us)
        place_on_hover(contact_us,contact_us)
        
        
        certificate_image_raw = Image.open(r"C:\Users\james\Downloads\Icons&bg\jpg-file.png")
        resize_certificate_image =  certificate_image_raw.resize((50,50))
        certificate_image = ImageTk.PhotoImage(image=resize_certificate_image)
        
        resume_image_raw = Image.open(r"C:\Users\james\Downloads\Icons&bg\pdf.png")
        resize_resume_image = resume_image_raw.resize((50,50))
        resume_image = ImageTk.PhotoImage(image=resize_resume_image)
        
        check_image_raw = Image.open(r"C:\Users\james\Downloads\Icons&bg\checkmark.png")
        resize_check_image = check_image_raw.resize((50,50))
        check_image = ImageTk.PhotoImage(image=resize_check_image)
        
        member = Applicant(
            parent=parent,
            resume_upload_img=resume_image,
            certificate_upload_img=certificate_image,
            chech_upload_image=check_image,
            login_frame = self,
            background_design = bg_design,
            enroll_button= enroll_button
        )
        def apply_member(event):
            enroll_button.place_forget()
            self.place_forget() # temporary hides it & place it back again if 
            #   the back_bttn was clicked.
            
            # adjust the canvas(school in the background) to fit the screen .
            bg_design.place_configure(relwidth=.99,relx=.5)
            
            # display the frame
            member.place_member_frame()
            
            def exit_member():
                member.place_forget_member_frame()
                
                bg_design.place( # adjust the bg
                    relheight=.98, relwidth=.59 , 
                    relx=.3,rely=.5, anchor='center')
                
                self.place( # bring back home a.k.a. self.
                    relx=.994,rely=.5,anchor='e',relheight=.98,relwidth=.4)
                
                enroll_button.place( # bring back enroll
                    anchor='center', relx=.5, rely=.9, 
                    relheight=.05, relwidth=.2)
            
            
            exit_apply_bttn = ttk.Button(
                member.member_frame,bootstyle='danger',text='EXIT',
                command=exit_member)
            exit_apply_bttn.place(
                relx=.932, rely=.05, anchor='center',
                relheight=.06, relwidth=.11)
        
        
        hire_label = ttk.Label(
            self,text='Join our Teaching Family',bootstyle='Secondary',
            anchor='center',font='helvetica 11')
        hire_label.place(
            anchor='center',relheight=.04,relwidth=.45,relx=.51,rely=.98)
        hire_label.bind("<Button-1>",func=apply_member) # make it clickable.
        
        
        def underline_on_hover(label):
            label.bind(
                "<Enter>", func=lambda l:label.configure(font='helvetica 11 underline'))
            label.bind(
                "<Leave>", func=lambda l:label.configure(font='helvetica 11'))
            
        
        
        underline_on_hover(hire_label)
        
        
        
        
        self.mainloop()
        

class mainMenu(ttk.Frame):
    def __init__(self,trunk) -> None:
        super().__init__()
        try:
            # if the user exit the application without login or signing
            #   this code will gonna throw some error .
            self.my_gmail = trunk.my_gmail
            self.my_password = trunk.my_password
            self.account_type = trunk.account_type
            print(trunk.account_type)
            
            print(f'home/trunk is instance of Home ={isinstance(trunk,Home)}') #True
            print(f'app/trunk.root is instance of App class ={isinstance(trunk.root,App)}') #True
            
            # destroying parent.root will make the app quit
            trunk.destroy()
            
        except AttributeError: # make sure the application is exited
            print('attribute errror - No account logged or exited')
            trunk.root.quit()
            self.quit()
            
            return None # to avoid unnecessary indentaion.
        
        
        self.configure(bootstyle='secondary')
        self.place_configure(
            relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # print(self.winfo_parent())
        
        
        # this frame will be the parent all of the widgets to keep the
        #   self frame clean and ready for any update or changes .
        main_frame = ttk.Frame(self,bootstyle='warning')
        main_frame.place(
            relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # main_frame.columnconfigure(0,weight=30)
        # main_frame.columnconfigure(1,weight=70)
        # main_frame.rowconfigure(0,weight=1)
        self.main_frame = main_frame
        
        my_account = databaseAccountConnect(
            gmail=self.my_gmail,passw=self.my_password,
            accountType=self.account_type,)
        
        user_profile = Profile(main_frame,my_account,accountType=self.account_type)
        self.user_profile = user_profile
        menu_frame = ttk.Frame(main_frame,bootstyle='default')
        menu_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        
        
        def menu_frame_row_col():
            menu_frame.columnconfigure(0,weight=1)
            menu_frame.columnconfigure(1,weight=1)
            menu_frame.columnconfigure(2,weight=1)
            menu_frame.columnconfigure(3,weight=1)
            menu_frame.columnconfigure(4,weight=1)
            menu_frame.columnconfigure(5,weight=1)
            menu_frame.rowconfigure(0,weight=1)
            menu_frame.rowconfigure(1,weight=1)
            menu_frame.rowconfigure(2,weight=2)
            menu_frame.rowconfigure(3,weight=1)
            menu_frame.rowconfigure(4,weight=2)
            menu_frame.rowconfigure(5,weight=1)
            menu_frame.rowconfigure(6,weight=2)
            menu_frame.rowconfigure(7,weight=1)
        menu_frame_row_col()
        
        # Name of School
        menu_header = ttk.Label(
            menu_frame,text='University of School Name in Somewhere',
            font=('System',20))
        menu_header.grid(
            column=1,row=0,columnspan=4,sticky=tk.N+tk.S)
        
        # show button and hide button will contrast each other.
        def show_profile_frame(event):
            hamburger_show_bttn.place_forget()
            user_profile.show_frame()
            menu_frame.place_configure(anchor='nw',relx=.3,relheight=1,relwidth=.7)
        
        
        def hide_frame(event):
            user_profile.hide_frame()
            menu_frame.place_configure(relheight=1,relwidth=1,relx=0,rely=0)
            hamburger_show_bttn.place(
                relheight=.08,relwidth=.06,relx=.01,rely=.01)
        
        # Image for button to toggle on the Profile panel . 
        img_profile = Image.open(r"C:\Users\james\Downloads\Icons&bg\user.png")
        img_profile = img_profile.resize((50,50))
        image_profile =ImageTk.PhotoImage(image=img_profile)
        # once the user is logged the Profile panel is hide and can toggle to 
        #   appear using button . 
        hamburger_show_bttn = ttk.Frame(
            menu_frame, bootstyle='default',)
        hamburger_show_bttn.place(
                relheight=.08,relwidth=.06,relx=.01,rely=.01)
        label_show_bttn = ttk.Label(borderwidth=0,
            master=hamburger_show_bttn, image=image_profile)
        label_show_bttn.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        label_show_bttn.bind(
            "<Button-1>",func=show_profile_frame)
        
        # Since the parent of Hide Profile button is Profile panel, the hide
        #   button is in the Profile Class and the picture is pass to public
        #   variable of Profile Class .
        img_back_profile = Image.open(r"C:\Users\james\Downloads\Icons&bg\left-arrow (1).png")
        img_back_profile = img_back_profile.resize((50,50))
        image_back_profile = ImageTk.PhotoImage(image=img_back_profile)
        user_profile.hide_profile_bttn.configure(image=image_back_profile)
        user_profile.hide_profile_bttn.bind("<Button-1>",func=hide_frame)
        
        def hide_Profile():
            user_profile.frame.place_forget()
            menu_frame.place_forget()
        def bringback_profile():
            # user_profile.frame.place(anchor='nw',relheight=1,relwidth=.3)
            menu_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
            hamburger_show_bttn.place(
                relheight=.08,relwidth=.06,relx=.01,rely=.01)
        UserType(
            accountType=self.account_type,
            menuFrame=menu_frame,
            mainFrame=main_frame,
            backProfile=bringback_profile,
            hideProfile=hide_Profile)


        self.mainloop()


if __name__ == '__main__':
    app = App()
    home = Home(app)
    mainMenu(home)