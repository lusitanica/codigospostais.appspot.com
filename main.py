import os

import webapp2

from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, self))

app = webapp2.WSGIApplication([('/', MainPage)])		
