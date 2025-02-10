import tkinter as tk
import winsound
import threading

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('Cronofocus')
        self.master.geometry('400x300')
        
        # Time left in seconds
        self.time_left = {'50': 4, '40': 3, '30': 2, '25': 1, 'break': 5}  # Modify values to change the time
        self.running = {'50': False, '40': False, '30': False, '25': False, 'break': False}
        
        # Sound instance
        self.sound_instance = Sound()

        # Main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=20, padx=20, fill='none', expand=True)
        
        # Timers frame
        self.timers_frame = tk.Frame(self.main_frame)
        self.timers_frame.pack(fill='both', expand=True)
        
        # Dictionary to store labels
        self.labels = {}
        
        for minutes in ['50', '40', '30', '25']:
            frame = tk.Frame(self.timers_frame)
            frame.pack(pady=5, padx=20, fill='both', expand=True)
            
            self.labels[minutes] = tk.Label(frame, text=self.format_time(self.time_left[minutes]), font=('Times New Roman', 20))
            self.labels[minutes].pack(side='left', fill='both', expand=True)

            start_button = tk.Button(frame, text=f'Start {minutes} min', font=('Times New Roman', 10), command=lambda m=minutes: self.start_timer(m))
            start_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)
        
        # Break timer
        break_frame = tk.Frame(self.timers_frame)
        break_frame.pack(pady=5, padx=20, fill='both', expand=True)
        
        self.labels['break'] = tk.Label(break_frame, text=self.format_time(self.time_left['break']), font=('Times New Roman', 20))
        self.labels['break'].pack(side='left', fill='both', expand=True)

        break_button = tk.Button(break_frame, text='Start Break', font=('Times New Roman', 10), command=lambda: self.start_timer('break'))
        break_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)
        
        # Stop Sound button
        self.stop_sound_button = tk.Button(self.main_frame, text='Stop Sound', font=('Times New Roman', 10), command=self.sound_instance.stop_sound)
        self.stop_sound_button.pack(pady=5)
    
    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f'{minutes:02}:{seconds:02}'
    
    def update_timer(self, timer_name):
        if self.running[timer_name] and self.time_left[timer_name] > 0:
            self.time_left[timer_name] -= 1
            self.labels[timer_name].config(text=self.format_time(self.time_left[timer_name]))
            self.master.after(1000, lambda: self.update_timer(timer_name))
        elif self.time_left[timer_name] == 0:
            self.running[timer_name] = False
            self.labels[timer_name].config(text="Time's up!")
            self.sound_instance.play_sound()

    def start_timer(self, timer_name):
        if not self.running[timer_name]:
            self.running[timer_name] = True
            self.update_timer(timer_name)

class Sound:
    def __init__(self):
        self.sound_playing = False

    def play_sound(self):
        if not self.sound_playing:
            self.sound_playing = True
            threading.Thread(target=self._play_continuous_sound, daemon=True).start()

    def stop_sound(self):
        self.sound_playing = False

    def _play_continuous_sound(self):
        while self.sound_playing:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
