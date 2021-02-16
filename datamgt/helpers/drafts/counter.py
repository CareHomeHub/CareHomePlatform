import json


with open("locationsDataCQC.json", "r") as read_file:
    data = json.load(read_file)
    
    
with open("CQC_data_file.json", "r") as read_file:
    data1 = json.load(read_file)
    

# print(f"loc Orig = {data} \n\n)  #loc comp = {data1}")
# print(f"loc Orig = {len(data)} \n\n  loc comp = {len(data)}")
cnt =0
for i in data['locations']:
    print(i)
    cnt += 1

print(f"cnt data = {cnt}")

# cntr =0
# for i in data1:
#     print(i['req'])
#     cnt += 1

# print(f"cnt data = {cnts}    cntr data1 = {cntr}")
    