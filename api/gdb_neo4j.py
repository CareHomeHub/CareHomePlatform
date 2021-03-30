from neo4j import GraphDatabase
import json

uri = "bolt://graph_db:7687"
driver = GraphDatabase.driver(uri, encrypted=False)


from .data import mocks

def get_gdb():
    return driver


def save_feedback(feedback):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("""
                CREATE (a :feedback) SET a += $props
            """, {"props": feedback})  
            

def save_contribution(contribution):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("""
                CREATE (a :CAREHOME) SET a += $props
            """, {"props": contribution})  

feedback = {"ref":"uuid_0001", "author":"John Doe", "comments":"Average performance", "rating":3}

contribution = {"ref":"uuid_1001", "author":"Jane Doe", "comments":"Above Average performance, impressed by price", "rating":4}



save_feedback(feedback)
save_contribution(contribution)


def seed_loc_data():
    with open('app/data/mocks/loc_marker_list.json') as f:
        data = json.load(f)

    for item in data:
        save_contribution(item)
    
    

