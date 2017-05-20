from .resource import Resource, ResourceAPI


class Project(Resource):
    _repr_attrs = ('id', 'name')

    def labels(self):
        return self.api.labels.filter_by_project(project_id=self.id)

    def persons(self):
        return self.api.persons.filter_by_project(project_id=self.id)

    def sections(self):
        return self.api.sections.filter_by_project(project_id=self.id)

    def tasks(self, **kwargs):
        return self.api.tasks.filter_by_project(project_id=self.id, **kwargs)


class ProjectsAPI(ResourceAPI):
    _resource = Project

    def create(self, data):
        return self._create_object(url='/projects', data=data)

    def get(self, id):
        return self._get_object(url='/projects/{id}'.format(id=id))

    def update(self, id, data):
        return self._update_object(url='/projects/{id}'.format(id=id), data=data)

    def all(self, **kwargs):
        return self._get_list(url='/projects', **kwargs)
