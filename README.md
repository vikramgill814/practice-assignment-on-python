# practice-assignment-on-python

## Program Descriptions

### 1. backup.py
This script copies all files from a source directory to a destination directory. If a file with the same name already exists in the destination, it appends a timestamp to the filename to ensure uniqueness. It handles errors such as missing directories.

**Command to run:**
```bash
python backup.py /path/to/source /path/to/destination
```
**Instructions:**  
- Replace `/path/to/source` and `/path/to/destination` with your actual directory paths.
- Both directories must exist before running the script.

---

### 2. check-health-of-cpu.py
This program continuously monitors the CPU usage of your local machine. If the CPU usage exceeds a predefined threshold (80%), it displays an alert message. The program runs indefinitely until interrupted.

**Command to run:**
```bash
python check-health-of-cpu.py
```
**Instructions:**  
- Make sure the `psutil` library is installed (`pip install psutil`).
- Stop monitoring by pressing `Ctrl+C`.

---

### 3. check-password-strength.py
This script checks the strength of a password entered by the user. It evaluates the password based on length, use of uppercase and lowercase letters, digits, and special characters. The script provides feedback on whether the password is poor, medium, or strong.

**Command to run:**
```bash
python check-password-strength.py
```
**Instructions:**  
- Enter your password when prompted.
- Review the feedback to improve your password strength.