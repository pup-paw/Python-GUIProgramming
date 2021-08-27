from tkinter import *

root = Tk()
root.title("pup-paw GUI")
root.geometry("640x480")  # 가로*세로

# 여러줄 입력 가능 (enter 줄바꿈 가능)
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 한 줄 입력 필요시 사용가능 ex)아이디, 패스워드...
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")  # 현재 비어있어 0대신 END를 사용해도 동일함


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
