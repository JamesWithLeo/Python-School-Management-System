# import json
import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import sys_db

class accountLogin:
    """dedicated and only for login page"""
    def __init__(self,parent) -> None:
        def change_on_hover(entry,label):
            """to change the color of the label when cursor \n
            hover on the entry. only for gmail and pass label """
            entry.bind(
                "<Enter>",func=lambda l:label.configure(bootstyle='primary'),
                add=True)
            entry.bind(
                "<Leave>",func=lambda l:label.configure(bootstyle='default'),
                add=True)


        border_frame = ttk.Labelframe(
            parent,bootstyle='primary',labelanchor='n',text='Account')
        border_frame.place(
            relx=.5,rely=.4,
            relheight=.3,relwidth=.7,
            anchor='center')
        
        gmail_label = ttk.Label(
            border_frame,
            text='Gmail :',
            font='system 10',bootstyle='default')
        gmail_label.place(
            relx=.08,rely=.19,
            relwidth=.2,relheight=.2,anchor='nw')
        
        gmail_str_var = tk.StringVar()
        gmail_entry = ttk.Entry(
            border_frame,width=24,font='system 10',
            textvariable=gmail_str_var)
        gmail_entry.place(
            relx=.28,rely=.21,
            relheight=.15,relwidth=.62,anchor='nw')
        change_on_hover(entry=gmail_entry,label=gmail_label)

        password_label = ttk.Label(
            border_frame,
            text='Password :',
            font='system 10',bootstyle='default')
        password_label.place(
            relx=.08,rely=.49,
            relwidth=.28,relheight=.2,
            anchor='nw')
        password_str_var = tk.StringVar()
        password_entry = ttk.Entry(
            border_frame,font='system 10',
            textvariable=password_str_var)
        password_entry.place(
            relx=.38,rely=.51,
            relheight=.15,relwidth=.52,anchor='nw')
        change_on_hover(entry=password_entry,label=password_label)

        # bind the widgets to the instance, so it can 
        #   access outside the class .
        self.border_frame = border_frame
        self.gmail_entry = gmail_entry
        self.password_entry = password_entry
        self.my_gmail = gmail_str_var
        self.my_password = password_str_var

