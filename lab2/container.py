


class Container:
    def __init__(self, username):
        self.username = username
        self.container = set()
        self.filename = f'{username}.dat'
        self.users = {username: self.container}

    def add(self, *keys):
        added_keys = self.container.union(keys).difference(self.container)
        not_added_keys = self.container.intersection(keys)
        if added_keys:
            print('Added: ', ', '.join(added_keys))
        if not_added_keys:
            print('Already in the container: ', ', '.join(not_added_keys))
        self.container.update(keys)

    def remove(self, key):
        if key in self.container:
            self.container.remove(key)
            print(key, ' removed from the container.')
        else:
            print(key, 'is not in the container.')

    def find(self, *keys):
        found_keys = self.container.intersection(keys)
        if found_keys:
            print('Items found: ', ', '.join(found_keys))
        else:
            print('No such elements.')