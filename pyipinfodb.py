import requests
import logging

# Constants for the API
BASE_URL = "https://api.ip2location.io/"
FORMAT = "json"

# Set up basic logging
logging.basicConfig(level=logging.INFO)

class IpInfoDb:
    """
    A wrapper class for the IPInfoDB API that provides methods to retrieve geolocation data.
    """

    def __init__(self, api_key):
        # Initialize the API key and a session for persistent connections
        self.session = requests.Session()
        self.session.headers.update({'api_key': api_key})
    
    def _get_response(self, ip_address):
        """
        Private method to get the response from the API for a given IP address.
        """
        # Parameters passed as a dictionary for better readability and maintenance
        params = {
            'key': self.session.headers['api_key'],
            'ip': ip_address,
            'format': FORMAT
        }
        try:
            # Use the session to make the request
            response = self.session.get(BASE_URL, params=params)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.json()  # Return the JSON response
        except requests.RequestException as e:
            # Log any request-related issues
            logging.error(f"Request failed: {e}")
            return None

    def get_info(self, ip_address):
        """
        Public method to get all geolocation information for a given IP address.
        """
        return self._get_response(ip_address)

    def get_field(self, response, field_name):
        """
        Generic method to extract a field from the response.
        """
        return response.get(field_name)  # Using .get() to avoid KeyError if the field is not present

    # Examples of specific field retrieval methods using the generic get_field method
    def get_country_code(self, response):
        return self.get_field(response, "country_code")

    def get_country(self, response):
        return self.get_field(response, "country_name")

    