# widgets for taking personal information
class getStudents:
    """Widgets containing entries for sign up/ enroll \n
    with methods to remove frame and fetch string variable"""
    def __init__(self,parent):
        """class for taking name and account"""
        def change_on_hover(entry,label):
            """to change the color of the label when cursor \n
            hover on the entry. """
            entry.bind(
                "<Enter>",
                func=lambda l:label.configure(bootstyle='primary'),
                add=True)
            entry.bind(
                "<Leave>",
                func=lambda l:label.configure(bootstyle='default'),
                add=True)
        student_main_frame = ttk.Frame(parent, bootstyle='default')
        student_main_frame.place(relx=.5,rely=.5,relheight=.8,relwidth=.8,anchor='center')
        student_main_frame.columnconfigure(0,weight=2)
        student_main_frame.columnconfigure(1,weight=2)
        student_main_frame.columnconfigure(2,weight=1)
        student_main_frame.columnconfigure(3,weight=2)
        student_main_frame.columnconfigure(4,weight=2)
        student_main_frame.rowconfigure(0,weight=2)
        student_main_frame.rowconfigure(1,weight=2)
        student_main_frame.rowconfigure(2,weight=1)
        student_main_frame.rowconfigure(3,weight=2)
        student_main_frame.rowconfigure(4,weight=2)
        
        
        fullname_frame = ttk.Labelframe(
            student_main_frame, bootstyle='primary', text='Student-information',
            labelanchor='n')
        fullname_frame.grid(
            column=0,columnspan=2,row=0,rowspan=2,
            sticky=tk.N+tk.S+tk.W+tk.E,padx=2,pady=2)
        
        def col_pos_entries_frame():
            fullname_frame.columnconfigure(0,weight=1)
            fullname_frame.columnconfigure(1,weight=1)
            fullname_frame.columnconfigure(2,weight=1)
            fullname_frame.columnconfigure(4,weight=1)
            
            fullname_frame.rowconfigure(0,weight=1)
            fullname_frame.rowconfigure(1,weight=1)
            fullname_frame.rowconfigure(2,weight=1)
            fullname_frame.rowconfigure(3,weight=1)
            fullname_frame.rowconfigure(4,weight=1)
            fullname_frame.rowconfigure(5,weight=1)
            fullname_frame.rowconfigure(6,weight=1)
            fullname_frame.rowconfigure(7,weight=1)
            fullname_frame.rowconfigure(8,weight=1)
        col_pos_entries_frame()
        
        gmail_lbl = ttk.Label(
            fullname_frame,anchor='center', text='gmail :',
            font=('arial',14))
        gmail_lbl.grid(
            column=1,row=1,sticky=tk.W)
        gmail_str_var = tk.StringVar()
        gmail_entry = ttk.Entry(
            fullname_frame,textvariable=gmail_str_var)
        gmail_entry.grid(
            column=2,row=1,sticky=tk.W+tk.E)
        change_on_hover(gmail_entry,gmail_lbl)
        
        password_label = ttk.Label(
            fullname_frame,text='password :',
            font=('Arial',14))
        password_label.grid(
            column=1,row=2,sticky=tk.W)
        password_var = tk.StringVar()
        password_entry = ttk.Entry(
            fullname_frame,textvariable=password_var)
        password_entry.grid(
            column=2,row=2,sticky=tk.W+tk.E)
        change_on_hover(password_entry,password_label)
        
        phone_no_lbl = ttk.Label(
            fullname_frame,
            text='phone number :',font=('arial',14)
        )
        phone_no_lbl.grid(
            column=1,row=3,sticky=tk.W)
        phone_no_str_var = tk.StringVar()
        phone_no_entry = ttk.Entry(
            fullname_frame,textvariable=phone_no_str_var,
        )
        phone_no_entry.grid(
            column=2,row=3,sticky=tk.W+tk.E)
        change_on_hover(phone_no_entry,phone_no_entry)
        sep = ttk.Separator(
            fullname_frame,bootstyle='secondary',orient='horizontal')
        sep.grid(column=1,row=4,columnspan=2,sticky=tk.W+tk.E)
        name_lbl = ttk.Label(
            fullname_frame,text='name :',font=('arial',14)
        )
        name_lbl.grid(
            column=1,row=5,sticky=tk.W)
        name_str_var = tk.StringVar()
        name_entry = ttk.Entry(
            fullname_frame,textvariable=name_str_var,
        )
        name_entry.grid(
            column=2,row=5,sticky=tk.W+tk.E)
        change_on_hover(name_entry,name_lbl)

        mid_name_lbl = ttk.Label(
            fullname_frame,text='Middle name :',font=('arial',14)
        )
        mid_name_lbl.grid(
            column=1,row=6,sticky=tk.W)
        mid_name_str_var = tk.StringVar()
        mid_name_entry = ttk.Entry(
            fullname_frame,textvariable=mid_name_str_var,
        )
        mid_name_entry.grid(
            column=2,row=6,sticky=tk.W+tk.E)
        change_on_hover(mid_name_entry,mid_name_lbl)
        
        last_name_lbl = ttk.Label(
            fullname_frame,text='lastname :',font=('arial',14)
        )
        last_name_lbl.grid(
            column=1,row=7,sticky=tk.W)
        last_name_str_var = tk.StringVar()
        last_name_entry = ttk.Entry(
            fullname_frame,textvariable=last_name_str_var,
        )
        last_name_entry.grid(
            column=2,row=7,sticky=tk.W+tk.E)
        change_on_hover(last_name_entry,last_name_lbl)
        
        suffix_name_lbl = ttk.Label(
            fullname_frame,text='suffix :',font=('arial',14)
        )
        suffix_name_lbl.grid(
            column=1,row=8,sticky=tk.W)
        suffix_name_str_var = tk.StringVar()
        suffix_name_entry = ttk.Entry(
            fullname_frame,textvariable=suffix_name_str_var,
        )
        suffix_name_entry.grid(
            column=2,row=8,sticky=tk.W+tk.E)
        change_on_hover(suffix_name_entry,suffix_name_lbl)
        
        gender_frame = ttk.Labelframe(
            student_main_frame,text='SEX',bootstyle='primary')
        gender_frame.grid(
            column=0,row=3,sticky=tk.N+tk.S+tk.W+tk.E,padx=2,pady=2)
        gender_frame.columnconfigure(0,weight=1)
        gender_frame.columnconfigure(1,weight=1)
        gender_frame.rowconfigure(0,weight=1)
        gender_frame.rowconfigure(1,weight=1)
        
        gender_str_var = tk.StringVar()
        male_lbl = ttk.Label(
            gender_frame, text='male :',font=('arial',14))
        male_lbl.grid(column=0,row=0)
        male_rb = ttk.Radiobutton(
            gender_frame,variable=gender_str_var,
            value='Male')
        male_rb.grid(column=1,row=0)
        
        female_lbl = ttk.Label(
            gender_frame, text='female :',font=('arial',14))
        female_lbl.grid(column=0,row=1,sticky=tk.N)
        female_rb = ttk.Radiobutton(
            gender_frame,variable=gender_str_var,
            value='Female')
        female_rb.grid(column=1,row=1)
        
        
        birth_frame = ttk.Labelframe(
            student_main_frame,text='DATE-OF-BIRTH',
            bootstyle='primary')
        birth_frame.grid(column=0,row=4,sticky=tk.N+tk.S+tk.W+tk.E,padx=2,pady=2)
        birth_frame.columnconfigure(0,weight=1)
        birth_frame.columnconfigure(1,weight=1)
        birth_frame.rowconfigure(0,weight=1)
        birth_frame.rowconfigure(1,weight=1)
        birth_frame.rowconfigure(2,weight=1)
        
        month_lbl = ttk.Label(
            birth_frame,text='month :',font=('arial',14))
        month_lbl.grid(column=0,row=0)
        month_str_var = tk.StringVar()
        month_cb = ttk.Combobox(
            birth_frame,values=list(range(1,13)),
            width=10, textvariable=month_str_var)
        month_cb.grid(column=1,row=0)
        
        day_lbl = ttk.Label(
            birth_frame,text='day :',font=('arial',14))
        day_lbl.grid(column=0,row=1)
        day_str_var = tk.StringVar()
        day_cb = ttk.Combobox(
            birth_frame,values=list(range(1,32)),
            width=10, textvariable=day_str_var)
        day_cb.grid(column=1,row=1)
        
        year_lbl = ttk.Label(
            birth_frame,text='year :',font=('arial',14))
        year_lbl.grid(column=0,row=2)
        year_str_var = tk.StringVar()
        year_cb = ttk.Combobox(
            birth_frame,values=list(range(1900,2024)),
            width=10,height=5, textvariable=year_str_var)
        year_cb.grid(column=1,row=2)
        
        
        nationality_frame = ttk.Labelframe(
            student_main_frame,bootstyle='primary',text='others')
        nationality_frame.grid(
            column=1,row=3,rowspan=2,sticky=tk.N+tk.S+tk.E+tk.W,padx=2,pady=2)
        nationality_frame.columnconfigure(0,weight=1)
        nationality_frame.rowconfigure(0,weight=1)
        nationality_frame.rowconfigure(1,weight=1)
        nationality_frame.rowconfigure(2,weight=1)
        nationality_frame.rowconfigure(3,weight=1)
        nationality_frame.rowconfigure(4,weight=1)
        nationality_frame.rowconfigure(5,weight=1)
        
        civil_val = ['SINGLE','MARRIED', 'DIVORCED', 'WIDOW']
        civil_lbl = ttk.Label(
            nationality_frame,text='civil status',font=('helveltica',14))
        civil_lbl.grid(column=0,row=0,sticky=tk.S,pady=1)
        civil_str_var = tk.StringVar()
        civil_cb = ttk.Combobox(
            nationality_frame,values=civil_val,
            width=12, textvariable=civil_str_var)
        civil_cb.grid(column=0,row=1)
        
        nationality_lbl = ttk.Label(
            nationality_frame,text='nationality',font=('arial',14))
        nationality_lbl.grid(column=0,row=4,sticky=tk.S)
        nationality_str_var = tk.StringVar()
        nationality_entry = ttk.Entry(
            nationality_frame,width=15, textvariable=nationality_str_var)
        nationality_entry.grid(column=0,row=5,sticky=tk.N)
        
        religion_lbl = ttk.Label(
            nationality_frame,text='religion',font=('arial',14))
        religion_lbl.grid(column=0,row=2,sticky=tk.S)
        religion_str_var = tk.StringVar()
        religion_entry = ttk.Entry(
            nationality_frame,width=15, textvariable=religion_str_var)
        religion_entry.grid(column=0,row=3,sticky=tk.N)
        
        
        address_frame = ttk.Labelframe(
            student_main_frame,labelanchor='n',text='ADDRESS' ,
            bootstyle='primary')
        address_frame.grid(
            column=3,columnspan=2,row=0,rowspan=2,
            sticky=tk.N+tk.S+tk.E+tk.W,padx=2,pady=2)
        address_frame.columnconfigure(0,weight=1)
        address_frame.columnconfigure(1,weight=1)
        address_frame.columnconfigure(2,weight=1)
        address_frame.columnconfigure(3,weight=1)
        address_frame.columnconfigure(4,weight=1)
        
        address_frame.rowconfigure(0,weight=1)
        address_frame.rowconfigure(1,weight=1)
        address_frame.rowconfigure(2,weight=1)
        address_frame.rowconfigure(3,weight=1)
        address_frame.rowconfigure(4,weight=1)
        # address_frame.rowconfigure(5,weight=1)
        
        street_lbl = ttk.Label(
            address_frame,text='street :',font=('arial',14))
        street_lbl.grid(column=1,row=0,sticky=tk.W)
        street_str_var = tk.StringVar()
        street_entry = ttk.Entry(
            address_frame,width=19, textvariable=street_str_var)
        street_entry.grid(column=2,row=0,sticky=tk.W+tk.E)
        
        municipality_lbl = ttk.Label(
            address_frame,text='municipality :',font=('arial',14))
        municipality_lbl.grid(column=1,row=2,sticky=tk.W)
        municipality_str_var = tk.StringVar()
        municipality_cb = ttk.Combobox(
            address_frame,width=17, textvariable=municipality_str_var)
        municipality_cb.grid(column=2,row=1,sticky=tk.W+tk.E)
        
        barangay_lbl = ttk.Label(
            address_frame,text='barangay :',font=('arial',14))
        barangay_lbl.grid(column=1,row=1,sticky=tk.W)
        barangay_str_var = tk.StringVar()
        barangay_cb = ttk.ttk.Combobox(
            address_frame,width=17, textvariable=barangay_str_var)
        barangay_cb.grid(column=2,row=2,sticky=tk.W+tk.E)
        
        
        zipcode_lbl = ttk.Label(
            address_frame,text='zip code :',font=('arial',14))
        zipcode_lbl.grid(column=1,row=3,sticky=tk.W)
        zipcode_str_var = tk.StringVar()
        zipcode_entry = ttk.Entry(
            address_frame,width=19, textvariable=zipcode_str_var)
        zipcode_entry.grid(column=2,row=3,sticky=tk.W+tk.E)
        
        contact_no_lbl = ttk.Label(
            address_frame,text='contact number :',font=('arial',14))
        contact_no_lbl.grid(column=1,row=4,sticky=tk.W)
        contact_str_var = tk.StringVar()
        contact_no_entry = ttk.Entry(
            address_frame,width=19, textvariable=contact_str_var)
        contact_no_entry.grid(column=2,row=4,sticky=tk.W+tk.E)
        
        birth_place_lbl = ttk.Label(
            address_frame,text='birth place :',font=('arial',14))
        birth_place_lbl.grid(column=1,row=5,sticky=tk.W)
        birth_place_str_var = tk.StringVar()
        birth_place_entry = ttk.Entry(
            address_frame,width=19, textvariable=birth_place_str_var)
        birth_place_entry.grid(column=2,row=5,sticky=tk.W+tk.E)
        
        education_frame = ttk.Labelframe(
            student_main_frame,text='EDUCATION',labelanchor='n' 
            ,bootstyle='primary')
        education_frame.grid(
            column=3,columnspan=2,row=3,rowspan=2,
            sticky=tk.N+tk.S+tk.E+tk.W,padx=2,pady=2)
        education_frame.columnconfigure(0,weight=1)
        education_frame.columnconfigure(1,weight=1)
        education_frame.columnconfigure(2,weight=1)
        education_frame.columnconfigure(3,weight=1)
        
        education_frame.rowconfigure(0,weight=1)
        education_frame.rowconfigure(1,weight=1)
        education_frame.rowconfigure(2,weight=1)
        
        high_school_lbl = ttk.Label(
            education_frame,text='high school :',font=('arial',14)
        )
        high_school_lbl.grid(
            column=1,row=0,sticky=tk.W)
        high_school_str_var = tk.StringVar()
        high_school_entry = ttk.Entry(
            education_frame,textvariable=high_school_str_var,
        )
        high_school_entry.grid(
            column=2,row=0,sticky=tk.W+tk.E)
        change_on_hover(high_school_entry,high_school_lbl)
        sep = ttk.Separator(
            education_frame,orient='horizontal',bootstyle='secondary')
        sep.grid(column=1,columnspan=2,row=0,sticky=tk.S+tk.W+tk.E)
        course_lbl = ttk.Label(
            education_frame,text='course :',font=('arial',14)
        )
        course_lbl.grid(
            column=1,row=1,sticky=tk.W)
        course_str_var = tk.StringVar()
        course_entry = ttk.Combobox(
            education_frame,textvariable=course_str_var
        )
        course_entry.grid(
            column=2,row=1,sticky=tk.W+tk.E)
        change_on_hover(course_entry,course_lbl)
        
        college_lvl_lbl = ttk.Label(
            education_frame,text='college level :',font=('arial',14)
        )
        college_lvl_lbl.grid(
            column=1,row=2,sticky=tk.W)
        college_lvl_str_var = tk.StringVar()
        college_lvl_entry = ttk.Combobox(
            education_frame,textvariable=college_lvl_str_var
        )
        
        college_lvl_entry.grid(
            column=2,row=2,sticky=tk.W+tk.E)
        change_on_hover(college_lvl_entry,college_lvl_lbl)
        
        
        # all text variable
        self.my_gmail = gmail_str_var
        self.my_password = password_var
        self.my_phone_no = phone_no_str_var
        
        self.my_name = name_str_var
        self.my_middle_name = mid_name_str_var
        self.my_last_name = last_name_str_var
        self.my_suffix = suffix_name_str_var
        
        self.my_gender = gender_str_var
        
        self.my_month = month_str_var
        self.my_day = day_str_var
        self.my_year = year_str_var
        
        self.my_civil_status = civil_str_var
        self.my_nationality = nationality_str_var
        self.my_religion = religion_str_var
        
        self.my_street = street_str_var
        self.my_barangay = barangay_str_var
        self.my_municipality = municipality_str_var
        self.my_zipcode = zipcode_str_var
        self.my_contact_no = contact_str_var
        self.my_birth_place = birth_place_str_var
        
        self.my_highschool = high_school_str_var
        self.my_course = course_str_var
        self.my_college_level = college_lvl_str_var


        # all class child frame
        self.student_main_frame = student_main_frame
        self.fullname_frame = fullname_frame
        self.gender_frame = gender_frame
        self.birth_date_frame = birth_frame
        self.nationality_frame = nationality_frame
        self.address_frame = address_frame
        self.education_frame = education_frame

        # all entry
        self.gmail_entry = gmail_entry
        self.password_entry = password_entry
        self.phone_no_entry = phone_no_entry
        self.name_entry = name_entry
        self.mid_name_entry = mid_name_entry
        self.last_name_entry = last_name_entry
        self.suffix_name_entry = suffix_name_entry
        self.month_cb  = month_cb 
        self.day_cb = day_cb
        self.year_cb = year_cb
        self.civil_cb = civil_cb
        self.nationality_entry = nationality_entry
        self.religion_entry = religion_entry
        self.street_entry = street_entry
        self.barangay_cb = barangay_cb
        self.municipality_cb = municipality_cb
        self.barangay_cb = barangay_cb
        self.zipcode_entry = zipcode_entry
        self.contact_no_entry = contact_no_entry
        self.birth_place_entry = birth_place_entry
        self.high_school_entry = high_school_entry
        self.course_entry = course_entry
        self.college_lvl_entry = college_lvl_entry
        
        # all label
        # self.gmail_lbl = gmail_lbl
        # self.password_label = password_label
        # self.phone_no_lbl = phone_no_lbl
        # self.name_lbl = name_lbl
        # self.mid_name_lbl = mid_name_lbl
        # self.last_name_lbl = last_name_lbl
        # self.month_lbl = month_lbl
        # self.day_lbl = day_lbl
        # self.year_lbl = year_lbl
        # self.civil_lbl = civil_lbl
        # self.nationality_lbl = nationality_lbl
        # self.religion_lbl = religion_lbl
        # self.street_lbl = street_lbl
        # self.municipality_lbl = municipality_lbl
        # self.barangay_lbl = barangay_lbl
        # self.zipcode_lbl = zipcode_lbl
        # self.contact_no_lbl = contact_no_lbl
        # self.birth_place_lbl = birth_place_lbl
        # self.high_school_lbl = high_school_lbl
        # self.course_lbl = course_lbl
        # self.college_lvl_lbl = college_lvl_lbl
        
    def verify_gmail(self,mstr):
        gmail = self.my_gmail.get().strip()
        gmail_label = ttk.Label(master=mstr, text=f'Gamil: {gmail}')
        gmail_label.pack()
        
        
        pw = self.my_password.get().strip()
        pw_label = ttk.Label(master=mstr, text=f'Password: {pw}')
        pw_label.pack()
        
        
        phone_no = self.my_phone_no.get().strip()
        phone_no_label = ttk.Label(master=mstr, text=f'Phone No.: {phone_no}')
        phone_no_label.pack()


    def verify_name(self,mstr):
        fullname = []
        name_var = [
            self.my_name,self.my_middle_name,self.my_last_name,self.my_suffix]
        
        for name in name_var[:-1]:
            name = name.get().strip()
            fullname.append(name)
        fullname = ((' '.join(fullname))+' '+self.my_suffix.get()).strip()
        fullname_label = ttk.Label(master=mstr, text=f'Name: {fullname}')
        fullname_label.pack()


    def verify_bday(self,mstr):
        birthday_list = []
        bday_var = [self.my_month, self.my_day, self.my_year]
        for date in bday_var:
            date = date.get().strip()
            birthday_list.append(date)
        
        bday = ' '.join(birthday_list)
        bday_label = ttk.Label(master=mstr, text=f'Birth day: {bday}')
        bday_label.pack()


    def verify_gender(self,mstr):
        gender = self.my_gender.get()
        gender_label = ttk.Label(master=mstr, text=f'Gender: {gender}')
        gender_label.pack()


    def verify_status(self,mstr):
        civil = self.my_civil_status.get().strip()
        natio = self.my_nationality.get().strip()
        reli = self.my_religion.get().strip()
        
        civil_label = ttk.Label(master=mstr, text=f'Civil status: {civil}')
        civil_label.pack()
        
        natio_label = ttk.Label(master=mstr, text=f'Nationality: {natio}')
        natio_label.pack()
        
        reli_label = ttk.Label(master=mstr, text=f'Religion: {reli}')
        reli_label.pack()



    def verify_address(self,mstr):
        address = []
        address_list = [
            self.my_street.get().strip(),
            self.my_barangay.get().strip(),
            self.my_municipality.get().strip(),
        ]
        for i in address_list:
            address.append(i)
        address = ' '.join(address)
        
        birth_place = self.my_birth_place.get().strip()
        zipc = self.my_zipcode.get().strip()
        contact_no = self.my_contact_no.get().strip()
        
        birth_place_lbl = ttk.Label(
            master=mstr, text=f'Birth place: {birth_place}')
        birth_place_lbl.pack()
        
        addres_lbl = ttk.Label(master=mstr, text=f'Address: {address}')
        addres_lbl.pack()
        
        zipc_lbl = ttk.Label(master=mstr, text=f'Zipcode: {zipc}')
        zipc_lbl.pack()
        
        contact_no_label = ttk.Label(
            master=mstr, text=f'Contact: {contact_no}')
        contact_no_label.pack()


    def verify_edu(self,mstr):
        highschool = self.my_highschool.get().strip()
        course = self.my_course.get().strip()
        college_lvl = self.my_college_level.get().strip()
        
        highschool_lbl = ttk.Label(
            master=mstr, text=f'Highschool: {highschool}')
        highschool_lbl.pack()
        
        course_lbl = ttk.Label(master=mstr, text=f'Course: {course}')
        course_lbl.pack()
        
        college_lvl_lbl = ttk.Label(
            master=mstr, text=f'College level: {college_lvl}')
        college_lvl_lbl.pack()


    def hide_frame(self)->None:
        self.student_main_frame.place_forget()



    def display_frame(self)->None:
        self.student_main_frame.place(
            relx=.5,rely=.5,relheight=.8,relwidth=.8,anchor='center')


    def get_all_data(self):
        """This bool method will check, if entry is empty \n
        return true if all of the entry is filled, else return false"""
        str_vars_for_student_widgets = [
            [self.gmail_entry, self.my_gmail],
            [self.password_entry, self.my_password],
            [self.phone_no_entry, self.my_phone_no],
            [self.name_entry, self.my_name],
            [self.mid_name_entry, self.my_middle_name],
            [self.last_name_entry, self.my_last_name],
            [self.my_suffix],
            [self.my_gender],
            [self.month_cb, self.my_month],
            [self.day_cb, self.my_day],
            [self.year_cb, self.my_year],
            [self.civil_cb, self.my_civil_status],
            [self.religion_entry, self.my_religion],
            [self.nationality_entry, self.my_nationality],
            [self.street_entry, self.my_street],
            [self.municipality_cb, self.my_municipality],
            [self.barangay_cb, self.my_barangay],
            [self.zipcode_entry, self.my_zipcode],
            [self.contact_no_entry, self.my_contact_no],
            [self.birth_place_entry, self.my_birth_place],
            [self.high_school_entry, self.my_highschool],
            [self.course_entry, self.my_course],
            [self.college_lvl_entry, self.my_college_level],
        ]
        # try:
        #     for widget in str_vars_for_student_widgets:
        #         # skip gender and suffix since gender is radiobutton and
        #         # suffix can be number or alphabet .
        #         if widget[0] is self.my_suffix or \
        #             widget[0] is self.my_gender:
        #             continue
                
        #         elif widget[1].get() == '':
        #             # empty entry will remain color red as a sign of warning
        #             #   for user, and should be filled to continue for enroll .
        #             widget[0].configure(bootstyle='danger')
        #             raise ValueError
                
        #         widget[0].configure(bootstyle='default')
        # except ValueError:
        #     # deleting will refresh entries .
        #     del str_vars_for_student_widgets
        #     return False
        # else:
        return True # if all of entries are filled

