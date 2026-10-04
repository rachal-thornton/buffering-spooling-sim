# Author: Rachal Thornton
# Class: CS 405
# Date: 10/04/26
# Desc: This program defines a class for a Job.

# CLASSES
# Job class
class Job:
    def __init__(self, name, cpu_bursts, input_data):
        # Job name
        self.name = name

        # CPU burst times
        self.cpu_bursts = cpu_bursts

        # Amount of input requested after each CPU burst
        self.input_data = input_data
