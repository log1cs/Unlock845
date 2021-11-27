import sqlite3
from pathlib import Path


class DatabaseLockedError(sqlite3.OperationalError):
    def __init__(self, exception_obj, path, browsername='browser'):
        self.path = path
        self.browsername = browsername
        self.exception_obj = exception_obj
    
    def __str__(self):
        return (
            f'\n\nUnable to open database file: `{self.path.name}`\n  for `{self.browsername}` \nat `{self.path.parent}`\n'
            f'Database is locked and in use by some other process.\n'
        )


class TableAccessError(sqlite3.OperationalError, sqlite3.DatabaseError):
    def __init__(self, exception_object, path, tablename):
        self.path = path
        self.tablename = tablename
        self.exception_object = exception_object
    
    def __str__(self):
        return (f'The file {self.path} is not a database '
                f'or does not have the table {self.tablename}.')


# excep = DatabaseLockedError()
# print(excep)
