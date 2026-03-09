
import datetime

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
  
