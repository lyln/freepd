import axios from 'axios'

baseURL: process.env.VUE_APP_BASE_API

export function douyin(data) {
    return axios({
        method: "post",
        url: "http://127.0.0.1:8000/douyin", 
        data: {
            url: data.url
        }
      })
  }

export function wangyiyun(data) {
    return axios({
        method: "post",
        url: "http://127.0.0.1:8000/wangyiyun", 
        data: {
            url: data.url
        }
      })
  }