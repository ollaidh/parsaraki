import unittest
from firestore_adapter import *
import requests


def delete_collection_firestore(coll_ref):
    docs = coll_ref.list_documents()

    for doc in docs:
        print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
        doc.delete()


class TestFirestoreAdapter(unittest.TestCase):
    def setUp(self) -> None:
        emulator_host = os.getenv('FIRESTORE_EMULATOR_HOST')
        self.assertIsNotNone(emulator_host)
        project_id = os.getenv('PARSARAKI_PROJECT_ID')
        self.assertIsNotNone(project_id)
        url = f'http://{emulator_host}/emulator/v1/projects/{project_id}/databases/(default)/documents'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)

    def test_add_search_results(self):
        adapter = FirestoreAdapter()

        adapter.add_search_results(
            {
                1: {"date": '2022-12-12', "price": 2500, "bedrooms": 1, "link": 'link1'},
                2: {"date": '2022-12-12', "price": 2600, "bedrooms": 2, "link": 'link2'},
                3: {"date": '2022-12-12', "price": 2700, "bedrooms": 3, "link": 'link3'},
            }
        )

        # test adding new properties to database:
        result1 = adapter.db.collection("properties").document("1").get().to_dict()
        self.assertEqual(
            {"bedrooms": 1, "link": 'link1', "price": {'2022-12-12': 2500}},
            result1
        )
        result2 = adapter.db.collection("properties").document("2").get().to_dict()
        self.assertEqual(
            {"bedrooms": 2, "link": 'link2', "price": {'2022-12-12': 2600}},
            result2
        )
        result3 = adapter.db.collection("properties").document("3").get().to_dict()
        self.assertEqual(
            {"bedrooms": 3, "link": 'link3', "price": {'2022-12-12': 2700}},
            result3
        )

        # test adding partly new properties, partly existing
        adapter.add_search_results(
            {
                1: {"date": '2022-12-13', "price": 2550, "bedrooms": 1, "link": 'link1'},  # existing property
                4: {"date": '2022-12-13', "price": 2600, "bedrooms": 2, "link": 'link4'},  # new property
                5: {"date": '2022-12-13', "price": 2700, "bedrooms": 3, "link": 'link5'},  # new property
            }
        )
        result11 = adapter.db.collection("properties").document("1").get().to_dict()
        self.assertEqual(
            {"bedrooms": 1, "link": 'link1', "price": {'2022-12-12': 2500, '2022-12-13': 2550}},
            result11
        )
        result4 = adapter.db.collection("properties").document("4").get().to_dict()
        self.assertEqual(
            {"bedrooms": 2, "link": 'link4', "price": {'2022-12-13': 2600}},
            result4
        )
        result5 = adapter.db.collection("properties").document("5").get().to_dict()
        self.assertEqual(
            {"bedrooms": 3, "link": 'link5', "price": {'2022-12-13': 2700}},
            result5
        )

        delete_collection_firestore(adapter.db.collection("properties"))

