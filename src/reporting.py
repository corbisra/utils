from abc import ABC
from typing import Protocol

class Processor(ABC):
   def __init__(self, **kwargs):
      self.attributes_ = kwargs

   def getkwargs(self):
        print(self.attributes_)
        return self.attributes_
   '''
    This is the base class for all processors to enable location and identification
   '''
   def initialise(self) -> None:
        raise NotImplementedError()
        
   def process(self) -> None:
        raise NotImplementedError()
        
   def finalise(self) -> None:
        raise NotImplementedError()
        
        
class Reporting(Processor):
   '''
    Sample processor
   '''
   def initialise(self):
       '''
        database context
       '''
       print("none")
       
   def process(self):
       print("none")
       
   def finalise(self):
       print("none")    

class Calculator(Processor):
   def initialise(self):
       print("none")
       
   def process(self):
       print("none")
       
   def finalise(self):
       print("none")      

