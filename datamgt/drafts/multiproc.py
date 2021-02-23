import json
import time
import random

from getPostcode import find_postcode as gPc
from getLocationInfo import find_loc_info as gLi

# dataList = []

with open("locationsDataCQC.json", "r") as read_file:
    data = json.load(read_file)

locations = data["locations"]

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

    
from multiprocessing import Pool


def get_info(loc):
    info(f"Info processing {loc}")
    return gLi(loc)

def get_postcode(loc):
    info(f"Postcode processing {loc}")
    return gPc(loc)


def square(loc):
    info(f"processing {loc}")
    time.sleep(random.randint(1,5))
    # calculate the square of the value of x
    print (f"Locations = {loc}")
    loc_postcode = get_postcode(loc['postalCode'])
    loc_info = get_info(loc['locationId'])

    ist = {'req' : loc,
        'loc' : loc_info,
        'postcode' :loc_postcode
        }
    with open("CQC_data_file_multiples.json", "a") as write_file:
        json.dump(ist, write_file)

    return

if __name__ == '__main__':

    # Define the dataset
    dataset = locations

    # Run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 10
    chunksize = 15
    with Pool(processes=agents) as pool:
        pool.map(square, dataset, chunksize)

