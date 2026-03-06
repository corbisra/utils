

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
   def getMonthLastBusinessDate(input=30.04.2023'):
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
      for key in dir(moduleName):
        if isinstance( getattr(thisModule, key), type ):
          if key ==classname:
            newClass=getattr(thisModule, key)
            return newClass()
      raise Exception(moduleName+"Package has no known Class : "+ classname)    
    
    return createObject

   @staticmethod
   def extractCommandLinParams(params):
    try:
       args=balmutils.BALMArgsèarser(params)
       args.initialise()
       args.parseCommandline()
       params= params(**args.requiredArgs())
    except:
        traceback.print_exc()
    finally: pass
  
    return params

   @staticmethod
   def loadUtilsModuleFunction(modulename, funcname):
     functionToCall = None
     module = importlib.import_module(modulename)
     if module.__name__ = getattr(module, funcname)
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
      runSystemBootstrap()
  
      runner = None
      myArgs = None
  
      try:
        myEnv=balmutils.SystemUtils()

        parser=argparse.ArgumentParser(description="")
        parser.addArgument(str('--Module'), type=str)
        parser.addArgument(str('--Class'), type=str)
        parser.addArgument(str('--Debug'), type=int, default=0)
        
        myArgs, unkown=parser.parse_known_args()
        myFactory =balmutils.abstractFactory( myArgs.Module )
        runner = myFactory( myArgs.Class )
        
        if 0 != myArgs.Debug:
           pdb.set_trace()
 
        logLevel=myUtils.SystemUtils().getConfig().get('LOG','level')
        level = logging.DEBUG
      
        logLevel = logLevel.upper()
        level = logging.getLevelName(logLevel)
        myUtils.LoggingUtils().getLog.setLevel(level)         
        params = myUtils.extactCommandLineParams(runner.getParams())
        if (None == params) or (None == runner):
          raise Exception("No parameters or runner defined but required")
          
        runner.initialise(params)
        runner.processing(params)
        runner.finalise(params)
      except:
        traceback.print_exc()
    