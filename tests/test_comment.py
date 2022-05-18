import unittest
from app.models import Comments, User
from app import db

class CommentTest(unittest.TestCase):
    '''
    Test Test Class to test the behaviour of the Comment class
    '''
    def setUp(self):
        self.user_John_Doe = User(username = 'John Doe', password = 'qwerty900', email = 'johndoe@gmail.com',
        profile_pi_path = 'https://image.tmdb.org/t/p/w500/jdjdjdjn', blog = 'talk is cheap show me the codes')
        self.new_comment = Comments(comment_id=1234  , comment = 'Thoughts on Atom? Anyone?', user_id = 1234, blog_id=12345, time = '12,02,2021',)

    def tearDown(self):
        Comments.Clear_comments()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_id, 'Lovely')
        self.assertEquals(self.new_comment.comment, 'Thoughts on Atom? Anyone?')
       
        self.assertEquals(self.new_comment.user_id, 1234)
        self.assertEquals(self.new_comment.blog_id, 1234)

        self.assertEquals(self.new_comment.time, '12,02,2021')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all() > 0))

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comments.get_comment(1234)
        self.assertTrue(len(got_comments) == 1)