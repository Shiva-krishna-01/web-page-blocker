# Web Page Blocker 🛑

A simple Python script that blocks distracting websites during scheduled hours by modifying the system's `hosts` file.  
This helps students and professionals focus better during working hours.

## 📌 Features
- Blocks any list of websites you provide
- Works during a specific time range (e.g., 9 AM to 11 AM)
- Automatically unblocks websites after hours
- Runs continuously in the background

## 🖥️ How It Works
- The script modifies your system’s `hosts` file to redirect distracting websites to `127.0.0.1`
- Every 5 minutes, it checks the current time and either blocks or unblocks sites accordingly

## 🧠 Requirements
- Python 3.x

## ⚙️ Setup & Usage
1. Clone this repository:
   ```
   git clone https://github.com/Shiva-krishna-01/web-page-blocker.git
   ```
2. Run the script as Administrator (required for editing the hosts file):
   ```
   python MiniProject.py
   ```

3. Customize your working hours and website list in the script.

## ⚠️ Note
- On Windows, **you must run the script as Administrator**.
- On macOS/Linux, use `sudo` to execute the script.

---

## 📄 License
This project is open-source and free to use under the MIT License.
