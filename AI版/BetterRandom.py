import random

def normal_random(min_val, max_val, mu=None, sigma=None):
    """生成带自定义参数的正态分布随机数
    :param min_val: 最小值
    :param max_val: 最大值
    :param mu: 平均值（可选）
    :param sigma: 标准差（可选）
    """
    if min_val > max_val:
        min_val, max_val = max_val, min_val
        
    # 设置默认参数
    mu = mu if mu is not None else (min_val + max_val) / 2
    sigma = sigma if sigma is not None else (max_val - min_val) / 4
    
    # 生成符合正态分布的值并进行边界约束
    while True:
        val = random.gauss(mu, sigma)
        if min_val < val < max_val:
            return type(min_val)(val) if isinstance(min_val, int) else val