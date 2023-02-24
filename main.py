import customtkinter as CTk
from PIL import Image

class App(CTk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("460x370")
        self.title("Password Generator")
        self.resizable(False,False)

        self.logo = CTk.CTkImage(dark_image = Image.open("LogoPass_G.png"), size= (460,150))
        self.logo_label = CTk.CTkLabel(master = self, text = "", image = self.logo)
        self.logo_label.grid(row = 0, column = 0)

        self.password_frame = CTk.CTkFrame(master = self,fg_color="transparent")
        self.password_frame.grid(row= 1, column= 0, padx=(20,20),sticky= "nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame,width=300)
        self.entry_password.grid(row = 0, column = 0, padx = (0,20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame,text = "Generate", width=100,
                                          command=self.set_password)
        self.btn_generate.grid(row = 0,column = 1)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row = 2, column = 0, padx =(20,20),pady = (20,0),sticky = "nsew")

        self.password_lengh_slider = CTk.CTkSlider(master=self.settings_frame, from_=1, to=50, number_of_steps=50,
                                                   command=self.slider_event)
        self.password_lengh_slider.grid(row=1, column=0,columnspan= 3,pady = (20,20), sticky="ew")

        self.password_lengh_entry = CTk.CTkEntry(master=self.settings_frame,width=50)
        self.password_lengh_slider.grid(row=1, column= 3,padx= (20,10),sticky="we")

        

    def slider_event(self):
        pass

    def set_password(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()