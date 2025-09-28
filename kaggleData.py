from kaggle.api.kaggle_api_extended import KaggleApi
import os

def download_academic_dataset(path="dataSources"):
    os.makedirs(path, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        "spscientist/students-performance-in-exams",
        path=path,
        unzip=True
    )
    print("Kaggle dataset downloaded.")

download_academic_dataset()