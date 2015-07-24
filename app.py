# -*- coding: utf-8 -*-
import cherrypy
import hashlib
import os
from jinja2 import *
from controllers import *

import smtplib
import email.utils
from email.mime.text import MIMEText

env = Environment(loader=FileSystemLoader('views'))

class ConexionCiencia(object):

    def __init__(self):
        self.us = None

    @cherrypy.expose
    def index(self):
        html = env.get_template('index.html')
        c = Conexion()
        r = c.consultar("select contenido from defacebook;");
        return html.render(elementos = r)

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST', 'GET'])
    def send_email(self, nombre=None, correo=None, asunto=None, mensaje=None):

        if (asunto is None or mensaje is None):
            raise cherrypy.HTTPRedirect("index")

        if (nombre is None or nombre == ""):
            nombre = 'Usuario Anonimo'
        if (correo is None or correo == ""):
            correo = 'Correo Anonimo'

        # Create the message
        msg = MIMEText('Mensaje de '+correo+ '\n\n'+ mensaje)
        msg['To'] = email.utils.formataddr(('Conexión Ciencia', 'hyaoki123@gmail.com'))
        msg['From'] = email.utils.formataddr((nombre, correo))
        msg['Subject'] = asunto

        server = smtplib.SMTP("smtp.gmail.com", 587)
        try:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('comentconexciencia@gmail.com', 'conexion123')
            server.sendmail('comentconexciencia@gmail.com', ['hyaoki123@gmail.com'], msg.as_string())
            server.quit()
            server.close()
            return "Si"
        except:
            return "No"

    @cherrypy.expose
    def quienes_somos(self):
        html = env.get_template('portfolio.html')
        return html.render()
    @cherrypy.expose
    def integrantes(self):
        html = env.get_template('about-us.html')
        return html.render()

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(ConexionCiencia(), "" ,"app.conf")