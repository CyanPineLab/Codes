# Spectral (Finite) Volume Method for 1D hyperbolic conservation laws

# Contents
- [目标问题](#目标问题)
- [环境依赖](#环境依赖)
- [目录结构](#目录结构描述)

### 目标问题
$$
u_t+u_x=0.
$$

### 环境依赖
* matlab

### 目录结构描述
├── Main.m // 主程序 </br>
├ 剖分网格
├── Division.m
├── Getmesh.m
├── legs.m
├── legslb.m
├── legsrd.m
├── lepoly.m
├ 数值计算
├── RK_solution.m
├── SepctrlVolume_1D.m
├── Projection.m
├── L_operator.m
├── Reconstruct_value.m
├── Reconstruct_value_deri_1.m
├── Reconstruct_value_new.m
├── Reconstruct_value_new_1.m
├ 误差分析
├── Data_result.m
├── Data_result_super.m
├── Error_analysis.m
├── Error_analysis_super.m
├── Error_calculation.m
├── Error_calculation_super.m
├── struct_error.m
├── struct_error_super.m
├── Results of Error and Rate.xls
├── Results_super of Error and Rate.xls
├ 结果展示
├── Rate_show.m
├── Rate_show_super.m
└── Pic_show.m