# widgets for taking family information
class getGuardian:
    def __init__(self,parent) -> None:
        guardian_parent = ttk.Frame(parent,bootstyle='default')
        guardian_parent.columnconfigure(0,weight=1)
        # guardian_parent.columnconfigure(1,weight=1)
        # guardian_parent.columnconfigure(2,weight=1)
        guardian_parent.rowconfigure(0,weight=1)
        guardian_parent.rowconfigure(1,weight=1)
        guardian_parent.rowconfigure(2,weight=1)
        
        self.frame = guardian_parent
        
        father_frame = ttk.Labelframe(
            guardian_parent,bootstyle='primary',
            text='FATHER',labelanchor='n')
        father_frame.grid(column=0,row=0,sticky=tk.N+tk.S+tk.E+tk.W)
        father_frame.columnconfigure(0,weight=1)
        father_frame.columnconfigure(1,weight=1)
        father_frame.columnconfigure(2,weight=1)
        father_frame.columnconfigure(3,weight=1)
        
        father_frame.rowconfigure(0,weight=1)
        father_frame.rowconfigure(1,weight=1)
        
        
        father_fullname_lbl = ttk.Label(
            father_frame,text='full name :',font=('arial',14))
        father_fullname_lbl.grid(
            column=0,row=0)
        father_fullname_str_var = tk.StringVar()
        father_fullname_entry = ttk.Entry(
            father_frame,textvariable=father_fullname_str_var,)
        father_fullname_entry.grid(
            column=1,row=0)

        father_address_lbl = ttk.Label(
            father_frame,text='address :',font=('arial',14))
        father_address_lbl.grid(
            column=0,row=1)
        father_address_str_var = tk.StringVar()
        father_address_entry = ttk.Entry(
            father_frame,textvariable=father_address_str_var,
        )
        father_address_entry.grid(
            column=1,row=1)
        
        father_contact_lbl = ttk.Label(
            father_frame,text='contact number :',font=('arial',14))
        father_contact_lbl.grid(
            column=2,row=0)
        father_contact_str_var = tk.StringVar()
        father_contact_entry = ttk.Entry(
            father_frame,textvariable=father_contact_str_var,
        )
        father_contact_entry.grid(
            column=3,row=0)
        
        father_occupation_lbl = ttk.Label(
            father_frame,text='occupation :',font=('arial',14)
        )
        father_occupation_lbl.grid(
            column=2,row=1)
        father_occupation_str_var = tk.StringVar()
        father_occupation_entry = ttk.Entry(
            father_frame,textvariable=father_occupation_str_var,
        )
        father_occupation_entry.grid(
            column=3,row=1)
        
        mother_frame = ttk.Labelframe(
            guardian_parent,bootstyle='primary',
            text='MOTHER', labelanchor='n')
        mother_frame.grid(column=0,row=1,sticky=tk.N+tk.S+tk.E+tk.W)
        mother_frame.columnconfigure(0,weight=1)
        mother_frame.columnconfigure(1,weight=1)
        mother_frame.columnconfigure(2,weight=1)
        mother_frame.columnconfigure(3,weight=1)
        mother_frame.rowconfigure(0,weight=1)
        mother_frame.rowconfigure(1,weight=1)
        
        mother_fullname_lbl = ttk.Label(
            mother_frame,text='maiden\nfull name :',font=('arial',14))
        mother_fullname_lbl.grid(
            column=0,row=0)
        mother_fullname_str_var = tk.StringVar()
        mother_fullname_entry = ttk.Entry(
            mother_frame,textvariable=mother_fullname_str_var)
        mother_fullname_entry.grid(
            column=1,row=0)

        mother_address_lbl = ttk.Label(
            mother_frame,text='address :',font=('arial',14))
        mother_address_lbl.grid(
            column=0,row=1)
        mother_address_str_var = tk.StringVar()
        mother_address_entry = ttk.Entry(
            mother_frame,textvariable=mother_address_str_var)
        mother_address_entry.grid(
            column=1,row=1)
        
        mother_contact_lbl = ttk.Label(
            mother_frame,text='contact number :',font=('arial',14))
        mother_contact_lbl.grid(
            column=2,row=0)
        mother_contact_str_var = tk.StringVar()
        mother_contact_entry = ttk.Entry(
            mother_frame,textvariable=mother_contact_str_var)
        mother_contact_entry.grid(
            column=3,row=0)
        
        mother_occupation_lbl = ttk.Label(
            mother_frame,text='occupation :',font=('arial',14))
        mother_occupation_lbl.grid(
            column=2,row=1)
        mother_occupation_str_var = tk.StringVar()
        mother_occupation_entry = ttk.Entry(
            mother_frame,textvariable=mother_occupation_str_var,
        )
        mother_occupation_entry.grid(column=3,row=1)


        guardian_frame = ttk.Labelframe(
            guardian_parent,bootstyle='primary',
            text='GUARDIAN', labelanchor='n')
        guardian_frame.grid(column=0,row=2,sticky=tk.N+tk.S+tk.E+tk.W)
        guardian_frame.columnconfigure(0,weight=1)
        guardian_frame.columnconfigure(1,weight=1)
        guardian_frame.columnconfigure(2,weight=1)
        guardian_frame.columnconfigure(3,weight=1)
        guardian_frame.rowconfigure(0,weight=1)
        guardian_frame.rowconfigure(1,weight=1)
        guardian_fullname_lbl = ttk.Label(
            guardian_frame,text='full name :',font=('arial',14))
        guardian_fullname_lbl.grid(
            column=0,row=0)
        guardian_fullname_str_var = tk.StringVar()
        guardian_name_entry = ttk.Entry(
            guardian_frame,textvariable=guardian_fullname_str_var)
        guardian_name_entry.grid(
            column=1,row=0)

        guardian_address_lbl = ttk.Label(
            guardian_frame,text='address :',font=('arial',14))
        guardian_address_lbl.grid(
            column=0,row=1)
        guardian_address_str_var = tk.StringVar()
        guardian_address_entry = ttk.Entry(
            guardian_frame,textvariable=guardian_address_str_var)
        guardian_address_entry.grid(
            column=1,row=1)
        
        guardian_contact_lbl = ttk.Label(
            guardian_frame,text='contact number :',font=('arial',14))
        guardian_contact_lbl.grid(
            column=2,row=0)
        guardian_contact_str_var = tk.StringVar()
        guardian_contact_entry = ttk.Entry(
            guardian_frame,textvariable=guardian_contact_str_var)
        guardian_contact_entry.grid(
            column=3,row=0)
        
        guardian_occupation_lbl = ttk.Label(
            guardian_frame,text='occupation :',font=('arial',14))
        guardian_occupation_lbl.grid(
            column=2,row=1)
        guardian_occupation_str_var = tk.StringVar()
        guardian_occupation_entry = ttk.Entry(
            guardian_frame,textvariable=guardian_occupation_str_var)
        guardian_occupation_entry.grid(
            column=3,row=1)

        self.my_father_fullname = father_fullname_str_var
        self.my_father_address = father_address_str_var
        self.my_father_contact = father_contact_str_var
        self.my_father_occupation = father_occupation_str_var
        
        self.my_mother_fullname = mother_fullname_str_var
        self.my_mother_address= mother_address_str_var
        self.my_mother_contact = mother_contact_str_var 
        self.my_mother_occupation = mother_occupation_str_var
        
        self.my_guardian_fullname = guardian_fullname_str_var
        self.my_guardian_address = guardian_address_str_var
        self.my_guardian_contact = guardian_contact_str_var
        self.my_guardian_occupation = guardian_occupation_str_var

        self.father_frame = father_frame
        self.mother_frame = mother_frame
        self.guardian_frame = guardian_frame
        
    def display_frame(self):
        """Place the frame for guardian"""
        self.frame.place(
            relx=.5,rely=.49,relheight=.8,relwidth=.9,anchor='center')


    def hide_frame(self):
        self.frame.place_forget()

    def get_all_data(self):
        str_vars = [
        [self.father_frame, self.my_father_fullname,self.my_father_address,
        self.my_father_contact,self.my_father_occupation],
        [self.mother_frame, self.my_mother_fullname,self.my_mother_address,
        self.my_mother_contact,self.my_mother_occupation],
        [self.guardian_frame, self.my_guardian_fullname,self.my_guardian_address,
        self.my_guardian_contact,self.my_guardian_occupation]]
        
        # try:
        #     for list_of_var in str_vars:
        #         for i in list_of_var[1:]:
        #             if i.get().strip() == '':
        #                 list_of_var[0].configure(bootstyle='danger')
        #                 raise ValueError
        #             else:
        #                 list_of_var[0].configure(bootstyle='secondary')
        #                 print(i.get())
        # except ValueError:
        #     del str_vars
        #     return False
        # else:return True
        return True


