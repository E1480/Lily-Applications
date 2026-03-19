from src import lily, procKiller, processes
from multiprocessing import Process

if __name__ == "__main__":
    lily = Process(target=lily.Lily)
    procKill = Process(target=procKiller.Prockiller)
    proc = Process(target=processes.ProcTree)

    lily.start()
    procKill.start()
    proc.start()

    lily.join()
    procKill.join()
    proc.join()
    
    