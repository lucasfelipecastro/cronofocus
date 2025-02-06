import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronofocus")
        self.master.geometry("400x200")
        
        # Time left in seconds
        self.time_left = 3
        self.running = False

        # Create the main frame
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Create a label (timeline)
        self.label = tk.Label(self.frame, text=self.format_time(self.time_left), font=("Times New Roman", 48))
        self.label.pack(side="left", fill="both", expand=True)
        
        # Create a start button
        self.start_button = tk.Button(self.frame, text="Start Timer", font=("Times New Roman", 24), command=self.start_timer)
        self.start_button.pack(side="right", fill="both", expand=True)
        
    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
    
    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=self.format_time(self.time_left))
            self.master.after(1000, self.update_timer)
        
        elif self.time_left == 0:
            self.running = False
            self.label.config(text="Time's up!")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