# if user is logged this is where user information can be located.
#   this frame can toggle to hide or show .
class Profile:
    def __init__(self,parentFrame,account) -> None:
        profile_menu_frame = ttk.Frame(
            master=parentFrame,bootstyle='secondary')
        profile_menu_frame.grid(column=0,row=0,sticky=tk.N+tk.S+tk.W+tk.E)
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
        name = ttk.Label(
            profile_menu_frame, text=account.full_name,
            font=('helvetica',15))
        name.grid(column=2,row=4,sticky=tk.W)
        
        stu_id = ttk.Label(
            profile_menu_frame, text=account.stud_id,
            font=('helvetica',15))
        stu_id.grid(column=2,row=5,sticky=tk.W)
        
        course = ttk.Label(
            profile_menu_frame, text=account.course,
            font=('helvetica',15))
        course.grid(column=2,row=6,sticky=tk.W)
        
        gender_and_age = ttk.Label(
            profile_menu_frame, text=account.gender,
            font=('helvetica',15))
        gender_and_age.grid(column=2,row=7,sticky=tk.W)
        
        address = ttk.Label(
            profile_menu_frame, text=account.address,
            font=('helvetica',15))
        address.grid(column=2,row=8,sticky=tk.W)
        
        
    def hide_frame(self):
        self.frame.place_forget()
    
    def show_frame(self):
        self.frame.grid(
            column=0,row=0,sticky=tk.N+tk.S+tk.W+tk.E)

