from pymeistertask.comments import Comment
from pymeistertask.labels import Label
from pymeistertask.tasklabels import TaskLabel
from pymeistertask.tasks import Task

from .base import BaseTest


class TestTasksAPI(BaseTest):
    def test_create(self):
        with self.recorder.use_cassette("tasksapi_create"):
            project, section, task = self.create_task()

            assert isinstance(task, Task)
            assert type(task.id) is int
            assert task.name == "Test Task"

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_get(self):
        with self.recorder.use_cassette("tasksapi_get"):
            project, section, task = self.create_task()
            same_task = self.api.tasks.get(id=task.id)

            assert isinstance(same_task, Task)
            assert task.id == same_task.id

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_update(self):
        with self.recorder.use_cassette("tasksapi_update"):
            project, section, task = self.create_task()
            task = self.api.tasks.update(id=task.id, data={"name": "Renamed Task"})

            assert isinstance(task, Task)
            assert task.name == "Renamed Task"

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_all(self):
        with self.recorder.use_cassette("tasksapi_all"):
            project, section, task = self.create_task()
            all_tasks = self.api.tasks.all()

            assert isinstance(all_tasks, list)
            assert len(all_tasks)
            assert all([isinstance(obj, Task) for obj in all_tasks])

            self.api.projects.update(id=project.id, data={"status": 4})


class TestTask(BaseTest):
    def test_repr(self):
        with self.recorder.use_cassette("task_repr"):
            project, section, task = self.create_task()

            assert repr(task) is not None

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_comments(self):
        with self.recorder.use_cassette("task_comments"):
            project, section, task = self.create_task()
            self.api.comments.create(task_id=task.id, data={"text": "Test Comment"})

            comments = task.comments()

            assert isinstance(comments, list)
            assert len(comments)
            assert all([isinstance(obj, Comment) for obj in comments])

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_labels(self):
        with self.recorder.use_cassette("task_labels"):
            project, section, task = self.create_task()
            label = self.api.labels.create(project_id=project.id, data={"name": "Test Label"})
            self.api.tasklabels.create(task_id=task.id, data={"label_id": label.id})

            labels = task.labels()

            assert isinstance(labels, list)
            assert len(labels)
            assert all([isinstance(obj, Label) for obj in labels])

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_tasklabels(self):
        with self.recorder.use_cassette("task_tasklabels"):
            project, section, task, tasklabel = self.create_tasklabel()

            tasklabels = task.tasklabels()

            assert isinstance(tasklabels, list)
            assert len(tasklabels)
            assert all([isinstance(obj, TaskLabel) for obj in tasklabels])

            self.api.projects.update(id=project.id, data={"status": 4})
