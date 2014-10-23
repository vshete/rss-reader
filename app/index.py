import os
import webapp2
from google.appengine.ext.webapp import template

class homeHandler(webapp2.RequestHandler):
	def get(self):
		template_values = {
			'title': 'Home'
		}
		path = os.path.join(os.path.dirname(__file__), 'views/index.html')
		self.response.out.write(template.render(path, template_values))