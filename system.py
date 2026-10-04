# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program defines a class for a System.

# CLASSES
# System class
class System:
    def __init__(
            self,
            tape_block_size,
            tape_transfer_time,
            disk_size,
            disk_block_size,
            disk_transfer_time,
            memory_size,
            input_size,
            buffer_size):

        # Tape to disk
        self.tape_block_size = tape_block_size
        self.tape_transfer_time = tape_transfer_time
        
        # Disk size
        self.disk_size = disk_size

        # Disk to memory
        self.disk_block_size = disk_block_size
        self.disk_transfer_time = disk_transfer_time
        
        # Memory size
        self.memory_size = memory_size
        
        # Job input size
        self.input_size = input_size

        # Buffer size
        self.buffer_size = buffer_size