# Upper lvl class
class menuSection:
    def do_when_click(self,event):
        pass

    def when_on_hover(self,event):
        self.picture.grid_configure(sticky=tk.N+tk.S)
        self.label.configure(font=('Helvetica bold', 20))
        
    def when_leave_hover(self,event):
        self.picture.grid_configure(sticky=tk.S)
        self.frame.configure(bootstyle='default')
        self.frame.grid_configure(padx=60,pady=0)
        self.label.configure(bootstyle='default',font=('Helvetica bold', 18))
        
    def __init__(
        self,frame_master,col_pos,row_pos,title,main_frame,
        back_profile=None,hide_pro_func=None) -> None:
        self.hide_profile = hide_pro_func
        self.back_profile = back_profile
        self.section_frame = frame_master
        self.col = col_pos
        self.row = row_pos
        self.title = title
        self.main_frame = main_frame
        
        frame = ttk.Frame(self.section_frame, bootstyle='default')
        frame.grid(
            column=self.col,row=self.row,sticky=tk.N+tk.S+tk.W+tk.E,
            padx=60,pady=0)
        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=2)
        frame.rowconfigure(1,weight=2)
        frame.rowconfigure(2,weight=1)
        
        
        sep = ttk.Separator(frame,orient='horizontal',bootstyle='primary')
        sep.grid(column=0,row=1,sticky=tk.W+tk.E+tk.N)
        sep = ttk.Separator(frame,orient='horizontal',bootstyle='primary')
        sep.grid(column=0,row=2,sticky=tk.W+tk.E+tk.S)
        sep = ttk.Separator(frame,orient='vertical',bootstyle='primary')
        sep.grid(column=0,row=1,rowspan=3,sticky=tk.N+tk.E+tk.S)
        sep = ttk.Separator(frame,orient='vertical',bootstyle='primary')
        sep.grid(column=0,row=1,rowspan=3,sticky=tk.W+tk.N+tk.S)
        
        label_title = ttk.Label(
            frame,text=self.title,font=('Helvetica', 18),anchor='center')
        # label_title.place(relheight=.25,relwidth=.7,relx=.15,rely=.7)
        label_title.grid(column=0,row=2)
        
        self.frame = frame
        self.label = label_title
        
        frame.bind(
            "<Enter>",func=self.when_on_hover)
        frame.bind(
            "<Leave>",func=self.when_leave_hover)
        
        frame.bind(
            "<Button-1>",func=self.do_when_click, add='+')
        label_title.bind(
            "<Button-1>",func=self.do_when_click, add='+')
        
    
