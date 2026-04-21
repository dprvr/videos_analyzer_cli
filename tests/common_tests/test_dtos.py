import pytest

from common.value_objects import VideoCTR, Count, VideoRetentionRate, VideoTitle, VideoWatchTime
from common.dtos import VideoData


class TestVideoData:
    @pytest.mark.parametrize('title', (None, VideoTitle.default()))
    @pytest.mark.parametrize('ctr', (None, VideoCTR.default()))
    @pytest.mark.parametrize('retention_rate', (None, VideoRetentionRate.default()))
    @pytest.mark.parametrize('views', (None, Count.default()))
    @pytest.mark.parametrize('likes', (None, Count.default()))
    @pytest.mark.parametrize('avg_watch_time', (None, VideoWatchTime.default()))
    def test_creation_fail_correctly(self, title, ctr, retention_rate, views, likes, avg_watch_time):
        if all(map(lambda x: x is not None, (title, ctr, retention_rate, views, likes, avg_watch_time))):
            pytest.skip("Skip when all args correct.")
        with pytest.raises(ValueError):
            VideoData(title, ctr, retention_rate, views, likes, avg_watch_time)

    @pytest.mark.parametrize('title', (VideoTitle('title'), VideoTitle('white')))
    @pytest.mark.parametrize('ctr', (VideoCTR(63.18), VideoCTR(74.19)))
    @pytest.mark.parametrize('retention_rate', (VideoRetentionRate(78), VideoRetentionRate(25)))
    @pytest.mark.parametrize('views', (Count(652), Count(1743)))
    @pytest.mark.parametrize('likes', (Count(625), Count(89721)))
    @pytest.mark.parametrize('avg_watch_time', (VideoWatchTime(78.277), VideoWatchTime(24.90)))
    def test_initialize_correctly(self, title, ctr, retention_rate, views, likes, avg_watch_time):
        video_data = VideoData(title, ctr, retention_rate, views, likes, avg_watch_time)
        assert video_data.title == title
        assert video_data.ctr == ctr
        assert video_data.retention_rate == retention_rate
        assert video_data.views == views
        assert video_data.likes == likes
        assert video_data.avg_watch_time == avg_watch_time

