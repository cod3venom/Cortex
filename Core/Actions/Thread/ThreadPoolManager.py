import time
from concurrent.futures.thread import ThreadPoolExecutor
from Core.Security.Global import AppendToFactory, ClearFactory, GetFactory


class ThreadPoolManager:

    def __init__(self, total_process_number: str, target_function):
        self.total_process_number = int(total_process_number)
        self.target_function = target_function

    def Run(self) -> list:
        pass
