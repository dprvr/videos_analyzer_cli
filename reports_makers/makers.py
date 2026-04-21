

from abc import ABC
from common.dtos import VideoData
from reports.reports import ClickbaitReport, ClickbaitReportRow
from reports_makers.maker import ReportMaker


class VideoDataReportMaker[TReport](ReportMaker[tuple[VideoData, ...], TReport], ABC):
    pass


class ClickbaitReportMaker(VideoDataReportMaker[ClickbaitReport]):
    def make_report(self, data: tuple[VideoData, ...]) -> ClickbaitReport:
        if not isinstance(data, tuple):
            raise ValueError(f'The data must be an instance of tuple class, but was <{type(data)}> type.')
        if any(map(lambda x: not isinstance(x, VideoData), data)):
            raise ValueError(f'The each element of data must be an instance of VideoData class.')

        clickbait_videos = [v for v in data if v.ctr.value > 15 and v.retention_rate.value < 40]
        report_rows = [ClickbaitReportRow(title=v.title, ctr=v.ctr, retention_rate=v.retention_rate) for v in clickbait_videos]
        report_rows.sort(key=lambda r: (r.ctr.value), reverse=True)
        report_rows = tuple(report_rows)
        report = ClickbaitReport(data=report_rows)
        return report
    
