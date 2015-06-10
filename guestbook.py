import cStringIO
import webapp2

from google.appengine.ext import ndb


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

class Post(ndb.Model):
    content = ndb.StringProperty()


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        posts_query = Post.query()
        posts = posts_query.fetch()

        formatted_posts = cStringIO.StringIO()
        for post in posts:
            formatted_posts.write('    <p>{0}</p>\n'.format(post.content))
        self.response.write(PAGE.format(
                existing_posts=formatted_posts.getvalue()))

    def post(self):
        # Don't do this! The user's input needs to be sanitized before
        # writing it back out, otherwise, a whole host of security
        # vulnerabilities can be exploited.
        post = Post()
        post.content = self.request.get('content')
        post.put()

        self.redirect('/')


app = webapp2.WSGIApplication([
        ('/', MainPage),
])
