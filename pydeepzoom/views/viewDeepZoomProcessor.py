import logging
log = logging.getLogger(__name__)

from pyramid.response import Response, FileResponse
from pyramid.view import (view_config, view_defaults)
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPSeeOther, exception_response
from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')

from pydeepzoom.lib.TilesGenerator import TilesGenerator
from pydeepzoom.lib.RequestParameters import RequestParameters
from pydeepzoom.lib.CachedImage import CachedImage
from pydeepzoom.lib.DomainCheck import DomainCheck

#from pydeepzoom.lib.base64Convert import url2base64string, base64string2url
from pydeepzoom.lib.urlConvert import url2filename
from pydeepzoom.lib.dzi2json import dzi2json

import pudb
import json
import time
import os


class DeepZoomProcessorView(object):

	def __init__(self, request):
		self.request = request
		self.view_name = "DeepZoom Processor"
		
		self.tilesdir = config.get('tiles_cache', 'dir', fallback = './tilescache')
		
		self.max_sleep_time = 10
		
		
	
	@view_config(route_name='deepzoom', renderer='jsonp')
	def deepzoomprocessorview(self):
		#pudb.set_trace()
		
		requestparams = RequestParameters(self.request)
		requestparams.readRequestParams()
		
		imageurl = requestparams.getImageURL()
		if imageurl is None:
			return HTTPNotFound()
		
		log.info(imageurl)

		domaincheck = DomainCheck(imageurl)
		if domaincheck.isAllowedDomain() is False:
			raise exception_response(403, detail='Domain of image url is not allowed')
		
		jsondict = {}
		urlfilename = url2filename(imageurl)
		tempfilepath = None
		
		dzifile = self.tilesdir + '/' + urlfilename + '.dzi'
		dzimarker = self.tilesdir + '/' + urlfilename + '.dzi.part'
		
		if os.path.isfile(dzimarker):
			count = 0
			while count <= self.max_sleep_time:
				if os.path.isfile(dzifile):
					jsondict = dzi2json(dzifile)
					if 'Format' in jsondict:
						break
				time.sleep(1)
				count += 1
		
		elif os.path.isfile(dzifile):
			jsondict = dzi2json(dzifile)
		
		else:
			fd = open(dzimarker, 'w')
			fd.close()
			
			try:
				cachedimage = CachedImage(imageurl, urlfilename)
				tempfilepath = cachedimage.createTempFile()
				
			except ValueError:
				raise exception_response(400, detail='image url does not provide a valid image')
			
			tilesgenerator = TilesGenerator(cachedimage, self.tilesdir + '/' + urlfilename)
			jsondict = dzi2json(os.getcwd() + '/' + dzifile)
			
			cachedimage.closeTempFile()
		
		if os.path.isfile(dzimarker):
			os.remove(dzimarker)
		
		jsondict['Url'] = self.request.application_url + '/tilesCache/' + urlfilename + '_files/'
		
		
		return jsondict
		

