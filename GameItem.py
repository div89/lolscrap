
class GameItem:
   empCount = 0

   def __init__(self, gameType, gameTime):
      self.gameType = gameType
      self.gameTime = gameTime
   
   def printFormatedDate(self):
      return self.gameTime.strftime("%d.%m.%Y %H:%M:%S")
   
   def printAllInfo(self):
      print(f"{self.gameType}, time: , {self.printFormatedDate()}")
