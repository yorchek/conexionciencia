#-*- coding: utf-8 -*-
import cherrypy
import hashlib
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


if __name__ == '__main__':
    cherrypy.quickstart(Admin(), "" ,"app.conf")
