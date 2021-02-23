import graph as model
import hashlib



def test_graph_df():
    queryStr = "MATCH (a:CELL)-[:CURRENT_STATE]->()  RETURN a.cell_ref"

    exp = "REF_0001"
    act = model.executeQry_df(queryStr)
    data = (act.iloc[0][0])
    print(f"Data - {data}")
    assert exp==data, f"expected {exp} but recieved {data}."
    
# test_graph_df()

# queryStr1 = "UNWIND range(1, 3) AS n RETURN n, n * n as n_sq"
# 
# def test_graph_tbl():
#     exp = "REF_0001"
#     act = model.executeQry_tbl(queryStr1)
#     data = hashlib.sha256(act)
#     print(f"Data - {data}")
#     assert exp==data, f"expected {exp} but recieved {data}."

# test_graph_tbl()
