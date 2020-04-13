import glob,os
import datetime
import shutil




class Files:

    def __init__(self,folder):
        self.folder = folder
        os.chdir(f'M:\\{self.folder}\\scan')
        self.scanFiles = [{"location": str(os.getcwd() + "\\" + _f), "fileName": _f} for _f in glob.glob("*")]


    @property
    def toError(self):
        return f"M:\\{self.folder}\\error"

    def Move(self,dst,fileName,folderType):
        dir = self.__createDir(f"M:\\{self.folder}\\{folderType}\\")
        tgt = dir+"\\"+fileName
        shutil.move(dst,tgt)

    def __createDir(self,dir):
        dirName = dir+str(datetime.date.today()).replace("-","")
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            return dirName
        return dirName



