import inspect
import argparse
import traceback

class ArgsParser(argsparse.ArgumentParser):
  def __init__(self, params, description='basic'):
    self.parser_ = argsparse.ArgumentParser(description=description)
    self.argsToPass_ = {}
    self.argsToCapture = None
    self.myArgs        = None
    
    try:
    except Exception:
      traceback.print_exc()
      self.argsToCapture = None
    finally: pass
    
  def initialise(self):
    if None == self.argsToCapture_:
     return
     
    if "self" in self.argsToCapture_:
      self.argsToCapture_remove("self")
    
    for arg in self.argsToCapture_:
      self.parser_.add_argument(str('--'+arg), type=str) 
      self.argsToPass_.update({arg:0})  

  def addArgument(self, argument, defaultValue, helpDescription)      
    self.parser_.add_argument(str('--'+argument), type=str, default=defaultValue, help=helpDescription)
    self.argsToPass_.update({arg:0})
  
  def parseCommandline(self):
    self.myArgs_, unknown=self.parser_.parse_known_args()
    for arg in vars(self.myArgs_):
      self.argsToPass_.update({arg:getattr(self.myArgs_, arg)})
  
  def actualArgs(self):
    return self.myArgs_
  
  def allArgsPopulated(self):
    return (all(vars(self.actualArgs()).values()))
  
  def requiredArgs(self):
    return self.argsToPass_