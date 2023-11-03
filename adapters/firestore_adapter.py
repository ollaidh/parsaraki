import os
from google.auth.credentials import AnonymousCredentials
from google.cloud.firestore import Client


class FirestoreAdapter:
    def __init__(self):
        project_id = os.getenv('PARSARAKI_PROJECT_ID')
        if os.getenv('GOOGLE_APPLICATION_CREDENTIALS') is None:
            cred = AnonymousCredentials()
        else:
            cred = None
        self.db = Client(project=project_id, credentials=cred)

    def add_search_results(self, search: dict[int: dict]):
        apts_database = self.db.collection("properties")
        for apt_id, apt_info in search.items():
            curr_apt = apts_database.document(str(apt_id))
            doc = curr_apt.get()
            if doc.exists:
                data = doc.to_dict()
                print(data)
                data["price"][apt_info["date"]] = apt_info["price"]
                curr_apt.set(data)
            else:
                apt_info["price"] = {apt_info["date"]: apt_info["price"]}
                apt_info.pop("date", None)
                curr_apt.set(apt_info)
