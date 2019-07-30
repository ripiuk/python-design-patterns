"""
Borg - is a way to implement singleton behavior,
but instead of having only one instance of a class,
there are multiple instances that share the same state.
"""


class SQLDatabase:
    __shared_status = {}

    def __init__(self):
        self.__dict__ = self.__shared_status
        self.status = 'not connected'

    def __str__(self):
        return self.status


class PostreSQL(SQLDatabase):
    pass


if __name__ == '__main__':
    db1 = SQLDatabase()
    db2 = SQLDatabase()

    db1.status = 'connecting'
    db2.status = 'connected'

    print('db1: {}, db2: {}'.format(db1, db2))
    print(id(db1) == id(db2))

    db3 = PostreSQL()

    print('db1: {}, db2: {}, db3: {}'.format(db1, db2, db3))


# ================ Output ================
# db1: connected, db2: connected
# False
# db1: not connected, db2: not connected, db3: not connected
