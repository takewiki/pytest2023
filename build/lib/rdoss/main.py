from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import requests
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
class Rdfs(CosS3Client):
    def __init__(self,secretId,secretKey,regionName = 'ap-shanghai'):
        self.secretId =secretId
        self.secretKey = secretKey
        self.regionName =regionName
        token = None
        scheme = 'https'
        self.config = CosConfig(Region=self.regionName, SecretId=self.secretId, SecretKey=self.secretKey, Token=token, Scheme=scheme)
        CosS3Client.__init__(self=self,conf=self.config)
class RdBucket(Rdfs):
    def __init__(self,secretId,secretKey,regionName = 'ap-shanghai',bucketName='zhengjia-1251945645'):
        self.secretId = secretId
        self.secretKey = secretKey
        self.regionName = regionName
        self.bucketName = bucketName
        Rdfs.__init__(self,secretId=self.secretId,secretKey=self.secretKey,regionName=self.regionName)


    def list(self):
        res = Rdfs.list_buckets(self)
        return(res)
    def exists(self):
        '''
        check the bucket exists or not.
        :param bucketName:
        :return:
        '''
        res = Rdfs.bucket_exists(self,Bucket=self.bucketName)
        return(res)
    def head(self):
        '''
        check the bucket exists or not and the access right or not.
        :param bucketName:
        :return:
        '''
        res = Rdfs.head_bucket(self,
            Bucket=self.bucketName
        )
        return(res)
    def create(self):
        res = Rdfs.create_bucket(self,Bucket=self.bucketName)
        return(res)
    def delete(self):
        '''
        delete the bucket.
        :param bucketName:
        :return:
        '''
        res = Rdfs.delete_bucket(self,
            Bucket=self.bucketName
        )
        return(res)

class RdFile(Rdfs):
    def __init__(self,secretId,secretKey,key,bucketName='zhengjia-1251945645',regionName = 'ap-shanghai'):
        self.secretId = secretId
        self.secretKey = secretKey
        self.regionName = regionName
        self.bucketName = bucketName
        self.key = key
        Rdfs.__init__(self,secretId=self.secretId,secretKey=self.secretKey,regionName=self.regionName)
    def list(self):
        res = Rdfs.list_objects(self,
            Bucket=self.bucketName
        )
        return(res)
    def exists(self):
        '''
        check the object exists or not.
        :param key:
        :param bucketName:
        :return:
        '''
        res = Rdfs.object_exists(self,
            Bucket=self.bucketName,
            Key=self.key)
        return(res)
    def head(self):
        res = Rdfs.head_object(self,
            Bucket=self.bucketName,
            Key=self.key
        )
        return(res)
    def url(self):
        '''
        get the object url
        :param key:
        :param bucketName:
        :return:
        '''
        res = Rdfs.get_object_url(self,
            Bucket=self.bucketName,
            Key=self.key
        )
        return(res)
    def upload(self,fileName,storageClass='STANDARD',enableMD5=False):
        '''
        upload file in binary mode,default one
        :param key:
        :param fileName:
        :param bucketName:
        :param storageClass:
        :param enableMD5:
        :return:
        '''
        self.fileName =fileName
        self.storageClass = storageClass
        self.enableMD5 =enableMD5
        with open(self.fileName, 'rb') as fp:
            res = Rdfs.put_object(self,
                Bucket=self.bucketName,
                Body=fp,
                Key=self.key,
                StorageClass=self.storageClass,
                EnableMD5=self.enableMD5
            )
        return(res['ETag'])
    def uploadUrl(self,url):
        self.url = url
        stream = requests.get(self.url)
        res = Rdfs.put_object(self,
            Bucket=self.bucketName,
            Body=stream,
            Key=self.key
        )
        return(res['ETag'])
    def uploadPro(self,fileName,partSize=1,maxThread=10,enableMD5=False):
        '''
        automatically choose simple upload and splitBatch upload and will continue to upload after breaking.
        :param key:
        :param fileName:
        :param bucketName:
        :param partSize:
        :param maxThread:
        :return:
        '''
        self.fileName = fileName
        self.partSize= partSize
        self.maxThread =maxThread
        self.enableMD5 = enableMD5
        res = Rdfs.upload_file(self,
            Bucket=self.bucketName,
            LocalFilePath=self.fileName,
            Key=self.key,
            PartSize=self.partSize,
            MAXThread=self.maxThread,
            EnableMD5=self.enableMD5
        )
        print(response['ETag'])
    def download(self,fileName):
        self.fileName = fileName
        response = Rdfs.get_object(self,
            Bucket=self.bucketName,
            Key=self.key
        )
        response['Body'].get_stream_to_file(self.fileName)
    def delete(self):
        '''
        delete the file by Key.
        :param key:
        :param bucketName:
        :return:
        '''
        res = Rdfs.delete_object(self,
            Bucket=self.bucketName,
            Key=self.key
        )
        return(res)
    def copy(self,keyFrom,bucketNameFrom='zhengjia-1251945645',regionFrom='ap-guangzhou'):
        '''
        copy file by key from another region
        :param keyFrom:
        :param keyTo:
        :param bucketNameFrom:
        :param bucketNameTo:
        :param regionFrom:
        :return:
        '''
        self.keyFrom = keyFrom
        self.bucketNameFrom =bucketNameFrom

        self.regionFrom = regionFrom

        res = Rdfs.copy(self,
            Bucket=self.bucketName,
            Key=self.key,
            CopySource={
                'Bucket': self.bucketNameFrom,
                'Key': self.keyFrom,
                'Region': self.regionFrom
            }
        )
        return(res)

    def move(self, keyFrom,  bucketNameFrom='zhengjia-1251945645',
             regionFrom='ap-guangzhou'):
        '''
        move file by key from another region into 2 step with copy and delete
        :param keyFrom:
        :param keyTo:
        :param bucketNameFrom:
        :param bucketNameTo:
        :param regionFrom:
        :return:
        '''
        self.keyFrom = keyFrom
        self.bucketNameFrom = bucketNameFrom
        self.regionFrom = regionFrom

        res = self.copy(
                        keyFrom=self.keyFrom,
                        bucketNameFrom=self.bucketNameFrom,
                        regionFrom=self.regionFrom)
        app = Rdfs(secretId=self.secretId,secretKey=self.secretKey,regionName=self.regionFrom)
        app.delete_object(       Bucket=self.bucketNameFrom,
                                 Key=self.keyFrom
                                 )
        return(res)





if __name__ =='__main__':
    pass






