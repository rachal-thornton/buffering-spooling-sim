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
    print(f"{time}:\t\t TAPE to DISK transfer - CODE for JOB {job_num}")

# print_code_storage(time, job_num): print time when code for specific job is in storage
def print_code_storage(time, job_num):
    print(f"{time}:\t\t CODE for JOB {job_num} in STORAGE")

# print_disk_to_mem_code(time_job_num): print time for disk to memory transfer for specific job code
def print_disk_to_mem_code(time, job_num):
    print(f"{time}:\t\t DISK to MEMORY transfer - CODE for JOB {job_num}")

# print_code_mem(time, job_num): print time when code for specific job is in memory
def print_code_mem(time, job_num):
    print(f"{time}:\t\t CODE for JOB {job_num} in MEMORY")

# print_exec_start(time, job_num): print time when execution for specific job starts
def print_exec_start(time, job_num):
    print(f"{time}:\t\t START EXECUTION for JOB {job_num}")

# print_need_data(time, job_num): print time when data is needed for specific job
def print_need_data(time, job_num):
    print(f"{time}:\t\t NEED DATA for JOB {job_num}")

# print_tape_to_disk_data(time, job_num): print time for tape to disk transfer for specifc job data
def print_tape_to_disk_data(time, job_num):
    print(f"{time}:\t\t TAPE to DISK transfer - DATA for JOB {job_num}")

# print_data_storage(time, job_num): print time data for specific job is in storage
def print_data_storage(time, job_num):
    print(f"{time}:\t\t DATA for JOB {job_num} in STORAGE")

# print_disk_to_mem_data(time, job_num): print time for disk to memory transfer for data
def print_disk_to_mem_data(time, job_num):
    print(f"{time}:\t\t DISK to MEMORY transfer - DATA for JOB {job_num}")

# print_input_buffer_full(time): print time when input buffer is full
def print_input_buffer_full(time):
    print(f"{time}:\t\t INPUT BUFFER FULL")

# print_continue_job(time, job_num): print time when job is continued
def print_continue_job(time, job_num):
    print(f"{time}:\t\t CONTINUE JOB {job_num}")

# print_job_done(time, job_num): print time when specific jobs done
def print_job_done(time, job_num):
    print(f"{time}:\t\t JOB {job_num} DONE")

# print_all_jobs_done(time): print time when all jobs done
def print_all_jobs_done(time):
    print(f"{time}:\t\t ALL JOBS DONE")

# print_summary(total_time, user_time, system_time): print total time needed for completion, user time, and system time
def print_summary(total_time, user_time, system_time):
    print(f"{total_time}:\t\t TOTAL TIME to EXECUTE ALL JOBS")
    print(f"{user_time}:\t\t TIME to EXECUTE USER JOBS")
    print(f"{system_time}:\t\t TIME spent by SYSTEM")