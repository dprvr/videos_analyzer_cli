import logging
import os

from data_extracters.extracters import VideoDataExtracter
from processors.processor import Processor
from processors.processors import StandartProcessor
from reports_makers.makers import ClickbaitReportMaker
from reports_presenters.presenters import ClickbaitReportPresenter


class ProcessorsFactory:
    def try_create_processor(self, report_type: str, **kwargs) -> tuple[bool, Processor | None]:
        if report_type != 'clickbait':
            return False, None
        return self.__try_create_clickbait_report_processor(kwargs)

    def __try_create_clickbait_report_processor(self, kwargs: dict) -> tuple[bool, Processor | None]:
        filepaths = kwargs.get('filepaths')
        if filepaths is None:
            raise ValueError('Fail to create processor, because required argument "filepaths" not found.')
        
        processor = None
        try:
            processor = StandartProcessor(
                VideoDataExtracter(filepaths, os.cpu_count()),
                ClickbaitReportMaker(),
                ClickbaitReportPresenter(),
            )
        except Exception as e:
            logging.error(e)
            return False, None
        
        return True, processor