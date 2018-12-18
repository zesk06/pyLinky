#!/usr/bin/env python3
# encoding: utf-8

import argparse
import sys
import json
import os


from dotenv import load_dotenv, find_dotenv
from pylinky import LinkyClient


def main():
    """Main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="enedis username")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument(
        "-d", "--daily", help="Print daily consumption only", action="store_true"
    )
    parser.add_argument(
        "--csv", help="Print consumption using CSV format", action="store_true"
    )
    args = parser.parse_args()

    # parameter can be defined as environment variables
    # using a .env file
    load_dotenv(find_dotenv())

    username = args.username
    if not username and "PYLINKY_USERNAME" in os.environ:
        username = os.environ["PYLINKY_USERNAME"]
    password = args.password
    if not password and "PYLINKY_PASSWORD" in os.environ:
        password = os.environ["PYLINKY_PASSWORD"]
    client = LinkyClient(username, password)

    try:
        client.fetch_data()
    except BaseException as exp:
        print(exp)
        return 1
    finally:
        client.close_session()
    datas = client.get_data()
    output_datas = {}
    if args.daily:
        output_datas["daily"] = datas["daily"]
    if args.csv:
        print(";".join(("TYPE", "TIME", "CONSO")))
        for type_c, values in output_datas.items():
            for value in values:
                time_c = value["time"]
                cons_c = value["conso"]
                print("{};{};{}".format(type_c, time_c, int(cons_c)))
    else:
        print(json.dumps(output_datas, indent=2))


if __name__ == "__main__":
    sys.exit(main())

