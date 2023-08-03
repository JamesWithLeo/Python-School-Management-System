import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
import sys_db

# widgets for taking student personal information
class getStudents:
    """Widgets containing entries for sign up/ enroll \n
    with methods to remove frame and fetch string variable"""
    def __init__(self,parent,uploadImage):
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
        student_main_frame.place(relx=.5,rely=.485,relheight=.8,relwidth=.8,anchor='center')
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
            fullname_frame.rowconfigure(9,weight=1)
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
        
        gender_str_var = tk.StringVar(value='M')
        male_lbl = ttk.Label(
            gender_frame, text='male :',font=('arial',14))
        male_lbl.grid(column=0,row=0)
        male_rb = ttk.Radiobutton(
            gender_frame,variable=gender_str_var,
            value='M')
        male_rb.grid(column=1,row=0)
        
        female_lbl = ttk.Label(
            gender_frame, text='female :',font=('arial',14))
        female_lbl.grid(column=0,row=1,sticky=tk.N)
        female_rb = ttk.Radiobutton(
            gender_frame,variable=gender_str_var,
            value='F',)
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
        
        address_frame.rowconfigure(0,weight=2)
        address_frame.rowconfigure(1,weight=2)
        address_frame.rowconfigure(2,weight=2)
        address_frame.rowconfigure(3,weight=2)
        address_frame.rowconfigure(4,weight=2)
        address_frame.rowconfigure(5,weight=2)
        address_frame.rowconfigure(6,weight=1)
        
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
        municipality_cb = ttk.Entry(
            address_frame,textvariable=municipality_str_var)
        municipality_cb.grid(column=2,row=1,sticky=tk.W+tk.E)
        
        barangay_lbl = ttk.Label(
            address_frame,text='barangay :',font=('arial',14))
        barangay_lbl.grid(column=1,row=1,sticky=tk.W)
        barangay_str_var = tk.StringVar()
        barangay_cb = ttk.ttk.Entry(
            address_frame,textvariable=barangay_str_var)
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
        education_frame.rowconfigure(3,weight=1)
        
        
        high_school_lbl = ttk.Label(
            education_frame,text='high school :',font=('arial',14))
        high_school_lbl.grid(
            column=1,row=0,sticky=tk.W)
        high_school_str_var = tk.StringVar()
        high_school_entry = ttk.Entry(
            education_frame,textvariable=high_school_str_var,)
        high_school_entry.grid(
            column=2,row=0,sticky=tk.W+tk.E)
        change_on_hover(high_school_entry,high_school_lbl)

        sep = ttk.Separator(
            education_frame,orient='horizontal',bootstyle='secondary')
        sep.grid(column=1,columnspan=2,row=0,sticky=tk.S+tk.W+tk.E)


        transfer_lbl = ttk.Label(
            education_frame,text='transferee :',font=('arial',14))
        transfer_lbl.grid(column=1,row=1,sticky=tk.W)
        def checkTranfereeValue():
            if transferee.get() is True:
                print(True)
                # place the docs widget.
                moral_lbl.grid(column=1,row=4,sticky=tk.W)
                grade_lbl.grid(column=1,row=5,sticky=tk.W)
                upload_moral_button.grid(column=2,row=4,sticky=tk.W+tk.E)
                upload_grade_button.grid(column=2,row=5,sticky=tk.W+tk.E)
                # configure previous label
                transfer_lbl['font'] = ('arial',12)
                high_school_lbl['font'] = ('arial',12)
                college_lvl_lbl['font'] = ('arial',12)
                course_lbl['font'] = ('arial',12)
            
            elif transferee.get() is False:
                print(False)
                moral_lbl.grid_forget()
                grade_lbl.grid_forget()
                upload_moral_button.grid_forget()
                upload_grade_button.grid_forget()
                transfer_lbl['font'] = ('arial',14)
                high_school_lbl['font'] = ('arial',14)
                college_lvl_lbl['font'] = ('arial',14)
                course_lbl['font'] = ('arial',14)
        
        transferee = tk.BooleanVar(value=False)
        transfer_cb = ttk.Checkbutton(
            education_frame,variable=transferee,command=checkTranfereeValue,
            text='YES',offvalue=False,onvalue=True)
        transfer_cb.grid(column=2,row=1,sticky=tk.W)
        transfer_no_cb = ttk.Checkbutton(
            education_frame,variable=transferee,command=checkTranfereeValue,
            text='NO',offvalue=True,onvalue=False)
        transfer_no_cb.grid(column=2,row=1)
        
        self.good_moral = None
        self.grade = None
        def upload_moral():
            goodmoral = filedialog.askopenfilename()
            if goodmoral.endswith('.jpg'):
                upload_moral_button.configure(text='UPLOADED!',bootstyle='secondary')
                self.good_moral = goodmoral
                print(goodmoral)
            
        def upload_grade():
            grade = filedialog.askopenfilename()
            if grade.endswith('.jpg'):
                upload_grade_button.configure(text='UPLOADED!',bootstyle='secondary')
                self.grade = grade
                print(grade)
            
        moral_lbl = ttk.Label(master=education_frame,text="good moral :",font=('arial',12))
        grade_lbl = ttk.Label(master=education_frame,text="grade :",font=('arial',12))
        upload_moral_button = ttk.Button(
            education_frame,text='UPLOAD file must be in .jpg',
            bootstyle='secondary-outlined',padding=2,command=upload_moral)
        upload_grade_button = ttk.Button(
            education_frame,text='UPLOAD file must be in .jpg',
            bootstyle='secondary-outlined',padding=2,command=upload_grade)
        
        course_lbl = ttk.Label(
            education_frame,text='course :',font=('arial',14))
        course_lbl.grid(
            column=1,row=2,sticky=tk.W)
        course_value = ['BSIT','BSCS','BSIS','BSC']
        course_str_var = tk.StringVar()
        course_entry = ttk.Combobox(
            education_frame,textvariable=course_str_var,values=course_value,)
        course_entry.grid(
            column=2,row=2,sticky=tk.W+tk.E)
        change_on_hover(course_entry,course_lbl)


        college_lvl_lbl = ttk.Label(
            education_frame,text='college level :',font=('arial',14))
        college_lvl_lbl.grid(
            column=1,row=3,sticky=tk.W)
        college_lvl_value = ['FRESHMEN','1ST YEAR','2ND YEAR','3RD YEAR','4TH YEAR']
        college_lvl_str_var = tk.StringVar()
        college_lvl_entry = ttk.Combobox(
            education_frame,textvariable=college_lvl_str_var,
            values=college_lvl_value)
        college_lvl_entry.grid(
            column=2,row=3,sticky=tk.W+tk.E)
        change_on_hover(college_lvl_entry,college_lvl_lbl)
        def college_check():
            print("focus- college_lvl_entry ", college_lvl_str_var.get())
            if college_lvl_str_var.get().strip() not in college_lvl_value:
                self.college_lvl_loop = college_lvl_entry.after(3000,college_check)
            else:
                self.college_lvl_loop = college_lvl_entry.after(5000,college_check)
                if college_lvl_str_var.get() == 'FRESHMEN':
                    transfer_cb.configure(state="disabled")
                    transferee.set(value=True)
                    transfer_lbl.grid_remove()
                    transfer_cb.grid_remove()
                    transfer_no_cb.grid_remove()
                    checkTranfereeValue()
                else:
                    transfer_cb.configure(state="enabled")
                    # checkTranfereeValue()
                    transfer_lbl.grid(column=1,row=1,sticky=tk.W)
                    transfer_cb.grid(column=2,row=1,sticky=tk.W)
                    transfer_no_cb.grid(column=2,row=1)
        self.college_lvl_loop = college_lvl_entry.after(3000,college_check)
        
        
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
        self.transferee_bool = transferee
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
        self.college_lvl_entry.after_cancel(self.college_lvl_loop)


    def display_frame(self)->None:
        self.student_main_frame.place(
            relx=.5,rely=.485,relheight=.8,relwidth=.8,anchor='center')


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

