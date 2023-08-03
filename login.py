import ttkbootstrap as ttk
import tkinter as tk

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
