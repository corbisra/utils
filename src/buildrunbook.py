from typing import Protocol
import importlib
import pandas as pd
from baseutils.src import Processor
global myArgs
from baseutils.src import LoggingUtils

class BuildRunbook(Processor):
    
    def initialise(self):
       '''
         create file and ensure path folder exists if not  create    
       '''
       self.dfRunBook_ = pd.DataFrame({'Module':[], 'Class':[], 'method':[], 'comment':[]})
 
    
    def process(self):
       '''
         for the complete list of modules run through the aviable classes and 
         interrogate the __doc__ and __name__
       '''
       LoggingUtils().printLog("starting building runbook")

       for key,value in self.getkwargs().items():
         thisModule = importlib.import_module(value)
         
         for key in dir(thisModule):
           obj = getattr(thisModule, key)
           if isinstance(obj, type):
             print(f'{key}-isinstance')
             if isinstance(obj(), getattr(thisModule, 'Processor')):
               self.processClassMethods(obj, value)
        
       print(self.dfRunBook_)
    
    def finalise(self):       
       '''
         save the final file as a CSV or whatever format is required
       '''
    
    def processClassMethods(self, obj, packageName):
       methods = [ method for method in dir(obj) if '_' not in method ]
       for m in methods:
         text=getattr(obj, m).__doc__
         row={'Module':packageName, 'Class':obj.__name__, 'method':m, 'comment':text}
         self.dfRunBook_ = pd.concat([self.dfRunBook_, pd.DataFrame([row])], ignore_index=True)
         LoggingUtils().printLog(f'Class={obj.__name__}->{m}:{text}')