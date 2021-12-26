# imports
import socket
import platform
from tkinter import *
import psutil
from datetime import datetime

 # For the memory
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def root_window():
    
    # functions will be here at the top

    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    svmem = psutil.virtual_memory()
    cpufreq = psutil.cpu_freq()
    swap = psutil.swap_memory()
    #making an open funtion so we can open the next window with all the specifications inside
    def open_computer_info():
        global offl
        offl = Toplevel()
        offl.resizable(height=False, width=False)
        #Now we are showing the things in your pc, this is just by using the import moduel platform, and then using the framwork
        Label_space = Label(offl, text="\n").pack()
        Label_node = Label(offl, text="Your pc name is: " + platform.node()).pack()
        Label_machine = Label(offl, text="You are running: " + platform.machine()).pack()
        Label_python_version = Label(offl, text="Python compile version: " + platform.python_compiler()).pack()
        Label_release = Label(offl, text= "Release: " + platform.release()).pack()
        Label_processor_cpu = Label(offl, text="You are running: " + platform.processor() + " As your processor").pack()
        Label_version = Label(offl, text= "Version and platform: " + platform.version() +" "+ platform.platform()).pack()
        Label_uname = Label(offl, text= "This is your os name / Uname: " + str(platform.uname())).pack()
        Label_boottime = Label(offl, text=f"Last time you turned on your pc: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}").pack()
        Label_macfreq = Label(offl, text=f"Max Frequency: {cpufreq.max:.2f}Mhz").pack()
        Label_minfreq = Label(offl, text=f"Min Frequency: {cpufreq.min:.2f}Mhz").pack()
        Label_currentFreq = Label(offl, text=f"Current Frequency: {cpufreq.current:.2f}Mhz").pack()
        Label(offl, text="CPU Usage Per Core:").pack()
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            Label(offl, text=f"Core {i}: {percentage}%").pack()
        Label(offl, text=f"Total CPU Usage: {psutil.cpu_percent()}%").pack()
        Label(offl, text=print("="*40, "Memory Information", "="*40)).pack()
        Label_mem = Label(offl, text="Memory usage: ").pack()
        Label_totaalsvmem = Label(offl, text=f"Total: {get_size(svmem.total)}").pack()
        Label_Ava = Label(offl, text=f"Available: {get_size(svmem.available)}").pack()
        Label_Use = Label(offl, text=f"Used: {get_size(svmem.used)}").pack()
        Label_percent = Label(offl, text=f"Percentage: {svmem.percent}%").pack()
        Label_space = Label(offl, text="\n").pack()


    def privopen():
        global screenP
        screenP = Toplevel()
        screenP.title("Network Information")
        screenP.resizable(width=False, height=False)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                Label(screenP, text=f"=== Interface: {interface_name} ===").grid()
                if str(address.family) == 'AddressFamily.AF_INET':
                    Label(screenP, text=f"  Local host address: {address.address}").grid()
                    Label(screenP, text=f"  Netmask: {address.netmask}").grid()
                    Label(screenP, text=f"  Broadcast IP: {address.broadcast}").grid()
                elif str(address.family) == 'AddressFamily.AF_gridET':
                    Label(screenP, text=f"  MAC Address: {address.address}").grid()
                    Label(screenP, text=f"  Netmask: {address.netmask}").grid()
                    Label(screenP, text=f"  Broadcast MAC: {address.broadcast}").grid()
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        Label(screenP, text=f"Total Bytes Sent: {get_size(net_io.bytes_sent)}").grid()
        Label(screenP, text=f"Total Bytes Received: {get_size(net_io.bytes_recv)}").grid()


    def moreFeatures():
        Label_moreFeatures = Label(root, text="More features, click the buttons").grid()

        moreFeaturesButton1 = Button(root, text="Network Information",borderwidth=0, bg="#b6b6b6", width=20, height=1, command=privopen).grid(row=15, column=0)
        moreFeaturesButton2 = Button(root, text="Computer Information", borderwidth=0, bg="#b6b6b6", width=20, height=1, command=open_computer_info).grid()

        root.geometry("400x515")


    # I -------------- This is the main root of the window ---------------------- I
    root = Tk()
    root.title('GUI')
    root.geometry("385x380")
    root.resizable(height=False, width=False)
    

    # I ---------------- Labels and buttons ---------------------------------- I

    Label_header_buttom = Label(root, text="_" * 55).grid()

    label_something = Label(root, text="\n").grid()

    label_welcome = Label(root, text=f"Welcome, {socket.gethostname()} to buity GUI", font=("Bold", 13)).grid()

    label_something = Label(root, text="\n").grid()

    button_more_features = Button(root, text="More features in buity GUI",borderwidth=0, bg="#b6b6b6",  command=moreFeatures).grid()
    
    Label_basic_info = Label(root, text="Basic information:").grid()
    Label_space = Label(root, text="\n").grid()
    Label_machine = Label(root, text="You are running: " + platform.machine() + " architecture").grid()
    Label_processor_cpu = Label(root, text="You are running: " + platform.processor() + " As your processor").grid()
    Label_release = Label(root, text= "Release: " + platform.release()).grid()



    Label_space = Label(root, text="\n\n" * 2).grid()
    
    Label_header_buttom = Label(root, text="_" * 55).grid()

    # I -------------------------------------------------------------- I

    root.mainloop()

root_window()