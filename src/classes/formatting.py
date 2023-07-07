
def add_border(title:str = "", text:str = ""):
  print("-" * 50)

  word = ""
  
  for letter in title:
    word += letter.upper()
    word += " "

  print(word)

  print(text)

  print("-" * 50)