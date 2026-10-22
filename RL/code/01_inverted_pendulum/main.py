import gym
import random
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import rc
# import numpy as np
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
# from torch.distributions import Categorical

# 创建倒立摆环境
# print(gym.__version__)
env = gym.make('CartPole-v0')

# state = env.reset() # 重置环境的状态为S_0\
# print(state)
#
# action_space = env.action_space # 推车有几个动作（左、右）
# print(action_space)


# --------------------

state = env.reset() # 重置环境的状态 Python
done = False # 游戏是否结束，初始值为False，也就是未结束
episode_rewards = [] # 每回合奖励[𝑅0, 𝑅1, ⋯, 𝑅𝑇]
total_reward = 0 # 带折扣因子的回报（总奖励）
frames = [] # 保存每一帧
gamma = 0.95 # 折扣因子𝛾

# done=True时结束
while not done:
    # 渲染画面，并保存帧
    frames.append(env.render(mode="rgb_array"))

    # 随机选择一个动作𝐴𝑡，0：向左推，1：向右推
    action = random.choice([0, 1])

    # 下一个状态𝑆𝑡+1，即时奖励𝑅𝑡，是否结束，_
    next_state, reward, done, _ = env.step(action)
    # [𝑅0, 𝑅1, ⋯, 𝑅𝑇]
    episode_rewards.append(reward)

# 逆序计算𝐺𝑡 = 𝑅𝑡 + 𝛾𝐺𝑡+1
for r in episode_rewards[::-1]:
    # 𝐺𝑡 = 𝑅𝑡 + 𝛾𝐺𝑡+1
    total_reward = r + gamma * total_reward

print("total_reward:", total_reward)
env.close()
