from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print("pass value",x)
    
    @abstractmethod
    def task(self):
        print("We are inside abstract class task")

class basetest_class(absclass):
    def task(self):
        print("We are inside basetest_class")

object = basetest_class()
object.task()
object.print(100)
    

