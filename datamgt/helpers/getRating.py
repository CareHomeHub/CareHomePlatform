

def getRatings(cqc_data):
    cnt = 0
    # count = len(cqc_data)
    # print(count)
    result = []
    for element in cqc_data:
        cnt += 1
        doc={}
        if 'currentRatings' in element['loc']:
            doc["loc"] = element['loc']['locationId']
            doc["overall"] = element['loc']['currentRatings']['overall']['rating']
            doc["safe"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][0]['rating']
            doc["Well-led"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][1]['rating']
            doc["Caring"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][2]['rating']
            doc["Responsive"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][3]['rating']
            doc["Effective"] = element['loc']['currentRatings']['overall']['keyQuestionRatings'][4]['rating']
            result.append(doc)
        else:
            print(f"currentRatings {element['loc']} missing")
            print(f"cqc_data ratings overall: {element['loc']}")

    print(f"\n\n\nResult (getRatings ) :\n\ {result}")
    return result
