import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('Cronofocus')
        self.master.geometry('400x200')
        
        # Time left in seconds
        self.time_50_left = 4 # Modify this value to change the time
        self.time_40_left = 3 # Modify this value to change the time
        self.time_30_left = 2 # Modify this value to change the time
        self.time_25_left = 1 # Modify this value to change the time
        self.running_50 = False
        self.running_40 = False
        self.running_30 = False
        self.running_25 = False
        
        # Main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=20, padx=20, fill='none', expand=True)
        
        # Timer 50 minutes frame
        self.timer_50_frame = tk.Frame(self.main_frame)
        self.timer_50_frame.pack(pady=20, padx=20, fill='both', expand=True)

        self.label_50 = tk.Label(self.timer_50_frame, text=self.format_time(self.time_50_left), font=('Times New Roman', 25))
        self.label_50.pack(side='left', fill='both', expand=True)

        self.start_button_50 = tk.Button(self.timer_50_frame, text='Start 50 min', font=('Times New Roman', 10), command=self.start_timer_50)
        self.start_button_50.pack(side='left', fill='x', padx=3, pady=1, expand=True)
        
        # Timer 40 minutes frame
        self.timer_40_frame = tk.Frame(self.main_frame)
        self.timer_40_frame.pack(pady=20, padx=20, side='top', fill='both', expand=True)

        self.label_40 = tk.Label(self.timer_40_frame, text=self.format_time(self.time_40_left), font=('Times New Roman', 25))
        self.label_40.pack(side='left', fill='both', expand=True)

        self.start_button_40 = tk.Button(self.timer_40_frame, text='Start 40 min', font=('Times New Roman', 10), command=self.start_timer_40)
        self.start_button_40.pack(side='left', fill='x', padx=3, pady=1, expand=True)

        # Timer 30 minutes frame
        self.timer_30_frame = tk.Frame(self.main_frame)
        self.timer_30_frame.pack(pady=20, padx=20, side='top', fill='both', expand=True)

        self.label_30 = tk.Label(self.timer_30_frame, text=self.format_time(self.time_30_left), font=('Times New Roman', 25))
        self.label_30.pack(side='left', fill='both', expand=True)

        self.start_button_30 = tk.Button(self.timer_30_frame, text='Start 30 min', font=('Times New Roman', 10), command=self.start_timer_30)
        self.start_button_30.pack(side='left', fill='x', padx=3, pady=1, expand=True)

        # Timer 25 minutes frame    
        self.timer_25_frame = tk.Frame(self.main_frame)
        self.timer_25_frame.pack(pady=20, padx=20, side='top', fill='both', expand=True)

        self.label_25 = tk.Label(self.timer_25_frame, text=self.format_time(self.time_25_left), font=('Times New Roman', 25))
        self.label_25.pack(side='left', fill='both', expand=True)

        self.start_button_25 = tk.Button(self.timer_25_frame, text='Start 25 min', font=('Times New Roman', 10), command=self.start_timer_25)
        self.start_button_25.pack(side='left', fill='x', padx=3, pady=1, expand=True)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f'{minutes:02}:{seconds:02}'
    
    def update_timer_50(self):
        if self.running_50 and self.time_50_left > 0:
            self.time_50_left -= 1
            self.label_50.config(text=self.format_time(self.time_50_left))
            self.label_40.config(text=self.format_time(self.time_50_left))
            self.master.after(1000, self.update_timer_50)
        elif self.time_50_left == 0:
            self.running_50 = False
            self.label_50.config(text="Time's up!")

    def update_timer_40(self):
        if self.running_40 and self.time_40_left > 0:
            self.time_40_left -= 1
            self.label_40.config(text=self.format_time(self.time_40_left))
            self.master.after(1000, self.update_timer_40)
        elif self.time_40_left == 0:
            self.running_40 = False
            self.label_40.config(text="Time's up!")

    def update_timer_30(self):
        if self.running_30 and self.time_30_left > 0:
            self.time_30_left -= 1
            self.label_30.config(text=self.format_time(self.time_30_left))
            self.master.after(1000, self.update_timer_30)
        elif self.time_30_left == 0:
            self.running_30 = False
            self.label_30.config(text="Time's up!")

    def update_timer_25(self):
        if self.running_25 and self.time_25_left > 0:
            self.time_25_left -= 1
            self.label_25.config(text=self.format_time(self.time_25_left))
            self.master.after(1000, self.update_timer_25)
        elif self.time_25_left == 0:
            self.running_25 = False
            self.label_25.config(text="Time's up!")

    def start_timer_50(self):
        if not self.running_50:
            self.running_50 = True
            self.update_timer_50()

    def start_timer_40(self):
        if not self.running_40:
            self.running_40 = True
            self.update_timer_40()

    def start_timer_30(self):
        if not self.running_30:
            self.running_30 = True
            self.update_timer_30()

    def start_timer_25(self):
        if not self.running_25:
            self.running_25 = True
            self.update_timer_25()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
