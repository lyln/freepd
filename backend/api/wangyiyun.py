# -*-coding: utf-8 -*-

import re

from .music163 import Wangyiyun

from pydantic import BaseModel, Field, HttpUrl
from .base import BaseResponseModel

class RequestModel(BaseModel):
    url: HttpUrl = Field(..., description='网易云链接地址')

class ResponseModel(BaseResponseModel):
    data: dict = None


async def process(request: RequestModel) -> ResponseModel:
        """
        aduios或者videos
        """
        url = request.url
        data = {}
        wangyiyun = Wangyiyun()
        resource_url = wangyiyun.get(url)
        if not resource_url:
            return {"msg": "获取失败"}
        if "mv" in url or "video" in url:
            data["videos"] = [resource_url]
        elif "song" in url:
            data["audios"] = [resource_url]
        print(data)
        return ResponseModel(ok=True,data=data)