import psutil 
# process id
# process name

def display_all_running_processess():
    for proc in psutil.process_iter(['pid', 'name']):
        process_info = proc.info
        pid = process_info['pid']
        name = process_info['name']
        print(f"PID: {pid}")
        print(f"name: {name}")
        print(f"--------------")

if __name__ == "__main__":
    display_all_running_processess()