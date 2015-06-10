import cgi
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

ENTITY_GROUP_KEY = ndb.Key('Guestbook', 'my_entity_group')


class Post(ndb.Model):
    content = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        posts_query = Post.query(
            ancestor=ENTITY_GROUP_KEY).order(-Post.timestamp)
        posts = posts_query.fetch()

        formatted_posts = cStringIO.StringIO()
        for post in posts:
            formatted_posts.write('<p>{0}</p>\n'.format(post.content))
        self.response.write(PAGE.format(
                existing_posts=formatted_posts.getvalue()))

    def post(self):
        post = Post(parent=ENTITY_GROUP_KEY)
        post.content = cgi.escape(self.request.get('content'))
        post.put()

        self.redirect('/')


app = webapp2.WSGIApplication([
        ('/', MainPage),
])
