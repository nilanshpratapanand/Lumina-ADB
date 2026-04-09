import os
import sys
import subprocess
import threading
import tkinter as tk
import customtkinter as ctk

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ToolApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lumina Pro ADB/Fastboot Suite")
        self.geometry("1000x700")
        ctk.set_appearance_mode("dark")

        # Path Logic
        self.bin_folder = get_resource_path("bin")
        if os.path.exists(self.bin_folder):
            os.environ["PATH"] = self.bin_folder + os.pathsep + os.environ["PATH"]

        # Main Layout: Sidebar (Buttons) | Center (Terminal)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (Scrollable for many buttons) ---
        self.sidebar = ctk.CTkScrollableFrame(self, width=280, label_text="COMMAND PANEL")
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        # 1. GENERAL & REBOOT
        self.add_section_label("REBOOT & POWER")
        self.add_btn("ADB Devices", "adb devices")
        self.add_btn("Reboot System", "adb reboot")
        self.add_btn("Reboot Bootloader", "adb reboot bootloader")
        self.add_btn("Reboot Recovery", "adb reboot recovery")
        self.add_btn("Power Off", "adb shell reboot -p", color="#7b241c")

        # 2. ADVANCED DEBUGGING
        self.add_section_label("DEBUGGING & INFO")
        self.add_btn("Get Device Props", "adb shell getprop")
        self.add_btn("Check Battery Status", "adb shell dumpsys battery")
        self.add_btn("List Installed Apps", "adb shell pm list packages")
        self.add_btn("ADB Over WiFi (Port 5555)", "adb tcpip 5555")
        self.add_btn("Take Screenshot", "adb shell screencap -p /sdcard/screen.png && adb pull /sdcard/screen.png")

        # 3. APP MANAGEMENT
        self.add_section_label("APP MANAGEMENT")
        self.add_btn("Uninstall Mi Glance", "adb shell pm uninstall -k --user 0 com.miui.android.fashiongallery", color="#2e4053")
        self.add_btn("Clear App Data (Google)", "adb shell pm clear com.google.android.gms")

        # 4. FASTBOOT FLASHING (Use Caution!)
        self.add_section_label("FASTBOOT / FLASHING")
        self.add_btn("Fastboot Devices", "fastboot devices", color="#d35400")
        self.add_btn("Unlock Bootloader", "fastboot flashing unlock", color="#922b21")
        self.add_btn("Flash Boot (boot.img)", "fastboot flash boot boot.img", color="#d35400")
        self.add_btn("Flash Recovery (recovery.img)", "fastboot flash recovery recovery.img", color="#d35400")
        self.add_btn("Wipe Data (Factory Reset)", "fastboot -w", color="#c0392b")
        self.add_btn("Fastboot Reboot", "fastboot reboot", color="#d35400")

        # --- TERMINAL AREA ---
        self.terminal = ctk.CTkTextbox(self, font=("Consolas", 13), border_width=2)
        self.terminal.grid(row=0, column=1, padx=(10, 20), pady=(20, 10), sticky="nsew")
        self.terminal.insert("0.0", "--- Lumina Suite Ready ---\n")

        # Manual Entry
        self.input_field = ctk.CTkEntry(self, placeholder_text="Manual command (e.g. adb shell dumpsys cpuinfo)...")
        self.input_field.grid(row=1, column=1, padx=(10, 20), pady=20, sticky="ew")
        self.input_field.bind("<Return>", lambda e: self.run_cmd(self.input_field.get()))

    def add_section_label(self, text):
        label = ctk.CTkLabel(self.sidebar, text=text, font=("Arial", 12, "bold"), text_color="#5dade2")
        label.pack(pady=(15, 5))

    def add_btn(self, text, cmd, color=None):
        btn = ctk.CTkButton(self.sidebar, text=text, command=lambda: self.run_cmd(cmd))
        if color: btn.configure(fg_color=color, hover_color="#515a5a")
        btn.pack(pady=5, padx=15, fill="x")

    def run_cmd(self, cmd):
        if not cmd.strip(): return
        self.terminal.insert("end", f"\n[EXECUTING]: {cmd}\n")
        self.terminal.see("end")
        threading.Thread(target=self.execute, args=(cmd,), daemon=True).start()

    def execute(self, cmd):
        try:
            process = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            stdout, stderr = process.communicate()
            output = stdout if stdout else stderr
            self.after(0, lambda: self.terminal.insert("end", output if output else "Done.\n"))
        except Exception as e:
            self.after(0, lambda: self.terminal.insert("end", f"Error: {str(e)}\n"))
        self.after(0, lambda: self.terminal.see("end"))

if __name__ == "__main__":
    app = ToolApp()
    app.mainloop()