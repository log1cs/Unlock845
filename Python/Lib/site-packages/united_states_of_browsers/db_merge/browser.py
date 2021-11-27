# -*- encoding: utf-8 -*-
"""
Module containing fucntions to setup browser profile paths,
database file paths, and generator for browser records.
"""
from collections import namedtuple

from united_states_of_browsers.db_merge import exceptions_handling
from united_states_of_browsers.db_merge.imported_annotations import *
from united_states_of_browsers.db_merge.table import Table

TableMetadata = namedtuple('TableMetadata', 'browser profile file table')


def make_browser_records_yielder(browser: Text,
                                 profile_root: PathInfo,
                                 filename: Text,
                                 tablename: Text,
                                 profiles: Optional[Iterable[Text]] = None,
                                 fieldnames: Optional[Iterable[Text]] = None,
                                 copies_subpath: Optional[PathInfo] = None
                                 ) -> Generator[Mapping[Text, Text], None, None]:
    """ Creates a generator of browser database records.

    :param browser: browser name
    :param profile_root: path to directory/folder
            where the browser stores all of its profiles
    :param profiles: list of profile, default is all profiles
    :param fieldnames: Optional list of fieldnames for which data is to be retrieved.
    :param copies_subpath: path where a copy of the database files is created,
            and read from,instead of the original files.

    :return: Generator of records
    """
    paths = make_browser_paths(browser, profile_root, profiles)
    for profile_name, profile_path in paths.items():
        filepath = Path(profile_path, filename)
        profile_name = Path(profile_path).name
        table_obj = Table(table=tablename,
                          path=filepath,
                          browser=browser,
                          filename=filename,
                          profile=profile_name,
                          copies_subpath=copies_subpath,
                          )
        additional_info = {'browser': browser, 'profile': profile_name,
                           'file': filename, 'table': tablename,
                           }
        table_obj.make_records_yielder()
        if fieldnames:
            for record in table_obj.records_yielder:
                record = {field_name: field_value for
                          field_name, field_value in record.items() if
                          field_name in fieldnames}
                record.update(additional_info)
                yield record
        else:
            for record in table_obj.records_yielder:
                record.update(additional_info)
                yield record


def _make_firefox_profile_paths(profile_root: PathInfo, profiles: Iterable[Text]) -> Mapping[Text, PathInfo]:
    """
    Makes a dict of profile names and paths for Chrome broser.

    :param profile_root: Path where the specific browser stores
            all the profile directoris.
    :param profiles: List of profile names whose path is to be made.
            None gives path for all profiles detected.

    :return: Dict of profile names and corresponding path.
    """

    get_profile_name = lambda dir_entry: str(dir_entry).split(sep='.', maxsplit=1)[1]
    if profiles:
        profilepaths = {profile: entry for entry in profile_root.iterdir()
                             for profile in profiles
                             if '.' in entry.name and entry.is_dir() and entry.name.endswith(profile)
                             }
    else:
        profilepaths = {get_profile_name(entry): entry
                             for entry in profile_root.iterdir()
                             if '.' in entry.name and entry.is_dir()}
    return profilepaths


def _make_chrome_profile_paths(profile_root: PathInfo, profiles: Iterable[Text]) -> Mapping[Text, PathInfo]:
    """
    Makes a dict of profile names and paths for Chrome broser.

    :param profile_root: Path where the specific browser stores
            all the profile directoris.
    :param profiles: List of profile names whose path is to be made.
            None gives path for all profiles detected.

    :return: Dict of profile names and corresponding path.
    """
    if profiles:
        profilepaths = {entry.name: entry
                             for profile_name in profiles
                             for entry in profile_root.iterdir()
                             if entry.name.endswith(profile_name)}
    else:
        profilepaths = {entry.name: entry for entry in profile_root.iterdir()
                             if entry.name.startswith('Profile') or entry.name == 'Default'}
    return profilepaths


def make_browser_paths(browser: Text, profile_root: PathInfo, profiles: Iterable[Text]) -> Mapping[Text, PathInfo]:
    """
    Makes a dict of profile names and paths.

    :param browser: Browser name [ 'firefox', 'chrome'] .
    :param profile_root: Path where the specific browser stores
            all the profile directoris.
    :param profiles: List of profile names whose path is to be made.
            None gives path for all profiles detected.
            
    :return: Dict of profile names and corresponding path.
    """
    make_path_chooser = {'firefox': _make_firefox_profile_paths, 'chrome': _make_chrome_profile_paths,
                         'opera': _make_chrome_profile_paths, 'vivaldi': _make_chrome_profile_paths,
                         }
    try:
        profilepaths = make_path_chooser[browser](profile_root, profiles)
    except FileNotFoundError as excep:
        invalid_path = exceptions_handling.invalid_path_in_tree(excep.filename)
        # print(f'In {excep.filename},\npath {invalid_path} does not exist.\nMoving on...')
        raise excep
    else:
        return profilepaths
