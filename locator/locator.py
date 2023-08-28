import requests

class Locator():
    
    def __init__(self):
        self.domain = 'https://ipinfo.io/'
        self.verify = True
    
    def createErrorMessage(status_code):
        return 'Status:', status_code, 'Problem with the request. Exiting.'

    def getDetails(self, ip):
        if ip == None:
            response = requests.get(self.domain + '/json', verify=self.verify)
        else:
            response = requests.get(self.domain + ip + '/json', verify=self.verify)

        if response.status_code != 200:
            errorMessage = self.createErrorMessage(response.status_code)
            return errorMessage
        
        data = response.json()
        return data

if __name__ == '__main__':
    locator = Locator()
    details = locator.getDetails('1.1.1.1')
    print(details)