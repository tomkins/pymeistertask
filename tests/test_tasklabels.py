from pymeistertask.tasklabels import TaskLabel

from .base import BaseTest


class TestTaskLabelsAPI(BaseTest):

    def test_create(self):
        with self.recorder.use_cassette('tasklabelsapi_create'):
            project, section, task, tasklabel = self.create_tasklabel()

            assert isinstance(tasklabel, TaskLabel)
            assert type(tasklabel.id) is int

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_get(self):
        with self.recorder.use_cassette('tasklabelsapi_get'):
            project, section, task, tasklabel = self.create_tasklabel()
            same_tasklabel = self.api.tasklabels.get(id=tasklabel.id)

            assert isinstance(same_tasklabel, TaskLabel)
            assert tasklabel.id == same_tasklabel.id

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_delete(self):
        with self.recorder.use_cassette('tasklabelsapi_delete'):
            project, section, task, tasklabel = self.create_tasklabel()
            deleted = self.api.tasklabels.delete(id=tasklabel.id)

            assert deleted is True

            self.api.projects.update(id=project.id, data={'status': 4})


class TestTaskLabel(BaseTest):

    def test_repr(self):
        with self.recorder.use_cassette('tasklabel_repr'):
            project, section, task, tasklabel = self.create_tasklabel()

            assert repr(tasklabel) is not None

            self.api.projects.update(id=project.id, data={'status': 4})
