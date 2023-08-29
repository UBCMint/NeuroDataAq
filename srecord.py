import tkinter as tk

class SRecord(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        button_back = tk.Button(self, text="Back", padx=10, pady=4, command=lambda: [self.show_page()])

        self.srecord1 = tk.Frame(self)
        self.srecord2 = tk.Frame(self)
        self.srecord3 = tk.Frame(self)
        self.srecord4 = tk.Frame(self)

        self.current_frame = self.srecord1  # Track the currently displayed frame
        
        self.create_widgets_srecord1(button_back)
        self.create_widgets_srecord2(button_back)
        self.create_widgets_srecord3(button_back)

        self.show_page(self.srecord1)
        
    def create_widgets_srecord1(self, button_back):

        button_back.pack(side="left", anchor="nw")

        label1 = tk.Label(self.srecord1, text="Headset Status", font=("Helvetica", 24))

        # button1 does not have capability to check if it's connected or not yet, showing default for now

        button1 = tk.Label(self.srecord1, text="Connected", height=2, font=("Helvetica", 16), bg="lightgreen")

        label2 = tk.Label(self.srecord1, text="Start Recording?", font=("Helvetica", 24))
        label3 = tk.Label(self.srecord1, text="When the recording starts, a numpy file will be stored \n in the designated path!", font=("Helvetica", 16))

        button2 = tk.Button(self.srecord1, text="Start", height=2, font=("Helvetica", 16), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.srecord2)])
        button3 = tk.Button(self.srecord1, text="Use pre-recorded file", height=2, font=("Helvetica", 16), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.srecord3)])

        label1.pack(fill=tk.X, pady=10)
        button1.pack(fill=tk.X, pady=10, padx=180)
        label2.pack(fill=tk.X, pady=10)
        label3.pack(fill=tk.X, pady=10)
        button2.pack(fill=tk.X, side=tk.LEFT, padx=5, expand=True)
        button3.pack(fill=tk.X, side=tk.RIGHT, padx=5, expand=True)

    def create_widgets_srecord2(self, button_back):
        label1 = tk.Label(self.srecord2, text="Ready to Record?", font=("Helvetica", 24))

        label1.pack(fill=tk.X, pady=10)
        text = tk.Text(self.srecord2, wrap=tk.WORD, font=("Arial", 12))
        text.pack(fill=tk.BOTH, expand=True)

        disclaimer = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "

        text.insert(tk.END, disclaimer)

        button1 = tk.Button(self.srecord2, text="Start!", height=2, font=("Helvetica", 16), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.srecord4)])
        button2 = tk.Button(self.srecord2, text="Predict", height=2, font=("Helvetica", 16), command=lambda: [button_back.pack(side="left", anchor="nw"), self.show_page(self.srecord3)]) # predict not yet implemented

    def create_widgets_srecord3(self, button_back):
        int

    def show_page(self, page):
        self.stack.push(page)  # Push the current frame onto the stack
        self.current_frame.pack_forget()
        self.current_frame = page
        page.pack()

    def go_back(self):
        previous_page = self.stack.pop()  # Pop the previous frame from the stack
        if previous_page:
            previous_page.pack_forget()  # Forget the current frame
            self.show_page(previous_page)  # Show the previous frame