class Enroll(menuSection):
    def hide_inside_section(self,event):
        # self.inside_section.place_forget()
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.grid()
        
    def do_when_click(self,event):
        self.hide_profile()
        self.section_frame.grid_remove()
        # ----------------
        
        
        # ----------------
        inside_frame = ttk.Frame(self.main_frame,bootstyle='secondary')
        inside_frame.place(relheight=.85,relwidth=.8,relx=.5,rely=.5,anchor='center')
        self.inside_frame = inside_frame
        def widgets_frame_row_col():
            inside_frame.columnconfigure(0,weight=1)
            inside_frame.columnconfigure(1,weight=1)
            inside_frame.columnconfigure(2,weight=1)
            inside_frame.rowconfigure(0,weight=1)
            inside_frame.rowconfigure(1,weight=1)
            inside_frame.rowconfigure(2,weight=1)
        widgets_frame_row_col()
        
        sep = ttk.Separator(inside_frame,orient='horizontal',bootstyle='primary')
        sep.grid(column=0,row=0,columnspan=3,sticky=tk.W+tk.E+tk.N)
        sep = ttk.Separator(inside_frame,orient='horizontal',bootstyle='primary')
        sep.grid(column=0,row=2,columnspan=3,sticky=tk.W+tk.E+tk.S)
        sep = ttk.Separator(inside_frame,orient='vertical',bootstyle='primary')
        sep.grid(column=2,row=0,rowspan=3,sticky=tk.N+tk.E+tk.S)
        sep = ttk.Separator(inside_frame,orient='vertical',bootstyle='primary')
        sep.grid(column=0,row=0,rowspan=3,sticky=tk.W+tk.N+tk.S)
        
        back_to_menu = ttk.Button(inside_frame,text='<- BACK',)
        back_to_menu.place(relx=.9,rely=.02,relheight=.05,relwidth=.08)
        back_to_menu.bind(
            "<Button-1>",func=self.hide_inside_section)


