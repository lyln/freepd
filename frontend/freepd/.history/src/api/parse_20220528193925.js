import axios from 'axios'

let baseURL='http://127.0.0.1:8080'

export function douyin(data) {
    return axios({
        method: "post",
        url: baseURL+"/douyin", 
        data: {
            url: data.url
        }
      })
  }

export function wangyiyun(data) {
    return axios({
        method: "post",
        url: "http://127.0.0.1:8080/wangyiyun", 
        data: {
            url: data.url
        }
      })
  }