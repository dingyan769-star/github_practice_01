# 加法
def add(a, b):
    return a + b


# 减法
def sub(a, b):
    return a - b

# 除法
def divide(a, b):
    if b == 0:
        print(f'除数不能为0')
        return
    return a / b

if __name__ == "__main__":

    print(f'加法:')
    print(f"请输入第一个提示： ")
    a = int(input())
    print(f"请输入第二个提示： ")
    b = int(input())
    print(add(a, b))

    print(f'除法:')
    print(f"请输入第一个提示： ")
    a = int(input())
    print(f"请输入第二个提示： ")
    b = int(input())
    print(divide(a, b))