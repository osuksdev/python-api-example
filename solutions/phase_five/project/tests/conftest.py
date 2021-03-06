# project/tests/conftest.py

import pytest
from project import create_app, db
from project.api.models import User

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app # this is where the testing happens

@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db # this is where the testing happens
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='function')
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    return _add_user
