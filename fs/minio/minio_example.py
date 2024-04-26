from minio import Minio
import os

# create a connection to server
minioClient = Minio('127.0.0.1:9000',
                    access_key='minioadmin',
                    secret_key='minioadmin',
                    secure=False)
minioClient.make_bucket('example')

# open the file and put the object in bucket called example
with open('file.txt', 'rb') as file_data:
    file_stat = os.stat('file.txt')
    minioClient.put_object('example', 'file.txt', file_data,
                           file_stat.st_size)

# List all object paths in bucket that begin with my-prefixname.
objects = minioClient.list_objects('example', recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)
