#!/usr/bin/python
from os import pathsep
import os
import boto3
from boto.s3.connection import S3Connection
from boto.s3.key import Key

AWS_ACCESS_KEY = '#########'
AWS_ACCESS_SECRET_KEY = '###########33'
bucket = "mybucketdefault"

conn = S3Connection(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, host='s3.us-east-2.amazonaws.com')

bucket = conn.get_bucket(bucket, validate=True)

s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key= AWS_ACCESS_SECRET_KEY)

bucket2 = s3.Bucket("mybucketdefault")

l = bucket.get_all_keys()


for keys in l:
    try:

        k = Key(bucket)
        
        print(k)
        k.key = keys.key
        ruta = k.key
        ruta2 = ruta.split("/")
        rutaEnd = ''
        print(ruta2)
        for r in ruta2:
            val = r.find('.csv')
            if val > 1:
                print(r)
            else:
                rutaEnd = rutaEnd + '/' + r
        print('ruta final')
        rutaEnd = rutaEnd + '/'
        path = './' + str(k.key)
        print(rutaEnd)

        os.makedirs(rutaEnd, exist_ok=True)
        if os.path.exists(path):
            print('Archivo existe')
        else:
            bucket2.download_file(k.key, path)
    except ValueError as err:
        print('<-- error --> \n')
        print(err)
    finally:
        print(keys.key)
