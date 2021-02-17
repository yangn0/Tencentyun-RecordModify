import requests
import json
import time
import hmac
import base64
import hashlib
import random
import api

getip_url='https://ipv4.jsonip.com/'

while(1):
    try:
        r=requests.get(getip_url)
        ip=json.loads(r.text)['ip']
        print(ip)
        qcloud = api.QcloudApi()
        ret = qcloud.get(module='cns', action='RecordModify', domain='yangning.work', recordId=742259884, subDomain='@', value=ip, recordType='A', recordLine='默认')
        print(ret)
        time.sleep(600)
    except:
        print("失败")
        time.sleep(600)
        continue