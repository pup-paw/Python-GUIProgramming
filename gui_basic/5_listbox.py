from tkinter import *

root = Tk()
root.title("pup-paw GUI")
root.geometry("640x480")  # 가로*세로

# height : 0일때는 모든 목록을 보여주고, 숫자일때는 해당 숫자만큼의 목록만 보여줌
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(0)  # 맨 앞 항목을 삭제 (0->END : 맨 뒤 항목을 삭제)

    # 갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요.")

    # 항목 확인 (시작 인덱스, 끝 인덱스)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 -> 위치로 반환 ex) (1, 2, 3)
    print("선택된 항목 :", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
