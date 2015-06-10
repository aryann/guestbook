import webapp2

PAGE = """\
<!doctype html>
<html>
  <body>
    <form action="/" method="POST">
      <textarea name="content" rows="5" cols="60"></textarea>
      <input type="submit" value="Sign!" />
    </form>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(PAGE)


app = webapp2.WSGIApplication([
        ('/', MainPage),
])
