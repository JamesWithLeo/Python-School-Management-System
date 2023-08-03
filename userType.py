from sections import *


class UserType:
    def __init__(
        self,accountType,menuFrame,mainFrame,
        backProfile,hideProfile) -> None:
        if accountType == "ADMIN":
            admin = AdminType(
                showProfileFunc=backProfile,
                hideProfileFunc=hideProfile
            )
            admin.showMenuOptions(
                menuF=menuFrame,
                mainF=mainFrame,)
            
            
        if accountType == 'STUDENT':
            student = StudentType(
                showProfileFunc=backProfile,
                hideProfileFunc=hideProfile
            )
            student.showMenuOptions(
                menuF=menuFrame,
                mainF=mainFrame,)
    
class AdminType: #super user/account
    def __init__(self,showProfileFunc,hideProfileFunc) -> None:
        self.showProfile = showProfileFunc
        self.hideProfile = hideProfileFunc
    def showMenuOptions(self,menuF,mainF):
        Promote(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=2, row_pos=2,
            title='POSITIONS',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Server(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=3, row_pos=2,
            title='DATABASE',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        SuperSetting(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=4, row_pos=2,
            title='CONFIGURE UI',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        # The following section is not for admin stuff but still used 
        #   in developement. e.g (Library, Canteen & Gallery)
        Library(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=2, row_pos=3,
            title='DATABASE',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Canteen(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=3, row_pos=3,
            title='CANTEEN',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )


class ProffType:
    def __init__(self,showProfileFunc,hideProfileFunc) -> None:
        self.showProfile = showProfileFunc
        self.hideProfile = hideProfileFunc
    def showMenuOptions(self,menuF,mainF,):
        Enroll(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=2, row_pos=2,
            title='ROOM',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Activity(
            
            frame_master=menuF,
            main_frame=mainF,
            col_pos=3, row_pos=2,
            title='ACTIVITIES',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Library(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=4, row_pos=2,
            title='Library',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Canteen(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=2, row_pos=3,
            title='CANTEEN',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Gallary(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=3,row_pos=3,
            title='GALLERY',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )


class StudentType:
    def __init__(self,showProfileFunc,hideProfileFunc) -> None:
        self.showProfile = showProfileFunc
        self.hideProfile = hideProfileFunc
    def showMenuOptions(self,menuF,mainF,):
        Room(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=2, row_pos=2,
            title='ROOM',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Activity(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=3, row_pos=2,
            title='ACTIVITIES',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Library(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=4, row_pos=2,
            title='LIBRARY',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Canteen(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=2, row_pos=3,
            title='CANTEEN',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )
        Gallary(
            frame_master=menuF,
            main_frame=mainF,
            col_pos=3,row_pos=3,
            title='GALLERY',
            back_profile=self.showProfile,
            hide_pro_func=self.hideProfile,
        )