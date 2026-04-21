

from dataclasses import dataclass
from common.value_objects import VideoTitle, VideoCTR, VideoRetentionRate, Count, VideoWatchTime


@dataclass(frozen=True)
class VideoData:
    title: VideoTitle
    ctr: VideoCTR
    retention_rate: VideoRetentionRate
    views: Count
    likes: Count
    avg_watch_time: VideoWatchTime

    def __post_init__(self):
        if not isinstance(self.title, VideoTitle):
            raise ValueError(f'The title must be an instance of VideoTitle class, but was <{type(self.title)} type.>')
        if not isinstance(self.ctr, VideoCTR):
            raise ValueError(f'The ctr must be an instance of VideoCTR class, but was <{type(self.ctr)} type.>')
        if not isinstance(self.retention_rate, VideoRetentionRate):
            raise ValueError(f'The retention rate must be an instance of  class, but was <{type(self.retention_rate)} type.>')
        if not isinstance(self.likes, Count):
            raise ValueError(f'The likes must be an instance of Count class, but was <{type(self.likes)} type.>')
        if not isinstance(self.views, Count):
            raise ValueError(f'The views must be an instance of Count class, but was <{type(self.views)} type.>')
        if not isinstance(self.avg_watch_time, VideoWatchTime):
            raise ValueError(f'The average watch time must be an instance of  class, but was <{type(self.avg_watch_time)} type.>')
        
        