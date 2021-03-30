import json
# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


# import logging

# def findByRef(ref="", dataset=[]):
#     """Summary or Description of the Function

#     Parameters:
#     argument1 (int): Description of arg1

#     Returns:
#     int:Returning value

#    """
    
#     if ref=="":
#         # logger.info("No Reference Supplied to findByRef function")
#         return {"result":  "error1"}
#     if (dataset==[]):
#         # logger.info("No Dataset Supplied to findByRef function")
#         return {"result":  "error2"}
    
#     if ref in dataset:
#         return {"result":  "IN"}
#     else:
#         return {"result":  "OUT"}
    
   
# ans = findByRef(4, [1,2,3,4]) 
# print(f"{ans['result']}")

# ans = findByRef(5, [1,2,3,4]) 
# print(f"{ans['result']}")


with open('mocks/CQC_data.json') as f: 
    cqc_data = json.load(f)

def getGeoData(cqc_data):
    result = []
    cnt = 0
    for element in cqc_data:
        geo = {}
        if 'result' in element['postcode']:
            cnt += 1
            geo['location'] = element['loc']['locationId']
            geo["postcode"] = element['postcode']['result']['postcode']
            geo["outcode"] = element['postcode']['result']['outcode']
            geo["country"] = element['postcode']['result']['country']
            geo["nhs_ha"] = element['postcode']['result']['nhs_ha']
            geo["longitude"] = element['postcode']['result']['longitude']
            geo["latitude"] = element['postcode']['result']['latitude']
            geo["eastings"] = element['postcode']['result']['eastings']
            geo["northings"] = element['postcode']['result']['northings']
            geo["primary_care_trust"] = element['postcode']['result']['primary_care_trust']
            geo["parliamentary_constituency"] = element['postcode']['result']['parliamentary_constituency']
            geo["region"] = element['postcode']['result']['region']
            geo["lsoa"] = element['postcode']['result']['lsoa']
            geo["incode"] = element['postcode']['result']['incode']
            geo["admin_county"] = element['postcode']['result']['admin_county']
            geo["admin_ward"] = element['postcode']['result']['admin_ward']
            result.append(geo)
            
        else: 
            cnt += 1
            geo['location'] = element['loc']['locationId']
            geo["postcode"] = "NO POSTCODE DETAILS"
        
    print(f"RESULT (getGeoData): {result}")
    return result
  


def getRatings(cqc_data):
    cnt = 0
    count = len(cqc_data)
    # print(count)
    result = []
    for element in cqc_data:
        cnt += 1
        doc={}
        if 'currentRatings' in element['loc']:
            # print(f"\n\ncurrentRatings: {element['loc']['currentRatings']}")
            if element['loc']['currentRatings']['overall']['rating'] == "No published rating":
                doc["reportLinkId"] = "No published report"
                doc["reportDate"] = "No published report"
            else:
                doc["reportLinkId"] = element['loc']['currentRatings']['overall']['reportLinkId']
                doc["reportDate"] = element['loc']['currentRatings']['overall']['reportDate']
            doc["loc"] = element['loc']['locationId']
            doc["overall"] = element['loc']['currentRatings']['overall']['rating']
            doc["safe"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][0]['rating']
            doc["Well-led"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][1]['rating']
            doc["Caring"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][2]['rating']
            doc["Responsive"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][3]['rating']
            doc["Effective"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][4]['rating']
            result.append(doc)
        else:
            print(f"currentRatings missing")
            # print(f"cqc_data ratings overall: {element['loc']}")
            
    # print(f"\n\n\nResult (getRatings) :\n\ {result}")  
    return result      
            

            
geodata = getGeoData(cqc_data)
ratingdata = getRatings(cqc_data)

with open("geodata.json", "w") as write_file:
        json.dump(geodata, write_file)
        
    
with open("ratingdata.json", "w") as write_file:
        json.dump(ratingdata, write_file)


