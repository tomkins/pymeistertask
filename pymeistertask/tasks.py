from .resource import Resource, ResourceAPI


class Task(Resource):
    _repr_attrs = ('id', 'section_id', 'name')

    def comments(self):
        return self.api.comments.filter_by_task(task_id=self.id)

    def labels(self):
        return self.api.labels.filter_by_task(task_id=self.id)

    def tasklabels(self):
        return self.api.tasklabels.filter_by_task(task_id=self.id)


class TasksAPI(ResourceAPI):
    _resource = Task

    def create(self, section_id, data):
        return self._create_object(
            url='/sections/{section_id}/tasks'.format(section_id=section_id),
            data=data,
        )

    def get(self, id):
        return self._get_object(url='/tasks/{id}'.format(id=id))

    def update(self, id, data):
        return self._update_object(url='/tasks/{id}'.format(id=id), data=data)

    def all(self, **kwargs):
        return self._get_list(url='/tasks', **kwargs)

    def filter_by_project(self, project_id, **kwargs):
        return self._get_list(
            url='/projects/{project_id}/tasks'.format(project_id=project_id), **kwargs
        )

    def filter_by_section(self, section_id, **kwargs):
        return self._get_list(
            url='/sections/{section_id}/tasks'.format(section_id=section_id), **kwargs
        )
