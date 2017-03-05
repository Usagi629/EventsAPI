import datetime
import time
import cgi
import types
import logging
import os
import urllib
from urllib2 import HTTPError, HTTPErrorProcessor, urlopen, Request, build_opener
from ConfigParser import ConfigParser

class UASMeetup:
    """

    """

    # Global Parameters
    # __url = ""  # URL to POST to **{REQUIRED}
    # __key = {'key': ""}  # API Key **{REQUIRED}
    # __group_id = 0  # Group hosting the event **{REQUIRED}
    # __group_urlname = ""  # URL name of the Group hosting the event **{REQUIRED}

    # Configuration Parameters
    __configFilePath = "meetup.cfg"  # Path to the config file
    __configHandle = ConfigParser    # Handle to the config file (for getting configs)

    def __init__(self):

        if len(self.__configFilePath) == 0:
            raise Exception("The config file path was empty")

        self.__validateConfigFile()


    def postEvent(self):

        __name = "This is a Test."  # Name of the event. May not be longer than 80 characters. **{REQUIRED}
        __description = ""  # Longer description of the event, in HTML. May not be longer than 50000 characters.
        __simple_html_description = ""  # simple HTML formatted event description. May not be longer than 50000 characters.
        __time = 1494003519000  # Event start time in milliseconds epoch, or relative to the current time in the d/w/m format
        __three_hours = 10800000  # 1 hour
        __duration = __three_hours  # Event duration in milliseconds. To clear event duration, set this to 0


        __venue_id = "189995872" # Numeric identifier of a venue
        __values = {'group_id': self.getGroupID(),
                  'group_urlname' : self.getGroupURLName(),
                  'name' : __name,
                  'time' : __time }

        __key = {'key': self.getAPIKey()}

        __full_url = self.getEventPostURL() + '?' + urllib.urlencode(__key)
        __data = urllib.urlencode(__values)
        __request = Request(__full_url, __data)

        print("url", __full_url)
        print("data: ", __data)

        try: __response = urlopen(__request)
        except HTTPError as e:
            print("Caught HTTPError: (", e.errno, ")", e.reason, e.filename)
        else:
            token_string = __response.read()
            print(token_string)


    def getAPIKey(self):
        """ Getter for the Twitter access key """
        return self.__configHandle.get('global', 'api-key')


    def getGroupID(self):
        """ Getter for the Twitter access secret """
        return self.__configHandle.get('global', 'group-id')


    def getGroupURLName(self):
        """ Getter for the Twitter consumer key """
        return self.__configHandle.get('global', 'group-url-name')


    def getEventPostURL(self):
        """ Getter for the Twitter consumer secret """
        return self.__configHandle.get('event-post', 'url')

    def __validateConfigFile(self):
        """ Makes sure that the config file contains all of the required information

            Raises Exception if:
                Any field is not present

        """
        if os.path.isfile(self.__configFilePath) == False:
            raise Exception("The configuration file '%s' does not exist" % (self.__configFilePath))
        self.__configHandle = ConfigParser()
        self.__configHandle.read(self.__configFilePath)

        try:
            self.getAPIKey()
        except:
            raise Exception("Could not find API key in config file '%s'", self.__configFilePath)

        try:
            self.getGroupID()
        except:
            raise Exception("Could not find Group ID in config file '%s'", self.__configFilePath)

        try:
            self.getGroupURLName()
        except:
            raise Exception("Could not find Group URL Name config file '%s'", self.__configFilePath)

        try:
            self.getEventPostURL()
        except:
            raise Exception("Could not find Event Post URL in config file '%s'", self.__configFilePath)

