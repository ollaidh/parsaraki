import json
import requests

from search_parameters import SearchParameters
from bazaraki_connector import *
from pydantic import ValidationError
import argparse


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i")
    parser.add_argument("--output", "-o")
    return parser.parse_args(args)


def main():
    args = parse_args()

    search_parameters = args.input
    output_path = args.output

    try:
        with open(search_parameters) as file:
            request = SearchParameters.model_validate_json(file.read())
            req = search_bazaraki(request)
            ads = parse_single_ads(req)
            postfix = str(datetime.date.today())  # add postfix to filename

            with open(output_path.replace("%d", postfix), "w+") as f:
                f.write(json.dumps(ads))

    except ValidationError as e:
        print("ERROR IN INPUT JSON:\n", e)


if __name__ == '__main__':
    main()
