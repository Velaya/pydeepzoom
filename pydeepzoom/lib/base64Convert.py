import pudb
import base64
import re
import math

def url2base64string(url):
	try:
		urlbytes = url.encode()
		b64 = base64.b64encode(urlbytes)
		b64string = b64.decode()
		b64string = remove_padding(b64string)
		b64string = replace_for_filesystem(b64string)
		return b64string
	except:
		return None


def base64string2url(b64string):
	try:
		b64string = replace_for_url(b64string)
		b64string = add_padding(b64string)
		b64 = b64string.encode()
		urlbytes = base64.b64decode(b64)
		url = urlbytes.decode()
		return url
	except:
		return None


def remove_padding(b64string):
	b64string = re.sub(r'(\=+)$', '', b64string)
	return b64string


def add_padding(b64string):
	string_length = math.ceil(len(b64string)/3)
	b64string = b64string.ljust(string_length * 3, '=')
	return b64string


def replace_for_filesystem(b64string):
	b64string = b64string.replace('/', '.').replace('+', '_')
	return b64string


def replace_for_url(b64string):
	b64string = b64string.replace('.', '/').replace('_', '+')
	return b64string
