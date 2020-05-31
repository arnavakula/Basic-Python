class Duck:
    def talk(self):
        print("Quack")

class Human:
    def talk(self):
        print("Hello")

def callTalk(obj):
    obj.talk()

duck = Duck()
human = Human()

callTalk(duck)
callTalk(human)