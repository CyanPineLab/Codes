# Spectral (Finite) Volume Method for 1D hyperbolic conservation laws

# Contents
- [目标问题](#目标问题)
- [环境依赖](#环境依赖)
- [目录结构](#目录结构描述)

### 目标问题
$$
u_t+u_x=0.
$$

求解一维空间中的双曲守恒律，系数为常系数。并可分析误差收敛性、超收敛性等性质。

### 环境依赖
* matlab

### 目录结构描述
├── Main.m // 主程序 </br>
├ 剖分网格 </br>
├── Division.m </br>
├── Getmesh.m </br>
├── legs.m </br>
├── legslb.m </br>
├── legsrd.m </br>
├── lepoly.m </br>
├ 数值计算 </br>
├── RK_solution.m </br>
├── SepctrlVolume_1D.m </br>
├── Projection.m </br>
├── L_operator.m </br>
├── Reconstruct_value.m </br>
├── Reconstruct_value_deri_1.m </br>
├── Reconstruct_value_new.m </br>
├── Reconstruct_value_new_1.m </br>
├ 误差分析 </br>
├── Data_result.m </br>
├── Data_result_super.m </br>
├── Error_analysis.m </br>
├── Error_analysis_super.m </br>
├── Error_calculation.m </br>
├── Error_calculation_super.m </br>
├── struct_error.m </br>
├── struct_error_super.m </br>
├── Results of Error and Rate.xls </br>
├── Results_super of Error and Rate.xls </br>
├ 结果展示 </br>
├── Rate_show.m </br>
├── Rate_show_super.m </br>
└── Pic_show.m
