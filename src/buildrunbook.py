from typing import Protocol
import importlib

class BuildRunbook():
    def __init__(self):
       self.modules_  = None
       self.path_     = None
       self.filename_ = None
    
    
    def initialise(self, modules, path, filename):
       '''
         create file and ensure path folder exists if not  create
       '''
       self.modules_  = modules
       self.path_     = path
       self.filename_ = filename
 
    
    def process(self):
       '''
         for the complete list of modules run through the aviable classes and 
         interrogate the __doc__ and __name__
       '''
       for mod in self.modules_:
         module = importlib(mod)
         
         for key in dir(module):
           methods = [ method for method in dir(obj) if callable(getattr(key, method)) and '__' not in method ]
           for m in methods:
             getattr(thisModule, m).__doc__
        
    
    def finalise(self):
       '''
         save the final file as a CSV or whatever format is required
       '''