from abc import ABC
from typing import Protocol
from utils.src import LoggingUtils

class Processor(ABC):
   '''
    base class is the processor from which all extensions will inherit
    this class has direct acesss to the command line paramaters all other 
    classes inheriting will have this functionality
   '''
   def __init__(self, **kwargs):
       self.attributes_ = kwargs

   def getkwargs(self):
       '''
       read all parameters from command line anything else can be injected via config
       '''
       return self.attributes_
   
   '''
    This is the base class for all processors to enable location and identification
   '''
   def initialise(self) -> None:
       ''' abstract
       '''
       raise NotImplementedError()
        
   def process(self) -> None:
       ''' abstract
       '''       
       raise NotImplementedError()
        
   def finalise(self) -> None:
       ''' abstract
       '''       
       raise NotImplementedError()
        
        
class Reporting(Processor):
   '''
    Reporting base class this is the root for all reporting implementations
   '''
   def __init__(self, **kwargs):
       super().__init__(**kwargs)   
       
   def initialise(self):
       '''
       standard initialisation context for user to ensure state is ready
       '''
       LoggingUtils().printLog(self.getkwargs(), 'debug')
       
   def process(self):
       '''
       standard processing context for user reporting
       '''       

       
   def finalise(self):
       '''
       standard completion context to ensure the data and any/all completion checks are green
       '''       
       


class Calculator(Processor):
   '''
    Calculator base class this is the root for all Quant/Calculations implementations
   '''
   def __init__(self, **kwargs):
       super().__init__(**kwargs)  
       
   def initialise(self):
       '''
       standard initialisation context for user computaion ensure state is ready
       '''       
       LoggingUtils().printLog(self.getkwargs(), 'debug')
       
   def process(self):
       '''
       standard processing context for user calcualtions
       '''       

       
   def finalise(self):
       '''
       standard completion context to ensure the data and any/all completion checks are green
       '''             


