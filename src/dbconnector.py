
import os
import pandas as pd
import pyodbc

from utils.src import SystemUtils,LoggingUtils


class DBODBCConnector():
  # Function with the new connector : 
  def __init__(self, database=None, schema=None):
    self._database   = database
    self._schema     = schema
    self._rootFolder = None
    self._sfCon      = None
    self._sfCursor   = None 
    
    self.initialise()
  
  def initialise(self):
    if (self._database is None) or (self._database is None):
      self._database   = SystemUtils().getConfig().get('database').get('database')
      self._schema     = SystemUtils().getConfig().get('database').get('schema')
      
    self._sfCon      = pyodbc.connect(dsn="SnowflakeRM")
    self._sfCon.setencoding(encoding='utf-8')
    self._sfCon.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    self._sfCursor   = self._sfCon.cursor()      
    
    self._rootFolder = SystemUtils().getConfig().get('database').get('root_path_to_sql_files')
    LoggingUtils().printLog(f'setup db with sql path to : {self._rootFolder}',"info")
    
      
  def query(self, query="", isFile=True, **kwargs):
    dfResult = None
    fileToOpen = str(self._rootFolder) + "/"+ str(query)
    
    try :
      fileExists = True if os.path.exists(fileToOpen) else False
      if isFile and fileExists:
         query = open(fileToOpen, "r").read()
      
      query = query.format(**kwargs)
      
      dfResult=pd.read_sql_query(query, self._sfCon)
      ## dfResult=pd.read_sql_query("SELECT * from riskmgmt.datamart.RMA_STRESS_SCENARIOS", con)
      ## cursor.execute("SELECT * from riskmgmt.datamart.RMA_STRESS_SCENARIOS")
      ## dfResult = pd.read_sql(query, self._sfCon)
      dfResult = None if dfResult.empty else dfResult
    except: pass
              
    return dfResult    
  
  def __del__(self):
    if self._sfCon is None:
      self._sfCon.close()
    
    self._sfCon    = None
    self._sfCursor = None