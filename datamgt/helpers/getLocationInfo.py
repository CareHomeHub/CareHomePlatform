import requests


def find_loc_info(ref='X99XX'):
    if ref=='X99XX':
        return {'Error': "No Location reference supplied"}
    
    resp = requests.get(f'https://api.cqc.org.uk/public/v1/locations/{ref}')
    print(resp.json())
    if resp.status_code !=200:
        return {'Error': f"No Location reference found for {ref}"}
    
    return resp.json()