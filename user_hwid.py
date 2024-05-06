import hashlib
import subprocess

def get_hwid():
    FLAG = 0x08000000
    
    cpu_info = subprocess.check_output('wmic cpu get ProcessorId', shell=True, creationflags=FLAG).decode().split('\n')[1].strip()
    
    disk_info = subprocess.check_output('wmic diskdrive get SerialNumber', shell=True, creationflags=FLAG).decode().split('\n')[1].strip()
    
    motherboard_info = subprocess.check_output('wmic baseboard get SerialNumber', shell=True, creationflags=FLAG).decode().split('\n')[1].strip()
    
    hwid = hashlib.md5((cpu_info + disk_info + motherboard_info).encode()).hexdigest()
    
##    return hwid

def user_hwid():
    
    user_hwid = requests.get("").text
    
    return user_hwid
if get_hwid() in user_hwid():
    
else:
    
    messagebox.showwarning("警告","你还没有购买软件")