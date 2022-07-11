import axios from 'axios'

// let baseURL='http://127.0.0.1:9000/'
axios.defaults.baseURL= 'http://0.0.0.0:9000/'

export function douyin(data) {
    return axios({
        method: "post",
        url: "douyin", 
        data: {
            url: data.url
        }
      })
  }

export function wangyiyun(data) {
    return axios({
        method: "post",
        url: "wangyiyun", 
        data: {
            url: data.url
        }
      })
  }
export function kuaishou(data) {
    return axios({
        method: "post",
        url: "kuaishou", 
        data: {
            url: data.url
        }
      })
  }
export function lizhiFM(data) {
    return axios({
        method: "post",
        url: "lizhiFM", 
        data: {
            url: data.url
        }
      })
  }
export function bilibili(data) {
    return axios({
        method: "post",
        url: "bilibili", 
        data: {
            url: data.url
        }
      })
  }