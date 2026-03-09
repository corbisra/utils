from abc import ABC
from typing import Protocol

class Processor(ABC):
   '''
    base class is the processor from which all extensions will inherit
    this class has direct acesss to the command line paramaters all other 
    classes inheriting will have this functionality
   '''
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
    Reporting base class this is the root for all reporting implementations
   '''
   def initialise(self):
       print("none")
       
   def process(self):
       print("none")
       
   def finalise(self):
       print("none")    


class Calculator(Processor):
   '''
    Calculator base class this is the root for all Quant/Calculations implementations
   '''
    
   def initialise(self):
       print("none")
       
   def process(self):
       print("none")
       
   def finalise(self):
       print("none")      

