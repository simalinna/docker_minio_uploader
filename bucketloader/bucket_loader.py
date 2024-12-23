import os

from minio import Minio
from minio.error import S3Error



minio_client = Minio(
    os.environ['MINIO_ENDPOINT'],
    access_key=os.environ['MINIO_ACCESS_KEY'],
    secret_key=os.environ['MINIO_SECRET_KEY'],
    secure=False
)



def load_image_in_bucket(bucket_name, image_ind):
    filename = f"hypnosis{image_ind}.jpg"
    path = "./hypnosis.jpeg"
    try:
        minio_client.fput_object(bucket_name, filename, path)
        print(f"Загружен файл {filename}")
        return True
    except S3Error as error:
        print(f"Ошибка при загрузке файла: {error}")
        return False



def main():

    if not minio_client.bucket_exists("bucket1"):
        minio_client.make_bucket("bucket1")
    
    image_ind = 0
    uploading = load_image_in_bucket("bucket1", image_ind)
    while uploading:
        image_ind +=1
        uploading = load_image_in_bucket("bucket1", image_ind)



if __name__ == "__main__":
    main()
    