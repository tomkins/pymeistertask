from pymeistertask.labels import Label
from pymeistertask.persons import Person
from pymeistertask.projects import Project
from pymeistertask.sections import Section
from pymeistertask.tasks import Task

from .base import BaseTest


class TestProjectsAPI(BaseTest):

    def test_create(self):
        with self.recorder.use_cassette('projectsapi_create'):
            project = self.create_project()

            assert isinstance(project, Project)
            assert type(project.id) is int
            assert project.name == 'Test Project'

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_get(self):
        with self.recorder.use_cassette('projectsapi_get'):
            project = self.create_project()
            same_project = self.api.projects.get(id=project.id)

            assert isinstance(same_project, Project)
            assert project.id == same_project.id

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_update(self):
        with self.recorder.use_cassette('projectsapi_update'):
            project = self.create_project()
            project = self.api.projects.update(id=project.id, data={'name': 'Renamed Project'})

            assert isinstance(project, Project)
            assert project.name == 'Renamed Project'

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_all(self):
        with self.recorder.use_cassette('projectsapi_all'):
            project = self.create_project()
            all_projects = self.api.projects.all()

            assert isinstance(all_projects, list)
            assert len(all_projects)
            assert all([isinstance(obj, Project) for obj in all_projects])

            self.api.projects.update(id=project.id, data={'status': 4})


class TestProject(BaseTest):

    def test_repr(self):
        with self.recorder.use_cassette('project_repr'):
            project = self.create_project()

            assert repr(project) is not None

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_labels(self):
        with self.recorder.use_cassette('project_labels'):
            project = self.api.projects.create({'name': 'Test Project'})
            self.api.labels.create(project_id=project.id, data={'name': 'Test Label'})
            labels = project.labels()

            assert isinstance(labels, list)
            assert len(labels)
            assert all([isinstance(obj, Label) for obj in labels])

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_persons(self):
        with self.recorder.use_cassette('project_persons'):
            project = self.api.projects.create({'name': 'Test Project'})
            persons = project.persons()

            assert isinstance(persons, list)
            assert len(persons)
            assert all([isinstance(obj, Person) for obj in persons])

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_sections(self):
        with self.recorder.use_cassette('project_sections'):
            project = self.api.projects.create({'name': 'Test Project'})
            self.api.sections.create(project_id=project.id, data={'name': 'Test Section'})
            sections = project.sections()

            assert isinstance(sections, list)
            assert len(sections)
            assert all([isinstance(obj, Section) for obj in sections])

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_tasks(self):
        with self.recorder.use_cassette('project_tasks'):
            project = self.api.projects.create({'name': 'Test Project'})
            section = self.api.sections.create(
                project_id=project.id, data={'name': 'Test Section'}
            )
            self.api.tasks.create(section_id=section.id, data={'name': 'Test Task'})

            tasks = project.tasks()

            assert isinstance(tasks, list)
            assert len(tasks)
            assert all([isinstance(obj, Task) for obj in tasks])

            self.api.projects.update(id=project.id, data={'status': 4})
