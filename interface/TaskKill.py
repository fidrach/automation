from wrapper.ExecutableWrapper import ExecutableWrapper


class TaskKill(ExecutableWrapper):

    def __init__(self, args):
        super(TaskKill, self).__init__(r"C:\Windows\System32", "taskkill.exe", args)