#-*- coding: utf-8 -*-
import cherrypy
import hashlib
import os
from jinja2 import *

__all__ = ['Administrador']

SESSION_KEY = '_cp_username'

env = Environment(loader=FileSystemLoader('views'))

class Admin(object):

    def __init__(self):
        self.us = None

    @cherrypy.expose
    def index(self):
        html = env.get_template('index.html')
        return html.render()

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(Admin(), "" ,"app.conf")
