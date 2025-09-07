import abc
import functools

class Item(abc.ABC):
    listT = "te sad as sad asd asd as dassa das das dasd qwdwqd asd asd as das".split()
    @abc.abstractmethod
    def isempty(self):
        """ Return True if item is empty"""    
        
class offshoreItem(Item):    
    def __init__(self,*desc):
        super().__init__()
        self.itemDesc : str = desc
    def isempty(self):
        return not bool(self.itemDesc)    
    def __len__(self):
        return len(self.listT)
    def __getitem__(self,pos):
        return self.listT[pos]

if __name__ == "__main__":
    it = [offshoreItem("tedsadasd"),offshoreItem("tedsadasd"),offshoreItem("tedsadasd")]
    test = it[0]
    print(test[0:2])