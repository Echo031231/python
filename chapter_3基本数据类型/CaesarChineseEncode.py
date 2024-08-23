ptxt = input("请输入明文文本:")

for p in ptxt:
    if 'a' <= p <= 'z':
        print(chr((ord(p)-ord('a')-3)%26 + ord('a')), end="" )
    elif 'A' <= p <= 'Z':
        print(chr((ord(p)-ord('A')-3)%26 + ord('A')), end="" )
    elif 0x4E00 <= ord(p) <= 0x9FA5:   # 中文字符加密处理
        print(chr(ord(p) + 3), end="")
    else:
        print(p,end="")


