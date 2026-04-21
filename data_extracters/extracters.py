import os

from concurrent.futures import ThreadPoolExecutor
from csv import reader
from common.dtos import VideoData
from data_extracters.extracter import DataExtracter
from common.value_objects import VideoTitle, VideoCTR, VideoRetentionRate, Count, VideoWatchTime


class VideoDataExtracter(DataExtracter[tuple[VideoData, ...]]):
    def __init__(self, sources_files_pathes: tuple[str, ...], threads_count: int):
        if not isinstance(sources_files_pathes, tuple):
            raise ValueError(f'The sources files pathes must be an instance of tuple class, but was <{type(sources_files_pathes)}> type.')
        if any(map(lambda s: not isinstance(s, str), sources_files_pathes)):
            raise ValueError(f'The each of sources files pathes must be an instance of str class.')
        if any(map(lambda s: not os.path.isfile(s), sources_files_pathes)):
            raise ValueError(f'The each of sources files pathes must be a correct file path.')
        if any(map(lambda s: not os.path.splitext(s)[1] == '.csv', sources_files_pathes)):
            raise ValueError(f'The each of source files pathes must be a path to .csv file.')

        if not isinstance(threads_count, int):
            raise ValueError(f'The threads count must be an instance of int class, but was <{type(threads_count)}> type.')

        self.__sources = sources_files_pathes
        self.__threads_count = threads_count
        self.__expected_header = {'title', 'ctr', 'retention_rate', 'views', 'likes', 'avg_watch_time'}

    def extract_data(self) -> tuple[VideoData, ...]:
        data_parts = None
        with ThreadPoolExecutor(max_workers=self.__threads_count) as executor:
            data_parts = executor.map(self.__extract_data_from_file, self.__sources)
        data = tuple(item for lst in data_parts for item in lst)
        return data

    def __extract_data_from_file(self, filepath: str) -> list[VideoData]:
        data = list[VideoData]()
        with open(filepath, mode='r') as stream:
            file_reader = reader(stream)
            first_line = next(file_reader)
            first_line_is_header = self.__is_line_header(first_line)
            if not first_line_is_header:
                raise ValueError(f'The first line of the csv file must be a correct header consist of next tuple({self.__expected_header}).')
            for line_n, line in enumerate(file_reader, 2):
                if len(line) != len(first_line):
                    raise ValueError(f'Looks like the csv file contains line ({line_n}) with incorrect count of values.')
                video_data_dict = {attr: line[i] for i, attr in enumerate(first_line)}
                parsed, video_data = self.__parse_line_items(video_data_dict)
                if not parsed:
                    raise ValueError(f'Failed to parse {line_n} line, looks like that line contains invalid values.')
                data.append(video_data)
        return data

    def __is_line_header(self, line: list[str]):
        header = set(line)
        is_header = self.__expected_header == header
        return is_header

    def __parse_line_items(self, line_items: dict[str, str]) -> tuple[bool, VideoData]:
        video_data = None
        try:
            video_data = VideoData(
                title=VideoTitle.parse(line_items['title']),
                ctr=VideoCTR.parse(line_items['ctr']),
                retention_rate=VideoRetentionRate.parse(line_items['retention_rate']),
                views=Count.parse(line_items['views']),
                likes=Count.parse(line_items['likes']),
                avg_watch_time=VideoWatchTime.parse(line_items['avg_watch_time']),
            )
        except:
            return False, None
        return True, video_data

    