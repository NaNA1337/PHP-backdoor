import hashlib
import base64


def decrypt_request(cmd, key):
    # Base64解码key
    decoded_key = base64.b64decode(key).decode()

    # 反转cmd
    reversed_cmd = cmd[::-1]

    # 计算反转命令的MD5哈希
    hashed_reversed_cmd = hashlib.md5(reversed_cmd.encode()).hexdigest()

    # 检查hash值与解码后的key是否匹配
    if hashed_reversed_cmd != decoded_key:
        raise ValueError("Invalid key")

    # Base64解码cmd
    decrypted_cmd = base64.b64decode(cmd).decode()
    return decrypted_cmd


if __name__ == "__main__":
    # 示例：假设从PHP脚本中获取到的cmd和key
    cmd = "d2hvYW1p"  # Base64编码后的命令
    key = "MGY4Y2MzYWI0NmFmN2U3MTE4YWE2NTBlYmIyN2MyMDI=="  # Base64编码后的MD5哈希

    try:
        decrypted_command = decrypt_request(cmd, key)
        print(f"Decrypted command: {decrypted_command}")
    except ValueError as e:
        print(e)
