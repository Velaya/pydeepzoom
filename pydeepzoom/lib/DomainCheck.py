import pudb
import re

from urllib.parse import urlparse

from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')

class DomainCheck():
	def __init__(self, url):
		urldict = urlparse(url)
		self.domain = urldict.netloc
		
		self.whitelist = [wl.strip() for wl in config.get('allowed_domains', 'whitelist', fallback = '').split(',')]
		self.blacklist = [bl.strip() for bl in config.get('allowed_domains', 'blacklist', fallback = '').split(',')]


	def isAllowedDomain(self):
		if (self.isInList(self.whitelist)):
			allowed = True
		if (self.isInList(self.blacklist)):
			allowed = False
		return allowed


	def isInList(self, domainlist):
		if len(domainlist) > 0:
			if self.domain in domainlist:
				return True
			else:
				return False
		else:
			return True







