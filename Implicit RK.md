# Implicit Runge-Kutta Method

# Contents
- [目标问题](#目标问题)
- [环境依赖](#环境依赖)
- [目录结构](#目录结构描述)

### 目标问题
$$
y'= f(x,y),y(x_0)=y_0.
$$

### 环境依赖
* matlab

### 目录结构描述
├── Main.m                      // 主程序 </br>
├── Division                    // 划分域 </br>
├   ├── Division.m              // 划分域子程序，返回划分好的区域边界点 </br>
├   ├── legs.m                  // 计算高斯-勒让德划分点 </br>
├   ├── legslb.m                // 计算高斯-洛巴托划分点 </br>
├   ├── legsrd.m                // 计算高斯-拉道划分点 </br>
├   ├── lepoly.m                // 计算勒让德多项式及其导数 </br>
├── coefficient                 // 获取系数 </br>
├   ├── GetA.m                  // 获取参数A矩阵 </br>
├   ├── GetB.m                  // 获取参数B矩阵 </br>
├── f.m                         // 修改初始条件及函数f </br>
└── CalY.m                      // 决定方法阶数并计算下一时刻的目标函数值
