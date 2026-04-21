

from dataclasses import dataclass


@dataclass(frozen=True)
class Report[T]:
    data: T


# report_type: str
#     data_source: str
#     creation_time: datetime
#     data: tuple[Any]
    