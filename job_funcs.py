# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program handles all job functions needed to simulate all cases of buffering and/or spooling.

# IMPORTS
import time_stamps as t

# CONSTANTS
CODE_SIZE = 200
INPUT_SIZE = 100

# FUNCTIONS
# single_neither(my_system, my_jobs): simulates a single job on a system with no buffering or spooling
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def single_neither(my_system, my_jobs):
    curr_time = 0       # Current time
    usr_time = 0        # User time

    # Simulate for each job in the list
    for job in my_jobs:
        # Identify current job number
        job_num = job.name

        # Transfer job code from tape to disk
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_tape_to_disk_code(curr_time, job_num)
            curr_time += my_system.tape_to_disk_time(my_system.tape_block_size)
            code_rem_space -= my_system.tape_block_size

        t.print_code_storage(curr_time, job_num)
        print()

        # Transfer job code from disk to memory
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_disk_to_mem_code(curr_time, job_num)
            curr_time += my_system.disk_to_mem_time(my_system.disk_block_size)
            code_rem_space -= my_system.disk_block_size

        t.print_code_mem(curr_time, job_num)
        print()
        
        # Execution for each CPU burst
        for i, cpu_burst in enumerate(job.cpu_bursts):
            # Print starting execution only if first CPU burst
            if i == 0:
                t.print_exec_start(curr_time, job_num)
            
            curr_time += cpu_burst
            usr_time += cpu_burst

            # Check for input after CPU burst
            if i < len(job.input_data):
                input_amount = job.input_data[i]

                # Check input capacity
                if input_amount > my_system.input_size:
                    print(f"ERROR: Job {job_num} requests {input_amount} units, "
                          f"which exceeds the input size capacity of {my_system.input_size} units.")
                    return
                
                # Job needs data
                t.print_need_data(curr_time, job_num)
                print()

                # Transfer input data from tape to disk
                if i == 0:
                    input_rem = input_amount

                    while input_rem > 0:
                        t.print_tape_to_disk_data(curr_time, job_num)
                        curr_time += my_system.tape_to_disk_time(my_system.tape_block_size)
                        input_rem -= my_system.tape_block_size

                    t.print_data_storage(curr_time, job_num)
                    print()

                # Transfer input data from disk to memory
                input_rem = input_amount

                while input_rem > 0:
                    t.print_disk_to_mem_data(curr_time, job_num)
                    curr_time += my_system.disk_to_mem_time(my_system.disk_block_size)
                    input_rem -= my_system.disk_block_size

                # Input buffer full
                t.print_input_buffer_full(curr_time, job_num)
                print()

                # Continue job
                t.print_continue_job(curr_time, job_num)
                print()
            
        # Current job is complete
        t.print_job_done(curr_time, job_num)
        print()

    # All jobs are complete, summary of time
    t.print_all_jobs_done(curr_time)
    print() 

    system_time = curr_time - usr_time
    t.print_summary(curr_time, usr_time, system_time)

