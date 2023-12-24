import psutil, win32gui, win32con
from pypresence import Presence

win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

client = "" # your application id here, https://discord.com/developers
RPC = Presence(client)
RPC.connect()

def get():
    cores = psutil.cpu_percent(interval=5, percpu=True)
    cpu = sum(cores) / len(cores) * 1.5
    ram = psutil.virtual_memory().percent
    return cpu, ram

while True:
    cpu, ram = get()
    RPC.update(details=f"CPU: {cpu:.2f}%", state=f"RAM: {ram:.2f}%", large_image="https://schuh.wtf/resources/images/dawg.png")
