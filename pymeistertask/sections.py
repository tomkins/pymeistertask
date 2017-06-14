from .resource import Resource, ResourceAPI


class Section(Resource):
    _repr_attrs = ('id', 'project_id', 'name')

    def tasks(self, **kwargs):
        return self.api.tasks.filter_by_section(section_id=self.id, **kwargs)


class SectionsAPI(ResourceAPI):
    _resource = Section

    def create(self, project_id, data):
        return self._create_object(
            url='/projects/{project_id}/sections'.format(project_id=project_id),
            data=data,
        )

    def get(self, id):
        return self._get_object(url='/sections/{id}'.format(id=id))

    def update(self, id, data):
        return self._update_object(url='/sections/{id}'.format(id=id), data=data)

    def all(self):
        return self._get_list(url='/sections')

    def filter_by_project(self, project_id):
        return self._get_list(url='/projects/{project_id}/sections'.format(project_id=project_id))
