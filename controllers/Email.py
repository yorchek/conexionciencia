#-*- coding: utf-8 -*-
import cherrypy
import hashlib
import os



class Email(object):

    def __init__(self):
        self.us = None


cherrypy.tree.mount(Email(), "/email/", "app.conf")