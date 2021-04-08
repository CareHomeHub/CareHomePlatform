


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