# single_buff(my_system, my_jobs): simulates a single job on a system with only buffering
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation
def single_buff(my_system, my_jobs):
    curr_time = 0       # Current time
    usr_time = 0        # User time

    # Simulate for each job in the list
    for job in my_jobs:
        # Identify current job number
        job_num = job.name

        # Transfer job code from tape to disk
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_tape_to_disk_code(curr_time, job_num)
            curr_time += my_system.tape_to_disk_time(my_system.tape_block_size)
            code_rem_space -= my_system.tape_block_size

        t.print_code_storage(curr_time, job_num)
        print()

        # Transfer job code from disk to memory
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_disk_to_mem_code(curr_time, job_num)
            curr_time += my_system.disk_to_mem_time(my_system.disk_block_size)
            code_rem_space -= my_system.disk_block_size

        t.print_code_mem(curr_time, job_num)
        print()

        # Start executing job
        t.print_exec_start(curr_time, job_num)
        cpu_time = curr_time

        # Execute CPU bursts
        for i, cpu_burst in enumerate(job.cpu_bursts):

            # Buffer input needed after this CPU burst
            if i < len(job.input_data):
                input_amount = job.input_data[i]

                # Check input capacity
                if input_amount > my_system.input_size:
                    print(
                        f"ERROR: Job {job_num} requests {input_amount} units, "
                        f"which exceeds the input size capacity of {my_system.input_size} units."
                    )
                    return

                input_time = cpu_time
                input_rem = input_amount

                # First input, transfer from tape to disk
                if i == 0:

                    while input_rem > 0:
                        t.print_tape_to_disk_data(input_time, job_num)
                        input_time += my_system.tape_to_disk_time(my_system.tape_block_size)
                        input_rem -= my_system.tape_block_size

                    t.print_data_storage(input_time, job_num)
                    print()

                # Transfer input from disk to memory/buffer
                input_rem = input_amount

                while input_rem > 0:
                    t.print_disk_to_mem_data(input_time, job_num)
                    input_time += my_system.disk_to_mem_time(my_system.disk_block_size)
                    input_rem -= my_system.disk_block_size

                t.print_input_buffer_full(input_time, job_num)
                print()

            # Execute CPU bursts
            cpu_time += cpu_burst
            usr_time += cpu_burst

            # Job needs input after this CPU burst
            if i < len(job.input_data):
                t.print_need_data(cpu_time, job_num)
                print()
                # Input already buffered
                t.print_continue_job(cpu_time, job_num)
                print()
        
        curr_time = cpu_time

        # Job complete
        t.print_job_done(curr_time, job_num)
        print()

    # All jobs complete, summary
    t.print_all_jobs_done(curr_time)
    print()

    system_time = curr_time - usr_time
    t.print_summary(curr_time, usr_time, system_time)


# single_both(my_system, my_jobs): simulates a single job with both spooling and buffering
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def single_both(my_system, my_jobs):
    curr_time = 0   # Current time
    usr_time = 0    # User time

    tape_time = 0   # Tape time shows when tape available
    disk_time = 0   # Disk time shows when disk available

    code_ready = {} # Job's code reaches disk
    data_ready = {} # Job's input data reaches disk

    # Spool all jobs from tape to disk
    for job in my_jobs:
        job_num = job.name

        # Transfer job code from tape to disk
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_tape_to_disk_code(tape_time, job_num)
            tape_time += my_system.tape_to_disk_time(my_system.tape_block_size)
            code_rem_space -= my_system.tape_block_size

        t.print_code_storage(tape_time, job_num)
        print()
        code_ready[job_num] = tape_time

        # Transfer job input data from tape to disk
        data_ready[job_num] = []

        for input_amount in job.input_data:
            input_rem = input_amount

            while input_rem > 0:
                t.print_tape_to_disk_data(tape_time, job_num)
                tape_time += my_system.tape_to_disk_time(my_system.tape_block_size)
                input_rem -= my_system.tape_block_size

            t.print_data_storage(tape_time, job_num)
            print()
            data_ready[job_num].append(tape_time)

    # Execute jobs
    for job in my_jobs:
        job_num = job.name

        # Wait until job code on disk
        curr_time = max(curr_time, code_ready[job_num])

        # Transfer job code from disk to memory
        disk_time = max(disk_time, curr_time)
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_disk_to_mem_code(disk_time, job_num)
            disk_time += my_system.disk_to_mem_time(my_system.disk_block_size)
            code_rem_space -= my_system.disk_block_size

        curr_time = disk_time
        t.print_code_mem(curr_time, job_num)
        print()

        # Start executing job
        t.print_exec_start(curr_time, job_num)
        print()
        cpu_time = curr_time

        # Execute CPU bursts
        for i, cpu_burst in enumerate(job.cpu_bursts):
            cpu_time += cpu_burst
            usr_time += cpu_burst

            # Check if job needs input data
            if i < len(job.input_data):
                input_amount = job.input_data[i]

                # Check input capacity
                if input_amount > my_system.input_size:
                    print(f"ERROR: Job {job_num} requests {input_amount} units, "
                          f" which exceeds the input size capacity of {my_system.input_size} units.")

                    return

                # Job needs data
                t.print_need_data(cpu_time, job_num)
                print()

                # Determine when requested data is available
                input_time = max(disk_time, data_ready[job_num][i])

                # Transfer input data from disk to memory/buffer
                input_rem = input_amount

                while input_rem > 0:
                    t.print_disk_to_mem_data(input_time, job_num)
                    input_time += my_system.disk_to_mem_time(my_system.disk_block_size)
                    input_rem -= my_system.disk_block_size

                disk_time = input_time
                t.print_input_buffer_full(input_time, job_num)
                print()

                # Resume job when CPU and inmput are ready
                cpu_time = max(cpu_time, input_time)
                t.print_continue_job(cpu_time, job_num)
                print()

        curr_time = cpu_time

        # Job complete
        t.print_job_done(curr_time, job_num)
        print()

    # All jobs complete, summary
    curr_time = max(curr_time, disk_time, tape_time)
    t.print_all_jobs_done(curr_time)
    print()

    system_time = curr_time - usr_time
    t.print_summary(curr_time, usr_time, system_time)


