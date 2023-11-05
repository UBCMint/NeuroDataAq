import csv
import time
import random

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

class EEG8DataRecorder:
    def __init__(self, filename):

        # using cyton board
        # params = BrainFlowInputParams ()
        # params.serial_port = "COM3"

        # self.board = BoardShim (BoardIds.CYTON_BOARD.value, params)
        # self.board.prepare_session ()

        # BoardShim.log_message (LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')

        # self.board.release_session ()  
     
        # data structure setup
        self.channelCount = 8
        self.filename = filename
        self.startTime = time.time()
        self.eeg_data = [[] for _ in range(self.channelCount + 3)]  # time, state, direction, 8 channels for EEG data
        self.state = "stopped"
        # 1 - 4 going north east south west, 0 for centered
        self.direction = 0

    def start(self):
     #   if self.state == "stopped":
            self.eeg_data = [[] for _ in range(self.channelCount + 3)]  # Clear existing EEG data
            self.state = "recording"
            self.startTime = time.time()
            # self.board.start_stream ()

    def stop(self):
       # if self.state == "recording":
            self.state = "stopped"
            #self.board.release_session ()  

    def pause(self):
        #if self.state == "recording":
            self.state = "paused"
            #self.board.stop_stream ()

    def resume(self):
       # if self.state == "paused":
            self.state = "recording"
            #self.board.start_stream ()

    def setdirection(self, direction):
        self.direction = direction

    def add_eeg_data(self, data_point):
        #if self.state == "recording":  #if we only want recorded data welp here

            self.eeg_data[0].append(time.time() - self.startTime)
            self.eeg_data[1].append(self.state)
            self.eeg_data[2].append(self.direction)
            for i, value in enumerate(data_point):
                self.eeg_data[i + 3].append(value)

    def save_to_csv(self):
        if self.eeg_data:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "State", "Direction"] + [f"EEG{i}" for i in range(1, self.channelCount + 1)])

                for i in range(len(self.eeg_data[0])):
                    timestamp = self.eeg_data[0][i]
                    state = self.eeg_data[1][i]
                    direction = self.eeg_data[2][i]
                    eeg_values = self.eeg_data[3:]
                    writer.writerow([timestamp, state, direction] + [eeg_values[j][i] for j in range(self.channelCount)])

# Example usage:
if __name__ == "__main__":
    eeg_recorder = EEG8DataRecorder("eeg_data.csv")

    # Start recording
    eeg_recorder.start()

    # Simulate data acquisition

    for i in range(500):  # Simulate data

        data_point = [random.uniform(0.0, 1.0) for _ in range(8)]        
        if i == 50:
            eeg_recorder.pause()
            eeg_recorder.state = "paused"
        if i == 400:
            eeg_recorder.resume()
        if i == 100:
            eeg_recorder.stop()
        if i == 75:
            eeg_recorder.direction = 3
        eeg_recorder.add_eeg_data(data_point)

    # Stop recording and save data to CSV
    eeg_recorder.save_to_csv()