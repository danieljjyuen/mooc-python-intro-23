while True:
    word = input("Editor:")
    word = word.lower()
    if word == "notepad" or word == "word":
        print("awful")
    elif word != "visual studio code":
        print("not good")
    else:
        print("an excellent choice!")
        break
