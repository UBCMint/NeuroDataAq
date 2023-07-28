from tkinter import *
import tkinter as tk

class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EEG Record")
        self.geometry("300x200+10+10")

        button_back = tk.Button(self, text="Back", padx=5, pady=2, command=lambda: [self.show_pageMain(), button_back.pack_forget()])

        # Create the frames for different pages
        self.pageMain = tk.Frame(self)
        self.pageJoystick = tk.Frame(self)
        self.pageOpenBCI = tk.Frame(self)
        self.pageRecord = tk.Frame(self)

        # Create and place widgets in each page
        self.create_widgets_main(button_back)
        self.create_widgets_joystick()
        self.create_widgets_openbci()
        self.create_widgets_record()

        self.show_page(self.pageMain)

    def create_widgets_main(self, button_back):
        label = tk.Label(self.pageMain, text="EEG Data Recording", font=("Helvetica", 16))
        label.pack(pady=(20))

        # Buttons for navigation

        buttonframe = tk.Frame(self.pageMain)
        buttonframe.rowconfigure(0, weight=1)
        buttonframe.rowconfigure(1, weight=1)
        buttonframe.rowconfigure(2, weight=1)

        btn1 = tk.Button(buttonframe, text="Joystick", font=("Helvetica", 8), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.pageJoystick)])
        btn1.grid(row=0, column=0, pady=5, sticky="nsew")

        btn2 = tk.Button(buttonframe, text="OpenBCI Headset", font=("Helvetica", 8), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.pageOpenBCI)])
        btn2.grid(row=1, column=0, pady=5, sticky="nsew")

        btn3 = tk.Button(buttonframe, text="Start recording", font=("Helvetica", 8), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.pageRecord)])
        btn3.grid(row=2, column=0, pady=5, sticky="nsew")

        buttonframe.pack()
    
    def create_widgets_joystick(self):
        label = tk.Label(self.pageJoystick, text="Joystick", font=("Helvetica", 12))
        label.pack(pady=(10,40))

    def create_widgets_openbci(self):
        label = tk.Label(self.pageOpenBCI, text="Open BCI Headset", font=("Helvetica", 12))
        label.pack(pady=(10,40))

    def create_widgets_record(self):
        label = tk.Label(self.pageRecord, text="Recording", font=("Helvetica", 12))
        label.pack(pady=(10,40))

    def show_page(self, page):
        # Hide the main page and show the selected page
        self.pageMain.pack_forget()
        page.pack()

    def show_pageMain(self):
        # Hide all pages and show the main page
        self.pageRecord.pack_forget()
        self.pageJoystick.pack_forget()
        self.pageOpenBCI.pack_forget()
        self.pageMain.pack()

window = HomePage()
window.mainloop()
