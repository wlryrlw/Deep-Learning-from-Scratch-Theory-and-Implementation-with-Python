# 神经网络
神经网络的一个重要性质是它可以自动地从数据中学习到合适的权重参数


![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031557540.png)
**输入层**：最左边的一列，第 0 层
**输出层**：最右边的一列，第 1 层
**中间层（隐藏层）**：中间的一列，第 2 层

## 激活函数
### 引入激活函数
#### 感知机
$$y = h(b + w_1x_1 + w_2x_2)$$
$$h(x)=\begin{cases}
0& \text{x≤0}\\
1& \text{x≠0}
\end{cases}$$

> “朴素感知机” 指单层网络，即激活函数使用了阶跃函数 A 的模型
> “多层感知机” 指神经网络，即使用 sigmoid  函数等平滑的激活函数的多层网络

#### 激活函数
将输入信号的总和转换为输出信号
隐藏层中用 $h(x)$ 表示，输出层中用 $\sigma(x)$ 表示

#### 引入激活函数后的感知机
![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031630071.png)
$$a = b + w_1x_1 + w_2x_2$$
$$y = h(a)$$

### 阶跃函数
$$h(x)=\begin{cases}
0& \text{x≤0}\\
1& \text{x>0}
\end{cases}$$
以阈值为界，一旦输入超过阈值，就切换输出，值呈阶梯变化
![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031646050.png)

感知机中使用阶跃函数作为激活函数

### sigmoid 函数
$$h(x)=\frac{1}{1+e^{-x}}$$
![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031653162.png)

神经网络中使用 sigmoid 函数作为激活函数，转换后的信号被传送给下一个神经元

### 比较阶跃函数与 sigmoid 函数
**相同**：
非线性函数
具有相似的形状，即输入小时，输出接近 0(为 0)；输入增大，输出向 1 靠近(为 1)
输出信号的值都在 0 到 1 之间

**不同**：
平滑性不同，sigmoid 具有平滑性
阶跃函数只能返回 0 或 1，sigmoid 函数可以返回连续的实数值

神经网络的激活函数必须是非线性函数

### ReLU 函数
$$h(x)=\begin{cases}
0& \text{x≤0}\\
x& \text{x>0}
\end{cases}$$
![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031712732.png)


## 输出层设计
### 输出层激活函数
#### 恒等函数
用于回归问题
$$h(x)=x$$
对于输入的信息,不加以任何改动地直接输出

#### softmax 函数
用于分类问题
![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031856584.png)

$$y_k=\frac{exp(a_k)}{\Sigma_{i=1}^nexp(a_i)}=\frac{exp(a_k+C^{'})}{\Sigma_{i=1}^nexp(a_i+C^{'})}$$

输出层共有 $n$ 个神经元，计算第 $k$ 个神经元的输出 $y_k$ ，即输出层的各个神经元都受到所有输入信号的影响
加减某个常数不改变运算的结果，为了防止溢出， $C^{'}$ 一般取输入信号中的最大值的负数

**性质**：
softmax 函数的输出总和为 1，故可以将输出解释为“概率”
各个元素之间的大小关系不会改变

softmax 一般只用于训练（学习）阶段而非推理阶段
在进行分类时，输出层的 softmax 函数可以省略
在实际的问题中，输出层的 softmax 函数也一般会被省略

### 输出层神经元数量
输出层的神经元数量需要根据待解决的问题来决定
对于分类问题，输出层的神经元数量一般设定为类别的数量
![image.png](https://wlry-1323998276.cos.ap-nanjing.myqcloud.com/llm/202602031911305.png)
