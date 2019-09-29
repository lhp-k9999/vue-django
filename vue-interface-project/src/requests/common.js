import axios from 'axios'
// 定义后端服务ip和端口
axios.defaults.withCredentials = true;

const host = "http://127.0.0.1:8000/";

// 封装各种请求方法 GET，POST，PUT，DELETE就对应着对这个资源的 查，改，增，删 4个操作

// URL不存在参数上限的问题，HTTP协议规范没有对URL长度进行限制。这个限制是特定的浏览器及服务器对它的限制。
// IE对URL长度的限制是2083字节(2K+35)。对于其他浏览器
export const getRequest = function (path, data={}) {
    return axios.get(host + path, {
        params: data,
        withCredentials: true
    })
};

export const postRequest = function (path, data={}) {
    return axios.post(host + path, data)
};

export const deleteRequest = function (path, data={}) {
    return axios.delete(host + path, data)
};

export const putRequest = function (path, data={}) {
    return axios.put(host + path, data)
};

export const patchRequest = function (path, data={}) {
    return axios.patch(host + path, data)
};

// GET方法的行为很类似，但服务器在响应中只返回实体的主体部分
export const headRequest = function (path,data={}) {
    return axios.head(host+path,data)
}