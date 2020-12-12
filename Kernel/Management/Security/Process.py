import os, subprocess, psutil

from Kernel.Management.Security.Constants import Constants


class Process:
    def __init__(self, ):
        self.ALL_TASKS: dict = {}
        self.Command: str = Constants.EMPTY
        self.TITLES: str = Constants.EMPTY

    '''
        THIS FUNCTIONS IS USED TO REMOVE LAST COMMAND AND WINDOW TITLES,
        OTHERWISE LAST COMMAND WILL BE APPENDED TO THE NEW ONE AND THIS COLLISION
        WILL RECREATE PREVIOUS TMUX SPLITS PLUS NEW SPLITS
    '''

    def Reset(self):
        self.Command = Constants.EMPTY
        self.TITLES = Constants.EMPTY

    def Execute(self, Command: str, OPTIONS_ID=None):
        print(Command)
        process = subprocess.Popen(
            Command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        if OPTIONS_ID is not None:
            self.AddTask(process, OPTIONS_ID)
        self.Reset()

    def TaskExists(self, OPTION_ID):
        if OPTION_ID in self.ALL_TASKS.keys():
            return True
        return False

    def AddTask(self, Proc, OPTION_ID):
        if not self.TaskExists(OPTION_ID):
            self.ALL_TASKS[OPTION_ID] = Proc
            return True
        return False

    def RemoveTask(self, OPTION_ID):
        if self.TaskExists(OPTION_ID):
            del self.ALL_TASKS[OPTION_ID]
            return True
        return False

    def getAllTasks(self):
        return self.ALL_TASKS

    def RunSpider(self, CLIENT_IDENTIFIER: str, CLIENT_PASSWORD: str, OPTIONS_ID: str, TOTAL_PROCESS: str) -> int:
        Machines = Constants.EMPTY
        for index in range(int(TOTAL_PROCESS)):
            Machines += Constants.MACHINE_PREFIX+str(index) + Constants.SPACE

        self.Command = Constants.BOT_LAUNCHER.format(os.getcwd(),CLIENT_IDENTIFIER, CLIENT_PASSWORD, OPTIONS_ID, Machines)
        self.Execute(self.Command, OPTIONS_ID)


    def StopSpider(self, OPTIONS_ID):
        if self.TaskExists(OPTIONS_ID):
            pid = self.getAllTasks()[OPTIONS_ID].pid
            print(pid)
            psutil.Process(pid).terminate()
            self.RemoveTask(OPTIONS_ID)
            print(str(self.getAllTasks()))




