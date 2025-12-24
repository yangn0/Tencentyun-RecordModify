import idkey
import json
# 获取wan ip
import paramiko
pkey = paramiko.RSAKey.from_private_key_file('/home/yangn0/.ssh/id_rsa')
try:
    # 建立连接
    trans = paramiko.Transport(('192.168.123.2', 10022))
    trans.connect(username='yangn0', password=idkey.nassshpwd)

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig enp3s0 | grep 'scopeid 0x0<global>' | sed 's/^.*inet6 //g' | sed 's/prefixlen.*$//g'")
    stdin.close()

    # 获取输出
    ip=stdout.read().decode().strip(" \n")
    print(ip)
    # 关闭连接
    ssh.close()
except Exception as err:
    print(err)

# ipv4
try:
    # 建立连接
    trans = paramiko.Transport(('192.168.123.1', 10022))
    trans.connect(username=idkey.username, password=idkey.sshpwd)
    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig ppp0 | grep 'inet ' | sed 's/^.*addr://g' | sed s/P-t-P.*$//g")
    ipv4=stdout.read().decode().strip(" \n")
    print(ipv4)
    # 关闭连接
    ssh.close()
except Exception as err:
    print(err)

# import requests
# def get_external_ip():
#     try:
#         r = requests.get('https://www.ip.cn/api/index?ip&type=0')
#         d=json.loads(r.text)
#         return d["ip"]
#     except:
#         return None
# ip=get_external_ip()
# print(ip)

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models


try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
    # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
    # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
    cred = credential.Credential(idkey.SecretId, idkey.SecretKey)
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "dnspod.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = dnspod_client.DnspodClient(cred, "", clientProfile)
except:
    pass

try:
    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.ModifyRecordRequest()
    params = {
        "Domain": "yangning.work",
        "SubDomain": "nas",
        "RecordType": "AAAA",
        "RecordLine": "默认",
        "Value": ip,
        "RecordId": 2000299582
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个ModifyRecordResponse的实例，与请求对象对应
    resp = client.ModifyRecord(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

    params = {
        "Domain": "yangning.work",
        "SubDomain": "cloud",
        "RecordType": "AAAA",
        "RecordLine": "默认",
        "Value": ip,
        "RecordId": 2000301155
    }
    req.from_json_string(json.dumps(params))
    resp = client.ModifyRecord(req)
    print(resp.to_json_string())

except:
    pass

try:
    params = {
        "Domain": "yangning.work",
        "SubDomain": "nas",
        "RecordType": "A",
        "RecordLine": "默认",
        "Value": ipv4,
        "RecordId": 1968451021
    }
    req.from_json_string(json.dumps(params))
    resp = client.ModifyRecord(req)
    print(resp.to_json_string())

    params = {
        "Domain": "yangning.work",
        "SubDomain": "cloud",
        "RecordType": "A",
        "RecordLine": "默认",
        "Value": ipv4,
        "RecordId": 1968451393
    }
    req.from_json_string(json.dumps(params))
    resp = client.ModifyRecord(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
except Exception as err:
    print(err)
