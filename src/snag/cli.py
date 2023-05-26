import yaml
import argparse

import snagrecover.config as config

def cli():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    common = parser.add_argument_group("Common")
    common.add_argument("-f", "--file", help="set manifest file", default="snag.yaml")

    args = parser.parse_args()

    with open(args.file) as file:
        data = yaml.safe_load(file)

        config.init_config(data["recovery"])

        print(data)