import argparse
from Rest_Days import days_before_new_year
from Generator import generate_sample
from Toy import get_random_toy
from Diretory_struct import change_name_on_dir 
import logging
logging.basicConfig(
    level=logging.INFO, 
    filename = "mylog.log", 
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
    datefmt='%H:%M:%S',
    )
# logging.basicConfig(filename="logfile.log", level=logging.INFO, filemode="w")
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--action', help='what function do you want to run?')
parser.add_argument('-d', '--directory', help='specify a directory')

args = parser.parse_args()

if args.action == "NY":
    days_before_new_year()
    logging.info("Calculated days before 2023")
elif args.action == "Toy":
    get_random_toy()
    logging.info("Get random toy")
elif args.action == "R":
    directory = args.directory
    logging.info('Enter Restructure argument and directory argument')
    generate_sample(directory)
    logging.info("Generate files")   
    change_name_on_dir (directory)
logging.info("Restructure files")
# print(args)
