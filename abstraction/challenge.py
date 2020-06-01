from abc import *

class TouchScreenLaptop(ABC):
  
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling on HP")
    
class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling on Dell")
    
class HPNotebook(HP):

    def click(self):
        print("Clicking on HP Notebook")

class DellNotebook(HP):

    def click(self):
        print("Clicking on Dell Notebook")

hp_notebook = HPNotebook()
dell_notebook = DellNotebook()

hp_notebook.click()
dell_notebook.click()
hp_notebook.scroll()
dell_notebook.scroll()

    