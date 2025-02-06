import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("400x200")
        
        self.time_left = 50 * 60
        self.running = False

        self.label = tk.Label(master, text=self.format_time(self.time_left), font=("Times New Roman", 50))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start Timer", font=("Times New Roman", 24), command=self.start_timer)   
        self.start_button.pack()

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
