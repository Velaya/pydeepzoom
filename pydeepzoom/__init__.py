from pyramid.config import Configurator

def main(global_config, **settings):
	config = Configurator(settings=settings)
	config.include('pyramid_chameleon')
	
	config.add_route('deepzoom', '/deepzoom')
	config.add_route('tiles', '/tilesCache/{imageurl}/{dirnum}/{filename}')
	config.add_route('help', '/')
	
	config.add_static_view(name='static', path='deepzoom:static')
	
	config.scan('pydeepzoom.views')
	return config.make_wsgi_app()
