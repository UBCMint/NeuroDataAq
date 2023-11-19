import argparse
import time
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from recorder import EEG8DataRecorder


from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets

class HomePage(Tk):
    def __init__(self):
        super().__init__()
        self.title("EEG Record")
        self.geometry("600x400")
        
        self.currentDirection = "none"
        self.page_main()
        self.connectionState = False
        self.args = self.parse_arguments()
    
    def page_main(self):

        frame_main = Frame(self, width=600,height=400)
        frame_main.pack(fill=BOTH, expand=True)

        # Buttons for navigation

        label = Label(frame_main, text="EEG Data Recording", font=("Helvetica", 24))
        label.pack(pady=(25,75))

        btn1 = Button(frame_main, text="Joystick", font=("Helvetica", 12), bg="lightblue", command=lambda: [frame_main.pack_forget(), self.page_joystick()])
        btn1.pack(fill=BOTH, padx=200, pady=5)

        btn2 = Button(frame_main, text="OpenBCI Headset", font=("Helvetica", 12), bg="lightblue", command=lambda: [frame_main.pack_forget(), self.page_headset()])
        btn2.pack(fill=BOTH, padx=200, pady=5)

        btn3 = Button(frame_main, text="Start recording", font=("Helvetica", 12), bg="orange", command=lambda: [frame_main.pack_forget(), self.page_srecord1()])
        btn3.pack(fill=BOTH, padx=200, pady=5)

        btn4 = Button(frame_main, text="Config", font=("Helvetica", 12), bg="lightblue", command=lambda: [frame_main.pack_forget(), self.page_config()])
        btn4.pack(fill=BOTH, padx=200, pady=5)

    def page_headset(self):

        frame_headset = Frame(self, width=600,height=400)
        frame_headset.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_headset, text="Back", font=("Helvetica", 12), command=lambda: [frame_headset.pack_forget(), self.page_main()])
        btn_back.pack(anchor=NW)

        label = Label(frame_headset, text="Open BCI Headset", font=("Helvetica", 24))
        label.pack(pady=(0,40))
        button2 = Button(frame_headset, text="Connect", height=2, font=("Helvetica", 12), command=lambda: [self.headsetConnect()])
        button2.pack(fill=X, padx=(10,150), expand=True, anchor=CENTER)


    def page_srecord1(self):

        frame_srecord1 = Frame(self, width=600,height=400)
        frame_srecord1.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_srecord1, text="Back", font=("Helvetica", 12), command=lambda: [frame_srecord1.pack_forget(), self.page_main()])
        btn_back.pack(anchor=NW)

        label1 = Label(frame_srecord1, text="Headset Status", font=("Helvetica", 20))

        # button1 does not have capability to check if it's connected or not yet, showing default for now

        button1 = Label(frame_srecord1, text="Connected", height=2, font=("Helvetica", 16), bg="lightgreen") # checks if it's connected

        label2 = Label(frame_srecord1, text="Start Recording?", font=("Helvetica", 20))
        label3 = Label(frame_srecord1, text="When the recording starts, a numpy file will be stored \n in the designated path!", font=("Helvetica", 12))

        button2 = Button(frame_srecord1, text="Start", height=2, font=("Helvetica", 12), command=lambda: [frame_srecord1.pack_forget(), self.page_srecord2()])
        button3 = Button(frame_srecord1, text="Use pre-recorded file", height=2, font=("Helvetica", 12), command=lambda: [frame_srecord1.pack_forget(), self.page_srecord3()])

        label1.pack(fill=X, pady=10)
        button1.pack(fill=X, pady=10, padx=220)
        label2.pack(fill=X, pady=10)
        label3.pack(fill=X, pady=10)
        button2.pack(fill=X, side=LEFT, padx=(150,10), expand=True)
        button3.pack(fill=X, side=RIGHT, padx=(10,150), expand=True)

    def page_srecord2(self):

        frame_srecord2 = Frame(self, width=600,height=400)
        frame_srecord2.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_srecord2, text="Back", font=("Helvetica", 12), command=lambda: [frame_srecord2.pack_forget(), self.page_srecord1()])
        btn_back.pack(anchor=NW)

        label1 = Label(frame_srecord2, text="Ready to Record?", font=("Helvetica", 24))

        label1.pack(fill=X, pady=10)

        disclaimer = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "

        label2 = Label(frame_srecord2, text=disclaimer, font=("Helvetica", 12), wraplength=400)
        label2.pack(fill=X, pady=10)

        button1 = Button(frame_srecord2, text="Start!", height=2, font=("Helvetica", 12), command=lambda: [frame_srecord2.pack_forget(), self.page_srecord4()])
        button2 = Button(frame_srecord2, text="Predict", height=2, font=("Helvetica", 12), command=lambda: [frame_srecord2.pack_forget(), '''self.page_predictrun()''']) # predict run not yet implemented

        button1.pack(fill=X, side=LEFT, padx=(150,10), expand=True)
        button2.pack(fill=X, side=RIGHT, padx=(10,150), expand=True)

    def page_srecord3(self):

        frame_srecord3 = Frame(self, width=600,height=400)
        frame_srecord3.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_srecord3, text="Back", font=("Helvetica", 12), command=lambda: [frame_srecord3.pack_forget(), self.page_srecord1()])
        btn_back.pack(anchor=NW)

        label1 = Label(frame_srecord3, text="Pre-Recorded Data", font=("Helvetica", 20))

        self.file = ""
        
        label2 = Label(frame_srecord3, text="Ready to start? Load in your data file! Select your \n numpy file containing the voltage data!", font=("Helvetica", 12))
        button1 = Button(frame_srecord3, text="Browse", height=2, font=("Helvetica", 12), command=lambda: [self.browse_file(), label3.config(text = "The current file is \"" + self.file + "\"\n Use this file? ")])

        label3 = Label(frame_srecord3, text="The current file is \"" + self.file + "\"\n Use this file? ", font=("Helvetica", 12))

        button2 = Button(frame_srecord3, text="Begin", height=2, font=("Helvetica", 12), command=lambda: [frame_srecord3.pack_forget(), '''self.page_predictviz()''']) # predict viz not yet implemented

        label1.pack(fill=X, pady=10)
        label2.pack(fill=X, pady=10)
        button1.pack(fill=X, pady=10, padx=180)
        label3.pack(fill=X, pady=10)
        button2.pack(fill=X, padx=180, expand=True)


    def page_config(self):

        frame_config = Frame(self, width=600,height=400)
        frame_config.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_config, text="Back", font=("Helvetica", 12), command=lambda: [frame_config.pack_forget(), self.page_main(), self.cleanup()])
        btn_back.pack(anchor=NW)

    def browse_file(self):

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',)
        
        if filename != "":

            showinfo(
                title='Selected File',
                message=filename
            )

            if filename.endswith(".npy"):
                self.file = filename
            else:
                messagebox.showerror("Error", "Given file is not a numpy file.\nPlease select another file.")
        
    
    def page_srecord4(self):
        frame_srecord4 = Frame(self, width=600, height=400)
        frame_srecord4.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_srecord4, text="Back", font=("Helvetica", 12), command=lambda: [frame_srecord4.pack_forget(), self.page_srecord2()])
        btn_back.pack(anchor=NW)

        button1 = Button(frame_srecord4, text="With Joystick", height=15, width=20, bg="lightblue", font=("Helvetica", 16), command=lambda: [frame_srecord4.pack_forget(), self.page_arrow_display()])  # Navigate to arrow display screen

        button2 = Button(frame_srecord4, text="No Joystick", height=15, width=20, bg="orange", font=("Helvetica", 16), command=lambda: [frame_srecord4.pack_forget(), self.page_srecord6()])  # srecord6 not yet implemented

        button1.pack(fill=BOTH, side=LEFT, padx=5, expand=True)
        button2.pack(fill=BOTH, side=RIGHT, padx=5, expand=True)

    def page_arrow_display(self):
        import tkinter as tk
        import keyboard
        from PIL import Image, ImageTk

        frame_arrow_display = Frame(self, width=600, height=400)
        frame_arrow_display.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_arrow_display, text="Back", font=("Helvetica", 12), command=lambda: [frame_arrow_display.pack_forget(), self.page_srecord4, cleanup(board, recorder)])
        btn_back.pack(anchor=NW)

        # Create a dictionary to map arrow keys to their corresponding image file paths
        arrow_key_mapping = {
            'up': 'images/Up.png',
            'down': 'images/Down.png',
            'left': 'images/Left.png',
            'right': 'images/Right.png'
        }

        arrow_images = {
            'images/Up.png': (150, 0),
            'images/Down.png': (150, 250),
            'images/Left.png': (0, 125),
            'images/Right.png': (300, 125)
        }

        direction_mapping = {
            'up': 1,
            'right': 2,
            'down': 3,
            'left': 4
        }

        current_direction = 0

        # Create a tkinter canvas to display the arrow images
        canvas = tk.Canvas(frame_arrow_display, width=400, height=400)
        canvas.pack()

        # Function to update the canvas with the arrow image
        def update_arrow_image_press(event):
            nonlocal current_direction

            if event.name in arrow_key_mapping:
                x, y = arrow_images[arrow_key_mapping[event.name]]
                image_path = arrow_key_mapping[event.name]
                img = Image.open(image_path)
                img = img.resize((100, 100), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                canvas.create_image(x, y, image=img, anchor=tk.NW)
                canvas.image = img

        def update_arrow_image_release(event):
            if event.name in arrow_key_mapping:
                canvas.delete("all")

        def set_arrow_key_press(event):
            if event.name in arrow_key_mapping:
                self.arrowStatus = event.name
                recorder.setdirection(event.name)
        
        def set_arrow_key_release(event):
            if event.name == self.arrowStatus:
                self.arrowStatus = "none"
                recorder.setdirection("none")

        def cleanup(board, recorder):
            recorder.stop()
            recorder.save_to_csv()

            board.stop_stream()
            board.release_session()
        
        recorder = EEG8DataRecorder("eeg_data.csv")

        for key in arrow_key_mapping:
            keyboard.on_press_key(key, update_arrow_image_press)
            keyboard.on_release_key(key, update_arrow_image_release)

            keyboard.on_press_key(key, set_arrow_key_press)
            keyboard.on_release_key(key, set_arrow_key_release)

        button_back = Button(frame_arrow_display, text="Back", font=("Helvetica", 12), command=lambda: [frame_arrow_display.pack_forget(), self.page_srecord4()])
        button_back.pack(fill=X, pady=10)

        label_instruction = Label(frame_arrow_display, text="Press arrow keys to display arrows on the screen.", font=("Helvetica", 12))
        label_instruction.pack(fill=X, pady=10)

        try:
            board = self.headsetConnect(self.args)

            board.start_stream()
            recorder.start()

            frame_arrow_display.after(1000, self.record(recorder, board))

        except Exception as E:
            print(f"Error: {E}")


    # Make sure to call the page_arrow_display function to display arrows

    def record(recorder, board):

        # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
        data = board.get_board_data()  # get all data and remove it from internal buffer

        for i, value in enumerate(data):
            recorder.add_eeg_data(data[i])


    def page_joystick(self):

        frame_joystick = Frame(self, width=600,height=400)
        frame_joystick.pack(fill=BOTH, expand=True)

        btn_back = Button(frame_joystick, text="Back", font=("Helvetica", 12), command=lambda: [frame_joystick.pack_forget(), self.canvas.destroy(), self.page_main()])
        btn_back.pack(anchor=NW)

        self.center_x = 200
        self.center_y = 150
        self.radius = 100
        self.current_x = self.center_x
        self.current_y = self.center_y

        self.canvas = Canvas(self, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.move_joystick)
        self.canvas.bind("<B1-Motion>", self.move_joystick)
        self.canvas.bind("<ButtonRelease-1>", self.reset_joystick)

        self.draw_joystick()

    def draw_joystick(self):
        self.canvas.delete("joystick")

        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            outline="black", width=2, tags="joystick"
        )

        self.canvas.create_oval(
            self.current_x - 10,
            self.current_y - 10,
            self.current_x + 10,
            self.current_y + 10,
            fill="red", tags="joystick"
        )

    def move_joystick(self, event):
        x, y = event.x, event.y
        distance = ((x - self.center_x) ** 2 + (y - self.center_y) ** 2) ** 0.5

        if distance <= self.radius:
            self.current_x = x
            self.current_y = y

        self.draw_joystick()

    def reset_joystick(self, event):
        self.current_x = self.center_x
        self.current_y = self.center_y
        self.draw_joystick()
        
    def parse_arguments(self):
        BoardShim.enable_dev_board_logger()
        parser = argparse.ArgumentParser()
        # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
        parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False,
                            default=0)
        parser.add_argument('--ip-port', type=int, help='ip port', required=False, default=0)
        parser.add_argument('--ip-protocol', type=int, help='ip protocol, check IpProtocolType enum', required=False,
                            default=0)
        parser.add_argument('--ip-address', type=str, help='ip address', required=False, default='')
        parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='')
        parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')
        parser.add_argument('--other-info', type=str, help='other info', required=False, default='')
        
        parser.add_argument('--serial-number', type=str, help='serial number', required=False, default='')
        parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards',
        
                            required=True)
        parser.add_argument('--file', type=str, help='file', required=False, default='')
        parser.add_argument('--master-board', type=int, help='master board id for streaming and playback boards',
                            required=False, default=BoardIds.NO_BOARD)

        # print(parser.parse_args())
        
        return parser.parse_args()

    #add connection labels
    def headsetConnect(args):
        try:
            params = BrainFlowInputParams()
            params.ip_port = args.ip_port
            params.serial_port = args.serial_port
            params.mac_address = args.mac_address
            params.other_info = args.other_info
            params.serial_number = args.serial_number
            params.ip_address = args.ip_address
            params.ip_protocol = args.ip_protocol
            params.timeout = args.timeout
            params.file = args.file
            params.master_board = args.master_board

            return BoardShim(args.board_id, params)
        
        except Exception as e:
            
            return None
        


root = HomePage()
root.mainloop()
