#-*- coding: utf-8 -*-
import cherrypy
import hashlib
import os
from jinja2 import *
from model import *

env = Environment(loader=FileSystemLoader('views'))

SESSION_KEY = 'useremail'

class Administrador(object):

    @cherrypy.expose
    def login(self):
    	try:
            c = cherrypy.session[SESSION_KEY]
        except:
            cherrypy.session[SESSION_KEY] = None
            c = None
        if c is None:
        	html = env.get_template('login.html')
        	return html.render()
        else:
            raise cherrypy.HTTPRedirect("inicio")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def dologin(self, correo, contrasena):
    	c = Conexion()
    	r = c.consultar("select * from usuario where correo = '"+ str(correo) + "' and contrasena = '" + str(contrasena) + "';");
    	if r is None:
    		return "No"
    	cherrypy.session[SESSION_KEY] = correo
    	return "Si"

    @cherrypy.expose
    def inicio(self):
    	try:
            c = cherrypy.session[SESSION_KEY]
        except:
            cherrypy.session[SESSION_KEY] = None
            c = None
        if c is None:
            raise cherrypy.HTTPRedirect("login")
    	return 'Bienvenido <a href="salir"> Salir </a>'

    @cherrypy.expose
    def salir(self):
    	cherrypy.session[SESSION_KEY] = None
    	raise cherrypy.HTTPRedirect("login")

cherrypy.tree.mount(Administrador(), "/administrador/", "app.conf")