import pytest
import os

from data_extracters.extracters import VideoDataExtracter


class TestVideoDataExtracter:

    @pytest.mark.parametrize('sources', [(None, None), (1783, 17.039), ('some1', 'some2'), ('somefile1.py', 'somefile2.py')])
    @pytest.mark.parametrize('threads_count', [(None,), (17.34), (4,)])
    def test_initialize_fail_correctly(self, sources, threads_count):
        with pytest.raises(ValueError):
            VideoDataExtracter(sources, threads_count)

    @pytest.mark.parametrize('files_names', [
        ('invalid_header1.csv',),
        ('invalid_header2.csv',),
        ('invalid_header3.csv',),
        ('invalid_value1.csv',),
        ('invalid_value2.csv',),
        ('invalid_value3.csv',),
        ('invalid_value4.csv',),
    ])
    def test_fail_correctly_when_file_invalid(self, files_names):
        test_data_folder_path = f'{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}{os.sep}tests_data{os.sep}'
        pathes_to_files = tuple(test_data_folder_path + filename for filename in files_names)
        extracter = VideoDataExtracter(pathes_to_files, 3)
        with pytest.raises(ValueError):
            extracter.extract_data()
    

