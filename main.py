# import json
import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image

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
        self.my_password = password_str_var
        self.my_gmail = gmail_str_var
        self.password_entry = password_entry

class getName:
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
        fullname_frame = ttk.Frame(parent, bootstyle='default')
        fullname_frame.place(
            relx=.29, rely=.3,
            relheight=.4, relwidth=.4, anchor='center'
        )
        
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
            fullname_frame,textvariable=gmail_str_var
        )
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
            fullname_frame, orient='horizontal',
            bootstyle='secondary'
        )
        sep.grid(
            column=0,row=3,columnspan=5,sticky=tk.S+tk.W+tk.E)
        sep = ttk.Separator(
            fullname_frame, orient='horizontal',
            bootstyle='secondary'
        )
        sep.grid(
            column=0,row=0,columnspan=5,sticky=tk.N+tk.W+tk.E)
        sep = ttk.Separator(
            fullname_frame, orient='vertical',
            bootstyle='secondary'
        )
        sep.grid(
            column=0,row=0,rowspan=4,sticky=tk.N+tk.W+tk.S)
        sep = ttk.Separator(
            fullname_frame, orient='vertical',
            bootstyle='secondary'
        )
        sep.grid(
            column=4,row=0,rowspan=4,sticky=tk.N+tk.E+tk.S)
        
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
        
        sep = ttk.Separator(
            fullname_frame, orient='horizontal',
            bootstyle='secondary'
        )
        sep.grid(
            column=0,row=5,columnspan=5,sticky=tk.N+tk.W+tk.E)
        sep = ttk.Separator(
            fullname_frame, orient='horizontal',
            bootstyle='secondary'
        )
        sep.grid(
            column=0,row=9,columnspan=5,sticky=tk.S+tk.W+tk.E)
        sep = ttk.Separator(
            fullname_frame, orient='vertical',
            bootstyle='secondary'
        )
        sep.grid(
            column=0,row=5,rowspan=5,sticky=tk.N+tk.W+tk.S)
        sep = ttk.Separator(
            fullname_frame, orient='vertical',
            bootstyle='secondary'
        )
        sep.grid(
            column=4,row=5,rowspan=5,sticky=tk.N+tk.E+tk.S)
        gender_frame = ttk.Labelframe(
            parent,text='SEX',bootstyle='secondary')
        gender_frame.place(
            relx=.19,relheight=.118,relwidth=.2,rely=.57,anchor='center')
        gender_frame.columnconfigure(0,weight=1)
        gender_frame.columnconfigure(1,weight=1)
        gender_frame.rowconfigure(0,weight=1)
        gender_frame.rowconfigure(1,weight=1)
        
        gender_str_var = tk.StringVar()
        male_lbl = ttk.Label(
            gender_frame, text='male :',font=('arial',14))
        male_lbl.grid(column=0,row=0)
        male_rb = ttk.Radiobutton(
            gender_frame,textvariable=gender_str_var,
            value='M')
        male_rb.grid(column=1,row=0)
        
        female_lbl = ttk.Label(
            gender_frame, text='female :',font=('arial',14))
        female_lbl.grid(column=0,row=1,sticky=tk.N)
        female_rb = ttk.Radiobutton(
            gender_frame,textvariable=gender_str_var,
            value='F')
        female_rb.grid(column=1,row=1)
        
        
        
        birth_frame = ttk.Labelframe(
            parent,text='DATE-OF-BIRTH',
            bootstyle='secondary')
        birth_frame.place(
            relx=.19,relheight=.2,
            relwidth=.2,rely=.74,anchor='center')
        birth_frame.columnconfigure(0,weight=1)
        birth_frame.columnconfigure(1,weight=1)
        birth_frame.rowconfigure(0,weight=1)
        birth_frame.rowconfigure(1,weight=1)
        birth_frame.rowconfigure(2,weight=1)
        
        month_lbl = ttk.Label(
            birth_frame,text='month :',font=('arial',14))
        month_lbl.grid(column=0,row=0)
        month_cb = ttk.Combobox(
            birth_frame,values=list(range(1,13)),width=10)
        month_cb.grid(column=1,row=0)
        
        day_lbl = ttk.Label(
            birth_frame,text='day :',font=('arial',14))
        day_lbl.grid(column=0,row=1)
        day_cb = ttk.Combobox(
            birth_frame,values=list(range(1,32)),width=10)
        day_cb.grid(column=1,row=1)
        
        year_lbl = ttk.Label(
            birth_frame,text='year :',font=('arial',14))
        year_lbl.grid(column=0,row=2)
        year_cb = ttk.Combobox(
            birth_frame,values=list(range(1900,2024)),
            width=10,height=5)
        year_cb.grid(column=1,row=2)
        
        
        nationality_frame = ttk.Frame(
            parent,bootstyle='default')
        nationality_frame.place(
            relx=.4,relheight=.315,relwidth=.18,
            rely=.682,anchor='center')
        nationality_frame.columnconfigure(0,weight=1)
        nationality_frame.rowconfigure(0,weight=1)
        nationality_frame.rowconfigure(1,weight=1)
        nationality_frame.rowconfigure(2,weight=1)
        nationality_frame.rowconfigure(3,weight=1)
        nationality_frame.rowconfigure(4,weight=1)
        nationality_frame.rowconfigure(5,weight=1)
        
        sep = ttk.Separator(
            nationality_frame,bootstyle='secondary',orient='horizontal')
        sep.grid(column=0,row=0,sticky=tk.N+tk.W+tk.E)
        sep = ttk.Separator(
            nationality_frame,bootstyle='secondary',orient='horizontal')
        sep.grid(column=0,row=5,sticky=tk.S+tk.W+tk.E)
        sep = ttk.Separator(
            nationality_frame,bootstyle='secondary',orient='vertical')
        sep.grid(column=0,row=0,rowspan=6,sticky=tk.S+tk.W+tk.N)
        sep = ttk.Separator(
            nationality_frame,bootstyle='secondary',orient='vertical')
        sep.grid(column=1,row=0,rowspan=6,sticky=tk.S+tk.N+tk.E)
        civil_lbl = ttk.Label(
            nationality_frame,text='civil status',font=('helveltica',14))
        civil_lbl.grid(column=0,row=0,sticky=tk.S,pady=1)
        civil_cb = ttk.Combobox(
            nationality_frame,values=list(range(1,32)),width=12)
        civil_cb.grid(column=0,row=1)
        nationality_lbl = ttk.Label(
            nationality_frame,text='nationality',font=('arial',14))
        nationality_lbl.grid(column=0,row=4,sticky=tk.S)
        nationality_entry = ttk.Entry(nationality_frame,width=15)
        nationality_entry.grid(column=0,row=5,sticky=tk.N)
        
        religion_lbl = ttk.Label(
            nationality_frame,text='religion',font=('arial',14))
        religion_lbl.grid(column=0,row=2,sticky=tk.S)
        religion_entry = ttk.Entry(nationality_frame,width=15)
        religion_entry.grid(column=0,row=3,sticky=tk.N)
        
        
        address_frame = ttk.Labelframe(
            parent,labelanchor='n',text='ADDRESS' ,
            bootstyle='secondary')
        address_frame.place(
            relx=.71, rely=.3,
            relheight=.4, relwidth=.4, anchor='center')
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
        
        street_lbl = ttk.Label(
            address_frame,text='street :',font=('arial',14))
        street_lbl.grid(column=1,row=0,sticky=tk.W)
        street_entry = ttk.Entry(address_frame,width=19)
        street_entry.grid(column=2,row=0,sticky=tk.W+tk.E)
        
        barangay_lbl = ttk.Label(
            address_frame,text='barangay :',font=('arial',14))
        barangay_lbl.grid(column=1,row=1,sticky=tk.W)
        barangay_cb = ttk.ttk.Combobox(
            address_frame,width=17)
        barangay_cb.grid(column=2,row=1,sticky=tk.W+tk.E)
        
        municipality_lbl = ttk.Label(
            address_frame,text='municipality :',font=('arial',14))
        municipality_lbl.grid(column=1,row=2,sticky=tk.W)
        municipality_cb = ttk.Combobox(
            address_frame,width=17)
        municipality_cb.grid(column=2,row=2,sticky=tk.W+tk.E)
        
        zipcode_lbl = ttk.Label(
            address_frame,text='zip code :',font=('arial',14))
        zipcode_lbl.grid(column=1,row=3,sticky=tk.W)
        zipcode_entry = ttk.Entry(address_frame,width=19)
        zipcode_entry.grid(column=2,row=3,sticky=tk.W+tk.E)
        
        contact_no_lbl = ttk.Label(
            address_frame,text='contact number :',font=('arial',14))
        contact_no_lbl.grid(column=1,row=4,sticky=tk.W)
        contact_no_entry = ttk.Entry(address_frame,width=19)
        contact_no_entry.grid(column=2,row=4,sticky=tk.W+tk.E)
        
        birth_place_lbl = ttk.Label(
            address_frame,text='birth place :',font=('arial',14))
        birth_place_lbl.grid(column=1,row=5,sticky=tk.W)
        birth_place_entry = ttk.Entry(address_frame,width=19)
        birth_place_entry.grid(column=2,row=5,sticky=tk.W+tk.E)
        
        education_frame = ttk.Labelframe(
            parent,text='EDUCATION',labelanchor='n' 
            ,bootstyle='secondary')
        education_frame.place(
            relx=.71, rely=.679,
            relheight=.325, relwidth=.4, anchor='center'
        )
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
        
        self.my_gmail = gmail_str_var
        self.my_password = password_var
        self.my_name = name_str_var
        self.my_middle_name = mid_name_str_var
        self.my_last_name = last_name_str_var
        self.my_suffix = suffix_name_str_var
        
        self.fullname_frame = fullname_frame
        self.gender_frame = gender_frame
        self.birth_date_frame = birth_frame
        self.nationality_frame = nationality_frame
        self.address_frame = address_frame
        self.education_frame = education_frame
        
    def remove_f(self):
        self.fullname_frame.place_forget()
        self.gender_frame.place_forget()
        self.birth_date_frame.place_forget()
        self.nationality_frame.place_forget()
        self.address_frame.place_forget()
        self.education_frame.place_forget()
        
    def display_f(self):
        self.fullname_frame.place(
            relx=.29, rely=.3,
            relheight=.4, relwidth=.4, anchor='center')
        self.gender_frame.place(
            relx=.19,relheight=.118,
            relwidth=.2,rely=.57,anchor='center')
        self.birth_date_frame.place(
            relx=.19,relheight=.2,relwidth=.2
            ,rely=.74,anchor='center')
        self.nationality_frame.place(
            relx=.4,relheight=.315,relwidth=.18,
            rely=.682,anchor='center')
        self.address_frame.place(
            relx=.71, rely=.3,
            relheight=.4, relwidth=.4, anchor='center')
        self.education_frame.place(
            relx=.71, rely=.679,
            relheight=.325, relwidth=.4, anchor='center')
        def get_all_data():
                pass


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
            guardian_parent,bootstyle='primary',text='FATHER-INFO',labelanchor='nw')
        father_frame.grid(column=0,row=0,sticky=tk.N+tk.S+tk.E+tk.W)
        father_frame.columnconfigure(0,weight=1)
        father_frame.columnconfigure(1,weight=1)
        father_frame.columnconfigure(2,weight=1)
        father_frame.columnconfigure(3,weight=1)
        # father_frame.columnconfigure(4,weight=1)
        
        father_frame.rowconfigure(0,weight=1)
        father_frame.rowconfigure(1,weight=1)
        # father_frame.rowconfigure(2,weight=1)
        # father_frame.rowconfigure(3,weight=1)
        # father_frame.rowconfigure(4,weight=1)
        # father_frame.rowconfigure(5,weight=1)
        # father_frame.rowconfigure(6,weight=1)
        
        
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
            guardian_parent,bootstyle='primary',text='MOTHER-INFO')
        mother_frame.grid(column=0,row=1,sticky=tk.N+tk.S+tk.E+tk.W)
        mother_frame.columnconfigure(0,weight=1)
        mother_frame.columnconfigure(1,weight=1)
        mother_frame.columnconfigure(2,weight=1)
        mother_frame.columnconfigure(3,weight=1)
        mother_frame.rowconfigure(0,weight=1)
        mother_frame.rowconfigure(1,weight=1)
        
        mother_fullname_lbl = ttk.Label(
            mother_frame,text='maiden full name :',font=('arial',14))
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
            guardian_parent,bootstyle='primary',text='GUARDIAN-INFO')
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
        
    def display_f(self):
        self.frame.place(
            relx=.5,rely=.49,relheight=.8,relwidth=.8,anchor='center')


    def remove_f(self):
        self.frame.place_forget()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('School System')
        self.style = ttk.Style()
        self.style.configure('.',font=('System 20'))
        def app_geometry():
            scrn_w = int((self.winfo_screenwidth()-1000) / 2)
            scrn_h = int((self.winfo_screenheight()-700) / 2)
            self.geometry(f'1000x700+{scrn_w}+{scrn_h}')
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
            master=parent, bootstyle='primary',state='disabled')
        bg_design.place(
            relheight=.98, relwidth=.59 , relx=.3,rely=.5, anchor='center')
        # import any picture of school facade .
        # image_background = Image.open(
        #     r'picture in the bg.')
        # resized_img = image_background.resize((1560,900))
        # final_img = ImageTk.PhotoImage(image=resized_img)
        # image_cnvs = ttk.Label(
        #     master=bg_design,bootstyle='secondary')
        # image_cnvs.place(
        #     relx=.5, rely=.5 , relheight=.98, relwidth=.98, anchor='center',)
        # image_cnvs.configure(image=final_img)
        # image_cnvs.lower()
        
        
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
            """DB"""
            WRONG_GMAIL = None
            WRONG_PASSWORD = None
            if account.my_gmail.get().strip() == '' and \
                account.my_password.get().strip() == '' :
                account.gmail_entry.configure(bootstyle='danger')
                account.password_entry.configure(bootstyle='danger')
            
            elif account.my_gmail.get().strip() == '' and \
                account.my_password.get().strip() != '' :
                account.password_entry.configure(bootstyle='default')
                account.gmail_entry.configure(bootstyle='danger')
                
            
            elif account.my_password.get().strip() == '' and \
                account.my_gmail.get().strip() != '':
                account.gmail_entry.configure(bootstyle='default')
                account.password_entry.configure(bootstyle='danger')


            if account.my_password.get().strip() == '':
                account.password_entry.configure(bootstyle='danger')
            else:
                account.gmail_entry.configure(bootstyle='default')
                account.password_entry.configure(bootstyle='default')
                print('try')
                if account.my_gmail.get() not in ['james', 'leo']:
                    warn_no_acc_gmail.place(
                        relx=.5 , rely=.564 ,anchor='center'
                        # relheight=.03, relwidth=.34
                        )
                    account.border_frame.configure(bootstyle='danger')
                    WRONG_GMAIL = True
                    
                else:
                    account.gmail_entry.configure(bootstyle='primary')
                    warn_no_acc_gmail.place_forget()
                    account.border_frame.configure(bootstyle='primary')
                    self.my_gmail = account.my_gmail
                    if account.my_password.get() not in ['james','leo']:
                        account.password_entry.configure(bootstyle='danger')
                        warn_incorrect_pass.place(
                            relx=.41,rely=.4, 
                            # relheight=.09,relwidth=.458
                            )
                        WRONG_PASSWORD = True
                    else:
                        account.password_entry.configure(bootstyle='primary')            
                        self.my_password = account.my_password
                        if WRONG_GMAIL is True or  WRONG_PASSWORD is True:
                            pass
                        else:   # if account exist and correct password
                            self.quit()

        # Once enter key pressed, typed gmail and password will be submitted
        #   to  check its existence, authority, and to veritfy .
        # Basically its like loggin_button but it doesn't need mouse to work
        account.password_entry.bind(
            "<Return>", func=str_var_gmail_password)

        # Following labels is for entries, 
        #   it will only show depending on condition .
        warn_no_entry_gmail = ttk.Label(
            master=account.border_frame,
            text='INVALID GMAIL',
            bootstyle='danger-inversed',justify='center',font=('helveltica',10))

        warn_no_acc_gmail = ttk.Label(
            master=self,
            text='Account doesnt\'t exist',
            bootstyle='danger-inversed',justify='right',font=('arial',10))

        warn_incorrect_pass = ttk.Label(
            master=account.border_frame,
            text='INCORRECT PASSWORD',
            bootstyle='danger-inversed',justify='center',font=('helveltica',8))

        # Main button to check entries then proceed to mainMenu
        loggin_button = ttk.Button(
                account.border_frame, text='LOG IN',
                bootstyle='primary')
        loggin_button.place(
            relx=.5, rely=.83,
            relheight=.15, relwidth=.3, anchor='center')
        # basically command button ↓
        loggin_button.bind( "<Button-1>", func=str_var_gmail_password,add='+')


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
            bootstyle='primary',padding=8
        )
        forget_acc_label.place(
            relx=.5 , rely=.6,anchor='center',
            relheight=.04, #relwidth=.29
        )
        change_label_onhover(forget_acc_label)
        # forget_acc_label.bind("<ButtonPress>",func=str_var_gmail_password)
        
        # func for creating account
        def enroll():
            # grab the location and use it later .
            pos_x = self.place_info()['relx']
            pos_y = self.place_info()['rely']
            pos_w = self.place_info()['relwidth']
            pos_h = self.place_info()['relheight']
            
            enroll_frame = ttk.Frame(
                master=parent, bootstyle='default')
            enroll_frame.place(
                relx=.5,rely=.5,
                relheight=.8,relwidth=.7,anchor='center')
            bg_design.place_configure(relwidth=.99,relx=.5)
            
            self.place_forget() # temporary hides it and place it back again if 
            # back_bttn was clicked
            
            def back_to_log(x,y,h,w,target):
                # show back the Login Frame and its child widget and
                #  the hide the enroll frame .
                self.place(relx=x, rely=y, relheight=h, relwidth=w,anchor='e')
                bg_design.place_configure(relwidth=.59,relx=.3)
                target.place_forget()

            # use the lambda to pass the arguments.
            back_bttn = ttk.Button(
                enroll_frame,bootstyle='danger',text='EXIT',
                command=lambda:back_to_log(
                    x=pos_x, y=pos_y, 
                    h=pos_h, w=pos_w,target=enroll_frame))
            back_bttn.place(
                relx=.932, rely=.05,
                relheight=.08, relwidth=.11, anchor='center')
            
            # prompt the enroll_frame with widgets
            student_widgets = getName(enroll_frame)
            guardian_widgets = getGuardian(enroll_frame)
            def to_guardian():
                def back_prev_entry():
                    prev_bttn.place_forget()
                    next_bttn.place_configure(relx=.5)
                    student_widgets.display_f()
                    guardian_widgets.remove_f()
                    
                    
                student_widgets.remove_f()
                guardian_widgets.display_f()
                # adjust the next button to match with prev_utton position .
                next_bttn.place_configure(relx=.7)
                
                prev_bttn = ttk.Button(
                    master=enroll_frame, text='Back', bootstyle='warning',
                    command=back_prev_entry)
                prev_bttn.place(
                    relx=.3, rely=.93,
                    relheight=.06, relwidth=.15, anchor='center')
                
                
            next_bttn = ttk.Button(
                master=enroll_frame, text='NEXT', bootstyle='primary',
                command=to_guardian)
            next_bttn.place(
                relx=.5, rely=.93,relheight=.06, relwidth=.15, anchor='center')


        enroll_button = ttk.Button(
            self, text='Enroll Now', bootstyle='success',command=enroll,)
        enroll_button.place(
            anchor='center', relx=.5, rely=.8, relheight=.05, relwidth=.5)


        self.mainloop()

class mainMenu(ttk.Frame):
    def __init__(self,parent) -> None:
        super().__init__()
        print('bang', type(self))
        try:
            # if the user exit the application without login or signing
            #   this code will gonna throw some error  
            self.my_gmail = parent.my_gmail
            self.my_password = parent.my_password
            parent.destroy()
        except AttributeError:
            # to make sure the application is exited we gonna exit every frames
            print('attribute errror - No account logged')
            self.quit()
        else:
            self.configure(bootstyle='default')
            self.place(relx=0,rely=0,anchor='nw',relheight=1,relwidth= 1)
            
            
            menu_frame = ttk.Frame(master=self,bootstyle='dark')
            menu_frame.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)






            self.mainloop()


if __name__ == '__main__':
    app = App()
    home = Home(app)
    mainMenu(home)