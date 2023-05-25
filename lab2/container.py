import re
import pickle


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

    def list(self):
        if self.container:
            print('All elements in the container:')
            for element in self.container:
                print(element)
        else:
            print('Container is empty.')

    def grep(self, regex, ignor_case=False):
        if ignor_case:
            pattern = re.compile(regex, re.IGNORECASE)
        else:
            pattern = re.compile(regex)

        matches = [key for key in self.container if re.search(pattern, key)]

        if matches:
            print('Matches found:')
            for element in matches:
                print(element)
        else:
            print('No such elements.')

    def save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.container, file)
        print('Container saved to ', self.filename)     

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                self.container = pickle.load(file)
            print(self.username, '\'s container loaded.')
        except FileNotFoundError:
            print('No saved container for ', self.username)   

    def username_check(self, username):
        if username in self.users.keys():
            return True
        else:
            return False
        
    def new_user(self, username):
        if not self.username_check(username):
            self.users[username] = set()
            self.container = self.users[username]
            self.username = username
            self.filename = f'{username}.dat'
            print(f'Container of user {username} has been successfully loaded.')

    def switch(self, username):
        if not re.findall(r'\b[A-z]\w+\b', username):
            print('Incorrect name.')
            return

        if self.username_check(username):
            print('Load? (y/n):')
            while True:
                answer = input('> ')
                if answer == 'y' or answer == 'Y':
                    self.container = self.users[username]
                    print(f'Container of user {username} has been successfully loaded.')
                    break
                elif answer == 'n' or answer == 'N':
                    self.container = set()
                    break
            self.username = username
            self.filename = f'{username}.dat'
        else:
            print('This user does not exist. Would you like to create one? (y/n):')
            while True:
                answer = input('> ')
                if answer == 'y' or answer == 'Y':
                    self.new_user(username)
                    break
                elif answer == 'n' or answer == 'N':
                    print(f'Staying in the container {self. username}.')
                    break
