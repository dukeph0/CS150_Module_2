# Purpose: Use Python module psutil to display the running processes and information for each process, such as the process id and process name. 

# Expected Result: The program should display the running processes and information for each process, such as the process id and process name.

# reference: https://psutil.readthedocs.io/en/latest/#

# Version   Author      Date            Description
# 1         Duke Pham   2025-Sep-07     Display running processes

# use required import 
import psutil
import time

def displayAllRunningProcesses():

    # iterate through all the running processes and search for process id and name
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):

        # get all requested data
        processInfo = proc.info

        # extract data for status
        status = processInfo['status']

        # filter for only running processes 
        if status in [psutil.STATUS_RUNNING]:
            print(proc.info)

if __name__ == "__main__":
    displayAllRunningProcesses()