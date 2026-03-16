'''
  system environment and config singleton class
  this class is a system wide log ensure the same log is consistently formatted and shared across the python process
'''
import sys
import os
import configparser
import json

class SystemUtils:
   ''' SystemUtils Singleton to ensure consistent access to the config and base environment
       -- this class is not Thread safe
   '''
   
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(SystemUtils, cls).__new__(cls)
      cls._instance.__initialise()
      
    return cls._instance
  
  def __initialise(self):
    self._instance.configjson_ = None
    self._instance.MYENVPATH = os.environ.get('TEMP_HOME')
    self._instance.MYENV     = os.environ.get('ENVIRONMENT')
    ini_path = os.path.join(SystemUtils().getConfigPath(),'baseconfig.ini')
    json_path = os.path.join(SystemUtils().getConfigPath(),'baseconfig.json')
    fileExists = True if os.path.exists(ini_path) or os.path.exists(json_path) else False
    self.logPath_ = None
    
    if not fileExists:    
     self._instance.MYENVPATH= os.environ.get('HOME')
     ini_path = os.path.join(SystemUtils().getConfigPath(),'baseconfig.ini')
     json_path = os.path.join(SystemUtils().getConfigPath(),'baseconfig.json')
     if not self._instance.MYENVPATH:
         raise Exception("neither HOME not TEMP_HOME setup")
    
    self._instance.config_ = self._instance.configJson = None
    fileExists = True if os.path.exists(ini_path) else False
    if fileExists:
      self._instance.config_ = configparser.ConfigParser()
      self._instance.config_.read(ini_path)
      
    
    fileExists =  True if os.path.exists(json_path) else False
    if fileExists:
      with open(json_path, "r") as json_file:
        self._instance.configjson_ = json.load(json_file)
        envExist = self._instance.configjson_.get(self._instance.MYENV)
        generalSectionExist = self._instance.configjson_.get('GENERAL')
        if envExist is not None:
          self._instance.configjson_ = envExist
        
        if generalSectionExist is not None:
          self._instance.configjson_.update(generalSectionExist)
          self.logPath_ = str(self._instance.configjson_.get('LOG').get('absolute_path_to_logfile'))
          print(f'log path is :{self.logPath_}')
    
    if None is self._instance.config_:
      self._instance.config_ = self._instance.configjson_
   
  def getBasePath(self):
    return str(self._instance.MYENVPATH) 
  
  def getConfigPath(self):
    return str(self._instance.getBasePath()+'/config/')
  
  def getLogPath(self):
    if self.logPath_ is None:
      self.logPath_ = str(self._instance.getBasePath()+'/logs/')
    
    return self.logPath_
  
  def getParamPath(self):
    return str(self._instance.getBasePath()+'/params/')
    
  def getConfig(self):
    return self._instance.config_
  
  def getJson(self):
    self._instance.configJson_
     
      
