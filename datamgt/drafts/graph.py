from py2neo import Graph

graph = Graph("bolt://localhost:7687")

queryStr = """
merge (a :CELL { cell_ref:'REF_0001'})
merge (b :LOC {loc_ref:'REF_L0002'} )
merge (a)-[:CURRENT_STATUS]->(b)  
RETURN a
"""

queryStr1 = """
MATCH (a:CELL)-[:CURRENT_STATUS]->()  
RETURN a.cell_ref
"""

campaign = {"refID":"ref_000111", "desc":"The magic within you!"}

queryStr2 = """CREATE (a :feedback) SET a += $props""", {"props": campaign}

def executeQry_df(queryStr):
    dat = graph.run(queryStr).to_data_frame()
    print(f"dat: \n{dat}\n")
    return dat

tbl_qry = "UNWIND range(1, 3) AS n RETURN n, n * n as n_sq"

def executeQry_tbl(queryStr):
    tbl = graph.run(queryStr).to_table()
    print(f"tbl \n{tbl}\n")
    return tbl


def executeQry_tbl1(queryStr):
    tbl = graph.run(queryStr).to_table()
    print(f"tbl \n{tbl}\n")
    return tbl

executeQry_df(queryStr)
executeQry_df(queryStr1)

executeQry_tbl(tbl_qry)

executeQry_tbl(queryStr2)
