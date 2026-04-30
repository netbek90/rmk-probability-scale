# import requests
# import urllib3
# import os

# #api problems
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# #api config
# BASE_URL = "https://avaandmed.eesti.ee/api/opendata"
# #ACCOUNT TOKEN here 1777490687 , token changes every session...
# HEADERS = {
#     "X-API-Key": "1777490687"
# }

# #df search by keyword...


# #ds searc

# def search_datasets(query, limit=10):
#     """Ds keyword search"""
#     url = f"{BASE_URL}/search"
#     params = {"q": query, "limit": limit}
#     response = requests.get(url, headers=HEADERS, params=params, verify=False)
#     if response.status_code == 200:
#         data = response.json()
#         return data.get("data", [])
#     else:
#         print(f"Search error: {response.status_code}")
#         return []


# #search ds
# if __name__ == "__main__":
#     keywords = ["tulekahju", "metsa", "forest"]
    
#     for kw in keywords:
#         datasets = search_datasets(kw)
#         print(f"\nSearch: '{kw}' — найдено {len(datasets)} datasets")
#         for ds in datasets[:3]:
#             title = ds.get("title_et") or ds.get("title_en") or ds.get("title") or "No title"
#             ds_id = ds.get("id", "?")
#             print(f"  ID: {ds_id} | {title}")


    # meta = get_dataset_metadata("dataset_id_here")
    # for resource in meta.get("resources", []):
    #     if resource["format"] == "csv":
    #         download_resource(resource["url"], resource["name"])
    