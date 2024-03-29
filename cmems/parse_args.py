import datetime
import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description='Python script for downloading MLD data from the Copernicus Marine Environment Monitoring Service (CMEMS) using the MOTU client.')
    parser.add_argument('-s', '--start-date', dest="start_date", type=str, help='start date in format YYYY-MM-DD')
    parser.add_argument('-e', '--end-date', dest="end_date", type=str, help='end date in format YYYY-MM-DD')
    args = parser.parse_args(args)

    args.start_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
    args.end_date = datetime.datetime.strptime(args.end_date, '%Y-%m-%d')
    assert args.start_date < args.end_date, 'start date must be before end date'

    return args
