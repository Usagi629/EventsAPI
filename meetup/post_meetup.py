import datetime
import time
import cgi
import types
import logging
import urllib
from urllib2 import HTTPError, HTTPErrorProcessor, urlopen, Request, build_opener

# URL to POST to
url = "https://api.meetup.com/2/event"

# API Key
key = {'key' : "4b20653235c14221f447c524632"}

# Group hosting the event {Required}
group_id = 1556336

# URL name of the Group hosting the event
group_urlname = "Meetup-API-Testing"

# Name of the event. May not be longer than 80 characters.
name = "TEST-PLEASE-IGNORE"

# ###### Optional to Meetup API, but required by Events API ############

#sig_id = "182392542" # ?????????????????????????????????????????????????
#sig = "dcbca087c27bf646406905be84c9897166838624" # ?????????????????????

# Longer description of the event, in HTML. May not be longer than 50000 characters.
description = "What an awesome event this will be! I can't wait!"

# Description of the event, in simple HTML format. This value is translated to HTML
# to update the description. May not be longer than 50000 characters.
#simple_html_description = "" #

# Event duration in milliseconds. When not specified, a default of 3 hours may be
# assumed by applications. To clear event duration, set this to 0
duration = 3600000 # 1 hour

# Event start time in milliseconds since the epoch, or relative to the current time in the d/w/m format
time = 1433743200000

# Numeric identifier of a venue
venue_id = "189995872"

values = {'group_id' : group_id,
          'group_urlname' : group_urlname,
          'name' : name,
          'time' : time }

full_url = url + '?' + urllib.urlencode(key)
data = urllib.urlencode(values)

print "\nurl", full_url
print "data: ", data, "\n"

request = Request(full_url, data)

try: response = urlopen(request)
except HTTPError as e:
    print "Caught HTTPError: (", e.errno, ")", e.reason, e.filename
else:
    token_string = response.read()
    print token_string

