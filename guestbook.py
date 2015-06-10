import cStringIO
import webapp2

PAGE = """\
<!doctype html>
<html>
  <body>
    <form action="/" method="POST">
      <textarea name="content" rows="5" cols="60"></textarea>
      <input type="submit" value="Sign!" />
    </form>
    {existing_posts}
  </body>
</html>
"""

POSTS = []


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        formatted_posts = cStringIO.StringIO()
        for post in POSTS:
            formatted_posts.write('    <p>{0}</p>\n'.format(post))
        self.response.write(PAGE.format(
                existing_posts=formatted_posts.getvalue()))

    def post(self):
        POSTS.append(self.request.get('content'))
        self.redirect('/')


app = webapp2.WSGIApplication([
        ('/', MainPage),
])
