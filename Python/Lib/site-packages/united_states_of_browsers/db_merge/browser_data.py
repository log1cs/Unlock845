import os

from collections import namedtuple
from pathlib import Path

BrowserData = namedtuple('BrowserData',
                         'os browser path profiles file_tables table_fields')


def prep_browsers_info(parent_dir='~'):
    parent_dir = Path(parent_dir).expanduser()
    if os.name == 'nt':
        return _windows_browser_info(parent_dir)
    elif os.name == 'posix':
        return _linux_browser_info(parent_dir)


def _windows_browser_info(parent_dir):
    return [BrowserData(os='nt',
                        browser='firefox',
                        path=parent_dir.joinpath('AppData', 'Roaming',
                                                 'Mozilla', 'Firefox',
                                                 'Profiles'),
                        profiles=None,
                        file_tables={'places.sqlite': ['moz_places']},
                        table_fields={
                            'moz_places': ['id', 'url', 'title', 'visit_count',
                                           'last_visit_date',
                                           'last_visit_readable']
                            },
                        ),
            BrowserData(os='nt',
                        browser='chrome',
                        path=parent_dir.joinpath('AppData', 'Local', 'Google',
                                                 'Chrome', 'User Data'),
                        profiles=None,
                        file_tables={'history': ['urls']},
                        table_fields={
                            'urls': ['id', 'url', 'title', 'visit_count',
                                     'last_visit_time',
                                     'last_visit_readable']
                            },
                        ),
            BrowserData(os='nt',
                        browser='opera',
                        path=parent_dir.joinpath('AppData', 'Roaming',
                                                 'Opera Software'),
                        profiles=None,
                        file_tables={'History': ['urls']},
                        table_fields={
                            'urls': ['id', 'url', 'title', 'visit_count',
                                     'last_visit_time',
                                     'last_visit_readable']
                            },
                        ),
            BrowserData(os='nt',
                        browser='vivaldi',
                        path=parent_dir.joinpath('AppData', 'Local', 'Vivaldi',
                                                 'User Data'),
                        profiles=None,
                        file_tables={'History': ['urls']},
                        table_fields={
                            'urls': ['id', 'url', 'title', 'visit_count',
                                     'last_visit_time',
                                     'last_visit_readable']
                            },
                        ),
            ]


def _linux_browser_info(parent_dir):
    return [BrowserData(os='posix',
                        browser='firefox',
                        path=parent_dir.joinpath('.mozilla', 'firefox'),
                        profiles=None,
                        file_tables={'places.sqlite': ['moz_places']},
                        table_fields={
                            'moz_places': ['id', 'url', 'title', 'visit_count',
                                           'last_visit_date',
                                           'last_visit_readable']
                            },
                        ),
            BrowserData(os='posix',
                        browser='chrome',
                        path=parent_dir.joinpath('.config', 'google-chrome'),
                        profiles=None,
                        file_tables={'History': ['urls']},
                        table_fields={
                            'urls': ['id', 'url', 'title', 'visit_count',
                                     'last_visit_time',
                                     'last_visit_readable']
                            },
                        ),
            # BrowserData(os='nt',
            #             browser='opera',
            #             path=parent_dir.joinpath('AppData','Roaming',
            #                                      'Opera Software'),
            #             profiles=None,
            #             file_tables={'History': ['urls']},
            #             table_fields={'urls': ['id', 'url', 'title',
            #                                    'visit_count',
            #                                    'last_visit_time',
            #                                    'last_visit_readable']},
            #             ),
            # BrowserData(os='nt',
            #             browser='vivaldi',
            #             path=parent_dir.joinpath('AppData','Local','Vivaldi',
            #                                      'User Data'),
            #             profiles=None,
            #             file_tables={'History': ['urls']},
            #             table_fields={'urls': ['id', 'url', 'title',
            #                                    'visit_count',
            #                                    'last_visit_time',
            #                                    'last_visit_readable']},
            #             ),
            ]


history_table_fieldnames = ['id', 'url', 'title', 'visit_count', 'last_visit',
                            'last_visit_readable', 'browser',
                            'profile', 'file', 'tablename']
search_table_fields = ['rec_id', 'id',
                       'url', 'title',
                       'visit_count', 'last_visit',
                       'last_visit_readable',
                       'browser', 'profile', 'file', 'tablename']
