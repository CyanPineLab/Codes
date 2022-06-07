# Codes

A repository for codes.

## Contents
- [包含代码](#包含代码)
  - [隐式龙格-库塔法](#隐式龙格-库塔法)
  - [谱体积法](#谱体积法)
  - [谱体积法软件平台](#谱体积法软件平台)
  - [有限体积法](#有限体积法)
- [环境依赖](#环境依赖)
- [备注](#备注)

## 包含代码

#### 隐式龙格-库塔法
* 龙格-库塔法用于非线性常微分方程的解的重要的一类隐式或显式迭代法。显式龙格-库塔法的稳定区域被局限在一个特定的区域里，一般来讲不适用于求解刚性方程。隐式龙格库塔方法在每一步的计算里需要求解一个线性方程组。
* Implicit RK
* Matlab 代码
  
#### 谱体积法
* 求解一维空间中的双曲守恒律，系数为常系数。并可分析误差收敛性、超收敛性等性质。
* Program SV for 1D hyperbolic conservation laws
* Matlab 代码
  
#### 谱体积法软件平台
* 软件平台，分为计算模块和图形界面模块
* 计算模块：实现一维空间双曲守恒律以及Buegers方程的求解，并实现了二维空间双曲守恒律的求解。
* 图形界面模块：用户可通过图形界面调用计算模块进行计算。
* SV for 1D Python
* Python 代码

#### 有限体积法


## 环境依赖
* Matlab
* Python
  > 需要使用numpy库（数值计算）以及wxpython库（图形界面）。

## 备注
...
