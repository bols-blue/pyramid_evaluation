from wsgiref.simple_server import make_server
from pyramid.view import view_config
from pyramid.config import Configurator
from pyramid.response import Response


@view_config(route_name='hello')
class MyView(object):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        return Response('hello')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_route('hello2', '/hello2/{name}')
    #config.add_view(hello_world, route_name='hello')
    #config.add_view(MyView, route_name='hello2')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8888, app)
    server.serve_forever()
