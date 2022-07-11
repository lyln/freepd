import axios from 'axios'
import { jsonp } from 'vue-jsonp'

axios.defaults.baseURL= process.env.API_ROOT
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

// let baseURL='http://127.0.0.1:9000/'

let headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

export function douyin(data) {
    return jsonp({
        method: "post",
        headers: headers,
        url: "douyin", 
        data: {
            url: String(data.url)
        }
      })
  }

export function wangyiyun(data) {
    return jsonp({
        method: "post",
        headers: headers,
        url: "wangyiyun", 
        data: {
            url: data.url
        }
      })
  }
export function kuaishou(data) {
    return jsonp({
        method: "post",
        headers: headers,
        url: "kuaishou", 
        data: {
            url: data.url
        }
      })
  }
export function lizhiFM(data) {
    return jsonp({
        method: "post",
        headers: headers,
        url: "lizhiFM", 
        data: {
            url: data.url
        }
      })
  }
export function bilibili(data) {
    return jsonp({
        method: "post",
        headers: headers,
        url: "bilibili", 
        data: {
            url: data.url
        }
      })
  }