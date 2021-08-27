from tkinter import *

root = Tk()
root.title("pup-paw GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

# padx, pady : 버튼 padding 설정 (글자가 길어지면 크기도 변함)
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width, height : 버튼 자체의 크기 설정 (글자가 길어져도 크기 변하지 x)
btn4 = Button(root, width=10, height=5, text="버튼4")
btn4.pack()

# fg : foreground (글자 색), bg : background (배경 색)
# btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
# Mac OS에서는 버튼의 배경색 및 전경색 변경을 지원하지 않음
# 따라서 bg 대신  highlightbackground 사용
btn5 = Button(root, fg="purple", highlightbackground="yellow", text="버튼5")
btn5.pack()

# 이미지 버튼
photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()


# 동작하는 버튼
def btncmd():
    print("버튼이 클릭되었어요.")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
