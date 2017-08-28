import subprocess
import os

class ExecutableWrapperException(Exception):
    """ Standard ExecutableWrapper exception """
    pass

class ExecutableWrapper(object):

    def __init__(self, executablePath, executableName, args=None):
        self.executablePath = os.path.abspath(executablePath)
        self.executableName = executableName
        self.args = args
        self.__stdout = None
        self.__stderr = None
        self.__returnCode = None
        self.executableFilePath = None

        if self.executableName is not None and self.executablePath is not None:
            self.executableFilePath = os.path.join(self.executablePath, self.executableName)
        else:
            raise ExecutableWrapperException("Path: {} or Executable Name: {} was set to None".format(self.executablePath, self.executableName))

    def run(self):
        command = [self.executableFilePath]
        if self.args is not None:
            command = command + self.args
        p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.__stdout, self.__stderr = p.communicate()
        self.__returnCode = p.returncode

        if self.__returnCode != 0:
            raise ExecutableWrapperException("Return Code: {}. Program failed to execute".format(self.__returnCode))

    def getStdout(self):
        return self.__stdout

    def getStderr(self):
        return self.__stderr

    def getReturnCode(self):
        return self.__returnCode