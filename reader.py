# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program acts as a reader for a file containing system/job information.

# IMPORTS
from system import System
from job import Job

# FUNCTIONS
# read_jobs_file(filename): takes in a file to read line by line for system and jobs information
# Pre: jobs file passed in with expected formatting
# Post: creates a System object and a list of Job objects
def read_jobs_file(filename):
    with open(filename, "r") as file:
        # Block size for transfer from tape to disk (chunks/units)
        tape_block_size, tape_transfer_time = map(int, file.readline().split())
        # Size of disk (units)
        disk_size = int(file.readline())
        # Block size for transfer from disk to memory (chunks/units)
        disk_block_size, disk_transfer_time = map(int, file.readline().split())
        # Size of memory (units)
        memory_size = int(file.readline())
        # Size of input space for jobs (units)
        input_size = int(file.readline())
        # Size of buffer (units)
        buffer_size = int(file.readline())

        # Create a System object
        my_system = System(
            tape_block_size,
            tape_transfer_time,
            disk_size,
            disk_block_size,
            disk_transfer_time,
            memory_size,
            input_size,
            buffer_size
        )

        # Store jobs in a list
        jobs = []

        # Read remaining lines as jobs
        for line in file:
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Split line into parts for job info
            parts = line.split()

            job_name = parts[0]                 # Job name is first value
            values = list(map(int, parts[1:]))  # Remaining values are CPU/input data
            cpu_bursts = values[::2]            # CPU values at even indexes
            input_data = values[1::2]           # Input data at odd indexes

            # Create a Job object
            my_job = Job(
                job_name,
                cpu_bursts,
                input_data
            )

            # Add myJob object to list of jobs
            jobs.append(my_job)
            
        # Return mySystem and jobs
        return my_system, jobs

