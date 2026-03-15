from .processes import ProcTree
from .lily import Lily
from .procKiller import Prockiller

from multiprocessing import Process

if __name__ == "__main__":
    lily = Process(target=Lily)
    procKill = Process(target=Prockiller)
    proc = Process(target=ProcTree)

    lily.start()
    procKill.start()
    proc.start()

    lily.join()
    procKill.join()
    proc.join()
    
    