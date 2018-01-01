from pymeistertask.comments import Comment

from .base import BaseTest


class BaseCommentTest(BaseTest):

    def create_comment(self):
        project = self.api.projects.create({'name': 'Test Project'})
        section = self.api.sections.create(project_id=project.id, data={'name': 'Test Section'})
        task = self.api.tasks.create(section_id=section.id, data={'name': 'Test Task'})
        comment = self.api.comments.create(task_id=task.id, data={'text': 'Test Comment'})
        return project, section, task, comment


class TestCommentsAPI(BaseCommentTest):

    def test_create(self):
        with self.recorder.use_cassette('commentsapi_create'):
            project, section, task, comment = self.create_comment()

            assert isinstance(comment, Comment)
            assert type(comment.id) is int
            assert comment.text == 'Test Comment'

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_get(self):
        with self.recorder.use_cassette('commentsapi_get'):
            project, section, task, comment = self.create_comment()
            same_comment = self.api.comments.get(id=comment.id)

            assert isinstance(same_comment, Comment)
            assert comment.id == same_comment.id

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_delete(self):
        with self.recorder.use_cassette('commentsapi_delete'):
            project, section, task, comment = self.create_comment()
            deleted = self.api.comments.delete(id=comment.id)

            assert deleted is True

            self.api.projects.update(id=project.id, data={'status': 4})

    def test_filter_by_task(self):
        with self.recorder.use_cassette('commentsapi_filter_by_task'):
            project, section, task, comment = self.create_comment()
            filtered_comments = self.api.comments.filter_by_task(task_id=task.id)

            assert isinstance(filtered_comments, list)
            assert len(filtered_comments)
            assert all([isinstance(obj, Comment) for obj in filtered_comments])

            self.api.projects.update(id=project.id, data={'status': 4})
