from .resource import Resource, ResourceAPI


class Label(Resource):
    _repr_attrs = ('id', 'project_id', 'name')


class LabelsAPI(ResourceAPI):
    _resource = Label

    def create(self, project_id, data):
        return self._create_object(
            url='/projects/{project_id}/labels'.format(project_id=project_id),
            data=data,
        )

    def get(self, id):
        return self._get_object(url='/labels/{id}'.format(id=id))

    def update(self, id, data):
        return self._update_object(url='/labels/{id}'.format(id=id), data=data)

    def delete(self, id):
        return self._delete_object(url='/labels/{id}'.format(id=id))

    def filter_by_project(self, project_id):
        return self._get_list(url='/projects/{project_id}/labels'.format(project_id=project_id))

    def filter_by_task(self, task_id):
        return self._get_list(url='/tasks/{task_id}/labels'.format(task_id=task_id))
