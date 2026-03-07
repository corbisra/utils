from typing import Protocol
import importlib
from baseutils.src import Processor
global myArgs
from baseutils.src import LoggingUtils

class BuildRunbook(Processor):
    
    def initialise(self):
       '''
         create file and ensure path folder exists if not  create
    
       self.__dict__.update((key, False) for key in self.allowed_keys)
       self.__dict__.update((key, value) for key, value in self.getkwargs() if key in self.allowed_keys)
       '''
 
    
    def process(self):
       '''
         for the complete list of modules run through the aviable classes and 
         interrogate the __doc__ and __name__
       '''
       LoggingUtils().printLog("building runbook")
       LoggingUtils().printLog("starting building runbook")

       for key,value in self.getkwargs().items():
         thisModule = importlib.import_module(value)
         
         for key in dir(thisModule):
           obj = getattr(thisModule, key)
           if isinstance(obj, type):
             print(f'{key}-isinstance')
             if isinstance(obj(), getattr(thisModule, 'Processor')):
               methods = [ method for method in dir(obj) if '_' not in method ]
               print(methods)
               for m in methods:
                 getattr(obj, m).__doc__
        
    
    def finalise(self):
       '''
         save the final file as a CSV or whatever format is required
       '''