from UASMeetup import UASMeetup
import uuid

__name = "Just a Test"  # Name of the event. May not be longer than 80 characters. **{REQUIRED}
__description = "This is a test..."  # Longer description of the event, in HTML. May not be longer than 50000 characters.

# simple HTML formatted event description. May not be longer than 50000 characters.
__simple_html_description = "<b>An Awesome Fun Time</b><br/>Will be had by all. So, come on out."

__time = 1433743200000  # Event start time in milliseconds epoch, or relative to the current time in the d/w/m format
__three_hours = 10800000  # 1 hour
__duration = __three_hours  # Event duration in milliseconds. To clear event duration, set this to 0


meetup = UASMeetup()
meetup.postEvent()


