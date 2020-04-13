import datetime
from  connection import DB

def logger(fn):
    def inner(*args,**kwargs):
        start = datetime.datetime.now()
        output = fn(*args,**kwargs)
        toLog = Log(fn.__name__, output)
        toLog.writeToLog()
        print (output, datetime.datetime.now() - start)
    return inner




class Log(DB):

    def __init__(self,process_name,info,error=None):
        super(Log,self).__init__()
        self.process_name  = process_name
        self.info = str(info)
        self.error = repr(error)


    def writeToLog(self):
        insert = f"""
         insert into [stg].[process_log] ([process_name],[creation_date],[info],[error])
         values (?,getdate(),?,?)
        """
        data=(self.process_name,self.info,self.error)
        self.execQueryParams(insert,data)

