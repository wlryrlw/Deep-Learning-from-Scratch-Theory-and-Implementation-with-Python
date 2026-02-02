import numpy as np

def And(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
    
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1    

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == "__main__":
    # 定义输入组合
    inputs = [(0, 0), (1, 0), (0, 1), (1, 1)]

    print(f"{'Input':<10} | {'AND':<5} | {'NAND':<5} | {'OR':<5} | {'XOR':<5}")
    print("-" * 45)

    for x1, x2 in inputs:
        out_and  = AND(x1, x2)
        out_nand = NAND(x1, x2)
        out_or   = OR(x1, x2)
        out_xor  = XOR(x1, x2)
        
        print(f"({x1}, {x2})      | {out_and:<5} | {out_nand:<5} | {out_or:<5} | {out_xor:<5}")