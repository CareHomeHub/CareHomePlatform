import pytest

from helpers import getProviderInfo


expected = {'providerId': '1-118166130', 'locationIds': ['1-126473100', '1-126473117', '1-126473132'], 'organisationType': 'Provider', 'ownershipType': 'Organisation', 'type': 'Social Care Org', 'brandId': 'BD157', 'brandName': 'BRAND Allied Care Limited', 'odsCode': 'AP0T', 'uprn': '100061655474', 'name': 'Ashfield Care Homes Limited', 'registrationStatus': 'Registered', 'registrationDate': '2010-10-01', 'website': 'www.alliedcare.co.uk', 'postalAddressLine1': 'Throwleigh Lodge', 'postalAddressLine2': 'Ridgeway, Horsell', 'postalAddressTownCity': 'Woking', 'region': 'South East', 'postalCode': 'GU21 4QR', 'onspdLatitude': 51.327163, 'onspdLongitude': -0.567164, 'mainPhoneNumber': '01483772901', 'companiesHouseNumber': '02469345', 'inspectionDirectorate': 'Adult social care', 'constituency': 'Woking', 'localAuthority': 'Surrey', 'lastInspection': {'date': '2019-07-02'}, 'contacts': [], 'relationships': [], 'regulatedActivities': [{'name': 'Accommodation for persons who require nursing or personal care', 'code': 'RA2', 'nominatedIndividual': {'personTitle': 'Mrs', 'personGivenName': 'Catherine', 'personFamilyName': 'Meacham'}}], 'inspectionAreas': [], 'inspectionCategories': [{'code': 'S1', 'primary': 'true', 'name': 'Residential social care'}]}

def test_get_valid_provider():
    exp = expected
    act = getProviderInfo.find_prov_info("1-118166130")
    print(act)
    assert act == exp, "Error not as expected"
    
    

def test_get_invalid_provider():
    exp = {'Error': "No Provider reference found for 1-134558906"}
    act = getProviderInfo.find_prov_info("1-134558906")
    
    assert act == exp, "Error not as expected"
