import requests
import json
class IpInfoDb:
    """Class IPInfoDB, developed by Ionut Software on June 18, 2023.
 This class includes various functions that allow you to use the IP2 Geolocation API (IPInfoDB's API) more easily. Warning! The author is not responsible for any misuse you may give to this tool. The tool is made solely for educational purposes."""
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ip2location.io/"

    def get_info(self, ip_address):
        url = f"{self.base_url}?key={self.api_key}&ip={ip_address}&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            return None

    def get_country_code(self, response):
        country_code = response["country_code"]
        return country_code

    def get_country(self, response):
        country = response["country_name"]
        return country

    def get_region_name(self, response):
        region_name = response["region_name"]
        return region_name

    def get_city_name(self, response):
        city_name = response["city_name"]
        return city_name

    def get_latitude(self, response):
        latitude = response["latitude"]
        return latitude

    def get_longitude(self, response):
        longitude = response["longitude"]
        return longitude

    def get_zipcode(self, response):
        zipcode = response["zip_code"]
        return zipcode

    def get_timezone(self, response):
        timezone = response["time_zone"]
        return timezone

    def get_asn(self, response):
        asn = response["asn"]
        return asn

    def get_as(self, response):
        as_value = response["as"]
        return as_value

