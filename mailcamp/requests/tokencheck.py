"""
The token check endpoint

Checks to make sure that the token that you are using is a valid token.

Documentation: https://www.mailcamp.nl/api/en/#api-Additional-token
"""
from mailcamp.BaseApi import BaseApi
import xml.etree.ElementTree as et


class TokenCheck(BaseApi):
    """
    Check if the given token is valid
    """
    request_type = 'authentication'
    request_method = 'xmlapitest'
    
    def __init__(self, *args, **kwargs):
        super(TokenCheck, self).__init__(*args, **kwargs)

    def is_valid(self):
        """
        Returns if the given token is valid
        :return: True/False
        """
        request = self._get_xml_request(
            requesttype=self.request_type, requestmethod=self.request_method,
            details=None)
        response = self._mailcamp_client._post(request)
        for child in et.fromstring(response):
            if child.tag == 'status' and child.text == 'SUCCESS':
                return True
            return False
