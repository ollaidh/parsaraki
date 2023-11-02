import os
from google.auth.credentials import AnonymousCredentials
from google.cloud.firestore import Client


class FirestoreAdapter:
    def __init__(self):
        project_id = os.getenv('BUDBOT_PROJECT_ID')
        if os.getenv('GOOGLE_APPLICATION_CREDENTIALS') is None:
            cred = AnonymousCredentials()
        else:
            cred = None
        self.db = Client(project=project_id, credentials=cred)

    def add_search_results(self, search: dict[int: dict]):
        apts_database = self.db.collection("properties")
        for apt_id, apt_info in search.items():
            curr_apt = apts_database.document(str(apt_id))
            if curr_apt.get().to_dict():
                # curr_apt.collection("info").document("price")[apt_info["date"]] = apt_info["price"]
                # curr_info = curr_apt.collection("info").document("price").collection[]get().to_dict()
                # print(curr_apt.collection("info").get().docs.map())
                # print(curr_info)
                pass
            else:
                apt_info["price"] = {apt_info["date"]: apt_info["price"]}
                apt_info.pop("date", None)
                curr_apt.set({"info": apt_info})
