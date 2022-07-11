import axios from 'axios'

let baseURL='http://127.0.0.1:8080/'

export function douyin(data) {
    return axios({
        method: "post",
        url: baseURL+"douyin", 
        data: {
            url: data.url
        }
      })
  }

export function wangyiyun(data) {
    return axios({
        method: "post",
        url: baseURL+"wangyiyun", 
        data: {
            url: data.url
        }
      })
  }
export function kuaishou(data) {
    return axios({
        method: "post",
        url: baseURL+"kuaishou", 
        data: {
            url: data.url
        }
      })
  }
export function lizhiFM(data) {
    return axios({
        method: "post",
        url: baseURL+"lizhiFM", 
        data: {
            url: data.url
        }
      })
  }