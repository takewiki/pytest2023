from .main import RdFile
from .main import RdBucket
from .__config__ import secret_id
from .__config__ import secret_key
class Bucket(RdBucket):
    def __init__(self,regionName = 'ap-shanghai',bucketName='zhengjia-1251945645'):
        self.secretId = secret_id
        self.secretKey = secret_key
        self.bucketName =bucketName
        self.regionName =regionName
        RdBucket.__init__(self,secretId=self.secretId,secretKey=self.secretKey,regionName=self.regionName,bucketName=self.bucketName)
class File(RdFile):
    def __init__(self,key,bucketName='zhengjia-1251945645',regionName = 'ap-shanghai'):
        self.secretId = secret_id
        self.secretKey = secret_key
        self.regionName = regionName
        self.bucketName = bucketName
        self.key = key
        RdFile.__init__(self,secretId=self.secretId,secretKey=self.secretKey,key=self.key,bucketName=self.bucketName,regionName=self.regionName)

