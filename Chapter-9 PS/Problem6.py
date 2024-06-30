with open('log.txt') as f:
    content = f.read()

if 'Python' in content:
    print("Yes, Python is present in file")
else:
    print("No, Python is not present in file")