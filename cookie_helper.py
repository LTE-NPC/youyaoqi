class transCookie:
  def __init__(self, cookie):
     self.cookie = cookie

  def stringToDict(self):

     itemDict = {}
     items = self.cookie.split(';')
     for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
     return itemDict

if __name__ == "__main__":
  cookie = "你自己的cookie"
  trans = transCookie(cookie)
  print (trans.stringToDict())