# -*-coding: utf-8 -*-
# @Author: 'walkerlee'

import re,requests

from pydantic import BaseModel, Field, HttpUrl
from .base import BaseResponseModel

class RequestModel(BaseModel):
    url: HttpUrl = Field(..., description='bilibili链接地址')

class ResponseModel(BaseResponseModel):
    data: dict = None

def get(url: str) -> dict:
    """
    imgs、videos
    """
    data = {}
    headers = {
        "user-agent":
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Referer": "https://www.bilibili.com/",
    }

    av_number_pattern = r'(BV[0-9a-zA-Z]*)'
    cover_pattern = r"readyPoster: '(.*?)',"
    video_pattern = r"readyVideoUrl: '(.*?)',"
    title_pattern = r'title":"(.*?)",'

    av = re.findall(av_number_pattern, url)
    if av:
        av = av[0]
    else:
        data["msg"] = "链接可能不正确，因为我无法匹配到av号"
        return data
    url = f"https://www.bilibili.com/video/{av}"

    with requests.get(url, headers=headers, timeout=10) as rep:
        if rep.status_code == 200:
            cover_url = re.findall(cover_pattern, rep.text)
            if cover_url:
                cover_url = cover_url[0]
                if '@' in cover_url:
                    cover_url = cover_url[:cover_url.index('@')]
                data["imgs"] = ['https:' + cover_url]

            video_url = re.findall(video_pattern, rep.text)
            title_text = re.findall(title_pattern, rep.text)
            if video_url:
                video_url = video_url[0]
                data["videos"] = [video_url]
            if title_text:
                data["videoName"] = title_text[0]
        else:
            data["msg"] = "获取失败"
        return data

async def process(request: RequestModel) -> ResponseModel:
        """
        aduios或者videos
        """
        url = request.url
        data = get(url)
        return ResponseModel(ok=True,data=data)