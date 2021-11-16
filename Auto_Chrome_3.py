import subprocess
from tkinter import *
from tkinter.messagebox import WARNING, showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
import platform 


opsys = platform.system()
main_directory = os.getcwd()
file = None

print("Current program directory check: "+main_directory)

root = Tk()
root.title("Chrome Automation")
root.geometry("644x788")



def open_chrome_profile():
    browser_port=int(p.get())
    if opsys == "Windows":
        subprocess.Popen(['start', 'chrome', '--remote-debugging-port={port_num}'.format(port_num=browser_port), '--user-data-dir=' + main_directory + '/chrome_profile'], shell=True)
    elif opsys == "Darwin":
        cmd = "open -a /Applications/Google\ Chrome.app --args --remote-debugging-port={port_num} --user-data-dir={cwd}/chrome_profile".format(cwd = main_directory, port_num=browser_port)
        subprocess.Popen(cmd, shell=True)
    else:
        subprocess.Popen(['google-chrome', '--remote-debugging-port={port_num}'.format(port_num=browser_port), '--user-data-dir=' + main_directory + '/chrome_profile'], shell=True)

    print("Opening debug browser on port {port_num}".format(port_num=browser_port))
    
#####MENU BAR#####
def newFile():
    global file
    root.title("Untitled - Auto_Chrome")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Auto_Chrome")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Auto_Chrome")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def donate():
    showinfo("Donate", "https://linktr.ee/Cloudmaking")
def readme():
    showinfo("ReadMe", "Comand List:\ngo_to(adress)\ncss_and_key(code, key)\nxpath_and_key(code, key)\ncss_and_click(code)\nxpath_and_click(code)\nlinktext_key(code, key)\nlinktext_click(code)")
def about():
    showinfo("Auto_Chrome_3", "by @Cloudmaking")

MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="Open", command = openFile)
FileMenu.add_command(label = "Save", command = saveFile)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit", command = quitApp)
MenuBar.add_cascade(label = "File", menu=FileMenu)
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label = "Donate", command=donate)
HelpMenu.add_command(label = "ReadME", command=readme)
HelpMenu.add_command(label = "About Notepad", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
root.config(menu=MenuBar)
#####MENU BAR END#####



# _____MAIN_CODE_____
def main_program_loop(): 
    browser_port=int(p.get())
    ###new chrome options
    if opsys == "Windows":
        ser = Service(main_directory + "/chromedriver.exe")
    elif opsys == "Darwin":
        ser = Service(main_directory + "/chromedriver")
    else:
        ser = Service(main_directory + "/linuxchromedriver")
    
    op = webdriver.ChromeOptions()
    op.add_experimental_option("debuggerAddress", "localhost:{port_num}".format(port_num=browser_port))
    driver = webdriver.Chrome(service=ser, options=op)
    wait = WebDriverWait(driver, int(w.get()))

    print("Connected to browser on port {port_num}".format(port_num=browser_port))

    #establish main page
    main_page = driver.current_window_handle

    def xpath_and_click(code):
        x = wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
        x.click()

    def css_and_click(code):
        x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code)))
        x.click()

    def xpath_and_key(code, key):
        x = wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
        x.send_keys(key)
        #time.sleep(1)

    def css_and_key(code, key):
        x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code)))
        x.send_keys(key)
        #time.sleep(1)

    def linktext_click(code):
        x = wait.until(ExpectedConditions.presence_of_element_located((By.LINK_TEXT, code)))
        x.click()
        #time.sleep(1)

    def linktext_key(code, key):
        x = wait.until(ExpectedConditions.presence_of_element_located((By.LINK_TEXT, code)))
        x.send_keys(key)
        #time.sleep(1)

    def go_to(adress):
        driver.get(adress)

    loop_amount = int(e.get())

    exec(TextArea.get(1.0, END))


    
####UI ELEMENTS######
my_font = "Arial Black"

info = Label(text = "Make sure the browser is open before starting or the program might freeze/crash.\n Press Ctrl-C in debug window to stop mian loop", bg = "white")
info.pack()
info.config(font=("Arial", 9))

open_browser = Button(text = "Open Browser", command = open_chrome_profile, bg = "yellow", font=(my_font, 10))
open_browser.pack(anchor=N, pady=5, padx=5)

start_button = Button(text = "Start Main Loop", command = main_program_loop, bg = "green", font=(my_font, 10))
start_button.pack(anchor=N, pady=5, padx=5)

#number of loop entry
e = Entry(root)
e.insert(1, 1)
e.label = Label(text= "Loop amount:")
e.label.pack(anchor=W, pady=0, padx=1)
e.config(font=(my_font, 8))
e.label.config(font=(my_font, 8))
e.pack(anchor=W, pady=1, padx=1)

#wait time in sec
w = Entry(root)
w.insert(1, 30)
w.label = Label(text= "Wait amount(s):")
w.label.pack(anchor=W, pady=0, padx=1)
w.config(font=(my_font, 8))
w.label.config(font=(my_font, 8))
w.pack(anchor=W, pady=1, padx=1)

#port
p = Entry(root)
p.insert(1, 8989)
p.label = Label(text= "Port:")
p.label.pack(anchor=W, pady=0, padx=1)
p.config(font=(my_font, 8))
p.label.config(font=(my_font, 8))
p.pack(anchor=W, pady=1, padx=1)

#Add TextArea
TextArea = Text(root, font=("Arial", 10), bg = "light gray")
TextArea.pack(expand=True, fill=BOTH, anchor=S)

#scrooll bar
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
####UI ELEMENTS END####

root.mainloop()
