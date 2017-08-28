from wrapper.ExecutableWrapper import ExecutableWrapper
import os


class DropboxUninstaller(ExecutableWrapper):

    def __init__(self):
        self.executablePath = r"C:\Program Files (x86)\Dropbox\Client"
        super(DropboxUninstaller, self).__init__(self.executablePath, "DropboxUninstaller.exe", ["/S"])

    def checkDelete(self):
        if os.path.exists(self.executablePath):
            print("DEBUG: Dropbox is still installed")
            return False
        else:
            print("DEBUG: Dropbox has been deleted")
            return True