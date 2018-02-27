from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Book
from config import Config
# import requests

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        # print (self.client)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_user_register(self):
        # res = self.client().post('/auth/register', data=dict(id=1, username="susan", email="test@gmail.com", password_hash="test"))
        # self.assertEqual(res.status_code, 200)
        # res = self.client().post('/books/add', data=dict(id=1, title="susan", author="test@gmail.com", review="test", rating=1))

        self.assertEqual(res.status_code, 200)

    def test_user_login(self):
        u = User(username='susan', email='susan@gmail.com')
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))




if __name__ == '__main__':
    unittest.main(verbosity=2)
