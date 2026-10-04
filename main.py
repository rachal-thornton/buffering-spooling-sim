# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program simulates buffering and spooling in a single use and multi-user system.

# IMPORTS
from reader import read_jobs_file
import time_stamps as t
from job_funcs import *

# MAIN
# Pre: All functions inside main implemented correctly
# Post: Simulates 4 cases 
def main():
   # Print input
    print("INPUT: ")
    t.print_input("jobs.dat")
    print()
    
    # Print output
    print("OUTPUT: ")
    print()
    
    # single_neither()
    my_system, jobs = read_jobs_file("jobs.dat")    # System and job information
    print("SINGLE JOB - NO SPOOLING OR BUFFERING")
    t.print_time_event()
    single_neither(my_system, jobs)                 # Simulate
    t.print_divider()
    
    # single_buff()
    # Read system and job information from jobs.dat
    my_system, jobs = read_jobs_file("jobs.dat")    # System and job information
    print("SINGLE JOB - BUFFERING ONLY")
    t.print_time_event()
    single_buff(my_system, jobs)                    # Simulate
    t.print_divider()
    
    # single_both()
    # Read system and job information from jobs.dat
    my_system, jobs = read_jobs_file("jobs.dat")    # System and job information
    print("SINGLE JOB - SPOOLING AND BUFFERING")
    t.print_time_event()
    single_both(my_system, jobs)                    # Simulate
    t.print_divider()
    
    # multiple_both()
    # Read system and job information from jobs.dat
    my_system, jobs = read_jobs_file("jobs.dat")    # System and job information
    print("MULTIPLE JOBS - SPOOLING AND BUFFERING")
    t.print_time_event()
    multiple_both(my_system, jobs)                  # Simulate
    t.print_divider()

if __name__ == "__main__":
    main()