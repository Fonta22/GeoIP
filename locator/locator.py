import requests

class Locator:
    """
    Locator class fetches the ipinfo.io API and gets the details of the given IP address.

    Attributes:
        domain (str): The API's domain.

    Methods:
        __init__(self): Initializes the Locator class.
        getDetails(self, ip): Makes the API request and gets the details of the desired IP address.
        createErrorMessage(self, status_code): Creates an error message in case the API fetch doesn't respond with a status code of 200.
    """
    def __init__(self, ip):
        """
        Initialize the Locator class.

        Parameters:
            ip (str): IP address to get the details of.
        """
        self.ip = ip
        self.domain = 'https://ipinfo.io/'
        self.verify = True
    
    def createErrorMessage(self, status_code):
        """
        Create an error message in case the API fetch doesn't respond with a status code of 200.

        Parameters:
            status_code (str): The status code of the API fetch.
        """
        return 'Status:', status_code, 'Problem with the request. Exiting.'

    def getDetails(self):
        """
        Make the API request and get the details of the desired IP address.
        """
        if self.ip == None:
            response = requests.get(self.domain + '/json', verify=self.verify)
        else:
            response = requests.get(self.domain + self.ip + '/json', verify=self.verify)

        if response.status_code != 200:
            errorMessage = self.createErrorMessage(response.status_code)

            return {
                'message': errorMessage,
                'status_code': response.status_code
            }
        
        data = response.json()
        return data

if __name__ == '__main__':
    locator = Locator('1.1.1.1')
    details = locator.getDetails()
    print(details)