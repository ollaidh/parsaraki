import json
import pathlib
import datetime


def save_search_to_json(folder_name: str, ads: list[dict]):
    name_postfix = datetime.date.today()  # add today date to the end of file name
    folder_path = pathlib.Path(__file__).parent.resolve() / folder_name  # path to local folder to save search results
    json_path = folder_path / f'bazaraki_ads_{name_postfix}.json'  # json to dump search results

    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)

    with open(json_path, "w+") as f:
        f.write(json.dumps(ads))

