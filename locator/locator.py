import requests

def getDetails(ip):
    if ip == None:
        response = requests.get('https://ipinfo.io/json', verify=True)
    else:
        response = requests.get(f'https://ipinfo.io/{ip}/json', verify=True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
    
    data = response.json()
    return data

if __name__ == '__main__':
    details = getDetails()
    print(details)