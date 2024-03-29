from ast import arg
from ServiceDefs import DoesPathExistAndIsFile
from parse_args import parse_args
import sys
import os
import time
from datetime import timedelta
import copernicusmarine


USERNAME = 'YOUR_CMEMS_USERNAME'
PASSWORD = 'YOUR_CMEMS-PASSWD'
motu_uri = 'https://my.cmems-du.eu/motu-web/Motu'
serviceID = "GLOBAL_MULTIYEAR_PHY_001_030-TDS"
productID = "cmems_mod_glo_phy_my_0.083_P1D-m"

def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(days=n)


def download_mld_glorys():
    argv = sys.argv
    args = parse_args(argv[1:])
    start_date, end_date = args.start_date, args.end_date

    for curdate in date_range(start_date, end_date):
        OUTPUT_DIR = '.'
        OUTPUT_FILENAME = 'GLORYS12_MLD-%04d-%02d-%02d.nc' % (curdate.year, curdate.month, curdate.day)
        print('requesting data for %s' % curdate)

        copernicusmarine.subset(dataset_id="cmems_mod_glo_phy_my_0.083_P1M-m",variables=["mlotst"],minimum_longitude=-180,maximum_longitude=179.9166717529297,minimum_latitude=-80,maximum_latitude=90,start_datetime=curdate,end_datetime=curdate + timedelta(days=1),minimum_depth=0.49402499198913574,maximum_depth=0.49402499198913574,output_filename=OUTPUT_FILENAME,username=USERNAME,password=PASSWORD,force_download=True,overwrite_output_data=True)


if __name__ == '__main__':
    download_mld_glorys()
