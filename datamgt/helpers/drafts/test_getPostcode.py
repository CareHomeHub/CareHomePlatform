import pytest

import getPostcode
null = None
expected = {
  "status": 200,
  "result": {
    "postcode": "M33 7HF",
    "quality": 1,
    "eastings": 378615,
    "northings": 392375,
    "country": "England",
    "nhs_ha": "North West",
    "longitude": -2.323301,
    "latitude": 53.427726,
    "european_electoral_region": "North West",
    "primary_care_trust": "Trafford",
    "region": "North West",
    "lsoa": "Trafford 012B",
    "msoa": "Trafford 012",
    "incode": "7HF",
    "outcode": "M33",
    "parliamentary_constituency": "Altrincham and Sale West",
    "admin_district": "Trafford",
    "parish": "Trafford, unparished area",
    "admin_county": null,
    "admin_ward": "Ashton upon Mersey",
    "ced": null,
    "ccg": "NHS Trafford",
    "nuts": "Greater Manchester South West",
    "codes": {
      "admin_district": "E08000009",
      "admin_county": "E99999999",
      "admin_ward": "E05000820",
      "parish": "E43000163",
      "parliamentary_constituency": "E14000532",
      "ccg": "E38000187",
      "ccg_id": "02A",
      "ced": "E99999999",
      "nuts": "UKD34"
    }
  }
}

def test_get_valid_postcode():
    exp = expected
    act = getPostcode.find_postcode("M33 7HF")
    
    assert act == exp, "Error not as expected"
    
    

def test_get_invalid_postcode():
    exp = {'Error': F"No Postcode details found for 1-134558905"}
    act = getPostcode.find_postcode("1-134558905")
    
    assert act == exp, "Error not as expected"

def test_get_no_postcode():
    exp = {'Error': "No Postcode details supplied"}
    act = getPostcode.find_postcode("")
    
    assert act == exp, "Error not as expected"
