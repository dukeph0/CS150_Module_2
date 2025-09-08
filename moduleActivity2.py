# Purpose: Develop a Python program that analyzes and displays components of active system processes. This type of program is critical for optimizing
# application performance, ensuring system stability, and improving overall efficieny in real-world programming environments.

# Expected Result: The program should display the running processes and information for each process, such as the process id and process name.

# reference: https://psutil.readthedocs.io/en/latest/#

# Version   Author      Date            Description
# 1         Duke Pham   2025-Sep-07     Display running processes

# use required import 
import psutil
import time

def displayAllRunningProcesses():

    # add a wait to get a better reading on running processes
    time.sleep(1)

    print("Analyzing Active System Processes......")
    print("-" * 100)

    # iterate through all the running processes and search for process id and name
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
        try:

            # get all requested data
            processInfo = proc.info

            # extract data to be displayed
            processId = processInfo['pid']
            processName = processInfo['name']
            status = processInfo['status']
            cpuPercent = processInfo['cpu_percent']
            memoryPercent = processInfo['memory_percent']

            # filter for only running processes 
            if status in [psutil.STATUS_RUNNING]:

                # Display analyzed data in a human readable format
                print(f"Process: {processName} (PID: {processId})")
                print(f"    Status:  {status}")
                print(f"    CPU Usage: {cpuPercent:.10f}%")
                print(f"    Memory Usage: {memoryPercent:.10f}%")
                print("-" * 100)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # have a handler for processes that may have been terminated or are inaccessible
            continue

if __name__ == "__main__":
    displayAllRunningProcesses()