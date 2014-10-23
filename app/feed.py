import os
import webapp2
from google.appengine.ext.webapp import template
import feedparser

class feedHandler(webapp2.RequestHandler):
	def get(self):
		rss_url = self.request.get('url')
		
		if len(rss_url) == 0 or len(rss_url.strip(' ')) == 0:
			return webapp2.redirect('/')
		
		d = feedparser.parse(rss_url)
		
		if bool(d['entries']) == False:
			return webapp2.redirect('/')
		
		feedLeft = []
		feedRight = []
		i = 0

		for entry in d['entries']:
			if i==0:
				feedLeft.append(entry)
				i = 1
			else:
				feedRight.append(entry)
				i = 0

		template_values = {
			'title'    : 'Feed',
            'feedLeft' : feedLeft,
            'feedRight': feedRight
        }

		path = os.path.join(os.path.dirname(__file__), 'views/feed.html')
		self.response.out.write(template.render(path, template_values))