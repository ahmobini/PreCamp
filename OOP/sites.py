from users import User, UserManager


class Site:
    def __init__(self, url):
        self.registered_users = []
        self.active_users = []
        self.url = url

    def register(self, user_name):
        user = user_name if user_name in self.registered_users else None
        if user is not None:
            raise Exception('user already registered.')
        self.registered_users.append(user_name)
        print('register successful.')

    def login(self, password, **kwargs):
        keys = list(kwargs.keys())
        assert 'username' in keys or 'email' in keys, 'you cant login without passing username or email.'
        _user = None
        try:
            users = list(filter(lambda user: getattr(user, 'email', None) ==
                                kwargs['email'] and getattr(user, 'username', None) == kwargs['username'], self.registered_users))
        except Exception:
            users = list(filter(lambda user: getattr(user, keys[0], None) ==
                                kwargs[keys[0]], self.registered_users))
        finally:
            _user = users[0] if users else None
            if all([_user is not None, UserManager.compare_password(_user.password, bytes(password, 'utf-8'))]):
                if _user not in self.active_users:
                    self.active_users.append(users[0])
                    print('logged in')
                else:
                    print('user is already logged in')
            else:
                print('user not found')

    def logout(self, username):
        if username not in self.active_users:
            raise Exception('user not logged in.')
        self.active_users.remove(username)
        print('logged out')


if __name__ == '__main__':
    site = Site('shalghamkala.com')
    user = User('alireza_helali', '09163311945',
                'a.helali1995@gmail.com', "A.helali1995")

    site.register(user)
    site.login("A.helali1995", username="alireza_helali")
    print(site.active_users)
