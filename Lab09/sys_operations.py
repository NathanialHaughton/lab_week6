import os
import sys
import platform
import socket
import multiprocessing as mp

# Printing the machine type
print("The system is getting the machine type:", platform.machine())

# Printing the processor type
print("The system is retrieving the processor type:", platform.processor())

# Setting the default socket timeout to 50 seconds
print("The system is setting the default socket timeout to 50 seconds.")
socket.setdefaulttimeout(50)

# Getting the default socket timeout
print("The system is retrieving the default socket timeout:", socket.getdefaulttimeout())

# Getting the operating system name
print("The system is getting the operating system name:", os.name)

# Getting the current process ID
print("The system is fetching the current process ID:", os.getpid())

# Checking if the system supports process forking
if hasattr(os, 'fork'):
    print("The system is forking a new process.")
    pid = os.fork()
    if pid == 0:
        # Running the child process
        print("The child process is running with process ID:", os.getpid())
        os._exit(0)  # Exiting the child process
    else:
        # Waiting for the child process to finish
        print("The parent process is waiting for the child process to finish.")
        os.wait()  # Waiting for child process termination
else:
    print("The system is unable to fork a process because this is not a Unix-based system.")

# Opening (or creating) a file named fdpractice.txt
print("The system is opening (or creating) a file named fdpractice.txt.")
fd = os.open("fdpractice.txt", os.O_RDWR | os.O_CREAT)

# Printing the current process ID
print("The system is printing the current process ID:", os.getpid())

# Writing to the file
print("The system is writing 'Some string to write to the file' to fdpractice.txt.")
os.write(fd, b"Some string to write to the file")  # Writing bytes to the file

# Checking if the system supports forking for file handling
if hasattr(os, 'fork'):
    print("The system is forking a new process for file handling.")
    pid = os.fork()
    if pid == 0:
        # Running the child process and accessing the file
        print("The child process is running and accessing the file.")
        print("The child process ID is:", os.getpid())
        os.lseek(fd, 0, os.SEEK_SET)  # Moving the file pointer to the beginning of the file
        print("The child process is reading the file contents:")
        print(os.read(fd, 100).decode())  # Reading up to 100 bytes and decoding
        print("The child process is closing the file.")
        os.close(fd)  # Closing the file descriptor in the child process
        os._exit(0)  # Exiting the child process
    else:
        # Waiting for the child process to finish
        print("The parent process is waiting for the child to finish.")
        os.wait()  # Waiting for child process termination
        print("The parent process is closing the file.")
        os.close(fd)  # Closing the file descriptor in the parent process
else:
    print("The system is unable to fork a process. Using multiprocessing instead.")
    
    def child_process():
        # Running the child process and accessing the file
        print("The child process is running and accessing the file.")
        print("The child process ID is:", os.getpid())
        with open("fdpractice.txt", "r") as file:
            print("The child process is reading the file contents:")
            print(file.read(100))  # Reading up to 100 bytes from the file
        print("The child process is exiting.")  # Indicating the process is finishing
    
    if __name__ == "__main__":
        # Creating a multiprocessing context with spawn method
        context = mp.get_context("spawn")  
        # Initializing a new process with the child_process function
        p = context.Process(target=child_process)  
        # Starting the new process execution
        p.start()  
        # Waiting for the child process to complete execution  
        p.join()  
        print("The parent process is continuing execution.")
