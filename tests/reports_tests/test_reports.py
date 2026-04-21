import pytest

from common.value_objects import VideoTitle, VideoCTR, VideoRetentionRate
from reports.reports import ClickbaitReport, ClickbaitReportRow


class TestClickbaitReportRow:
    @pytest.mark.parametrize('title', (None, VideoTitle.default()))
    @pytest.mark.parametrize('ctr', (None, VideoCTR.default()))
    @pytest.mark.parametrize('retention_rate', (None, VideoRetentionRate.default()))
    def test_creation_fail_correctly(self, title, ctr, retention_rate):
        if all(map(lambda x: x is not None, (title, ctr, retention_rate))):
            pytest.skip("Skip when all args correct.")
        with pytest.raises(ValueError):
            ClickbaitReportRow(title, ctr, retention_rate)

    @pytest.mark.parametrize('title', (VideoTitle('title'), VideoTitle('white')))
    @pytest.mark.parametrize('ctr', (VideoCTR(63.18), VideoCTR(74.19)))
    @pytest.mark.parametrize('retention_rate', (VideoRetentionRate(78), VideoRetentionRate(25)))
    def test_initialize_correctly(self, title, ctr, retention_rate):
        report_row = ClickbaitReportRow(title, ctr, retention_rate)
        assert report_row.title == title
        assert report_row.ctr == ctr
        assert report_row.retention_rate == retention_rate


class TestClickbaitReport:
    @pytest.mark.parametrize('data', [
        (None),
        (123),
        (9.45),
        (True),
        ((None, None, None)),
        ((123, 87.2, 'str')),
        ((ClickbaitReportRow(VideoTitle('vid1'), VideoCTR(5.67), VideoRetentionRate(49))), (ClickbaitReportRow(VideoTitle('vid2'), VideoCTR(64.82), VideoRetentionRate(66))), None),
    ])
    def test_initialize_fails_correctly(self, data):
        with pytest.raises(ValueError):
            ClickbaitReport(data)

    @pytest.mark.parametrize('data', [
        (ClickbaitReportRow(VideoTitle('vid1'), VideoCTR(5.67), VideoRetentionRate(49)), ClickbaitReportRow(VideoTitle('vid2'), VideoCTR(64.82), VideoRetentionRate(66))),
    ])
    def test_initialize_correctly(self, data):
        report = ClickbaitReport(data)
        assert report.data == data

