#  neoloader
import csv, json
from neo4j import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687')


blogmodel = { "listing" : ["id", "title", "desc", "author", "published"], "article" : []}


memberList = "./mocks/mock_member.json"
blogList = "./mocks/mock_blog.json"


def read_csv_campaign(trg):
    with open(trg, newline='') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvdata, None)  # skip the headers
        print("CSVDATA campaign = {}".format(csvdata))
        # return csvdata        for item in csvdata:
        campaign = {}
        for item in csvdata:
            campaign["company_id"] = item[0]
            campaign["target"] = item[1]
            campaign["audience"] = item[2]
            campaign["campaign"] = item[3]
            campaign["type"] = item[4]
            with driver.session() as session:
                with session.begin_transaction() as tx:
                    tx.run("""
                        CREATE (a :campaign) SET a += {props}
                    """, {
                        "props": campaign
                    })


def read_json(trg):
    with open('hackniteblogsite/data/neo4j/mocks/mockblog.json') as json_file:
        data = json.load(json_file)
        return data




info = read_json(blogList)
for item in info:
    print("\n\nItem Id :- {} :\n".format(item["id"]))
    model = blogmodel["listing"]
    for x in model:
        print("{} : {}".format(x, item[x]))