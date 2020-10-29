from tkinter import *
import pyautogui
import time
def fun():
    root.withdraw()
    time.sleep(1)
    run=pyautogui.screenshot()
    run.save('C:/Users/91812/Desktop/scrsht.png')
root=Tk()
root.config(bg='red')
button=Button(root,text="TakeScreenShot",bg="pink",command=fun)
button.pack()
root.mainloop()

    
