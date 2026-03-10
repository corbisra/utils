from typing import Protocol
import importlib
import pandas as pd

from utils.src import LoggingUtils, Processor, Reporting


class BuildRunbook(Reporting):     
    '''
    BuildRunbook is a reporting child and falls under an example of Reporting Hierarchy
    '''
    def initialise(self):
       '''
         create file and ensure path folder exists if not  create    
       '''
       self.dfRunBook_ = pd.DataFrame({'Module':[], 'Class':[], 'method':[], 'comment':[]})
       LoggingUtils().printLog(f'executing initialise {self.__class__}', 'info')
 
    
    def process(self):
       '''
         for the complete list of modules run through the aviable classes and 
         interrogate the __doc__ and __name__
       '''
       LoggingUtils().printLog(f'executing process {self.__class__}', 'info')
       LoggingUtils().printLog("starting building runbook", 'debug')

       for value in  self.getkwargs().get('BuildRunbook').split(','):
         thisModule = importlib.import_module(value)
         
         for key in dir(thisModule):
           obj = getattr(thisModule, key)
           if isinstance(obj, type):
             print(f'{key}-isinstance')
             if isinstance(obj(), Processor):
               self.processClassMethods(obj, value)
        
    
    def finalise(self):               
       '''
         save the final file as a CSV or whatever format is required
       '''
       LoggingUtils().printLog(f'finalising {self.__class__}', 'info')
       print(self.dfRunBook_ )
    
    
    def processClassMethods(self, obj, packageName):
       methods = [ method for method in dir(obj) if '_' not in method ]
       row={'Module':packageName, 'Class':obj.__name__, 'method':'', 'comment':obj.__doc__}
       self.dfRunBook_ = pd.concat([self.dfRunBook_, pd.DataFrame([row])], ignore_index=True)       
       for m in methods:
         text=getattr(obj, m).__doc__
         row={'Module':packageName, 'Class':obj.__name__, 'method':m, 'comment':text}
         self.dfRunBook_ = pd.concat([self.dfRunBook_, pd.DataFrame([row])], ignore_index=True)
         LoggingUtils().printLog(f'Class={obj.__name__}->{m}:{text}', 'debug')