import  logging
import  os
from datetime import  datetime
import  threading
from  JKTest.readconfig import readconfig
class Log:
    def __init__(self):
        global logPath, resultPath,proDir
        proDir = readconfig.proDir()
        resultPath = os.path.join(proDir,"result")
        # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file name by localtime
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)
class myLog:
    logging = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if myLog.log is None:
            myLog.mutex.acquire()
            myLog.log = Log()
            myLog.mutex.release()

        return myLog.log