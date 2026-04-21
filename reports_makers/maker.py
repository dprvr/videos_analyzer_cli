

from abc import ABC, abstractmethod


class ReportMaker[TData, TReport](ABC):
    @abstractmethod
    def make_report(self, data: TData) -> TReport:
        pass