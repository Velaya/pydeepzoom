import pudb
import pyvips
from tempfile import NamedTemporaryFile

from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')


class TilesGenerator():
	def __init__(self, cachedimage, dzipath):
		self.cachedimage = cachedimage
		self.dzipath = dzipath
		
		self.loadImage()
		self.writeTiles()
		del self.img
	
	def loadImage(self):
		self.img = pyvips.Image.new_from_file(self.cachedimage.getFilePath())
	
	def writeTiles(self):
		self.img.dzsave(self.dzipath)
	
	'''
	def writeImage(self):
		if self.targetfileformat.lower() in ['tif', 'tiff']:
			self.img.tiffsave(self.cachedimage.getTargetFilePath(), squash = self.saveparams['squash'])
			
		elif self.targetfileformat.lower() in ['pgm', 'pnm', 'pbm']:
			self.img.ppmsave(self.cachedimage.getTargetFilePath(), squash = self.saveparams['squash'])
			
		elif self.targetfileformat.lower() in ['png']:
			self.img.pngsave(self.cachedimage.getTargetFilePath())
		
		elif self.targetfileformat.lower() in ['jpeg', 'jpg']:
			self.img.jpegsave(self.cachedimage.getTargetFilePath())
	
	
	def setTargetFileFormat(self, fileformat):
		# only set the targetfileformat attribute
		# will be used later in writeImage()
		self.targetfileformat = fileformat
		
		# ensure that the image data are fitting into the ppm formats if they are choosen
		if self.targetfileformat == 'pbm':
			self.colorMode('bitonal')
		elif self.targetfileformat == 'pgm':
			self.colorMode('gray')
	'''
	

		
	
	
	def getImageWidth(self):
		return self.img.width
	
	def getImageHeight(self):
		return self.img.height
	
	'''
	def getTargetFilePath(self):
		return self.cachedimage.getTargetFilePath()
	
	def getTargetFileFormat(self):
		return self.targetfileformat
	'''
	
	
	
