import unittest

import betamax
import pytest

from pymeistertask.api import MeisterTaskAPI


@pytest.mark.usefixtures('betamax_record', 'meistertask_settings')
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.api = MeisterTaskAPI(bearer_token=self.meistertask_token)
        default_cassette_options = {}
        if self.record is True:
            default_cassette_options['record_mode'] = 'once'
        self.recorder = betamax.Betamax(
            self.api.session, default_cassette_options=default_cassette_options
        )

    def create_project(self):
        project = self.api.projects.create({'name': 'Test Project'})
        return project

    def create_section(self):
        project = self.create_project()
        section = self.api.sections.create(project_id=project.id, data={'name': 'Test Section'})
        return project, section

    def create_label(self, project=None):
        if project is None:
            project = self.create_project()
        label = self.api.labels.create(project_id=project.id, data={'name': 'Test Label'})
        return project, label

    def create_task(self):
        project, section = self.create_section()
        task = self.api.tasks.create(section_id=section.id, data={'name': 'Test Task'})
        return project, section, task

    def create_tasklabel(self):
        project, section, task = self.create_task()
        project, label = self.create_label(project=project)
        tasklabel = self.api.tasklabels.create(task_id=task.id, data={'label_id': label.id})
        return project, section, task, tasklabel
