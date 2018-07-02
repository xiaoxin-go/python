"""
分割字符串或文本文件并交互地进行分页
"""
def more(text, numlies=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlies]
        lines = lines[numlies:]
        for line in chunk:print(line)
        if input('More?') not in ['y', 'Y']:break

if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(),10)