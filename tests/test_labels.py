from pymeistertask.labels import Label

from .base import BaseTest


class TestLabelsAPI(BaseTest):
    def test_create(self):
        with self.recorder.use_cassette("labelsapi_create"):
            project, label = self.create_label()

            assert isinstance(label, Label)
            assert type(label.id) is int
            assert label.name == "Test Label"

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_get(self):
        with self.recorder.use_cassette("labelsapi_get"):
            project, label = self.create_label()
            same_label = self.api.labels.get(id=label.id)

            assert isinstance(same_label, Label)
            assert label.id == same_label.id

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_update(self):
        with self.recorder.use_cassette("labelsapi_update"):
            project, label = self.create_label()
            label = self.api.labels.update(id=label.id, data={"name": "Renamed Label"})

            assert isinstance(label, Label)
            assert label.name == "Renamed Label"

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_delete(self):
        with self.recorder.use_cassette("labelsapi_delete"):
            project, label = self.create_label()
            deleted = self.api.labels.delete(id=label.id)

            assert deleted is True

            self.api.projects.update(id=project.id, data={"status": 4})


class TestLabel(BaseTest):
    def test_repr(self):
        with self.recorder.use_cassette("label_repr"):
            project, label = self.create_label()

            assert repr(label) is not None

            self.api.projects.update(id=project.id, data={"status": 4})
