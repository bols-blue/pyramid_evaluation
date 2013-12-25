# -*- coding: utf-8 -*-
__author__ = 'miyabi'

from pyramid.view import view_config
from js.bootstrap import bootstrap


@view_config(route_name='index', renderer='index.mako')
def main(request):
    bootstrap.need()
    return {}
    pass