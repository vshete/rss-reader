# from django.conf.urls import patterns, include, url
import webapp2

routes = [
	webapp2.Route(r'/', handler='app.index.homeHandler', name='home'),
	webapp2.Route(r'/feed', handler='app.feed.feedHandler', name='feed')
]