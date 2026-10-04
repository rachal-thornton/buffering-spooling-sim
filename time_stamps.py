# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program holds several helper functions to generate timestamps for jobFuncs.py.

# FUNCTIONS
# print_input(filename): takes in a file to read and print line by line
def print_input(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')  # Prevent double spacing
        print() # Line break

# print_divider(): print a line to break up blocks of text
def print_divider():
    print("-" * 70)

# print_time_event(): print time and event header
def print_time_event():
    print(f"TIME\t\t EVENT")

# print_tape_to_disk_code(time, job_num): print time for tape to disk transfer for specific job code
def print_tape_to_disk_code(time, job_num):
    print(f"{time}:\t\t tape to disk transfer - code for job '{job_num}'")

# print_code_storage(time, job_num): print time when code for specific job is in storage
def print_code_storage(time, job_num):
    print(f"{time}:\t\t code for job '{job_num}' in storage")

# print_disk_to_mem_code(time_job_num): print time for disk to memory transfer for specific job code
def print_disk_to_mem_code(time, job_num):
    print(f"{time}:\t\t disk to memory transfer - code for job '{job_num}'")

# print_code_mem(time, job_num): print time when code for specific job is in memory
def print_code_mem(time, job_num):
    print(f"{time}:\t\t code for job '{job_num}' in memory")

# print_exec_start(time, job_num): print time when execution for specific job starts
def print_exec_start(time, job_num):
    print(f"{time}:\t\t start execution for job '{job_num}'")

# print_need_data(time, job_num): print time when data is needed for specific job
def print_need_data(time, job_num):
    print(f"{time}:\t\t need data for job '{job_num}'")

# print_tape_to_disk_data(time, job_num): print time for tape to disk transfer for specifc job data
def print_tape_to_disk_data(time, job_num):
    print(f"{time}:\t\t tape to disk transfer - data for job '{job_num}'")

# print_data_storage(time, job_num): print time data for specific job is in storage
def print_data_storage(time, job_num):
    print(f"{time}:\t\t data for job '{job_num}' in storage")

# print_disk_to_mem_data(time, job_num): print time for disk to memory transfer for data
def print_disk_to_mem_data(time, job_num):
    print(f"{time}:\t\t disk to memory transfer - data for job '{job_num}'")

# print_input_buffer_full(time): print time when input buffer is full
def print_input_buffer_full(time, job_num):
    print(f"{time}:\t\t input buffer full for job '{job_num}'")

# print_continue_job(time, job_num): print time when job is continued
def print_continue_job(time, job_num):
    print(f"{time}:\t\t continue job '{job_num}'")

# print_job_done(time, job_num): print time when specific jobs done
def print_job_done(time, job_num):
    print(f"{time}:\t\t job '{job_num}' done")

# print_all_jobs_done(time): print time when all jobs done
def print_all_jobs_done(time):
    print(f"{time}:\t\t all jobs done")

# print_summary(total_time, user_time, system_time): print total time needed for completion, user time, and system time
def print_summary(total_time, user_time, system_time):
    print("SUMMARY: ")
    print(f"{total_time}:\t\t total time to execute all jobs")
    print(f"{user_time}:\t\t time spent executing user jobs")
    print(f"{system_time}:\t\t time spent by system")