from pymeistertask.sections import Section
from pymeistertask.tasks import Task

from .base import BaseTest


class TestSectionsAPI(BaseTest):
    def test_create(self):
        with self.recorder.use_cassette("sectionsapi_create"):
            project, section = self.create_section()

            assert isinstance(section, Section)
            assert type(section.id) is int
            assert section.name == "Test Section"

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_get(self):
        with self.recorder.use_cassette("sectionsapi_get"):
            project, section = self.create_section()
            same_section = self.api.sections.get(id=section.id)

            assert isinstance(same_section, Section)
            assert section.id == same_section.id

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_update(self):
        with self.recorder.use_cassette("sectionsapi_update"):
            project, section = self.create_section()
            section = self.api.sections.update(id=section.id, data={"name": "Renamed Section"})

            assert isinstance(section, Section)
            assert section.name == "Renamed Section"

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_all(self):
        with self.recorder.use_cassette("sectionsapi_all"):
            project, section = self.create_section()
            all_sections = self.api.sections.all()

            assert isinstance(all_sections, list)
            assert len(all_sections)
            assert all([isinstance(obj, Section) for obj in all_sections])

            self.api.projects.update(id=project.id, data={"status": 4})


class TestSection(BaseTest):
    def test_repr(self):
        with self.recorder.use_cassette("section_repr"):
            project, section = self.create_section()

            assert repr(section) is not None

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_tasks(self):
        with self.recorder.use_cassette("section_tasks"):
            project, section = self.create_section()
            self.api.tasks.create(section_id=section.id, data={"name": "Test Task"})

            tasks = section.tasks()

            assert isinstance(tasks, list)
            assert len(tasks)
            assert all([isinstance(obj, Task) for obj in tasks])

            self.api.projects.update(id=project.id, data={"status": 4})
