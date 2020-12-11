import os, subprocess

from Kernel.Settings.Constants import Constants


class Process:
    def __init__(self,):
        self.ALL_TASKS: list = []


    def Execute(self,Command: str):
        print(Command)
        process = subprocess.Popen(
            Command,
            stdout=subprocess.PIPE,
            stderr=None,
            shell=True
        )

        #self.AddTask(process)

    def TaskExists(self, Task):
        for Tasks in self.ALL_TASKS:
            if Task == Tasks:
                return True
        return False

    def AddTask(self, task):
        if not self.TaskExists(task):
            self.ALL_TASKS.append(task)


    def RemoveTask(self, task):
        if self.TaskExists(task):
            self.ALL_TASKS.remove(task)


    def getAllTasks(self):
        return self.ALL_TASKS

