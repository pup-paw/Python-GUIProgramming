from tkinter import *

root = Tk()
root.title("pup-paw GUI")
root.geometry("640x480")  # 가로*세로

Label(root, text="메뉴를 선택하세요").pack()


def btncmd():
    pass


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
