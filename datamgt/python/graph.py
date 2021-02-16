import pandas as pd
from py2neo import Graph

graph = Graph("bolt://localhost:7687")

queryStr = """merge (a :CELL { cell_ref:'REF_0001'})
merge (b :LOC {loc_ref:'REF_L0002'} )
merge (a)-[:CURRENT_STATE]->(b)  RETURN a"""

queryStr1 = "MATCH (a:CELL)-[:CURRENT_STATE]->()  RETURN a.cell_ref"

def executeQry_df(queryStr):
    dat = graph.run(queryStr).to_data_frame()
    print(f"dat = {dat[0]}")
    
tbl_qry = "UNWIND range(1, 3) AS n RETURN n, n * n as n_sq"   
    
def executeQry_tbl(queryStr):
    tbl = graph.run(queryStr).to_table()
    print(f"tbl = {tbl}")
      
    
executeQry_df(queryStr)
executeQry_df(queryStr1)

executeQry_tbl(tbl_qry)


