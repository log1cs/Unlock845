# -*- encoding: utf-8 -*-

from pathlib import Path
from os import PathLike
from typing import (Any,
                    AnyStr,
                    ByteString,
                    Dict,
                    Generator,
                    Iterable,
                    List,
                    Mapping,
                    NamedTuple,
                    Optional,
                    Sequence,
                    SupportsInt,
                    Text, Tuple, Type, TypeVar,
                    Union,
                    NewType,
                    )

PathInfo = NewType('PathInfo', Union[Path, PathLike, Text, ByteString])


class BrowserData(NamedTuple):
	os: Text
	browser: Text
	path: PathInfo
	profiles: Optional[Iterable[Text]]
	file_tables: Mapping[Text, Iterable[Text]]
	table_fields: Mapping[Text, Iterable[Text]]
