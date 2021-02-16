from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)

def create_friend_of(tx, name, friend):
    tx.run("CREATE  (a:Person {name: $name} )-[:KNOWS]->(f:Person {name: $friend})  RETURN f.name AS friend", name=name, friend=friend)

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Bob")

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Carl")

driver.close()

