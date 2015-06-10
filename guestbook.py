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
        # Don't do this! The user's input needs to be sanitized before
        # writing it back out, otherwise, a whole host of security
        # vulnerabilities can be exploited.
        POSTS.append(self.request.get('content'))

        self.redirect('/')


app = webapp2.WSGIApplication([
        ('/', MainPage),
])