# multiple_both(my_system, my_jobs): simulates multiple jobs with both spooling and buffering
# Pre: a System object and list of Job objects are initialized
# Post: printed out simulation 
def multiple_both(my_system, my_jobs):
    curr_time = 0   # Current time
    usr_time = 0    # User time

    tape_time = 0   # Tape time shows when tape available
    disk_time = 0   # Disk time shows when disk available

    code_ready = {} # Job's code reaches disk
    data_ready = {} # Job's input data reaches disk

    code_loaded = {} # Job's code in memory

    # Job tracking
    for job in my_jobs:
        code_ready[job.name] = None
        data_ready[job.name] = [None] * len(job.input_data)
        code_loaded[job.name] = None

    # Empty job list
    if not my_jobs:
        t.print_all_jobs_done(0)
        t.print_summary(0, 0, 0)
        return

    # Process each job
    for i, job in enumerate(my_jobs):
        job_num = job.name

        # Transfer job code from tape to disk
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_tape_to_disk_code(tape_time, job_num)
            tape_time += my_system.tape_to_disk_time(my_system.tape_block_size)
            code_rem_space -= my_system.tape_block_size

        t.print_code_storage(tape_time, job_num)
        print()
        code_ready[job_num] = tape_time

        # Transfer code from disk to memory
        disk_time = max(disk_time, code_ready[job_num])
        code_rem_space = CODE_SIZE

        while code_rem_space > 0:
            t.print_disk_to_mem_code(disk_time, job_num)
            disk_time += my_system.disk_to_mem_time(my_system.disk_block_size)
            code_rem_space -= my_system.disk_block_size

        code_loaded[job_num] = disk_time
        t.print_code_mem(disk_time, job_num)
        print()

        # Start executing job
        curr_time = max(curr_time, disk_time)
        t.print_exec_start(curr_time, job_num)
        print()

        # Execute CPU bursts and handle input data
        for i, cpu_burst in enumerate(job.cpu_bursts):
            curr_time += cpu_burst
            usr_time += cpu_burst

            # Check for input data
            if i < len(job.input_data):
                input_amount = job.input_data[i]

                # Check input capacity
                if input_amount > my_system.input_size:
                    print(f"ERROR: Job {job_num} requests {input_amount} units, "
                        f" which exceeds the input size capacity of {my_system.input_size} units.") 
                    
                    return

                # Job needs data
                t.print_need_data(curr_time, job_num)
                print()

                # Transfer input data from tape to disk
                input_rem = input_amount

                while input_rem > 0:
                    t.print_tape_to_disk_data(tape_time, job_num)
                    tape_time += my_system.tape_to_disk_time(my_system.tape_block_size)
                    input_rem -= my_system.tape_block_size

                t.print_data_storage(tape_time, job_num)
                print()
                data_ready[job_num][i] = tape_time

                # Transfer input data from disk to memory
                disk_time = max(disk_time, data_ready[job_num][i])
                input_rem = input_amount

                while input_rem > 0:
                    t.print_disk_to_mem_data(disk_time, job_num)
                    disk_time += my_system.disk_to_mem_time(my_system.disk_block_size)
                    input_rem -= my_system.disk_block_size

                t.print_input_buffer_full(disk_time, job_num)
                print()

                # Continue execution when input available
                curr_time = max(curr_time, disk_time)
                t.print_continue_job(curr_time, job_num)
                print()

        # Job finished
        t.print_job_done(curr_time, job_num)
        print()

    # All jobs finished and summary
    curr_time = max(curr_time, tape_time, disk_time)
    t.print_all_jobs_done(curr_time)
    print()

    system_time = curr_time - usr_time
    t.print_summary(curr_time, usr_time, system_time)

                