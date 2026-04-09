Lumina-ADB Pro Suite 🚀
Lumina-ADB is a modern, high-performance GUI designed for Android debugging and flashing. Built with CustomTkinter, it provides an intuitive interface for complex ADB and Fastboot operations, specifically optimized for developers and power users modding devices like the Redmi 9 Active.

✨ Key Features
One-Click Diagnostics: Instantly verify device connection status in both ADB and Fastboot modes.

Advanced Power Menu: Dedicated controls for Rebooting to System, Recovery, and Bootloader.

System Optimization: Pre-configured specialized commands to remove system bloatware (e.g., Mi Glance) and clear GMS data.

Flashing Utilities: Streamlined buttons for flashing boot.img and recovery.img partitions.

Integrated Terminal: Real-time feedback from the system with a manual input field for advanced shell commands.

Zero-Install Portability: Bundles necessary platform-tools (ADB/Fastboot) directly into the executable using PyInstaller's --add-data protocol.

🛠️ Technical Stack
Language: Python 3.14.

UI Framework: CustomTkinter (Dark Mode optimized).

Packaging: PyInstaller (Multi-resource bundling).

Concurrency: Multi-threading ensures the GUI remains responsive while executing long-running ADB commands.

📂 Project Structure
Plaintext
Lumina-ADB/
├── main.py              # Application logic and UI definition
├── bin/                 # Essential ADB and Fastboot binaries
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── LICENSE              # MIT License
🚀 Usage Instructions
For End-Users (Portable EXE)
Navigate to the Releases tab on GitHub.

Download the latest Lumina_ADB_Pro.exe.

Ensure USB Debugging is enabled on your Android device.

Run the application; the bundled binaries will automatically initialize.

For Developers (Build from Source)
Clone the Repo:

Bash
git clone https://github.com/nilanshpratapanand/Lumina-ADB.git
Install Dependencies:

Bash
pip install customtkinter pyinstaller
Compile with Binaries:
To bundle the bin folder into the .exe, use:

PowerShell
py -m PyInstaller --noconsole --onefile --add-data "bin;bin" --icon=lumina.ico main.py
⚠️ Important Warnings & Safety
Bootloader Unlocking: Unlocking the bootloader or flashing partitions can lead to data loss or a "bricked" device.

Xiaomi Devices: For Redmi/Xiaomi devices, this tool facilitates the connection check, but you must still use the official Mi Flash Unlocker for server-side token verification.

Disclaimer: This software is provided "as-is." The developer is not responsible for any hardware damage or data loss resulting from the use of this tool.

Developed by: Nilansh Pratap Anand

Academic background: BTech CSE (Data Science) | Lloyd Institute of Engineering & Technology

Focus: Android Modding, Software Development, and System Performance
