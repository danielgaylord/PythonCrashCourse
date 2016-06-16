from users import User
from privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name, 'None', 0)
        self.privileges = Privileges(privileges)


admin = Admin("Joe", "Shmoe", ['post', 'not post', 'over all pretty useless'])
admin.privileges.show_privileges()