class Room(menuSection):
    pass


class Activity(menuSection):
    pass


class Gallary(menuSection):
    pass


class Canteen(menuSection):
    pass


class Setting(menuSection):
    pass



# This class will be the connector to datebase and will communicate -
#   with mainMenu class. to do the fetching and updating .
class databaseAccountConnect:
    def __init__(self,gmail,passw) -> None:
        
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
            scrn_width = self.winfo_screenwidth()
            scrm_height = self.winfo_screenheight()
            scrn_w = int((self.winfo_screenwidth()-1000) / 2)
            scrn_h = int((self.winfo_screenheight()-700) / 2)
            self.geometry(f'{1000}x{700}+{scrn_w}+{scrn_h}')
            self.minsize(1000,700)
        app_geometry()
        ttk.Style(theme='superhero')

class Home(ttk.Frame):
    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.configure(bootstyle='default')
        self.place(relx=.994,rely=.5,anchor='e',relheight=.98,relwidth=.4)
        
        # the button reference as bg_design served as border design only .
        bg_design = ttk.Button(
            master=parent, bootstyle='primary-outline',state='disabled')
        bg_design.place(
            relheight=.98, relwidth=.59 , relx=.3,rely=.5, anchor='center')
        # import any picture of school facade .
        image_background = Image.open(
            r'\Icons&bg\pexels-craig-adderley-2566121.jpg')
        resized_img = image_background.resize((900,900))
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
            sys_db.cursor_exe(
                sql_code=sys_db.sql_get_gmail,
                target=[account.my_gmail.get().strip()]
            )
            request_gmail = sys_db.mycursor.fetchone()
            # throw some attribute if account is nonetype, meaning it 
            #   doesn't exitst .
            try:
                if account.my_gmail.get().strip() != \
                    request_gmail.get('gmail_account'):
                    return None
                else:
                    warn_no_acc_gmail.place_forget()
                    account.gmail_entry.configure(bootstyle='primary')
                    account.border_frame.configure(bootstyle='primary')
                
            except AttributeError:
                print('account doesnt exist')
                warn_no_acc_gmail.place(
                relx=.5 , rely=.564 ,anchor='center')
                account.border_frame.configure(bootstyle='danger')
                
            else:
                sys_db.cursor_exe(
                    sql_code=sys_db.sql_get_password,
                    target=[account.my_gmail.get().strip()])
                request_password = sys_db.mycursor.fetchone()
                
                if account.my_password.get().strip() != \
                    request_password.get('passwrd'):
                    account.password_entry.configure(bootstyle='danger')
                    warn_incorrect_pass.place(relx=.41,rely=.4,)
                    return None
                else:
                    account.password_entry.configure(bootstyle='primary')
                    self.my_gmail = account.my_gmail          
                    self.my_password = account.my_password
                    # if account exist and the password is correct .
                    bg_design.place_forget()
                    self.quit()


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
        # basically command button ↓
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
        
        def back_to_log(x,y,h,w,target):
            enroll_button.place(
                anchor='center', relx=.5, rely=.9, relheight=.05, relwidth=.2)
            target.place_forget()


        # func for creating account
        def enroll():
            enroll_button.place_forget()
            
            enroll_frame = ttk.Frame( # Frame for  creating account .
                master=parent, bootstyle='default')
            enroll_frame.place(
                relx=.5,rely=.5,
                relheight=.8,relwidth=.7,anchor='center')
            
            # use the lambda to pass the arguments .
            # button for exiting creating account/enroll .
            exit_enroll_bttn = ttk.Button(
                enroll_frame,bootstyle='danger',text='EXIT',
                command=lambda:back_to_log(
                    x=pos_x, y=pos_y, 
                    h=pos_h, w=pos_w,target=enroll_frame))
            exit_enroll_bttn.place(
                relx=.932, rely=.05,
                relheight=.06, relwidth=.11, anchor='center')
            
            
            # prompt the enroll_frame with widgets .
            student_widgets = getStudents(enroll_frame)
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
                
                # place the back button for going back to student widgets .
                prev_bttn = ttk.Button(
                    master=enroll_frame, text='Back', bootstyle='warning')
                prev_bttn.place(
                    relx=.3, rely=.93,
                    relheight=.06, relwidth=.15, anchor='center')
                prev_bttn.bind(
                    "<Button-1>", func=back_prev_entry)

                save_bttn = ttk.Button(
                    enroll_frame, text='SAVE',
                    bootstyle='primary',command=submit)
                save_bttn.place(
                    relx=.7, rely=.93,relheight=.06,
                    relwidth=.15, anchor='center')


            next_bttn = ttk.Button(
                master=enroll_frame, text='NEXT', bootstyle='primary',
                command=to_save_all)
            next_bttn.place(
                relx=.5, rely=.93,
                relheight=.06, relwidth=.15, anchor='center')

        def hide_enroll_show():
            account.border_frame.bind(
                "<Enter>",func=lambda b:enroll_button.place_forget())
            account.border_frame.bind(
                "<Leave>",
                func=lambda b:enroll_button.place(
                    anchor='center', relx=.5, rely=.9, 
                    relheight=.05, relwidth=.2))
        enroll_button = ttk.Button(
            image_cnvs, text='ENROLL NOW', bootstyle='success-outlined',command=enroll,)
        enroll_button.place(
            anchor='center', relx=.5, rely=.9, relheight=.05, relwidth=.2)
        hide_enroll_show()
        contact_us = ttk.Label(self,text='Contact us : 09123456789 | EMAIL: NameOfUni@fb.com',bootstyle='light')
        contact_us.place(relheight=.05,relwidth=.75,relx=.4,rely=.0001,anchor='nw')


        self.mainloop()


