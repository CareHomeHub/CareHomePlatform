import pytest

import getInfo


expected = {
  "locationId": "1-134558905",
  "providerId": "1-102643096",
  "organisationType": "Location",
  "type": "Social Care Org",
  "name": "Allied Healthcare Bournemouth",
  "brandId": "BD234",
  "brandName": "BRAND Allied Healthcare",
  "onspdCcgCode": "E38000045",
  "onspdCcgName": "NHS Dorset CCG",
  "registrationStatus": "Deregistered",
  "registrationDate": "2010-12-02",
  "deregistrationDate": "2016-11-28",
  "website": "www.nestor-healthcare.co.uk",
  "postalAddressLine1": "135-139 Belle Vue Road",
  "postalAddressLine2": "Southbourne",
  "postalAddressTownCity": "Bournemouth",
  "postalAddressCounty": "Dorset",
  "region": "South West",
  "postalCode": "BH6 3EN",
  "onspdLatitude": 50.721625,
  "onspdLongitude": -1.796861,
  "careHome": "N",
  "inspectionDirectorate": "Adult social care",
  "mainPhoneNumber": "01202420022",
  "constituency": "Bournemouth East",
  "localAuthority": "Bournemouth, Christchurch and Poole",
  "lastInspection": {
    "date": "2014-09-22"
  },
  "relationships": [
    
  ],
  "locationTypes": [
    
  ],
  "regulatedActivities": [
    
  ],
  "gacServiceTypes": [
    {
      "name": "Homecare agencies",
      "description": "Domiciliary care service"
    }
  ],
  "inspectionCategories": [
    {
      "code": "S2",
      "primary": "true",
      "name": "Community based adult social care services"
    }
  ],
  "specialisms": [
    {
      "name": "Caring for adults over 65 yrs"
    },
    {
      "name": "Caring for adults under 65 yrs"
    },
    {
      "name": "Caring for children"
    },
    {
      "name": "Dementia"
    },
    {
      "name": "Eating disorders"
    },
    {
      "name": "Learning disabilities"
    },
    {
      "name": "Mental health conditions"
    },
    {
      "name": "Physical disabilities"
    },
    {
      "name": "Sensory impairment"
    },
    {
      "name": "Substance misuse problems"
    }
  ],
  "inspectionAreas": [
    
  ],
  "currentRatings": {
    "overall": {
      "rating": "No published rating",
      "useOfResources": {
        
      },
      "keyQuestionRatings": [
        {
          "name": "Safe",
          "rating": "No published rating"
        },
        {
          "name": "Well-led",
          "rating": "No published rating"
        },
        {
          "name": "Caring",
          "rating": "No published rating"
        },
        {
          "name": "Responsive",
          "rating": "No published rating"
        },
        {
          "name": "Effective",
          "rating": "No published rating"
        }
      ]
    }
  },
  "reports": [
    {
      "linkId": "ea6e69f4-ebfb-402b-b7db-985599b44991",
      "reportDate": "2014-11-25",
      "reportUri": "/reports/ea6e69f4-ebfb-402b-b7db-985599b44991",
      "firstVisitDate": "2014-09-22"
    },
    {
      "linkId": "e2f9104a-5806-42c1-b808-5ac0922e6fc5",
      "reportDate": "2014-07-12",
      "reportUri": "/reports/e2f9104a-5806-42c1-b808-5ac0922e6fc5",
      "firstVisitDate": "2014-05-12"
    },
    {
      "linkId": "844ca86f-2dff-4672-9e3b-3ae240053a87",
      "reportDate": "2014-03-28",
      "reportUri": "/reports/844ca86f-2dff-4672-9e3b-3ae240053a87",
      "firstVisitDate": "2014-01-21"
    },
    {
      "linkId": "7327b3f9-6f84-4b3a-a571-a11d4e5bb1ea",
      "reportDate": "2013-04-19",
      "reportUri": "/reports/7327b3f9-6f84-4b3a-a571-a11d4e5bb1ea",
      "firstVisitDate": "2013-03-19"
    }
  ]
}






def test_get_valid_location():
    exp = expected
    act = getInfo.find_loc_info("1-134558905")
    
    assert act == exp, "Error not as expected"
    
    

def test_get_invalid_location():
    exp = {'Error': "No Location reference found for 1-134558906"}
    act = getInfo.find_loc_info("1-134558906")
    
    assert act == exp, "Error not as expected"
