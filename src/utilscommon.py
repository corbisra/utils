
import importlib
import traceback
import argparse
import inspect
import pdb
import logging

class UtilsDate:
    
  @staticmethod  
  def parseDateParam(asOfDate):
    for fmt in ('%d.%m%.%Y','%d%m%Y','%Y%m%d','%Y.%m.%d'):
      try:
        tmpAsOfDate=datetime.strptime(asOfDate, fmt)
        return tmpAsOfDate
      except ValueError:pass
    
    return ValueError("Uknown date format")
    
  @staticmethod
  def getMonthLastBusinessDate(input='30.04.2023'):
     inputDate=datetime.strptime(inputDate, '%d.%m.%Y')
     lastBusinessDay= max(calendar.monthcalendar(inputDate.year, inputDate.month)[-1:][0][:5])
     lastBusinessDate=pd.date_range('{}-{}-{}'.format(inputDate.year, inputDate.month, lastBusinessDay), periods=1, freq='d').date[0]
     lastBusinessDate=lastBusinessDate.strftime('%d.%m.%Y')
  
     return lastBusinessDate
  

class UtilsCommon:
  
  @staticmethod
  def abstractFactory(moduleName):
    thisModule = importlib.import_module(moduleName)
    
    def createObject(classname):
      for key in dir(thisModule):
        try:
          obj=getattr(thisModule, key)
          
          if isinstance( obj, type ):
            if key == classname:
              newClass=getattr(thisModule, key)
              return newClass
          else:
            if key == classname:
              raise ValidationError('Expected type %s for field %s, '\
                            'found %s (type %s)' % (type, classname, obj, type(obj)))
        except : pass
      raise Exception(moduleName+" package has no known Class : "+ classname)    
    
    return createObject
    
  '''
  @staticmethod
  def extractCommandLinParams(params):
    try:
       args=baseutils.BALMArgsèarser(params)
       args.initialise()
       args.parseCommandline()
       params= params(**args.requiredArgs())
    except:
        traceback.print_exc()
    finally: pass
  
    return params
  '''

  @staticmethod
  def loadUtilsModuleFunction(modulename, funcname):
    functionToCall = None
    module = importlib.import_module(modulename)
    if module.__name__ == getattr(module, funcname):
      functionToCall = getattr(module, funcname)
      if functionToCall.__name__ != funcname:
          functionToCall = None
      else:
          print("loaded"+functionToCall.__name__)
      
    return functionToCall

  @staticmethod
  def runSystemBootstrap():
    funcname='bootstrap_utils'
    modulename='utils.bootstrap_utils'
  
    systemBootstrap=None
    try:
        systemBootstrap =  loadUtilsModuleFunction(modulename, funcname)
        if systemBootstrap is not None:
          systemBootstrap()
    except Exception as e:
          print(str(""))
          print(e)

  @staticmethod
  def MainModule():
      #runSystemBootstrap()
      from baseutils.src import SystemUtils, LoggingUtils      
      runner = None
      myArgs = None
  
      try:
        myEnv     = SystemUtils()
        logger    = LoggingUtils()
          
        parser=argparse.ArgumentParser(description="")
        parser.add_argument(str('--Module'))
        parser.add_argument(str('--Class'))
        parser.add_argument(str('--Debug'), default="0")
        parser.add_argument(str('--BuildRunbook'))
        
        myArgs, unkown = parser.parse_known_args()
        if 0 != int(myArgs.Debug):
           print(f'starting debug {myArgs.Debug} {type(myArgs.Debug)}')
           pdb.set_trace()
           
        myFactory = UtilsCommon.abstractFactory( myArgs.Module )
        runner    = myFactory( myArgs.Class )
        runner    = runner(**myArgs.__dict__)

        '''
        '''
        logLevel=myEnv.getConfig().get('LOG','level').get('level')
        level = logging.DEBUG
        
        logLevel = logLevel.upper()
        level = logging.getLevelName(logLevel)
        logger.getLog().setLevel(level)
                
        ## params = UtilsCommon.extractCommandLineParams(runner.getParams())
        ## if (None == params) or (None == runner):
        ##   raise Exception("No parameters or runner defined but required")
          
        runner.initialise()
        runner.process()
        runner.finalise()
      except:
        traceback.print_exc()

