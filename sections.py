import ttkbootstrap as ttk
import tkinter as tk

# Upper lvl class
class menuSection:
    def do_when_click(self,event):
        pass

    def when_on_hover(self,event):pass
        # self.picture.grid_configure(sticky=tk.N+tk.S)
        # # self.frame.configure(bootstyle='primary')
        # # self.frame.grid_configure(padx=45,pady=0)
        # self.label.configure(font=('Helvetica bold', 20))
        
    def when_leave_hover(self,event):pass
        # self.picture.grid_configure(sticky=tk.S)
        # self.frame.configure(bootstyle='default')
        # self.frame.grid_configure(padx=60,pady=0)
        # self.label.configure(bootstyle='default',font=('Helvetica bold', 18))
        
    def __init__(
        self,frame_master,col_pos,row_pos,title,main_frame,
        back_profile=None,hide_pro_func=None,pic=None) -> None:
        self.hide_profile = hide_pro_func
        self.back_profile = back_profile
        self.section_frame = frame_master
        self.col = col_pos
        self.row = row_pos
        self.title = title
        self.main_frame = main_frame
        self.pic = pic
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
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.label_for_image.place_forget()
    def do_when_click(self,event):
        self.hide_profile()
        self.section_frame.grid_remove()
        # ----------------
        
        label_for_image = ttk.Label(master=self.main_frame,image=self.pic)
        label_for_image.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        self.label_for_image = label_for_image
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
    def hide_inside_section(self,event):
        # self.inside_section.place_forget()
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        
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


class Activity(menuSection):
    def hide_inside_section(self,event):
        # self.inside_section.place_forget()
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        
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


class Gallary(menuSection):
    def hide_inside_section(self,event):
        # self.inside_section.place_forget()
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        
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


class Canteen(menuSection):
    def hide_inside_section(self,event):
        # self.inside_section.place_forget()
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        
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


class Library(menuSection):
    def hide_inside_section(self,event):
        # self.inside_section.place_forget()
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.label_for_image.place_forget()
    def do_when_click(self,event):
        self.hide_profile()
        self.section_frame.grid_remove()
        # ----------------
        
        label_for_image = ttk.Label(master=self.main_frame,image=self.pic)
        label_for_image.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        self.label_for_image = label_for_image
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

class Promote(menuSection):
    def hide_inside_section(self,event):
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.label_for_image.place_forget()
    def do_when_click(self,event):
        self.hide_profile()
        self.section_frame.grid_remove()
        
        label_for_image = ttk.Label(master=self.main_frame,image=self.pic)
        label_for_image.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        self.label_for_image = label_for_image
        
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
        
        back_to_menu = ttk.Button(inside_frame,text='<- BACK',)
        back_to_menu.place(relx=.9,rely=.02,relheight=.05,relwidth=.08)
        back_to_menu.bind(
            "<Button-1>",func=self.hide_inside_section)


class Server(menuSection):
    def hide_inside_section(self,event):
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.label_for_image.place_forget()
    def do_when_click(self,event):
        self.hide_profile()
        self.section_frame.grid_remove()
        
        label_for_image = ttk.Label(master=self.main_frame,image=self.pic)
        label_for_image.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        self.label_for_image = label_for_image
        
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
        
        back_to_menu = ttk.Button(inside_frame,text='<- BACK',)
        back_to_menu.place(relx=.9,rely=.02,relheight=.05,relwidth=.08)
        back_to_menu.bind(
            "<Button-1>",func=self.hide_inside_section)

class SuperSetting(menuSection):
    def hide_inside_section(self,event):
        self.inside_frame.place_forget()
        self.back_profile()
        self.section_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.label_for_image.place_forget()
    def do_when_click(self,event):
        self.hide_profile()
        self.section_frame.grid_remove()
        
        label_for_image = ttk.Label(master=self.main_frame,image=self.pic)
        label_for_image.place(relheight=1,relwidth=1,relx=.5,rely=.5,anchor='center')
        self.label_for_image = label_for_image
        
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
        
        back_to_menu = ttk.Button(inside_frame,text='<- BACK',)
        back_to_menu.place(relx=.9,rely=.02,relheight=.05,relwidth=.08)
        back_to_menu.bind(
            "<Button-1>",func=self.hide_inside_section) 