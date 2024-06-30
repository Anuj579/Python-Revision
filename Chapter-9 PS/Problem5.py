words = ["Donkey", "Cow", "Dog"]

with open('file.txt') as f:
    content = f.read()
    if any(word in content for word in words): 
        for word in words:
            content = content.replace(word, '#' * len(word))
        with open('file.txt', 'w') as f:
            f.write(content)
        print("The words have been replaced.")
    else:
        print("Words are not in the file.")
