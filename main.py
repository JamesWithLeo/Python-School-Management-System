# import json
import tkinter as tk
import ttkbootstrap as ttk
# import inner_func

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('School System')
        self.style = ttk.Style()
        self.style.configure('.',font=('System 15'))
        def app_geometry():
            scrn_w = int((self.winfo_screenwidth()-1000) / 2)
            scrn_h = int((self.winfo_screenheight()-700) / 2)
            self.geometry(f'1000x700+{scrn_w}+{scrn_h}')
        app_geometry()

        ttk.Style(theme='superhero')

class Home(ttk.Frame):
    def __init__(self,parent) -> None:
        super().__init__()
        self.configure(bootstyle='secondary')
        self.place(relx=.994,rely=.5,anchor='e',relheight=.98,relwidth=.4)
        
        header_login = ttk.Label(
            master=self,bootstyle="default",
            text='LOGIN',font='system 19',)
        header_login.place(relx=.4,rely=.12,anchor='nw')

        class accountHome:
            def __init__(self) -> None:
                pass
            
        class accountLogin():
            def __init__(self,parent) -> None:
                def change_on_hover(entry,label):
                    entry.bind(
                        "<Enter>",func=lambda l:label.configure(bootstyle='primary'),
                        add=True
                        
                    )
                    entry.bind(
                        "<Leave>",func=lambda l:label.configure(bootstyle='default'),
                        add=True
                        
                    )
                border_frame = ttk.Frame(
                    parent,bootstyle='dark'
                )
                border_frame.place(
                    relx=.5,rely=.4,
                    relheight=.3,relwidth=.7,
                    anchor='center'
                )
                account_login_frame = ttk.Frame(
                    border_frame,bootstyle='default')
                account_login_frame.place(
                    relx=.5,rely=.5,relheight=.98,relwidth=.98,anchor='center')
                #
                
                gmail_label = ttk.Label(
                    account_login_frame,
                    text='Gmail :',
                    font='system 10',bootstyle='default'
                )
                gmail_label.place(
                    relx=.08,rely=.1,
                    relwidth=.2,relheight=.2,anchor='nw')
                gmail_str_var = tk.StringVar()
                gmail_entry = ttk.Entry(
                    account_login_frame,width=24,font='system 10',
                    textvariable=gmail_str_var)
                gmail_entry.place(
                    relx=.28,rely=.11,
                    relheight=.15,relwidth=.62,anchor='nw')
                change_on_hover(entry=gmail_entry,label=gmail_label)
                #
                password_label = ttk.Label(
                    account_login_frame,
                    text='Password :',
                    font='system 10',bootstyle='default'
                )
                password_label.place(
                    relx=.08,rely=.4,
                    relwidth=.28,relheight=.2,
                    anchor='nw')
                password_str_var = tk.StringVar()
                password_entry = ttk.Entry(
                    account_login_frame,font='system 10',
                    textvariable=password_str_var)
                password_entry.place(
                    relx=.4,rely=.41,
                    relheight=.15,relwidth=.5,anchor='nw')
                change_on_hover(entry=password_entry,label=password_label)
                self.frame = account_login_frame
                # self.border_frame = border_frame
                
                self.my_gmail = gmail_str_var
                self.gmail_entry = gmail_entry

                self.my_password = password_str_var
                self.password_entry = password_entry
        account = accountLogin(self)

        def str_var_gmail_password():
            """db"""
            WRONG_GMAIL = None
            WRONG_PASSWORD = None
            if account.my_gmail.get() not in ['james', 'leo']:
                account.gmail_entry.configure(bootstyle='danger')
                WRONG_GMAIL = True
            else:
                account.gmail_entry.configure(bootstyle='primary')
                self.my_gmail = account.my_gmail
                
            if account.my_password.get() not in ['james','leo']:
                account.password_entry.configure(bootstyle='danger')
                WRONG_PASSWORD = True
            else:
                account.password_entry.configure(bootstyle='primary')            
                self.my_password = account.my_password
            
            if WRONG_GMAIL is True or  WRONG_PASSWORD is True:
                pass
            else:
                # if account exist and correct password
                self.quit()
                
        loggin_button = ttk.Button(
                account.frame, text='LOGIN', 
                bootstyle='primary',command=str_var_gmail_password)
        loggin_button.place(
            relx=.35, rely=.73,
            relheight=.15, relwidth=.3, anchor='nw')
        self.mainloop()

class mainMenu(ttk.Frame):
    def __init__(self,parent) -> None:
        super().__init__()
        print('bang')
        self.my_gmail = parent.my_gmail
        self.my_password = parent.my_password
        parent.destroy()
        
        self.configure(bootstyle='secondary')
        self.place(relx=0,rely=0,anchor='nw',relheight=1,relwidth= 1)
        
        
        new_frame = ttk.Frame(master=self,bootstyle='default')
        new_frame.place(relx=.2, rely=.2, relheight=.4, relwidth=.4)
        
        
        self.mainloop()
        
if __name__ == '__main__':
    app = App()
    home = Home(app)
    mainMenu(home)