class mainMenu(ttk.Frame):
    def __init__(self,parent) -> None:
        super().__init__()
        try:
            # if the user exit the application without login or signing
            #   this code will gonna throw some error  
            self.my_gmail = parent.my_gmail
            self.my_password = parent.my_password
            parent.destroy()
        except AttributeError:
            # make sure the application is exited
            print('attribute errror - No account logged')
            parent.quit()
            self.quit()
            # replace else to avoid unnecessary indentaion. with return None.
            return None 
        self.configure(bootstyle='secondary')
        self.place_configure(
            relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # print(self.winfo_parent())
        
        
        # this frame will be the parent all of the widgets to keep the
        #   self frame clean and ready for any update or changes .
        main_frame = ttk.Frame(self,bootstyle='warning')
        main_frame.place(
            relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        main_frame.columnconfigure(0,weight=15)
        main_frame.columnconfigure(1,weight=30)
        main_frame.rowconfigure(0,weight=1)
        
        
        my_account = databaseAccountConnect(
            gmail=self.my_gmail,passw=self.my_password)
        
        user_profile = Profile(main_frame,my_account)
        
        menu_frame = ttk.Frame(main_frame,bootstyle='default')
        menu_frame.grid(column=1,row=0,sticky=tk.N+tk.S+tk.W+tk.E)
        def menu_frame_row_col():
            menu_frame.columnconfigure(0,weight=1)
            menu_frame.columnconfigure(1,weight=1)
            menu_frame.columnconfigure(2,weight=1)
            menu_frame.columnconfigure(3,weight=1)
            menu_frame.columnconfigure(4,weight=1)
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
            column=1,row=0,columnspan=3,sticky=tk.N+tk.S)
        
        # show button and hide button will contrast each other.
        def show_profile_frame(event):
            hamburger_show_bttn.place_forget()
            user_profile.show_frame()
            menu_frame.grid_configure(
                column=1,columnspan=1,row=0,sticky=tk.N+tk.S+tk.W+tk.E)
        
        
        def hide_frame(event):
            user_profile.hide_frame()
            menu_frame.grid_configure(
                column=0,columnspan=2,row=0,sticky=tk.N+tk.S+tk.W+tk.E)
            hamburger_show_bttn.place(
                relheight=.08,relwidth=.06,relx=.01,rely=.01)
            
        hamburger_show_bttn = ttk.Frame(
            menu_frame, bootstyle='default',)
        img_profile = Image.open(r'\Icons&bg\user.png')
        img_profile = img_profile.resize((50,50))
        image_profile =ImageTk.PhotoImage(image=img_profile)
        label_show_bttn = ttk.Label(borderwidth=0,
            master=hamburger_show_bttn, image=image_profile)
        label_show_bttn.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        label_show_bttn.bind(
            "<Button-1>",func=show_profile_frame)
        
        
        hamburger_hide_bttn = ttk.Frame(
            user_profile.frame, bootstyle='secondary')
        hamburger_hide_bttn.place(
            relheight=.08,relwidth=.14,relx=.03,rely=.02)
        img_back_profile = Image.open(r"\Icons&bg\left-arrow (1).png")
        img_back_profile = img_back_profile.resize((50,50))
        image_back_profile = ImageTk.PhotoImage(image=img_back_profile)
        label_hide_bttn = ttk.Label(borderwidth=0,background='#4e5d6c',
            master=hamburger_hide_bttn, image=image_back_profile)
        label_hide_bttn.place(relheight=1,relwidth=1,relx=.5,rely=.4,anchor='center')
        label_hide_bttn.bind(
            "<Button-1>",func=hide_frame)


        def hide_Profile():
            user_profile.frame.grid_remove()
        def bringback_profile():
            user_profile.frame.grid()
            
        # frame for each feature
        enroll = Enroll(
            menu_frame,1,2,'ENROLL',main_frame,
            back_profile=bringback_profile, hide_pro_func=hide_Profile)
        img = Image.open(r"C:\Users\james\Downloads\Icons&bg\student-card.png")
        img = img.resize((150,125))
        image =ImageTk.PhotoImage(image=img)
        l = ttk.Label(enroll.frame,image=image)
        l.grid(column=0,row=0,rowspan=2,sticky=tk.S)
        enroll.picture = l
        
        room = Room(
            menu_frame,3,2,'ROOM',main_frame,
            back_profile=bringback_profile, hide_pro_func=hide_Profile)
        img_chair = Image.open(r"C:\Icons&bg\classroom.png")
        img_chair = img_chair.resize((150,150))
        imagesd =ImageTk.PhotoImage(image=img_chair)
        chair_pic = tk.Label(room.frame,image=imagesd)
        chair_pic.grid(column=0,row=0,rowspan=2,sticky=tk.S)
        room.picture =chair_pic
        
        activity = Activity(
            menu_frame,1,4,'ACTIVITIES',main_frame,
            back_profile=bringback_profile, hide_pro_func=hide_Profile)
        img_exam = Image.open(r"\Icons&bg\quiz.png")
        img_exam = img_exam.resize((150,125))
        img_exam =ImageTk.PhotoImage(image=img_exam)
        activity_pic = tk.Label(activity.frame,image=img_exam)
        activity_pic.grid(column=0,row=0,rowspan=2,sticky=tk.S)
        activity.picture = activity_pic
        
        
        gallery = Gallary(
            menu_frame,3,4,'GALLERY',main_frame,
            back_profile=bringback_profile, hide_pro_func=hide_Profile)
        img_gallery = Image.open(r"\Icons&bg\education.png")
        img_gallery = img_gallery.resize((150,125))
        img_gallery =ImageTk.PhotoImage(image=img_gallery)
        galllery_pic = tk.Label(gallery.frame,image=img_gallery)
        galllery_pic.grid(column=0,row=0,rowspan=2,sticky=tk.S)
        gallery.picture = galllery_pic
        
        
        
        canteen = Canteen(
            menu_frame,1,6,'CANTEEN',main_frame,
            back_profile=bringback_profile, hide_pro_func=hide_Profile)
        img_canteen = Image.open(r"\Icons&bg\food.png")
        img_canteen = img_canteen.resize((150,150))
        img_canteen =ImageTk.PhotoImage(image=img_canteen)
        canteen_pic = tk.Label(canteen.frame,image=img_canteen)
        canteen_pic.grid(column=0,row=0,rowspan=2,sticky=tk.S)
        canteen.picture = canteen_pic
        





        self.mainloop()


if __name__ == '__main__':
    app = App()
    home = Home(app)
    mainMenu(home)