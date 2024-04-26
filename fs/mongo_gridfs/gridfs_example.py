from pymongo import MongoClient
import gridfs
import urllib.parse

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('admin')

db = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password)).gridfs_example
fs = gridfs.GridFS(db)

a = fs.put(b"hello world")

fs.get(a).read()

b = fs.put(fs.get(a), filename="foo", bar="baz")
print(b)
out = fs.get(b)
out.read()
print(out.filename)
print(out.bar)
print(out.upload_date)
