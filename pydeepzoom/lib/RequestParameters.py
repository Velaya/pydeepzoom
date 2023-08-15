import pudb
import pyvips
import re

from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')



class RequestParameters():
	def __init__(self, request):
		self.request = request


	def readRequestParams(self):
		#convert all parameter keys to lowercase 
		self.paramsdict = {}
		for param in self.request.params:
			try:
				pvalues = self.request.params.getall(param)
			except AttributeError: # -- not a multidict
				pvalues = [self.request.params[param]]
			self.paramsdict[param.lower()] = pvalues
		
		#self.readFileFormat()
		self.readImageURL()


	def readImageURL(self):
		if 'imageurl' in self.paramsdict:
			self.imageurl = self.paramsdict['imageurl'][0]
		else:
			self.imageurl = None

	'''
	def readFileFormat(self):
		if 'fileformat' in self.paramsdict:
			if self.paramsdict['fileformat'][0] in self.known_formats:
				self.fileformat = self.paramsdict['fileformat'][0]
		elif 'format' in self.paramsdict:
			if self.paramsdict['format'][0] in self.known_formats:
				self.fileformat = self.paramsdict['format'][0]
		else:
			self.fileformat = None
	'''


	def getImageURL(self):
		return self.imageurl


	'''
	def getFileFormat(self):
		return self.fileformat
	'''

