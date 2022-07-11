import axios from 'axios'

export function douyin(data) {
    return axios({
        method: "post",
        url: "http://127.0.0.1:8000/douyin", 
        data: {
            url: data.url
        }
      })
  }