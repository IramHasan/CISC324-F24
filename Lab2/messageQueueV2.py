from multiprocessing import Process, Queue
import time

"""
This program demonstrates IPC via message queue with multiple child processes.
Student Last name and ID:  
Hasan
20127302
"""

def childProcess(q, child_id, num_messages):
    """
    A Child process sends multiple messages to the message queue, q.
    """
    for i in range(num_messages):
        msg = f"Message {i+1} from Child {child_id}"
        q.put(msg)  # Put the message in the queue
        time.sleep(0.5)  # Simulate some work

def parentProcess(num_children, num_messages_per_child):
    """
    The parent process creates multiple child processes and receives messages from them.
    """
    q = Queue()  # Creating a shared message queue

    # Create and start child processes
    children = []
    for i in range(num_children):
        p = Process(target=childProcess, args=(q, i+1, num_messages_per_child))
        p.start()
        children.append(p)

    # Receive messages from the child processes
    total_messages = num_children * num_messages_per_child
    for _ in range(total_messages):
        msg = q.get()  # Get a message from the queue
        print("Received:", msg)

    # Wait for all child processes to finish
    for p in children:
        p.join()

if __name__ == '__main__':
    # Print your name and ID
    print("Hi, this is Iram Hasan and 20127302")

    # Define the number of child processes and messages per child
    num_children = 3  # Adjust as needed
    num_messages_per_child = 2  # Adjust as needed

    # Run the parent process with the specified number of children and messages
    parentProcess(num_children, num_messages_per_child)
