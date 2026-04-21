import logging

from argparse import ArgumentParser
from processors.processors_factory import ProcessorsFactory


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Simple cli video data analyzer.')
    parser.add_argument(
        '--files',
        required=True,
        nargs='+',
        help='The paths to csv files contais target data for analyze.'
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=['clickbait'],
        help='Type of output report.'
    )
    return parser

def configure_logging():
    logging.basicConfig(
        filename='errorlog.txt',
        level=logging.ERROR,
        filemode='w',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main_impl():
    configure_logging()
    parser = create_parser()
    args = parser.parse_args()
    filepaths = tuple(arg for arg in args.files)
    
    factory = ProcessorsFactory()
    
    created, processor = factory.try_create_processor(args.report, filepaths=filepaths)

    if not created:
        print(f'Failed to start files handle process, to get more info about error check the errorlog.txt.')
        return
    
    processor.process()

    if not processor.complete_successfully:
        print(processor.error_message)
        return

def main():
    try:
        main_impl()
    except Exception as e:
        logging.error(e)
        print(f'The unexpected program error acquired, looks like the program code invalid, to get more info about error check errorlog.txt')
    
if __name__ == '__main__':
    main()


