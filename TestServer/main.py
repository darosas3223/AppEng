from google.appengine.api import images
from google.appengine.ext import ndb
from models import Note
import webapp2

import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('./submit.html')
        self.response.out.write(template.render())

    def post(self):
        console.log("Done.")


class InfoHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_env.get_template('./main.html')
        self.response.out.write(template.render())

        descr = self.request.get('desc')

        if descr == None:
            print("There's nothing in here. ")

    def post(self):
        print("Done.")

        note = Note(
                img = self.request.get('img'), 
                describe = self.request.get('desc'),
                )

        note.put()
        
        template = jinja_env.get_template('./submit.html')
        self.response.out.write(template.render())

class Note(ndb.Model):
    img = ndb.BlobProperty()
    describe = ndb.StringProperty()


app = webapp2.WSGIApplication([
    ('/', InfoHandler),
    ('/sub', MainHandler),
    ('/view', InfoHandler),
], debug=True)
