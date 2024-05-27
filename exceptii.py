def lungimea_unui_text():
    try:
        text=input("Text: ")
        return len(text)
    except ValueError as e:
        print(e)
        return "Introduceti un string"
    
dict={"a":1,
      "b":2,
      "c":3
      }

def cheie_valoare(cheie):
    try:
        return dict[cheie]
    except KeyError as e:
        print(e)
        return f"Introduceti o cheie valida din dictionarul {dict.keys()}"