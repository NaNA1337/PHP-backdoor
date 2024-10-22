import base64
import hashlib

def encrypt_command_php_style(command):
    # 1. 对原始命令进行 Base64 编码
    base64_encoded_cmd = base64.b64encode(command.encode()).decode()

    # 2. 逐字符反转 Base64 编码的命令（严格按照 PHP 逻辑）
    reversed_cmd = ''.join(base64_encoded_cmd[i]
                           for i in range
                           (len
                            (base64_encoded_cmd) - 1, -1, -1))

    # 3. 计算反转后的命令的 MD5 哈希
    hashed_reversed_cmd = hashlib.md5(reversed_cmd.encode()).hexdigest()

    # 4. 对 MD5 哈希进行 Base64 编码，作为密钥
    key = base64.b64encode(hashed_reversed_cmd.encode()).decode()

    return base64_encoded_cmd, key

if __name__ == "__main__":
    # 原始命令
    original_command = ("cat /flag")

    # 加密命令和密钥
    cmd, key = encrypt_command_php_style(original_command)

    print(f"Encoded cmd: {cmd}")  # 输出 Base64 编码的命令
    print(f"Encoded key: {key}")  # 输出 Base64 编码的密钥
