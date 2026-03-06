
import time
import datetime
import logging
import sys
import os
import inspect
from pathlib import Path

from systemsettings import SystemUtils

def checkLogLevels(logType="info"):
  checklevels=list(logging._nameToLevel.keys())
  checkType=logType.upper()
  for i in checklevels:
    if checkType not in checklevels:
      raise Exception("unable to log message due to message level"+logType)
    
def printLog(string_, logType="info"):
  checkLogLevels(logType) 
  
  filename,func,line=loggingUtils().get_call_logstack(function_call_level=2)
  message = "{}--{}@{}:>\t{}".format(filename,func,line, string_)
  logMessage=getattr(loggingUtils.getLog(), logType)
  logMessage(logMessage)
  

class loggingUtils:
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(loggingUtils, cls).__new__(cls)
      cls._instance.__initialise()
      
    return cls._instance
  
  def __initialise(self, whoami):
    self._instance._log = logging.getLogger(whoami)
    self._instance._log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-%(message)s')
    
    now = datetime.datetime.now()
    dirname = str(SystemUtils.getLogPath()) + "/" + str(whoami)
    
    newDirectory = Path(dirname)
    newDirectory.mkdir(parents=True, exist_ok=True)
    
    fileHandler = logging.FileHandler(dirname+"/log_"+now.strftime("%Y-%m-%d")+".log")
    streamHandler = logging.StreamHandler()
    
    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)
    
    self._log.addHandler(fileHandler)
    self._log.addHandler(streamHandler)
   
  def getLog(self):
    return self._instance._log
    
  @staticmetod
  def get_call_logstack(function_call_level=2):
    stack = inspect.stack(0)
    filename = stack[function_call_level][1]
    if None is not stack[function_call_level].frame.f_locals.get('self'):
      filename = "".format(filename, stack[function_call_level].frame.f_locals['self'].__class__.__name__)
    
    func = stack[function_call_level][3]
    line = stack[function_call_level][2]
   
    return filename,func,line