from datetime import datetime
from typing import NamedTuple, Optional

time_filter = NamedTuple(
    "time_filter",
    [
        ("start", Optional[datetime]),
        ("end", Optional[datetime]),
        ("limit", Optional[int]),
    ],
)
