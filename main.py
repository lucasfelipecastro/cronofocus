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


    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
