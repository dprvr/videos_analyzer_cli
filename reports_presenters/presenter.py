


from abc import abstractmethod, ABC


class ReportPresenter[TReport](ABC):
    @abstractmethod
    def present(self, report: TReport):
        pass