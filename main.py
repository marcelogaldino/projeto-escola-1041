#!/usr/bin/env python


import os
import webapp2
import jinja2

from google.appengine.ext import db

#Jinja2 Directory Configuration
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


#Default Handler
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class User(db.Model):
  name = db.StringProperty( required = True)
  age = db.IntegerProperty()
  ra = db.IntegerProperty()

class MainHandler(Handler):

    def get(self):
        users = db.GqlQuery('SELECT * FROM User')
        self.render('index.html', users = users)        


    def post(self):
        name = self.request.get('name')
        age = self.request.get('age')
        ra = self.request.get('ra')

        if name and age:
            user = User(name = name, age = int(age), ra = int(ra)
            user.put()

            self.redirect( '/' )

        else:
            self.response.out.write( 'Erro: Ocorreu um erro no cadastro do usuario!' )

class CadastroHandler(Handler):
    def get(self):
        self.render('cadastro.html')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cadastro', CadastroHandler)
], debug=True)
