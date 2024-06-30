# Program to replace 'Donkey' word from the file.txt by #####
word = "Donkey"
with open('file.txt') as f:
    content = f.read()

    if "Donkey" in content:
        newContent = content.replace(word, '#####')
        with open('file.txt', 'w') as f:
            f.write(newContent)
        print("The word Donkey has been replaced by #####")
    else:
        print("The word Donkey is not present in the file.")
    