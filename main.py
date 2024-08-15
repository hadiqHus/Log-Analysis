import os
import time
import psutil
import keyboard
import pandas as pd 

def log_process_events():
    log_directory = "C:\\Users\\hadiq\\Desktop\\pythonstuff\\log analysis"
    log_file = os.path.join(log_directory, "process_log.csv")

    # Ensure the log directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    print("Process event logging started. Press 'Esc' to stop.")
    
    # Create a set of current PIDs
    existing_pids = set(psutil.pids())
    
    # DataFrame to store logs
    columns = ["Timestamp", "Event", "PID", "Process Name", "Command Line", "Status"]
    log_df = pd.DataFrame(columns=columns)

    while True:
        # Check if Esc key is pressed
        if keyboard.is_pressed('esc'):
            print("Process event logging stopped.")
            break

        # Get the current set of PIDs
        current_pids = set(psutil.pids())

        # Identify new processes
        new_pids = current_pids - existing_pids
        for pid in new_pids:
            try:
                p = psutil.Process(pid)
                log_entry = {
                    "Timestamp": time.ctime(),
                    "Event": "Started",
                    "PID": pid,
                    "Process Name": p.name(),
                    "Command Line": " ".join(p.cmdline()),
                    "Status": "Success"
                }
            except (psutil.AccessDenied, psutil.NoSuchProcess, PermissionError):
                log_entry = {
                    "Timestamp": time.ctime(),
                    "Event": "Started",
                    "PID": pid,
                    "Process Name": "Access Denied",
                    "Command Line": "Access Denied",
                    "Status": "Denied"
                }
            except Exception as e:
                print(f"Error: {e}")
                continue

            log_df = pd.concat([log_df, pd.DataFrame([log_entry])], ignore_index=True)
            print(f"Logged: {log_entry}")

        # Identify terminated processes
        terminated_pids = existing_pids - current_pids
        for pid in terminated_pids:
            log_entry = {
                "Timestamp": time.ctime(),
                "Event": "Terminated",
                "PID": pid,
                "Process Name": "N/A",
                "Command Line": "N/A",
                "Status": "Success"
            }
            log_df = pd.concat([log_df, pd.DataFrame([log_entry])], ignore_index=True)
            print(f"Logged: {log_entry}")

        # Update the existing PIDs set
        existing_pids = current_pids

        # Save to CSV every 5 seconds
        while True:
            try:
                log_df.to_csv(log_file, index=False)
                break  # Exit the loop once the file is successfully written
            except PermissionError:
                print(f"Permission denied when trying to write to {log_file}. Retrying in 5 seconds...")
                time.sleep(5)  # Wait for 5 seconds before retrying
            except Exception as e:
                print(f"Unexpected error when writing to file: {e}")
                break
        
        time.sleep(5)

if __name__ == "__main__":
    log_process_events()
