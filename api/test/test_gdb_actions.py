from ..data .data  import gdb_actions as gdb_acts
import json




# def test_findByRef_found():
#     exp = "IN"
#     act = gdb_acts.findByRef(3, [1,2,3,4,5])

#     assert exp == act['result'], f"{act['result']} is not as expected {exp}"
        
# def test_findByRef_Not_found():
#     exp = "OUT"
#     act = gdb_acts.findByRef(8, [1,2,3,4,5])
        
#     assert exp == act['result'], f"{act['result']} is not as expected {exp}"
        
# def test_findByRef_no_ref():
#     exp = "error1"
#     act = gdb_acts.findByRef( "", [1,2,3,4,5])

#     assert exp == act['result'], f"{act['result']} is not as expected {exp}"
    
    
# def test_findByRef_no_dataset():
#     exp = "error2"
#     act = gdb_acts.findByRef(8, [])

#     assert exp == act['result'], f"{act['result']} is not as expected {exp}"


def test_findByRef_with_datafile(ref= "1-1127939767", dataset="./loc_marker_list.json"):
    with open('./loc_marker_list.json') as f:
        data = json.load(f)
    # print(data[0])
    
    for item in data:
        print(item['loc_id'])
        if ref == item['loc_id']:
            return {"status":200, "result": item}
        
    return {"status":404, "result":"Item not found"}
    
    
    

ans = test_findByRef_with_datafile()
print (ans)