# Program to find whether a file is identical and matches the content of another file

with open('this.txt') as f:
    content1 = f.read()

with open('file.txt') as f:
    content2 = f.read()

if content1 == content2:
    print("These files contains same content and is identical.")
else:
    print("These files does not contain same content and not indentical")