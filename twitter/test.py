from UASTwitter import UASTwitter
import uuid
import base64

a = UASTwitter('creds.conf')
a.post('this is a test %s' % (uuid.uuid4()))
a.postWithImage('hi from bill %s' % (uuid.uuid4()), '1kohm5.jpg')

with open("1kohm5.jpg", "rb") as imageFile:
	b64 = base64.b64encode(imageFile.read())	
a.postWithImageBase64('hi from bill %s' % (uuid.uuid4()), b64) 

try:
	a.postWithImage('what what in the what', '1kohm5.jpg')
except:
	print 'yay!'

