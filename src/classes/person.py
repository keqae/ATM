class Person:
  def __init__(self, id:str = "", title:str = "", name:str = "", surname:str = "", balance:float = 0):
    self.id = id
    self.title = title
    self.name = name
    self.surname = surname
    self.balance = balance

  @property
  def statistics(self):
    return [self.id, self.title, self.name, self.surname, self.balance]
    
    