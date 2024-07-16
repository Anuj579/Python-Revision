a = 34

def func():
    global a
    a = 2
    print(a)

func()
print(a)