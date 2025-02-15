import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import winsound
import threading
from gspread.client import Client
from google.oauth2.service_account import Credentials
import time

def save_progress(session_name, session_time):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    row = [timestamp, session_time, '✅']
    worksheet.append_row(row)

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file(
    'C:/techWin11/pythonProjects/cronofocus/gen-lang-client-0841060528-1f4635a8f204.json',
    scopes=scope
)

client = Client(auth=creds)
spreadsheet = client.open_by_key('1K9-zcnVTqY_Ug975Yx_bWMxftAB6_kvB_VGkiIr0xQA')
worksheet = spreadsheet.get_worksheet(0)

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('Cronofocus')
        self.master.geometry('550x550')
        self.master.resizable(False, False)

        self.time_left = {'50': 3000, '40': 2400, '30': 1800, '25': 1500, 'break': 300}
        self.original_time = {'50': 3000, '40': 2400, '30': 1800, '25': 1500, 'break': 300}
        self.running = {'50': False, '40': False, '30': False, '25': False, 'break': False}

        self.sound_instance = Sound()

        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=20, padx=20, fill='none', expand=True)

        self.timers_frame = tk.Frame(self.main_frame)
        self.timers_frame.pack(fill='both', expand=True)

        self.labels = {}

        for minutes in ['50', '40', '30', '25']:
            frame = tk.Frame(self.timers_frame)
            frame.pack(pady=5, padx=20, fill='both', expand=True)

            self.labels[minutes] = tk.Label(frame, text=self.format_time(self.time_left[minutes]), font=('Arial', 20))
            self.labels[minutes].pack(side='left', fill='both', expand=True)

            start_button = tk.Button(frame, text=f'▶ Start {minutes} min', font=('Arial', 11), bd=1, command=lambda m=minutes: self.start_timer(m))
            start_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)

            pause_button = tk.Button(frame, text=f'|| Pause {minutes} min', font=('Arial', 11), bd=1, command=lambda m=minutes: self.pause_timer(m))
            pause_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)

            reset_button = tk.Button(frame, text=f'↻ Reset {minutes} min', font=('Arial', 11), bd=1, command=lambda m=minutes: self.reset_timer(m))
            reset_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)

        break_frame = tk.Frame(self.timers_frame)
        break_frame.pack(pady=5, padx=20, fill='both', expand=True)

        self.labels['break'] = tk.Label(break_frame, text=self.format_time(self.time_left['break']), font=('Arial', 20))
        self.labels['break'].pack(side='left', fill='both', expand=True)

        break_button = tk.Button(break_frame, text='Start Break', font=('Arial', 11), bd=1, command=lambda: self.start_timer('break'))
        break_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)

        self.pause_break_button = tk.Button(break_frame, text='Pause Break', font=('Arial', 11), bd=1, command=self.toggle_break_timer)
        self.pause_break_button.pack(side='left', fill='x', padx=3, pady=1, expand=True)

        self.change_break_label = tk.Label(self.main_frame, text='Set Break Time (in minutes):', font=('Arial', 12, 'bold'))
        self.change_break_label.pack(pady=10)

        self.break_time_entry = tk.Entry(self.main_frame, font=('Arial', 11), bd=1)
        self.break_time_entry.pack(pady=5)

        self.set_break_button = tk.Button(self.main_frame, text='Set Break Time', font=('Arial', 11), command=self.set_break_time)
        self.set_break_button.pack(pady=5)

        self.break_time_feedback = tk.Label(self.main_frame, text='', font=('Arial', 12, 'italic'), fg='green')
        self.break_time_feedback.pack(pady=5)

        self.stop_sound_button = tk.Button(self.main_frame, text=' ⃠   Stop Sound', font=('Arial', 11), command=self.sound_instance.stop_sound, width=15, height=2)
        self.stop_sound_button.pack(pady=5)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f'{minutes:02}:{seconds:02}'

    def update_timer(self, timer_name):
        if self.running[timer_name]:
            if self.time_left[timer_name] > 0:
                self.time_left[timer_name] -= 1
                self.labels[timer_name].config(text=self.format_time(self.time_left[timer_name]))
                self.master.after(1000, lambda: self.update_timer(timer_name))
            elif self.time_left[timer_name] == 0:
                self.running[timer_name] = False
                self.labels[timer_name].config(text="Time's up!")
                self.sound_instance.play_sound()
                self.complete_session(timer_name)
                if timer_name in ['50', '40', '30', '25']:
                    messagebox.showinfo('Timer Finished', f'{timer_name} minute timer has finished!')
                elif timer_name == 'break':
                    messagebox.showinfo('Break Finished', 'Break timer has finished!')

    def complete_session(self, session_name):
        if session_name in ['50', '40', '30', '25']:
            save_progress(session_name, self.original_time[session_name] // 60)

    def start_timer(self, timer_name):
        if not self.running[timer_name]:
            self.running[timer_name] = True
            self.update_timer(timer_name)

    def pause_timer(self, timer_name):
        self.running[timer_name] = False
        self.labels[timer_name].config(text=self.format_time(self.time_left[timer_name]))

    def reset_timer(self, timer_name):
        self.running[timer_name] = False
        self.time_left[timer_name] = self.original_time[timer_name]
        self.labels[timer_name].config(text=self.format_time(self.time_left[timer_name]))

    def toggle_break_timer(self):
        if self.running['break']:
            self.pause_break_timer()
        else:
            self.start_timer('break')

    def pause_break_timer(self):
        self.running['break'] = False
        self.labels['break'].config(text=self.format_time(self.time_left['break']))

    def set_break_time(self):
        try:
            break_minutes = int(self.break_time_entry.get())
            if break_minutes > 0:
                self.time_left['break'] = break_minutes * 60
                self.original_time['break'] = self.time_left['break']
                self.labels['break'].config(text=self.format_time(self.time_left['break']))
                self.break_time_feedback.config(text=f'Break time set to {break_minutes} minutes!', fg='green')
            else:
                self.break_time_feedback.config(text='Please enter a positive number!', fg='red')
        except ValueError:
            self.break_time_feedback.config(text='Invalid input! Please enter a number.', fg='red')

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
            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
