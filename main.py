import os
from src.data_cleaning import (
    clean_olympics_results,
    clean_gdp_population,
    clean_happiness
)
from src.analysis import (
    merge_olympics_gdp,
    medal_type_count,
    medal_gdp_corr,
    merge_with_happiness,
    china_trend_analysis
)
from src.visualization import (
    plot_medal_bar,
    plot_medal_stacked_bar,
    plot_medal_gdp_scatter,
    plot_medal_population_bubble,
    plot_china_trend,
    plot_corr_heatmap,
    plot_wordcloud,
    plot_gdp_hist,
    plot_medal_boxplot,
    plot_happiness_bar,
    plot_happiness_hist,
    plot_medal_pie,
    plot_gdp_boxplot,
    plot_happiness_gdp_scatter
)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == "__main__":
    # 路径配置
    olympics_path = "./data/Olympics-Dataset-master/clean-data/results.csv"
    noc_region_path = "./data/Olympics-Dataset-master/clean-data/noc_regions.csv"
    gdp_path = "./data/2020-All Country_data_GDP, Population, Electricity-consumption and many more.csv"
    happiness_path = "./data/Exploring-World-Happiness-main/Resources/2020.csv"
    fitness_path = "./data/fitness analysis.csv"

    output_dir = "./output/figures"
    ensure_dir(output_dir)

    # 数据清洗
    olympics_df = clean_olympics_results(olympics_path)
    gdp_df = clean_gdp_population(gdp_path)
    happiness_df = clean_happiness(happiness_path)

    # 数据分析
    merged_df = merge_olympics_gdp(olympics_df, gdp_df, noc_region_path)
    medal_type_df = medal_type_count(olympics_df, noc_region_path)
    corr_gdp, corr_pop = medal_gdp_corr(merged_df)
    print(f"奖牌数与GDP相关系数: {corr_gdp:.3f}，与人口相关系数: {corr_pop:.3f}")

    merged_happiness = merge_with_happiness(merged_df, happiness_df)
    china_medals, china_gdp_pop = china_trend_analysis(olympics_df, gdp_df)

    # 可视化
    plot_medal_bar(merged_df, save_path=f"{output_dir}/medal_bar.png")
    plot_medal_stacked_bar(medal_type_df, save_path=f"{output_dir}/medal_stacked_bar.png")
    plot_medal_gdp_scatter(merged_df, save_path=f"{output_dir}/medal_gdp_scatter.png")
    plot_medal_population_bubble(merged_df, save_path=f"{output_dir}/medal_population_bubble.png")
    plot_china_trend(china_medals, china_gdp_pop, save_path=f"{output_dir}/china_trend.png")
    plot_corr_heatmap(merged_df, ['medal_count', 'GDP_num', 'Population_num'], save_path=f"{output_dir}/corr_heatmap.png")
    plot_gdp_hist(merged_df, save_path=f"{output_dir}/gdp_hist.png")
    plot_medal_boxplot(merged_df, save_path=f"{output_dir}/medal_boxplot.png")
    plot_happiness_bar(happiness_df, save_path=f"{output_dir}/happiness_bar.png")
    plot_happiness_hist(happiness_df, save_path=f"{output_dir}/happiness_hist.png")
    plot_medal_pie(medal_type_df, country='China', save_path=f"{output_dir}/china_medal_pie.png")
    plot_gdp_boxplot(merged_df, save_path=f"{output_dir}/gdp_boxplot.png")
    plot_happiness_gdp_scatter(happiness_df, gdp_df, save_path=f"{output_dir}/happiness_gdp_scatter.png")
    # 词云（健身问卷）
    if os.path.exists(fitness_path):
        import pandas as pd
        fitness_df = pd.read_csv(fitness_path)
        if 'What motivates you to exercise?         (Please select all that applies )' in fitness_df.columns:
            plot_wordcloud(fitness_df['What motivates you to exercise?         (Please select all that applies )'],
                           save_path=f"{output_dir}/fitness_wordcloud.png")