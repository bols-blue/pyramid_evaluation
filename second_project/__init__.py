from pyramid_beaker import session_factory_from_settings
from pyramid_simpleauth import schema
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    # Configure a session factory, here, we're using `pyramid_beaker`.
    config.include('pyramid_beaker')
    config.set_session_factory(session_factory_from_settings(settings))

    # Include the packages.  The order is significant if you want
    # `pyramid_basemodel` to "just work".
    config.include('pyramid_simpleauth')
    config.include('pyramid_twitterauth')
    config.include('pyramid_basemodel')

    # Either include `pyramid_tm` or deal with committing transactions yourself.
    config.include('pyramid_tm')

    authn_policy = AuthTktAuthenticationPolicy(
        settings['auth.secret'],
    )
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
    )

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.add_route('users', '/users')
    config.add_route('user', '/user/{login}')

    config.add_route('pages', '/pages')
    config.add_route('create_page', '/create_page')
    config.add_route('page', '/page/{title}')
    config.add_route('edit_page', '/page/{title}/edit')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('test', '/test/')
    config.add_route('hello', '/hello/')
    config.add_route('twitter', '/twitter/')
    config.scan()
    return config.make_wsgi_app()
