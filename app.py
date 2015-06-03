#-*- coding: utf-8 -*-
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
        return html.render()

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def send_email(self, nombre=None, correo=None, asunto=None, mensaje=None):

        # Create the message
        msg = MIMEText(mensaje)
        msg['To'] = email.utils.formataddr(('Conexión Ciencia', 'hyaoki123@gmail.com'))
        msg['From'] = email.utils.formataddr(('Usuario X', 'comentconexciencia@gmail.com'))
        msg['Subject'] = asunto

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.set_debuglevel(True) # show communication with the server
        try:
            server.ehlo()
            print "primer ehlo"
            server.starttls()
            print "starttls"
            server.ehlo()
            print "segundo ehlo"
            server.login('comentconexciencia@gmail.com', 'conexion123')
            print "login"
            server.sendmail('comentconexciencia@gmail.com', ['hyaoki123@gmail.com'], msg.as_string())
            print "sendmail"
            server.quit()
            print "quit"
            server.close()
            return "Se evió el mensaje con éxito"
        except:
            return "Falló al eviar el mensaje"

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(ConexionCiencia(), "" ,"app.conf")