import pyautogui
import tkinter as pras
root=pras.Tk()
canvas=pras.Canvas(root,width=300,height=300)
canvas.pack()
def fun():
    run=pyautogui.screenshot()
    run.save('C:/Users/91812/Desktop/scrsht.png')
btn=pras.Button(text="Takescreenshot",command=fun(),bg="red",fg="white",font=10)
canvas.create_window(150,150,window=btn)
root.mainloop()
print("Your screen shot is saved")
    
