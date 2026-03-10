
import importlib
import traceback
import argparse
import inspect
import pdb
import logging

class UtilsCommon:
    
  @staticmethod
  def collapsePairListToDictionary(somelist):
      unkownArgs = {somelist[i]: somelist[i + 1] for i in range(0, len(somelist), 2)}
      return unkownArgs

  @staticmethod
  def MainModule():
      from utils.src import SystemUtils, LoggingUtils      
      runner = None
      myArgs = None
  
      try:
        ''' SystemUtils() must be constructed first for all config information
        '''
        myEnv     = SystemUtils()        
        logger    = LoggingUtils()
        
        arguments= myEnv.getConfig().get('arguments')          
        parser=argparse.ArgumentParser(description="")
        for arg in arguments:
          parser.add_argument(f'--{arg}')
        
        myArgs, unkown = parser.parse_known_args()
        unkownArgs = UtilsCommon.collapsePairListToDictionary(unkown)
        if 0 != int(myArgs.Debug):
           print(f'starting debug {myArgs.Debug} {type(myArgs.Debug)}')
           pdb.set_trace()
              
        myArgs.__dict__.update(unkownArgs)
        myFactory = UtilsCommon.abstractFactory( myArgs.Module )
        runner    = myFactory( myArgs.Class )
        runner    = runner(**myArgs.__dict__)

        logLevel=myEnv.getConfig().get('LOG','level').get('level')       
        logLevel = logLevel.upper()
        level = logging.getLevelName(logLevel)
        logger.getLog().setLevel(level)
                          
        runner.initialise()
        runner.process()
        runner.finalise()
      except:
        traceback.print_exc()    
        
  
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




