from wrapper.ExecutableWrapper import ExecutableWrapper
import os


class DropboxInstaller(ExecutableWrapper):

    def __init__(self):
        installerPath = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "dependency"
        super(DropboxInstaller, self).__init__(installerPath, "DropboxInstaller.exe", ["/S"])