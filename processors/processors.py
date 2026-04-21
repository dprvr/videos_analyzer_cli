import logging

from threading import Event, Thread
from time import sleep
from typing import Any, Callable
from data_extracters.extracter import DataExtracter
from processors.processor import Processor
from reports_makers.maker import ReportMaker
from reports_presenters.presenter import ReportPresenter


class StandartProcessor[TData, TReport](Processor):
    def __init__(self,
                extracter: DataExtracter[TData], 
                maker: ReportMaker[TData, TReport],
                presenter: ReportPresenter[TReport]) -> None:
        if not isinstance(extracter, DataExtracter):
            raise ValueError(f'The extracter must be an instance of DataExtracter sublclass, but was <{type(extracter)}> type.')
        if not isinstance(maker, ReportMaker):
            raise ValueError(f'The maker must be an instance of ReportMaker subclass, but was <{type(maker)}> type.')
        if not isinstance(presenter, ReportPresenter):
            raise ValueError(f'The presenter must be an instance of ReportPresenter subclass, but was <{type(presenter)}> type.')

        self.__extracter = extracter
        self.__maker = maker
        self.__presenter = presenter
        self.__progress_update_interval = 0.1
        self.__progress_symbol = '.'
        self.__progress_symbol_max_length = 3
        self.__complete_successfully = False
        self.__error_message = ''
        self.__stop = False
        self.__step_info = None
    
    @property
    def complete_successfully(self) -> bool:
        return self.__complete_successfully
    
    @property
    def error_message(self) -> str:
        return self.__error_message

    def process(self):
        pipeline = (
            (self.__extract_data, {'name': 'data extraction'}),
            (self.__make_report, {'name': 'report making'}),
            (self.__present_report, {'name': 'report presentation'}) 
        )
        step = 0
        prev_step_data = None
        while not self.__stop and step < len(pipeline):
            self.__step_info = pipeline[step][1]
            prev_step_data = pipeline[step][0](prev_step_data) if prev_step_data is not None else pipeline[step][0]()
            step += 1
        self.__complete_successfully = not self.__stop

    def __show_operation_progress(self, operation_name: str, completion_event: Event):
        current_symbol = self.__progress_symbol
        while not completion_event.is_set():
            print(f'\r{operation_name} {current_symbol}', end='', flush=True)
            current_symbol = self.__progress_symbol if len(current_symbol) + 1 > self.__progress_symbol_max_length else current_symbol + self.__progress_symbol
            sleep(self.__progress_update_interval)
        print(f'\r{operation_name} complete')

    def __perform_operation(self, operation: Callable[..., Any], args: tuple[Any, ...] | None, completion_event: Event, result: list[Any | None]):
        try:
            result.append(operation(*args) if args is not None else operation())
        except Exception as e:
            self.__stop = True
            logging.error(e)
            self.__error_message = f'Something went wrong on {self.__step_info["name"]} step, to get more info about error check errorlog.txt.'
            result.append(None)
        completion_event.set()

    def __perform_long_operation(self, operation: Callable[..., Any], operation_args: tuple[Any, ...] | None, operation_name: str, result: list[Any | None]):
        complete_event = Event()
        work_thread = Thread(target=self.__perform_operation, args=(operation, operation_args, complete_event, result))
        show_thread = Thread(target=self.__show_operation_progress, args=(operation_name, complete_event))
        show_thread.start()
        work_thread.start()
        work_thread.join()
        show_thread.join()

    def __extract_data(self) -> TData:
        data = list[TData]()
        self.__perform_long_operation(
            self.__extracter.extract_data,
            None,
            'Data extraction',
            data,
        )
        return data[0]

    def __make_report(self, data: TData) -> TReport:
        report = list[TReport]()
        self.__perform_long_operation(
            self.__maker.make_report,
            (data,),
            'Making report',
            report,
        )
        return report[0]

    def __present_report(self, report: TReport):
        self.__presenter.present(report)
