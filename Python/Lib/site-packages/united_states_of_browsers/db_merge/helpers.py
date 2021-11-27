from typing import Dict, Iterable, List, Sequence, Text, Union, Mapping


def make_queries(tablename: Text, primary_key_name: Text, fieldnames: Sequence[Text]) -> Dict:
    """ Constructs the queries necessary for specific purposes.
    Returns them as dict['purpose': 'query']
    """
    fieldnames_str = ', '.join(fieldnames)
    query_placeholder = '?, ' * len(fieldnames)
    queries = {'create': f'''CREATE TABLE IF NOT EXISTS {tablename} ({primary_key_name} integer PRIMARY KEY, {fieldnames_str[:]})'''}
    queries.update({'insert': f"INSERT INTO {tablename} ({fieldnames_str}) VALUES ({query_placeholder[:-2]})"})
    return queries


def query_sanitizer(query: str, allowed_chars: Union[str, Iterable]='_') -> str:
    """ Removes non-alphanumeric characters from a query.
    Retains characters passed in via `allowed_chars`. (Default: '_')
    Returns a string.
    """
    allowed_chars = set(allowed_chars)
    return ''.join([char
                    for char in query
                    if char.isalnum()
                    or char in allowed_chars])  #, '?', '(', ')', ','}])


def check_records_unique_with_field(records, field):
    all_ids = [record[field] for record in records]
    unique_ids = set(all_ids)
    return len(all_ids) == len(unique_ids)


def errors_display(error_msgs: List) -> List:
    print()
    for error_msg_ in error_msgs:
        try:
            print(f'{error_msg_.strerror}\n\t\t{error_msg_.filename}')
        except AttributeError:
            print(error_msg_)
    print()


def get_warnings_text(warnings_recorded: Iterable[Warning]
                      ) -> Mapping[Text, Warning]:
    """ Extracts the contents of each warning.
    :param warnings_recorded: List of Warnings
    :return: Dict of message and category category each warning.
    """
    return {str(warning_.message): warning_.category
            for warning_ in warnings_recorded
            }
