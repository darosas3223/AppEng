from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
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
            
        if self.request.get('img'):
        	photo = Photo.get_by_id(int(self.request.get('img')))

    def post(self):
        print("Done.")

        note = Note(
                img = self.request.get('img'), 
                describe = self.request.get('desc'),
                )

        note.put()
        
        template = jinja_env.get_template('./submit.html')
        self.response.out.write(template.render())

		
class ViewInfo(webapp2.RequestHandler):
	def _render_template(self, template_name, context = None):
		if context is None:
			context = {}
		
	def get(self):
		qry = Note.owner_query()
		context['notes'] = qry.fetch
		template_name = jinja_env.get_template('./view.html')
		return template.render(context)
		

class Note(ndb.Model):
    img = ndb.BlobProperty()
    describe = ndb.StringProperty()
    
    @classmethod
    def owner_query(cls):
        return cls.query().order(
            cls.date_created)


app = webapp2.WSGIApplication([
    ('/', InfoHandler),
    ('/sub', MainHandler),
    ('/view', InfoHandler),
    ('/viewinfo', ViewInfo),
], debug=True)
