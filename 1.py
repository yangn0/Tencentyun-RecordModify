import requests
import json
import time
import hmac
import base64
import hashlib
import random
import api

getip_url='http://jsonip.com'

while(1):
    try:
        time.sleep(60)
        r=requests.get(getip_url)
        ip=json.loads(r.text)['ip']
        print(ip)
        qcloud = api.QcloudApi()
        ret = qcloud.get(module='cns', action='RecordModify', domain='yangning.work', recordId=593013342, subDomain='@', value=ip, recordType='A', recordLine='默认')
        print(ret)
    except:
        print("失败")
        continue