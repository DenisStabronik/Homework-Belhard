import argparse
from Rest_Days import days_before_event
from Generator import generate_sample
from Toy import get_random_toy
from Diretory_struct import restructure_directory as rest_dir
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, filemode="w")

parser = argparse.ArgumentParser()
sub_parser = parser.add_subparsers(dest="command")

parser_newyear = sub_parser.add_parser("newyear")
parser_newyear.add_argument('--hours', help='Additional parameter,add hours to the days before the event ',
                            action='store_true')

parser_toy = sub_parser.add_parser("toy")

parser_restructure = sub_parser.add_parser("restructure")
parser_restructure.add_argument("directory", type=str)
args = parser.parse_args()

if args.command == "newyear":
    hour_flag = args.hours
    if hour_flag:
        logging.info("Received newyear argument with hours")
    else:
        logging.info("Received newyear argument without hours")
    days_before_event(hour_flag)
    logging.info("Calculated days before event")
if args.command == "toy":
    logging.info("Received toy argument")
    get_random_toy()
    logging.info("Generate random toy")
if args.command == "restructure":
    directory = args.directory
    logging.info(f"Received restructure argument with directory = {directory}")
    generate_sample(directory)
    logging.info("Generate samples")
    rest_dir(directory)
    logging.info("Restructure files")