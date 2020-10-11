import  gc
class Memory:
    def Free(self, object):
        object = None
        gc.collect()
        gc.garbage[:]