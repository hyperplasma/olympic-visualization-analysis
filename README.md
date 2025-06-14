# Olympic Visualization Analysis

[Hyperplasma](https://www.hyperplasma.top) [《奥运体育健康经济大数据可视化分析》——数据采集与可视化项目](https://www.hyperplasma.top/article/12872/)

本项目通过数据清洗、分析与可视化，系统性地探索了奥运奖牌、各国GDP、人口、幸福指数等多维度数据之间的关系。项目包含多种统计图表，支持对奥运奖牌分布、经济与社会指标的多角度分析。

## 主要方法

- **数据清洗**：对奥运奖牌、GDP与人口、幸福指数等原始数据进行标准化、缺失值处理和格式统一。
- **奖牌统计**：按国家/地区统计奖牌总数，并对团体项目去重，确保奖牌数准确。
- **数据合并**：将奖牌数据与经济、人口、幸福指数等数据集按国家/地区合并。
- **多样可视化**：实现了柱状图、堆积柱状图、散点图、气泡图、箱线图、直方图、热力图、饼图、折线图、词云等10余种统计图表，直观展示各类关系。

## 使用的数据集

- **奥运奖牌数据**：`data/Olympics-Dataset-master/clean-data/results.csv` 包含历届奥运会各项目奖牌获得者信息。
- **NOC与地区映射**：`data/Olympics-Dataset-master/clean-data/noc_regions.csv` 用于将NOC代码映射为国家/地区名。
- **全球GDP与人口数据**：data/ `2020-All Country_data_GDP, Population, Electricity-consumption and many more.csv `包含各国GDP（购买力平价）与人口等经济指标。
- **世界幸福指数数据**：`data/Exploring-World-Happiness-main/Resources/2020.csv` 包含各国幸福指数、GDP等社会指标。
- **健身问卷数据**：`data/fitness analysis.csv` 用于生成健身动机词云。
- 其他可选数据集

## 主要可视化图表

- 奖牌总数柱状图
- 奖牌类型堆积柱状图
- 奖牌数与GDP散点图
- 奖牌数与人口气泡图
- 中国历年奖牌与GDP趋势图
- 相关性热力图
- 各国GDP直方图与箱线图
- 各国奖牌数箱线图
- 幸福度前/后20国家柱状图、幸福度直方图
- 中国奖牌类型饼图
- 幸福度与GDP散点图
- 健身动机词云

## 快速开始

1. 克隆仓库并准备好上述数据集（保持目录结构一致）。
2. 根据 `requirements.txt`安装依赖。
3. 运行 `python main.py`，所有图表将输出至 `output/figures/` 目录。

## 依赖库

项目使用的主要Python库包括：

* **matplotlib** (3.7.2): 用于创建静态、动画和交互式可视化
* **numpy** (1.26.4): 提供数值计算支持
* **pandas** (2.0.3): 用于数据处理和分析
* **seaborn** (0.12.2): 基于matplotlib的统计数据可视化
* **wordcloud** (1.9.4): 用于生成词云图

可通过以下命令安装所需依赖：

```bash
pip install -r requirements.txt
```

## 致谢

- [Kaggle Olympics Dataset](https://www.kaggle.com/datasets/the-guardian/olympic-games)
- [World Happiness Report](https://worldhappiness.report/)
- 其他公开数据集
- [Hyperplasma](www.hyperplasa.top)

## LICENSE

[LICENSE](LICENSE)

---

如有问题欢迎提issue或PR！
