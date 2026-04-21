

from dataclasses import asdict
from tabulate import tabulate
from reports.reports import ClickbaitReport
from reports_presenters.presenter import ReportPresenter


class ClickbaitReportPresenter(ReportPresenter[ClickbaitReport]):
    def present(self, report: ClickbaitReport):
        report_table_data = [{k : v['value'] for k, v in asdict(row).items()} for row in report.data]
        report_table = tabulate(report_table_data, headers='keys', tablefmt='heavy_grid')
        print(report_table)

