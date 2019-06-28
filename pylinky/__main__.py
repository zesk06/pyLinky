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
    parser.add_argument("--output-file", "-o", help="output file, or stdout")
    parser.add_argument(
        "-d", "--daily", help="Print daily consumption only", action="store_true"
    )
    parser.add_argument(
        "--csv", help="Print consumption using CSV format", action="store_true"
    )
    parser.add_argument("--since", "-s", help="The since-date to fetch from")
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
        if args.since:
            client.fetch_daily_since(since=args.since)
        else:
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
    else:
        output_datas = datas
    output_str = ""
    if args.csv:
        output_str = ",".join(("TIME", "CONSO"))
        for type_c, values in output_datas.items():
            for value in values:
                time_c = value["time"]
                cons_c = value["conso"]
                line = ("{},{}".format(time_c, int(cons_c)))
                output_str = output_str + "\n" + line 
    else:
        output_str = json.dumps(output_datas, indent=2)

    if args.output_file:
        with open(args.output_file, "w") as output_f:
            output_f.write(output_str)
    else:
        print(output_str)

if __name__ == "__main__":
    sys.exit(main())

