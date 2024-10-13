def round_robin_scheduling(processes, quantum):
    """This code implements round robin scheduling algorithm
    Modified by: Iram Hasan, ID: 20127302
    """

    n = len(processes)
    rem_burst_times = [p[1] for p in processes]  # Remaining burst times for processes
    waiting_time = [0] * n  # Initialize waiting times
    turnaround_time = [0] * n  # Initialize turnaround times
    t = 0  # Current time
    order = []  # To track the order of execution

    context_switches = 0  # Track the number of context switches

    while any(rem_burst_times[i] > 0 for i in range(n)):  # While there are processes left to execute
        for i in range(n):
            if rem_burst_times[i] > 0:
                process_executed = False  # Track if the process was executed in this cycle
                
                if rem_burst_times[i] > quantum:
                    # Process runs for quantum time
                    t += quantum
                    rem_burst_times[i] -= quantum
                    process_executed = True
                    order.append((processes[i][0], quantum))  # Track the execution order
                
                else:
                    # Process finishes execution
                    t += rem_burst_times[i]
                    waiting_time[i] = t - processes[i][1]
                    order.append((processes[i][0], rem_burst_times[i]))  # Track the execution order
                    rem_burst_times[i] = 0
                    process_executed = True

                if process_executed:
                    print(f"Process {processes[i][0]} executed for {order[-1][1]} units")
                    context_switches += 1  # Increment context switches for each execution

    # Calculate turnaround times
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    # Calculate average times
    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    # Display results
    print("\nProcess ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting}")
    print(f"Average Turnaround Time: {avg_turnaround}")

    # Print execution order and number of context switches
    print("\nExecution Order (Process ID, Time Units):")
    for p_id, units in order:
        print(f"Process {p_id} executed for {units} units")

    print(f"\nTotal Context Switches: {context_switches}")

if __name__ == '__main__':
    # List of processes [process_id, burst_time]
    processes = [[1, 10], [2, 1], [3, 2], [4, 1], [5, 5]]

    while True:  # NOTE: Repeated execution loop
        # NOTE: Get time quantum from user input
        quantum = int(input("\nEnter the time quantum: "))
        
        # Execute the round robin scheduling algorithm
        round_robin_scheduling(processes, quantum)

        # NOTE: Ask the user if they want to continue or exit
        cont = input("Do you want to continue? (Y to repeat, any other key to exit): ").strip().upper()
        if cont != 'Y':
            print("Exit")
            break
