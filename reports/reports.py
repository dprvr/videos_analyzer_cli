

from dataclasses import dataclass
from common.value_objects import VideoCTR, VideoRetentionRate, VideoTitle
from reports.report import Report


@dataclass(frozen=True)
class ClickbaitReportRow:
    title: VideoTitle
    ctr: VideoCTR
    retention_rate: VideoRetentionRate

    def __post_init__(self):
        if not isinstance(self.title, VideoTitle):
            raise ValueError(f'The title must be an instance of VideoTitle class, but was <{type(self.title)} type.>')
        if not isinstance(self.ctr, VideoCTR):
            raise ValueError(f'The ctr must be an instance of VideoCTR class, but was <{type(self.ctr)} type.>')
        if not isinstance(self.retention_rate, VideoRetentionRate):
            raise ValueError(f'The retention rate must be an instance of  class, but was <{type(self.retention_rate)} type.>')


@dataclass(frozen=True)
class ClickbaitReport(Report[tuple[ClickbaitReportRow, ...]]):
    def __post_init__(self):
        if not isinstance(self.data, tuple):
            raise ValueError(f'The data must be an instance of tuple class, but was <{type(self.data)}> type.')
        if any(map(lambda x: not isinstance(x, ClickbaitReportRow), self.data)):
            raise ValueError(f'The each element of data must be an instance of ClickbaitReportRow class.')

