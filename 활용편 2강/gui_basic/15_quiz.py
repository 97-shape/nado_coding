import os
from tkinter import *

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")  # 가로 x 세로

# 메뉴 구현
menu = Menu(root)

# 파일
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):  # 파일 있으면 참, 없으면 거짓
        with open(filename, 'r', encoding="utf8") as file:
            txt.delete("1.0", END)  # 기존 입력 항목 삭제
            txt.insert(END, file.read())  # 모든 내용을 본문에 입력
    pass

def save_file():
    with open(filename, 'w', encoding="utf8") as file:
        file.write(txt.get("1.0", END))  # 모든 내용을 가져와서 저장
    pass

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="종료", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 기타 메뉴
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)

menu_form = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_form)

menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_view)

menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help)

# 스크롤
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

root.config(menu=menu)
root.mainloop()