from src.objects.people import all_people
from src.classes.formatting import add_border


add_border("welcome to the atm")

while True:
  try:
    user_id = str(input("Please enter your ID:/n>>/t"))
  
  except TypeError:
    add_border("incorrect id", "Please enter your ID again.")
  
  finally:
    pass
