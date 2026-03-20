""" 
Main entry point for the Lily-Applications multi-process application.

This module orchestrates three concurrent processes:
- Lily: The primary application process
- Prockiller: A process monitoring and termination handler
- ProcTree: A process tree manager

All processes are started and run concurrently, with the main thread
waiting for all child processes to complete before exiting.

Requires:
    - src.lily: Lily application module
    - src.procKiller: Process killer module
    - src.processes: Process tree management module
"""


from src import lily, procKiller, processes
from multiprocessing import Process

if __name__ == "__main__":
    
    # Create Proecesses
    lily = Process(target=lily.Lily)
    procKill = Process(target=procKiller.Prockiller)
    proc = Process(target=processes.ProcTree)

    # Start Proecesses
    lily.start()
    procKill.start()
    proc.start()

    # Wait untill Proecesses dies
    lily.join()
    procKill.join()
    proc.join()
    
    