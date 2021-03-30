from py2neo import Graph
import json 
import requests

graph = Graph("bolt://graph_db:7687")

# queryStr = """
# merge (a :CELL { cell_ref:'REF_0001'})
# merge (b :LOC {loc_ref:'REF_L0002'} )
# merge (a)-[:CURRENT_STATE]->(b)  
# RETURN a
# """

# queryStr1 = """
# MATCH (a:CELL)-[:CURRENT_STATE]->()  
# RETURN a.cell_ref
# """

# def executeQry_df1(queryStr):
#     dat = graph.run(queryStr).to_data_frame()
#     print(f"dat: \n{dat}\n")
#     return dat

# tbl_qry = "UNWIND range(1, 3) AS n RETURN n, n * n as n_sq"

# def executeQry_tbl1(queryStr):
#     tbl = graph.run(queryStr).to_table()
#     print(f"tbl \n{tbl}\n")
#     return tbl




# executeQry_df1(queryStr)
# executeQry_df1(queryStr1)

# executeQry_tbl1(tbl_qry)


with open('app/data/mocks/CQC_data.json') as f:
        data = json.load(f)

def load_data():
    # with open('data/mocks/CQC_data.json') as f:
    #     data = json.load(f)

    for item in data:
        # print(f"{data[0]}")
        # item = data[0]
        
        # print(f"{item['loc']['locationId']}")
        
        
        queryStr = "merge (a :HOME { locationId:'"+item['loc']['locationId']+"', locationName:'"+item['req']['locationName']+"',postalCode:'"+item['loc']['postalCode']+"',providerId:'"+item['loc']['providerId']+"',currentRatings:'"+item['loc']['currentRatings']['overall']['rating']+"'})\
                    merge (b :GEO {postcode:'"+item['postcode']['result']['postcode']+"',primary_care_trust:'"+item['postcode']['result']['primary_care_trust']+"',region:'"+item['postcode']['result']['region']+"',lsoa:'"+item['postcode']['result']['lsoa']+"'} )\
                    merge (a)-[:IS_LOCATED]->(b) RETURN a"
        dat = graph.run(queryStr) 
        print(f"QueryString : \n{queryStr}")  
        
# load_data()


def magic_cypher():
    # # Add uniqueness constraints.
    # # graph.run("CREATE CONSTRAINT ON (q:Question) ASSERT q.id IS UNIQUE;")
    with open('app/data/mocks/CQC_data.json') as g: 
        data = json.load(g)

    query = """
    WITH $json as data
    UNWIND data as q
     
    MERGE (location:CQCLocation {id:q.loc.locationId}) ON CREATE
    SET location.name = q.loc.name, location.web_link = q.loc.website, location.bed_count = q.loc.numberOfBeds, 
    location.registrationStatus = q.loc.registrationStatus, location.registrationDate = q.loc.registrationDate, location.deregistrationDate = q.loc.deregistrationDate, location.onspdLongitude = q.loc.onspdLongitude, location.onspdLatitude = q.loc.onspdLatitude

    MERGE (owner:PROVIDER {id:q.loc.providerId}) ON CREATE SET owner.postalAddressCounty = q.loc.postalAddressCounty
    MERGE (owner)-[:Provides]->(location)
    
    FOREACH (name IN q.loc.specialisms | MERGE (tag:specialism {name:name.name})  MERGE (location)-[:Specilises_In]->(tag)) 
    FOREACH (a IN q.loc.reports | MERGE (location)<-[:REPORTS]-(answer:REPORT {id:a.linkId}) ON CREATE SET answer.reportDate = a.reportDate, answer.reportUri= a.reportUri, answer.firstVisitDate = a.firstVisitDate)

    FOREACH (serviceType IN q.loc.gacServiceTypes | 
     MERGE (gacServiceType:gacServiceTypes {name:serviceType.name}) 
     MERGE (location)-[:Supplies_gacServiceType]->(gacServiceType) ) 

    """
    results = graph.run(query,json=data)


# MERGE (location)-[:CURRENT_RATING]->(rating :RATING { overall:q.loc.currentRatings.overall.rating }) ON CREATE SET rating.safe = q.loc.currentRatings.keyQuestionRatings[0].rating
# ON CREATE SET geodata.nhs_ha = q.postcode.result.nhs_ha, geodata.primary_care_trust = q.postcode.result.primary_care_trust, geodata.lsoa = q.postcode.result.lsoa, geodata.outcode = q.postcode.result.outcode, geodata.ccg = q.postcode.result.ccg, geodata.incode = q.postcode.result.incode
    
    with open('app/data/ratingdata.json') as h: 
        data1 = json.load(h)
    
    setRatingData = """
    WITH $json as data
    UNWIND data as q
    
    MATCH (n:CQCLocation) where n.id = q.loc 
    
    MERGE (rate:RATINGS {id:q.loc}) ON CREATE
    SET rate.reportID = q.reportLinkId, rate.reportDate=q.reportDate, rate.overall = q.overall, rate.safe = q.safe, rate.Well_led = q.Well_led, rate.Caring = q.Caring,rate.Responsive = q.Responsive,
    rate.Effective = q.Effective
    
    MERGE (n)-[:CURRENT_RATING]->(rate)
    
    """
    results = graph.run(setRatingData,json=data1)
    

    
    
    
    with open('app/data/geodata.json') as f: 
        data2 = json.load(f)
    
    setGeoData = """
    WITH $json as data
    UNWIND data as q
    
    MATCH (n:CQCLocation) where n.id = q.location 
    
    MERGE (geo:GeoData {id:q.location}) ON CREATE
    SET geo.postcode = q.postcode, geo.outcode = q.outcode, geo.country = q.country, geo.nhs_ha = q.nhs_ha, 
    geo.longitude = q.longitude, geo.latitude = q.latitude,geo.eastings = q.eastings,
    geo.northings = q.northings,
    geo.primary_care_trust = q.primary_care_trust,
    geo.parliamentary_constituency = q.parliamentary_constituency,
    geo.region = q.region,
    geo.lsoa = q.lsoa,
    geo.incode = q.incode,
    geo.admin_county = q.admin_county, geo.admin_ward = q.admin_ward
    MERGE (n)-[:IS_LOCATED_IN]->(geo)
    """
    results = graph.run(setGeoData,json=data2)
    
    tx = graph.begin()