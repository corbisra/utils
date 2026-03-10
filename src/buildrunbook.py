from typing import Protocol
import importlib
import pandas as pd

from utils.src import LoggingUtils, SystemUtils, Processor, Reporting


class BuildRunbook(Reporting):     
    ''' BuildRunbook is a reporting child and falls under an example of Reporting Hierarchy
    '''
    
    def initialise(self):
       ''' create file and ensure path folder exists if not  create    
       '''
       self.dfRunBook_ = pd.DataFrame({'Module':[], 'Class':[], 'method':[], 'comment':[]})
       LoggingUtils().printLog(f'executing initialise {self.__class__}', 'info')
 
    
    def process(self):
       ''' for the complete list of modules run through the aviable classes and \n
       interrogate the __doc__ and __name__
       '''
       LoggingUtils().printLog(f'executing process {self.__class__}', 'info')
       LoggingUtils().printLog("starting building runbook", 'debug')

       for value in  self.getkwargs().get('Packages').split(','):
         thisModule = importlib.import_module(value)
         
         for key in dir(thisModule):
           obj = getattr(thisModule, key)
           if isinstance(obj, type):
             LoggingUtils().printLog(f'{key}-isinstance', 'info')
             if isinstance(obj(), Processor):
               self.processClassMethods(obj, value)
        
    
    def finalise(self):               
       ''' save the final file as a CSV or whatever format is required
       '''
       buildRunBookConfig = SystemUtils().getConfig().get('BuildRunbook')        
       LoggingUtils().printLog(f'finalising will print until decision to save csv file decided, path:{buildRunBookConfig.get('path')}\
 filename:{buildRunBookConfig.get('filename')}', 'info')
       print(self.dfRunBook_ )
    
    
    def processClassMethods(self, obj, packageName):
       methods = [ method for method in dir(obj) if '_' not in method ]
       row={'Module':packageName, 'Class':obj.__name__, 'method':'', 'comment':obj.__doc__}
       self.dfRunBook_ = pd.concat([self.dfRunBook_, pd.DataFrame([row])], ignore_index=True)       
       for m in methods:
         text= "" if None is getattr(obj, m).__doc__ else getattr(obj, m).__doc__.strip()
         row={'Module':packageName, 'Class':obj.__name__, 'method':m, 'comment':text}
         self.dfRunBook_ = pd.concat([self.dfRunBook_, pd.DataFrame([row])], ignore_index=True)
         LoggingUtils().printLog(f'Class={obj.__name__}->{m}:{text}', 'debug')