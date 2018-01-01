from pymeistertask.persons import Person

from .base import BaseTest


class TestPersonsAPI(BaseTest):

    def test_me(self):
        with self.recorder.use_cassette('persons_me'):
            me = self.api.persons.me()

            assert isinstance(me, Person)
            assert type(me.id) is int
            assert me.email == self.meistertask_email

    def test_get(self):
        with self.recorder.use_cassette('persons_get'):
            me = self.api.persons.me()
            person = self.api.persons.get(id=me.id)

            assert isinstance(person, Person)
            assert me.id == person.id

    def test_all(self):
        with self.recorder.use_cassette('persons_all'):
            all_people = self.api.persons.all()

            assert isinstance(all_people, list)
            assert len(all_people)
            assert all([isinstance(obj, Person) for obj in all_people])


class TestPerson(BaseTest):

    def test_repr(self):
        with self.recorder.use_cassette('persons_me'):
            me = self.api.persons.me()

            assert repr(me) is not None
