import requests


def find_postcode(ref):
    if ref=='':
        return {'Error': "No Postcode details supplied"}
    
    resp = requests.get(f'http://api.postcodes.io/postcodes/{ref}')
    
    if resp.status_code !=200:
        return {'Error': F"No Postcode details found for {ref}"}
    
    return resp.json()