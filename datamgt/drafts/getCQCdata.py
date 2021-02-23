import json
import time

from getPostcode import find_postcode as gPc
from getInfo import find_loc_info as gLi

# dataList = []

with open("locationsDataCQC.json", "r") as read_file:
    data = json.load(read_file)

locations = data["locations"]

# for loc in locations:
#     time.sleep(3.75)
#     print (f"Locations = {loc}")

#     ist = {'req' : loc,
#         'loc' : gLi(loc['locationId']),
#         'postcode' :gPc(loc['postalCode'])}


#     # print (f"ist: {ist}")
#     dataList.append(ist)
#     # print (f"dataList : {dataList}")

#     with open("CQC_data_file.json", "w") as write_file:
#         json.dump(dataList, write_file)



from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
    
    
from multiprocessing import Pool

def square(loc):
    
    info(f'processing {loc}')
    
    time.sleep(1.75)
    # calculate the square of the value of x
    
    print (f"Locations = {loc}")

    ist = {'req' : loc,
        'loc' : gLi(loc['locationId']),
        'postcode' :gPc(loc['postalCode'])}

    return ist

if __name__ == '__main__':

    # Define the dataset
    dataset = locations

    # # Output the dataset
    # print ('Dataset: ' + str(dataset))

    # Run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 7
    chunksize = 5
    with Pool(processes=agents) as pool:
        result = pool.map(square, dataset, chunksize)

    # Output the result
    print ('Result:  ' + str(result))
    

    with open("CQC_data_file_multi.json", "w") as write_file:
        json.dump(result, write_file)