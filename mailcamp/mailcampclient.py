class MailCampClient:
    """
    MailCamp class to communicate with mailcamps XML API
    """
    def __init__(self, username, xml_token, url='http://mailing.effectiveprofiles.com/xml.php'):
        """
        Initialize the class with username, xml_token and url
        :param username: The username of a user in mailcamp
        :param xml_token: The xml_token provided by mailcamp
        :param url: The url where the requests are sent to.
        """
        self.username = username
        self.xml_token = xml_token
        self.url = url
