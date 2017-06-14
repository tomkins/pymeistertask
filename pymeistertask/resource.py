API_URL = 'https://www.meistertask.com/api{url}'


class Resource(object):
    _repr_attrs = None

    def __init__(self, api, attributes=None):
        self.api = api

        if attributes is None:
            attributes = {}

        self._setattrs = []
        for key, val in attributes.items():
            setattr(self, key, val)
            self._setattrs.append(key)

        super().__init__()

    def __repr__(self):
        repr_attrs = self._repr_attrs or self._setattrs

        repr_list = []
        for attr in repr_attrs:
            if hasattr(self, attr):
                repr_list.append('{}: {!r}'.format(attr, getattr(self, attr)))

        resource_repr = ', '.join(repr_list)
        return '<%s {%s} at %d>' % (self.__class__.__name__, resource_repr, id(self))

    def __iter__(self):
        for attr in self._setattrs:
            yield attr, getattr(self, attr)


class ResourceAPI(object):
    _resource = None

    def __init__(self, api):
        self.api = api
        super().__init__()

    def _get_list(self, url, **kwargs):
        r = self.api.session.get(API_URL.format(url=url), params=kwargs)
        r.raise_for_status()
        json = r.json()
        object_list = [self._resource(api=self.api, attributes=attrs) for attrs in json]
        return object_list

    def _get_object(self, url):
        r = self.api.session.get(API_URL.format(url=url))
        r.raise_for_status()
        json = r.json()
        obj = self._resource(api=self.api, attributes=json)
        return obj

    def _create_object(self, url, data):
        r = self.api.session.post((API_URL.format(url=url)), data=data)
        r.raise_for_status()
        json = r.json()
        obj = self._resource(api=self.api, attributes=json)
        return obj

    def _update_object(self, url, data):
        r = self.api.session.put((API_URL.format(url=url)), data=data)
        r.raise_for_status()
        json = r.json()
        obj = self._resource(api=self.api, attributes=json)
        return obj

    def _delete_object(self, url):
        r = self.api.session.delete((API_URL.format(url=url)))
        r.raise_for_status()
        return True
