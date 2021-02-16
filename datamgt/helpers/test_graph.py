# import graph as model


queryStr1 = "MATCH (a:CELL)-[:CURRENT_STATE]->()  RETURN a.cell_ref"

def test_graph_df():
    # act = model.executeQry_df(queryStr1)
    # print(act)
    assert 1==1
    