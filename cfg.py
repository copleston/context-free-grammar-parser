from pprint import pprint

read_data = 0

def read_cfg(input_file):
    global read_data   # Increase the scop of read_data variable
    with open(input_file, 'r') as f:
        read_data = f.readlines()

cfg = {
    "variables": ,
    "terminals": ,
    "rules": ,
    "start": ,
    }
    # print(read_data)

read_cfg("cfgA.txt")
print(read_data[4])
