def lungimea_unui_text():
    try:
        text=input("Text: ")
        return len(text)
    except ValueError as e:
        print(e)
        return "Introduceti un string"