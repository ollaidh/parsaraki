import json

from bazaraki_connector import *
from pydantic import ValidationError
import argparse


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i")
    parser.add_argument("--output", "-o")
    args = parser.parse_args(args)
    if args.input is None or args.output is None:
        raise ValueError("Some arguments are missing!")
    return args


def generate_filename(output_path: str) -> str:
    postfix = str(datetime.date.today())  # postfix to add to filename
    output_path = output_path.replace("%d", postfix)
    return output_path


def main():
    try:
        args = parse_args()

        search_parameters = args.input
        output_path = args.output

        try:
            with open(search_parameters) as file:
                request = SearchParameters.model_validate_json(file.read())
                req = search_bazaraki(request)
                ads = parse_single_ads(req)
                filename = generate_filename(output_path)

                with open(filename, "w+") as f:
                    f.write(json.dumps(ads))

        except ValidationError as e:
            print("ERROR IN INPUT JSON:\n", e)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
