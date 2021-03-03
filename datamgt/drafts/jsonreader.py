import pandas as pd
import json

from py2neo import Graph

graph = Graph("bolt://localhost:7687")

queryStr = """
merge (a :CELL { cell_ref:'REF_0001'})
merge (b :LOC {loc_ref:'REF_L0002'} )
merge (a)-[:CURRENT_STATE]->(b)  
RETURN a
"""

queryStr1 = """
MATCH (a:CELL)-[:CURRENT_STATE]->()  
RETURN a.cell_ref
"""

def executeQry_df(queryStr):
    dat = graph.run(queryStr).to_data_frame()
    print(f"dat: \n{dat}\n")
    return dat

tbl_qry = "UNWIND range(1, 3) AS n RETURN n, n * n as n_sq"

def executeQry_tbl(queryStr):
    tbl = graph.run(queryStr).to_table()
    print(f"tbl \n{tbl}\n")
    return tbl


# df = pd.read_json("CQC_data_file_multiples.json")
# print(f"Head = {df.iloc[0]}")

with open('CQC_data_file_multiples_shrt.json') as jsonfile:
    data = json.load(jsonfile)

# print(data[0]["loc"])

x = 0
for item in data:
    # while x < 1:
    #     print(item["loc"])
    #     print("\n\n- - - - - - - - - - - - - - - - - - - - - -\n")
    #     print(f' locationId : {item["loc"]["locationId"]}  \nServiceTypes : {item["loc"]["gacServiceTypes"]} \n\nSpecialism : {item["loc"]["specialisms"]} \n\nCurrentRatings : {item["loc"]["currentRatings"]}')
    #     print(f' \n\ntype : {item["loc"]["type"]}')
    #     print(f' \n\nname : {item["loc"]["name"]}')
    #     print(f' \n\nname : {item["loc"]["numberOfBeds"]}')
    #     print(f' \n\nLat : {item["loc"]["onspdLatitude"]}')
    #     print(f' \n\nLng : {item["loc"]["onspdLongitude"]}')
    #     print(f' \n\nRegistrationStatus : {item["loc"]["registrationStatus"]}')
    #     print("\n\- - - - - - - - - - - - - - - - - - - - - -n")
    #     print(item["postcode"]["result"])
    #     print("\n\- - - - - - - - - - - - - - - - - - - - - -n")
    #     x+=1
    
    
    for spec in item['loc']['specialisms']:
        queryStr = "merge (a :CELL { specialism: '"+spec['name']+"'})\
            merge (b :LOC {loc_ref:'"+item['loc']['locationId']+"'} )\
            merge (b)-[:Has_Specialism]->(a) RETURN a"

        print (f"queryStr : {queryStr}")


        dat = graph.run(queryStr).to_data_frame()
        print(f"dat: \n{dat}\n")
        # return dat
    
    queryStr = "merge (a :RegistrationStatus { RegistrationStatus: '"+item["loc"]["registrationStatus"]+"'})\
            merge (b :LOC {loc_ref:'"+item['loc']['locationId']+"'} )\
            merge (b)-[:Has_Registration_Status]->(a) RETURN a"
    dat = graph.run(queryStr)
    
    queryStr = "merge (a :geodata { postcode: '"+item["postcode"]["result"]["postcode"]+"'})\
            merge (b :LOC {loc_ref:'"+item['loc']['locationId']+"'} )\
            merge (b)-[:Has_geodata]->(a) RETURN a"
    dat = graph.run(queryStr)
    
    

    
    
        
    
