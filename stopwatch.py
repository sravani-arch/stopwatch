import time

def stopwatch():
    print("Press Enter to start the stopwatch, and press Enter again to stop it.")
    input()  # Wait for user to press Enter to start
    start_time = time.time()  # Record the start time
    
    input()  # Wait for user to press Enter to stop
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

stopwatch()
