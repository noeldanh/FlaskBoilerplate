from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_register(self):
        u = User(username='susan', email='susan@gmail.com')
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
        self.assertEqual(u.username, 'susan')

    def test_user_login(self):
        u = User(username='susan', email='susan@gmail.com')
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

if __name__ == '__main__':
    unittest.main(verbosity=2)