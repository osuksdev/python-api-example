# project/tests/conftest.py

import pytest
from project import app, db

@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app # this is where the testing happens

@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db # this is where the testing happens
    db.session.remove()
    db.drop_all()
