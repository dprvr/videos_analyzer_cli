import pytest

from common.value_objects import Count, VideoCTR, VideoRetentionRate, VideoTitle, VideoWatchTime


class TestVideoTitle:
    @pytest.mark.parametrize('title', [
        (None),
        (563),
        (7.19),
        (True),
    ])
    def test_initialize_fails_correctly(self, title):
        with pytest.raises(ValueError):
            VideoTitle(title)

    @pytest.mark.parametrize('title', [
        ('red'),
        ('sky'),
        ('wind'),
    ])
    def test_initialize_correctly(self, title):
        video_title = VideoTitle(title)
        assert video_title.value == title


class TestVideoCTR:
    @pytest.mark.parametrize('ctr', [
        (None),
        (563),
        (True),
        ("test"),
        (-1.0),
        (-1893.28),
        (101.0),
        (1892.78),
    ])
    def test_initialize_fails_correctly(self, ctr):
        with pytest.raises(ValueError):
            VideoCTR(ctr)

    @pytest.mark.parametrize('ctr', [
        (0.9),
        (16.67),
        (93.092),
    ])
    def test_initialize_correctly(self, ctr):
        video_ctr = VideoCTR(ctr)
        assert video_ctr.value == ctr


class TestVideoRetentionRate:
    @pytest.mark.parametrize('retention_rate', [
        (None),
        ('str'),
        (18.91),
        (-18),
        (-1),
        (101),
        (111),
    ])
    def test_initialize_fails_correctly(self, retention_rate):
        with pytest.raises(ValueError):
            VideoRetentionRate(retention_rate)

    @pytest.mark.parametrize('retention_rate', [
        (0),
        (100),
        (28),
        (72),
    ])
    def test_initialize_correctly(self, retention_rate):
        video_retention = VideoRetentionRate(retention_rate)
        assert video_retention.value == retention_rate


class TestCount:
    @pytest.mark.parametrize('_count', [
        (None),
        ('str'),
        (18.02),
        (-2830.90),
        (-1),
        (-128),
    ])
    def test_initialize_fails_correctly(self, _count):
        with pytest.raises(ValueError):
            Count(_count)

    @pytest.mark.parametrize('count', [
        (0),
        (12),
        (1782),
        (50373),
    ])
    def test_initialize_correctly(self, count):
        _count = Count(count)
        assert _count.value == count


class TestVideoWatchTime:
    @pytest.mark.parametrize('watch_time', [
        (None),
        ('str'),
        (-90),
        (-1),
        (18),
        (1728),
        (-19.78),
        (-1.273),
        (True),
    ])
    def test_initialize_fails_correctly(self, watch_time):
        with pytest.raises(ValueError):
            VideoWatchTime(watch_time)

    @pytest.mark.parametrize('watch_time', [
        (1.256),
        (452.9),
        (124.9),
    ])
    def test_initialize_correctly(self, watch_time):
        _watch_time = VideoWatchTime(watch_time)
        assert _watch_time.value == watch_time