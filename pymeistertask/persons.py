from .resource import Resource, ResourceAPI


class Person(Resource):
    _repr_attrs = ('id', 'firstname', 'lastname', 'email')


class PersonsAPI(ResourceAPI):
    _resource = Person

    def get(self, id):
        return self._get_object(url='/sections/{id}'.format(id=id))

    def all(self):
        return self._get_list(url='/persons')

    def filter_by_project(self, project_id):
        return self._get_list(url='/projects/{project_id}/persons'.format(project_id=project_id))

    def me(self):
        return self._get_object(url='/persons/me')
