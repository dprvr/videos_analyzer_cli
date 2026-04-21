import pytest

from common.value_objects import VideoTitle, Count, VideoCTR, VideoRetentionRate, VideoWatchTime
from common.dtos import VideoData
from reports.reports import ClickbaitReportRow
from reports_makers.makers import ClickbaitReportMaker


class TestClickbaitReportMaker:

    @pytest.mark.parametrize('data', [
        list(),
        None,
        'str',
        (None,),
        ('str',),
        (156,),
    ])
    def test_make_report_method_fails_correctly(self, data):
        maker = ClickbaitReportMaker()
        with pytest.raises(ValueError):
            maker.make_report(data)

    def test_make_report_method_filter_correct(self):
        data = (
            VideoData(VideoTitle('vid1'), VideoCTR(1.67), VideoRetentionRate(67), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid2'), VideoCTR(23.16), VideoRetentionRate(67), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid3'), VideoCTR(28.02), VideoRetentionRate(32), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid4'), VideoCTR(5.01), VideoRetentionRate(27), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid5'), VideoCTR(34.91), VideoRetentionRate(12), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid6'), VideoCTR(1.09), VideoRetentionRate(10), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid7'), VideoCTR(47.81), VideoRetentionRate(78), Count.default(), Count.default(), VideoWatchTime.default()),
        )
        expected = set(ClickbaitReportRow(v.title, v.ctr, v.retention_rate) for v in [data[2], data[4]])
        maker = ClickbaitReportMaker()
        
        report = maker.make_report(data)
        
        assert len(expected) == len(report.data)
        assert expected == set(report.data) 

    def test_make_report_method_sort_correct(self):
        data = (
            VideoData(VideoTitle('vid1'), VideoCTR(16.1), VideoRetentionRate(39), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid2'), VideoCTR(17.1), VideoRetentionRate(17), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid3'), VideoCTR(18.1), VideoRetentionRate(25), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid4'), VideoCTR(19.1), VideoRetentionRate(12), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid5'), VideoCTR(20.1), VideoRetentionRate(27), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid6'), VideoCTR(21.1), VideoRetentionRate(32), Count.default(), Count.default(), VideoWatchTime.default()),
            VideoData(VideoTitle('vid7'), VideoCTR(22.1), VideoRetentionRate(37), Count.default(), Count.default(), VideoWatchTime.default()),
        )
        expected = [ClickbaitReportRow(v.title, v.ctr, v.retention_rate) for v in reversed(data)]
        maker = ClickbaitReportMaker()

        report = maker.make_report(data)
        
        assert len(expected) == len(report.data)
        assert all(map(lambda index_row: index_row[1] == expected[index_row[0]], enumerate(report.data)))        