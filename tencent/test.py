import os
import json

from tencentcloud.common.common_client import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    # cred = credential.Credential(
    #     os.environ.get("TENCENTCLOUD_SECRET_ID"),
    #     os.environ.get("TENCENTCLOUD_SECRET_KEY"),
    # )
    cred = credential.ProfileCredential().get_credential()
    httpProfile = HttpProfile()
    # 域名首段必须和下文中CommonClient初始化的产品名严格匹配
    httpProfile.endpoint = "cvm.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    # common client方法支持指定header，如 X-TC-TraceId、X-TC-Canary
    headers = {"X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca"}

    # 实例化要请求的common client对象，clientProfile是可选的。
    common_client = CommonClient(
        "cvm", "2017-03-12", cred, "ap-shanghai", profile=clientProfile
    )
    # 接口参数作为json字典传入，得到的输出也是json字典，请求失败将抛出异常，headers为可选参数
    print(common_client.call_json("DescribeInstances", {"Limit": 10}, headers=headers))
except TencentCloudSDKException as err:
    print(err)
