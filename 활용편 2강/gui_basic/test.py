def open_file():
    t = open('mynote.txt', 'r')
    texts = t.readlines()
    print(texts)
    t.close()

open_file()