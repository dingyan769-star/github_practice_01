# 加法
def add(a, b):
    return a + b


# 减法
def sub(a, b):
    return a - b

if __name__ == "__main__":

    print(f"请输入第一个提示： ")
    a = int(input())
    print(f"请输入第二个提示： ")
    b = int(input())
    print(add(a, b))