# widgets for taking student family information
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

# widgets for taking employees personal information
class Applicant:
    """Class for hiring staff, professors, and dev"""
    def __init__(
        self,parent, resume_upload_img,
        certificate_upload_img,chech_upload_image,
        login_frame,
        background_design,
        enroll_button) -> None:
        hire_frame = ttk.Frame( # Frame for  creating account .
            master=parent, bootstyle='default')
        self.member_frame = hire_frame
        
        account_fullname_role_frames = ttk.Frame(
            hire_frame,bootstyle='default')
        account_fullname_role_frames.place(
            relheight=.8,relwidth=1,relx=.5,rely=.5,anchor='center')
        
        
        def change_on_hover(trigger,target,styleOn,styleOff='default'):
            trigger.bind(
                "<Enter>", 
                func=lambda t:target.configure(bootstyle=styleOn),add='+')
            trigger.bind(
                "<Leave>", 
                func=lambda t:target.configure(bootstyle=styleOff),add='+')
        
        
        account_frame = ttk.Frame(
            account_fullname_role_frames,bootstyle='default')
        account_frame.place(
            relwidth=.65,relheight=.3,relx=.5,rely=.15,anchor='center')
        def account_frame_row_col():
            change_on_hover(account_frame,account_frame,'secondary')
            account_frame.columnconfigure(0,weight=1)
            account_frame.columnconfigure(1,weight=1)
            account_frame.columnconfigure(2,weight=1)
            account_frame.columnconfigure(3,weight=1)
            account_frame.rowconfigure(0,weight=1)
            account_frame.rowconfigure(1,weight=1)
            account_frame.rowconfigure(2,weight=1)
            account_frame.rowconfigure(3,weight=1)
            account_frame.rowconfigure(4,weight=1)
            account_frame.rowconfigure(5,weight=1)
            account_frame.rowconfigure(6,weight=1)
            sep = ttk.Separator(account_frame,orient='horizontal')
            sep.grid(column=0,row=0,columnspan=4,sticky=tk.N+tk.W+tk.E)
            sep = ttk.Separator(account_frame,orient='horizontal')
            sep.grid(column=0,row=6,columnspan=4,sticky=tk.S+tk.W+tk.E)
            sep = ttk.Separator(account_frame,orient='vertical')
            sep.grid(column=0,row=0,rowspan=7,sticky=tk.W+tk.N+tk.S)
            sep = ttk.Separator(account_frame,orient='vertical')
            sep.grid(column=3,row=0,rowspan=7,sticky=tk.E+tk.N+tk.S)
        account_frame_row_col()    
        
        gmail_lbl = ttk.Label(
            account_frame,text='GMAIL :',font=('arial',11))
        gmail_lbl.grid(
            column=1,row=1,sticky=tk.W)
        phone_lbl = ttk.Label(
            account_frame,text='PHONE NUMBER :',font=('arial',11))
        phone_lbl.grid(
            column=1,row=3,sticky=tk.W)
        password_lbl = ttk.Label(
            account_frame,text='PASSWORD :',font=('arial',11))
        password_lbl.grid(
            column=1,row=5,sticky=tk.W)
        
        gmail_str_var = tk.StringVar()
        gmail_entry = ttk.Entry(account_frame,textvariable=gmail_str_var)
        gmail_entry.grid(column=2,row=1,sticky=tk.W+tk.E)
        phone_str_var = tk.StringVar()
        phone_entry = ttk.Entry(account_frame,textvariable=phone_str_var)
        phone_entry.grid(column=2,row=3,sticky=tk.W+tk.E)
        password_str_var = tk.StringVar()
        password_entry = ttk.Entry(account_frame,textvariable=password_str_var)
        password_entry.grid(column=2,row=5,sticky=tk.W+tk.E)
        
        
        role_frame = ttk.Frame(account_fullname_role_frames,bootstyle='default')
        role_frame.place(
            relwidth=.65,relheight=.2,relx=.5,rely=.45,anchor='center')
        def role_frame_row_col():
            change_on_hover(role_frame,role_frame,'secondary')
            role_frame.columnconfigure(0,weight=1)
            role_frame.columnconfigure(1,weight=2)
            role_frame.columnconfigure(2,weight=1)
            role_frame.columnconfigure(3,weight=2)
            role_frame.columnconfigure(4,weight=1)
            role_frame.columnconfigure(5,weight=2)
            role_frame.columnconfigure(6,weight=1)
            role_frame.rowconfigure(0,weight=1)
            role_frame.rowconfigure(1,weight=2)
            role_frame.rowconfigure(2,weight=1)
            role_frame.rowconfigure(3,weight=2)
            role_frame.rowconfigure(4,weight=1)
            sep = ttk.Separator(role_frame,orient='horizontal')
            sep.grid(column=0,row=0,columnspan=7,sticky=tk.N+tk.W+tk.E)
            sep = ttk.Separator(role_frame,orient='horizontal')
            sep.grid(column=0,row=4,columnspan=7,sticky=tk.S+tk.W+tk.E)
            sep = ttk.Separator(role_frame,orient='vertical')
            sep.grid(column=0,row=0,rowspan=5,sticky=tk.W+tk.N+tk.S)
            sep = ttk.Separator(role_frame,orient='vertical')
            sep.grid(column=6,row=0,rowspan=5,sticky=tk.E+tk.N+tk.S)
        role_frame_row_col()
        
        role_str_var = tk.StringVar()
        utility_staff = ttk.Radiobutton(
            role_frame,value="US",variable=role_str_var,padding=1.5)
        utility_staff.grid(
            column=2,row=1,sticky=tk.W)
        
        security_staff = ttk.Radiobutton(
            role_frame,value="SS",variable=role_str_var,padding=1.5)
        security_staff.grid(
            column=5,row=1,sticky=tk.W)
        
        admin_staff = ttk.Radiobutton(
            role_frame,value="AS",variable=role_str_var,padding=1.5)
        admin_staff.grid(
            column=2,row=3,sticky=tk.W)
        
        professor = ttk.Radiobutton(
            role_frame,value="PS",variable=role_str_var,padding=1.5)
        professor.grid(
            column=5,row=3,sticky=tk.W)
        
        utility_staff_label = ttk.Label(
            role_frame,text="UTILITY STAFF :",font=('arial',11))
        utility_staff_label.grid(
            column=1,row=1,sticky=tk.E)
        security_staff_label = ttk.Label(
            role_frame,text="SECURITY STAFF :",font=('arial',11))
        security_staff_label.grid(
            column=4,row=1,sticky=tk.E)
        admin_staff_label = ttk.Label(
            role_frame,text="ADMIN STAFF :",font=('arial',11))
        admin_staff_label.grid(
            column=1,row=3,sticky=tk.E)
        professor_label = ttk.Label(
            role_frame,text="PROFESSOR :",font=('arial',11))
        professor_label.grid(
            column=4,row=3,sticky=tk.E)


        fullname_frame = ttk.Frame(
            account_fullname_role_frames, bootstyle='default')
        fullname_frame.place(
            relheight=.4,relwidth=.65,relx=.5,rely=.8,anchor='center')
        change_on_hover(
            trigger=fullname_frame, target=fullname_frame,
            styleOn='secondary',styleOff='default')
        
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
            sep = ttk.Separator(fullname_frame,orient='horizontal',)
            sep.grid(column=0,row=0,columnspan=5,sticky=tk.W+tk.E+tk.N)
            
            sep = ttk.Separator(fullname_frame,orient='horizontal',)
            sep.grid(column=0,row=8,columnspan=5,sticky=tk.W+tk.E+tk.S)
            
            sep = ttk.Separator(fullname_frame,orient="vertical")
            sep.grid(column=0,row=0,rowspan=9,sticky=tk.N+tk.S+tk.W)
            
            sep = ttk.Separator(fullname_frame,orient="vertical")
            sep.grid(column=4,row=0,rowspan=9,sticky=tk.N+tk.S+tk.E)
        col_pos_entries_frame()
        
        
        name_lbl = ttk.Label(
            fullname_frame,text='name :',font=('arial',14))
        name_lbl.grid(
            column=1,row=1,sticky=tk.W)
        mid_name_lbl = ttk.Label(
            fullname_frame,text='Middle name :',font=('arial',14))
        mid_name_lbl.grid(
            column=1,row=3,sticky=tk.W)
        last_name_lbl = ttk.Label(
            fullname_frame,text='lastname :',font=('arial',14))
        last_name_lbl.grid(
            column=1,row=5,sticky=tk.W)
        suffix_name_lbl = ttk.Label(
            fullname_frame,text='suffix :',font=('arial',14))
        suffix_name_lbl.grid(
            column=1,row=7,sticky=tk.W)
        
        name_str_var = tk.StringVar()
        name_entry = ttk.Entry(
            fullname_frame,textvariable=name_str_var,)
        name_entry.grid(
            column=2,row=1,sticky=tk.W+tk.E)

        mid_name_str_var = tk.StringVar()
        mid_name_entry = ttk.Entry(
            fullname_frame,textvariable=mid_name_str_var,)
        mid_name_entry.grid(
            column=2,row=3,sticky=tk.W+tk.E)
        
        last_name_str_var = tk.StringVar()
        last_name_entry = ttk.Entry(
            fullname_frame,textvariable=last_name_str_var,)
        last_name_entry.grid(
            column=2,row=5,sticky=tk.W+tk.E)
        
        suffix_name_str_var = tk.StringVar()
        suffix_name_entry = ttk.Entry(
            fullname_frame,textvariable=suffix_name_str_var,)
        suffix_name_entry.grid(
            column=2,row=7,sticky=tk.W+tk.E)
        
        
        self.name = name_str_var
        self.middle_name = mid_name_str_var
        self.last_name = last_name_str_var
        self.suffix_name = suffix_name_str_var
        self.role = role_str_var
        self.gmail = gmail_str_var
        self.phone = phone_str_var
        self.password = password_str_var
        def next_frame():
            account_fullname_role_frames.place_forget()
            next_button.place_forget()
            
            
            address_contact_education = ttk.Frame(
                hire_frame,bootstyle='default')
            address_contact_education.place(
                relheight=.8,relwidth=1,relx=.5,rely=.5,anchor='center')
            
            address_frame = ttk.Frame(
                address_contact_education,bootstyle='seconday')
            address_frame.place(
                relheight=.45,relwidth=.65,relx=.5,rely=.25,anchor='center')
            def address_frame_row_col():
                address_frame.columnconfigure(0,weight=1)
                address_frame.columnconfigure(1,weight=1)
                address_frame.columnconfigure(2,weight=1)
                address_frame.columnconfigure(3,weight=1)
                address_frame.rowconfigure(0,weight=1)
                address_frame.rowconfigure(1,weight=1)
                address_frame.rowconfigure(2,weight=1)
                address_frame.rowconfigure(3,weight=1)
                address_frame.rowconfigure(4,weight=1)
                address_frame.rowconfigure(5,weight=1)
                address_frame.rowconfigure(6,weight=1)
                address_frame.rowconfigure(7,weight=1)
                address_frame.rowconfigure(8,weight=1)
                sep = ttk.Separator(address_frame,orient='horizontal')
                sep.grid(column=0,row=0,columnspan=4,sticky=tk.N+tk.W+tk.E)
                sep = ttk.Separator(address_frame,orient='horizontal')
                sep.grid(column=0,row=8,columnspan=4,sticky=tk.S+tk.W+tk.E)
                sep = ttk.Separator(address_frame,orient='vertical')
                sep.grid(column=0,row=0,rowspan=9,sticky=tk.W+tk.N+tk.S)
                sep = ttk.Separator(address_frame,orient='vertical')
                sep.grid(column=3,row=0,rowspan=9,sticky=tk.E+tk.N+tk.S)
            address_frame_row_col()
            
            street_lbl = ttk.Label(
                address_frame,text='STREET :',font=('arial',11))
            street_lbl.grid(column=1,row=1,sticky=tk.W)
            municipality = ttk.Label(
                address_frame,text='MUNICIPALITY :',font=('arial',11))
            municipality.grid(column=1,row=3,sticky=tk.W)
            barangay = ttk.Label(
                address_frame,text='BARANGAY :',font=('arial',11))
            barangay.grid(column=1,row=5,sticky=tk.W)
            contact_no = ttk.Label(
                address_frame,text='CONTACT NO :',font=('arial',11))
            contact_no.grid(column=1,row=7,sticky=tk.W)
            
            street_str_var = tk.StringVar()
            street_entry = ttk.Entry(
                address_frame,textvariable=street_str_var,)
            street_entry.grid(
                column=2,row=1,sticky=tk.W+tk.E)
            municipality_str_var = tk.StringVar()
            municipality_entry = ttk.Entry(
                address_frame,textvariable=municipality_str_var,)
            municipality_entry.grid(
                column=2,row=3,sticky=tk.W+tk.E)
            barangay_str_var = tk.StringVar()
            barangay_entry = ttk.Entry(
                address_frame,textvariable=barangay_str_var,)
            barangay_entry.grid(
                column=2,row=5,sticky=tk.W+tk.E)
            contact_str_var = tk.StringVar()
            contact_entry = ttk.Entry(
                address_frame,textvariable=contact_str_var,)
            contact_entry.grid(
                column=2,row=7,sticky=tk.W+tk.E)
            #
            #
            upload = ttk.Frame(
                address_contact_education,bootstyle='seconday')
            def upload_row_col():
                upload.columnconfigure(0,weight=1)
                upload.columnconfigure(1,weight=1)
                upload.columnconfigure(2,weight=1)
                upload.columnconfigure(3,weight=1)
                upload.rowconfigure(0,weight=1)
                upload.rowconfigure(1,weight=1)
                upload.rowconfigure(2,weight=1)
                sep = ttk.Separator(upload,orient='horizontal')
                sep.grid(column=0,row=0,columnspan=4,sticky=tk.N+tk.W+tk.E)
                sep = ttk.Separator(upload,orient='horizontal')
                sep.grid(column=0,row=3,columnspan=4,sticky=tk.S+tk.W+tk.E)
                sep = ttk.Separator(upload,orient='vertical')
                sep.grid(column=0,row=0,rowspan=4,sticky=tk.S+tk.W+tk.N)
                sep = ttk.Separator(upload,orient='vertical')
                sep.grid(column=3,row=0,rowspan=4,sticky=tk.S+tk.E+tk.N)
            upload_row_col()
            
            resume = None
            def upload_resume(event):
                nonlocal resume
                resume = filedialog.askopenfilename()
                resume_button.configure(image=chech_upload_image)
                
            certificate = None
            def upload_certificate(event):
                nonlocal certificate
                certificate = filedialog.askopenfilename()
                certificate_button.configure(image=chech_upload_image)
                
                
            resume_lbl = ttk.Label(
                upload,text='UPLOAD RESUME :',font=('arial',11))
            resume_lbl.grid(column=1,row=1,sticky=tk.W)
            resume_button = ttk.Label(
                upload,image=resume_upload_img,anchor='center')
            resume_button.grid(column=2,row=1)
            resume_button.bind("<Button-1>",func=upload_resume)
            
            certificate_lbl = ttk.Label(
                upload,text='UPLOAD CERTIFICATE :',font=('arial',11))
            certificate_button = ttk.Label(
                upload,image=certificate_upload_img,)
            certificate_button.bind("<Button-1>",func=upload_certificate)
            #
            #
            education = ttk.Frame(
                    address_contact_education,bootstyle='seconday')
            def education_row_col():
                education.columnconfigure(0,weight=1)
                education.columnconfigure(1,weight=1)
                education.columnconfigure(2,weight=1)
                education.columnconfigure(3,weight=1)
                education.rowconfigure(0,weight=1)
                education.rowconfigure(1,weight=1)
                education.rowconfigure(2,weight=1)
                sep = ttk.Separator(education,orient='horizontal')
                sep.grid(column=0,row=0,columnspan=4,sticky=tk.N+tk.W+tk.E)
                sep = ttk.Separator(education,orient='horizontal')
                sep.grid(column=0,row=2,columnspan=4,sticky=tk.S+tk.W+tk.E)
                sep = ttk.Separator(education,orient='vertical')
                sep.grid(column=0,row=0,rowspan=3,sticky=tk.N+tk.W+tk.S)
                sep = ttk.Separator(education,orient='vertical')
                sep.grid(column=3,row=0,rowspan=3,sticky=tk.N+tk.E+tk.S)
            education_row_col()
            degree_lbl = ttk.Label(
                education,text='COLLEGE DEGREE :',font=('arial',11))
            degree_lbl.grid(column=1,row=1,sticky=tk.W)
            degree_str_var = tk.StringVar()
            degree_entry = ttk.Entry(
                education,textvariable=degree_str_var,)
            degree_entry.grid(
                column=2,row=1,sticky=tk.W+tk.E)
            
            
            if role_str_var.get() == 'US':
                upload.place(
                    relheight=.2,relwidth=.65,relx=.5,rely=.6,anchor='center')
            else:
                education.place(
                    relheight=.15,relwidth=.65,relx=.5,rely=.6,anchor='center')
                upload.place(
                    relheight=.25,relwidth=.65,relx=.5,rely=.85,anchor='center')
                upload.rowconfigure(3,weight=1)
                certificate_lbl.grid(column=1,row=2,sticky=tk.W)
                certificate_button.grid(column=2,row=2)
                

            change_on_hover(upload,upload,'secondary')
            change_on_hover(
                address_frame,address_frame,'secondary')
            change_on_hover(education,education,'secondary')
            self.street = street_str_var
            self.municipality = municipality_str_var
            self.barangay = barangay_str_var
            self.contact = contact_str_var

            
            def submit():
                nonlocal certificate, resume
                print(certificate)
                print(resume)
                str_vars = [
                    self.street,
                    self.municipality,
                    self.barangay,
                    self.contact,]
                for var in str_vars:
                    if var.get().strip() == '':
                        return None
                    
                if role_str_var.get() == 'US':
                    if resume is None:
                        return None
                    elif resume == '':
                        return None
                else:
                    if resume is None or certificate is None:
                        return None
                    elif resume == '' or \
                        certificate == '':
                        return None
                self.place_forget_member_frame()
                self.resume = resume
                self.certificate = certificate
                login_frame.place(
                    relx=.994,rely=.5,anchor='e',relheight=.98,relwidth=.4)
                background_design.place(
                    relheight=.98, relwidth=.59 , relx=.3,rely=.5, anchor='center')
                enroll_button.place(
                    anchor='center', relx=.5, rely=.9, relheight=.05, relwidth=.2)
                print('win')
                address_contact_education.place_forget()
                account_fullname_role_frames.place(
                    relheight=.8,relwidth=1,relx=.5,rely=.5,anchor='center')
                back_button.place_forget()
                submit_button.place_forget()
                next_button.place(
                relheight=.05,relwidth=.15,relx=.5,rely=.94,anchor='center')
                
                # save entry
                gmail = gmail_str_var.get()
                phone_no = phone_str_var.get()
                password = password_str_var.get()
                role = role_str_var.get()
                name = name_str_var.get()
                middle_name = mid_name_str_var.get()
                last_name = last_name_str_var.get()
                suffix_name = street_str_var.get()
                degree = degree_str_var.get()
                street = street_str_var.get()
                municipality = municipality_str_var.get()
                barangay = barangay_str_var.get()
                contact_no = contact_str_var.get()
                
                applicant_data = [
                    gmail, phone_no, password, role,
                    name, middle_name, last_name, suffix_name,
                    degree,
                    street, municipality, barangay,
                    contact_no, resume
                ]
                if role == 'US':
                    sys_db.mycursor.execute(
                    sys_db.insert_applicant,
                    applicant_data)
                else:
                    applicant_data.append(certificate)
                    sys_db.cursor_exe(
                        sql_code=sys_db.insert_applicant_with_cert,
                        target=applicant_data)
                
                sys_db.commit_transact()
                # set the entry to default. So its ready for another applicant.
                gmail_str_var.set('')
                phone_str_var.set('')
                password_str_var.set('')
                role_str_var.set('')
                name_str_var.set('')
                mid_name_str_var.set('')
                last_name_str_var.set('')
                suffix_name_str_var.set('')
                street_str_var.set('')
                municipality_str_var.set('')
                barangay_str_var.set('')
                degree_str_var.set('')
                resume = None
                certificate = None
            
            
            submit_button = ttk.Button(
            hire_frame, text='submit', bootstyle='success',command=submit)
            submit_button.place(
            relheight=.05,relwidth=.15,relx=.65,rely=.94,anchor='center')

            def back_frame():
                account_fullname_role_frames.place(
                    relheight=.8,relwidth=1,relx=.5,rely=.5,anchor='center')
                address_contact_education.place_forget()
                back_button.place_forget()
                submit_button.place_forget()
                next_button.place(
                relheight=.05,relwidth=.15,relx=.5,rely=.94,anchor='center')
            
            back_button = ttk.Button(
            hire_frame, text='Back', bootstyle='danger',command=back_frame)
            back_button.place(
                relheight=.05,relwidth=.15,relx=.35,rely=.94,anchor='center')
            
            
        def verify_account_entries():
            str_vars = [
                self.name,
                self.middle_name,
                self.last_name,
                self.role,
                self.gmail,
                self.phone,
                self.password,]
            for var in str_vars:
                if var.get().strip() == '':
                    return None
            next_frame()
                        
        next_button = ttk.Button(
            hire_frame, text='Next', bootstyle='primary',
            command=verify_account_entries)
        next_button.place(
            relheight=.05,relwidth=.15,relx=.5,rely=.94,anchor='center')
        
        
    def place_member_frame(self):
        self.member_frame.place(
            relx=.5,rely=.5,
            relheight=.8,relwidth=.5,anchor='center')
    
    
    def place_forget_member_frame(self):
        self.member_frame.place_forget()
