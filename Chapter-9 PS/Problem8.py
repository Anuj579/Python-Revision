# Program to make a copy of this.txt file

with open('this.txt') as f:
    content = f.read()

with open('this-copy.txt', 'w') as f:
    f.write(content)