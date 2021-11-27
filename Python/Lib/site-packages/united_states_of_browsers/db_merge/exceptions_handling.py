import errno

from united_states_of_browsers.db_merge.custom_exceptions import *
from united_states_of_browsers.db_merge.imported_annotations import *

def invalid_path_in_tree(path_to_test: PathInfo) -> AnyStr:
    """ Accepts a path and returns the first invalid parent.
    """
    path_to_test = Path(path_to_test)
    first_invalid_path_in_tree = [path_parent for path_parent in path_to_test.parents if
                                  not path_parent.exists() or not path_parent.is_dir()]
    return first_invalid_path_in_tree[-1] if first_invalid_path_in_tree else None


def remove_new_empty_files(dirpath: PathInfo, existing_files: Iterable[Text]) -> None:
    """ Deletes any newly created files of size zero. Useful in removing files created during an aborted process.
    Accepts the directory where the files are present and the list of files in it before the process was initiated.
    """
    dirpath = Path(dirpath)
    files_post_connection_attempt = set(entry for entry in dirpath.iterdir() if entry.is_file())
    extra_files = files_post_connection_attempt.difference(existing_files)
    [file_.unlink() for file_ in extra_files if file_.stat().st_size == 0]


def exceptions_log_deduplicator(exceptions_log: Iterable):
    unique_exception_strings = {str(excep_): excep_ for excep_ in exceptions_log}
    return list(unique_exception_strings.values())


def determine_table_access_exception(exception_obj: Exception, calling_obj: object) -> Exception:
    """ Determines if the passed in exceptions is related to problems with accessing a db table.
    Returns a TableAccessError is yes, original exception if not.
    Processes them in OS agnostic manner.
     (Unix systems raise sqlite3.OperationalError: no such table
     Windows systems raise sqlite3.DatabaseError: file is not a database.)
     """
    tablename = calling_obj['table']
    path = calling_obj['path']
    
    msg = str(exception_obj).lower()
    
    if 'no such table' in msg or 'file is not a database' in msg:
        return TableAccessError(exception_obj, path, tablename)
    else:
        return exception_obj
