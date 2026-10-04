# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program handles all job functions needed to simulate all cases of buffering and/or spooling.

# IMPORTS
from time_stamps import *
from system import System 
from job import Job

# FUNCTIONS
# single_neither(my_system, my_jobs): simulates a single job on a system with no buffering or spooling
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def single_neither(my_system, my_jobs):
    single_neither_time = 0     # Variable to hold total overall time
    single_neither_usr_job = 0  # Variable to hold only total user job time

    # Simulate for each job in the list
    for job in my_jobs:
        # Transfer tape to disk
        # Transfer disk to memory
        # Start execution
    # Summary of time

# single_buff(my_system, my_jobs): simulates a single job on a system with only buffering
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def single_buff():
    single_buff_time = 0

# single_both(my_system, my_jobs): simulates a single job with both spooling and buffering
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def single_both():
    single_both_time = 0

# multiple_both(my_system, my_jobs): simulates multiple jobs with both spooling and buffering
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def multiple_both():
    multiple_both_time = 0
