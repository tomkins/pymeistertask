from .resource import Resource, ResourceAPI


class TaskLabel(Resource):
    _repr_attrs = ('id', 'task_id', 'label_id')


class TaskLabelsAPI(ResourceAPI):
    _resource = TaskLabel

    def create(self, task_id, data):
        return self._create_object(
            url='/tasks/{task_id}/task_labels'.format(task_id=task_id),
            data=data,
        )

    def get(self, id):
        return self._get_object(url='/task_labels/{id}'.format(id=id))

    def delete(self, id):
        return self._delete_object(url='/task_labels/{id}'.format(id=id))

    def filter_by_task(self, task_id):
        return self._get_list(url='/tasks/{task_id}/task_labels'.format(task_id=task_id))
