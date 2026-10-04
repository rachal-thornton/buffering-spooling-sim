# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program simulates buffering and spooling in a single use and multi-user system.

# IMPORTS
from reader import read_jobs_file
from time_stamps import *
# from job_funcs import *

# MAIN
def main():
    # Read system and job information from jobs.dat
    my_system, jobs = read_jobs_file("jobs.dat")

    # Print input
    print("INPUT: \n")
    print_input("jobs.dat")
    print()
    
    # Print output
    print("OUTPUT: ")
    print()
    
    # single_neither()
    print("SINGLE JOB - NO SPOOLING OR BUFFERING")
    print_divider()
    
    # single_buff()
    print("SINGLE JOB - BUFFERING ONLY")
    print_divider()
    
    # single_both()
    print("SINGLE JOB - SPOOLING AND BUFFERING")
    print_divider()
    
    # multiple_both()
    print("MULTIPLE JOBS - SPOOLING AND BUFFERING")
    print_divider()

if __name__ == "__main__":
    main()