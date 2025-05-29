import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud, STOPWORDS

import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Heiti TC']  # Mac 推荐字体
matplotlib.rcParams['axes.unicode_minus'] = False

def plot_medal_bar(medal_df, top_n=20, save_path=None):
    medal_df = medal_df.sort_values('medal_count', ascending=False).head(top_n)
    plt.figure(figsize=(12, 6))
    plt.bar(medal_df['region'], medal_df['medal_count'], color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('国家/地区')
    plt.ylabel('奖牌总数')
    plt.title(f'奖牌总数前{top_n}国家/地区')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_medal_stacked_bar(medal_type_df, top_n=20, save_path=None):
    medal_type_df = medal_type_df.set_index('region')
    medal_type_df = medal_type_df.loc[medal_type_df.sum(axis=1).sort_values(ascending=False).head(top_n).index]
    medal_type_df.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab20')
    plt.xlabel('国家/地区')
    plt.ylabel('奖牌数')
    plt.title(f'奖牌类型分布（前{top_n}国家/地区）')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_medal_gdp_scatter(merged_df, save_path=None):
    merged_df = merged_df.dropna(subset=['GDP_num', 'medal_count'])
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['GDP_num'], merged_df['medal_count'], alpha=0.7)
    plt.xlabel('GDP（美元）')
    plt.ylabel('奖牌总数')
    plt.title('奖牌总数与GDP关系')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_medal_population_bubble(merged_df, save_path=None, annotate_top_n=10):
    merged_df = merged_df.dropna(subset=['Population_num', 'medal_count', 'GDP_num'])
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['Population_num'], merged_df['medal_count'],
                s=merged_df['GDP_num']/1e10, alpha=0.5, c='orange', edgecolors='w', linewidths=0.5)
    top = merged_df.sort_values('medal_count', ascending=False).head(annotate_top_n)
    for _, row in top.iterrows():
        plt.annotate(row['region'], (row['Population_num'], row['medal_count']), fontsize=9, xytext=(5,2), textcoords='offset points')
    plt.xlabel('人口')
    plt.ylabel('奖牌总数')
    plt.title('奖牌总数与人口关系（气泡大小代表GDP）')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_china_trend(china_medals, china_gdp_pop, save_path=None):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(china_medals['year'], china_medals['medal_count'], 'r-o', label='奖牌数')
    ax1.set_xlabel('年份')
    ax1.set_ylabel('奖牌数', color='r')
    ax2 = ax1.twinx()
    try:
        gdp = float(str(china_gdp_pop['GDP (purchasing power parity)'].values[0]).replace('$', '').replace(',', ''))
        ax2.plot(china_medals['year'], [gdp]*len(china_medals), 'b--', label='GDP')
        ax2.set_ylabel('GDP（美元）', color='b')
    except Exception:
        pass
    plt.title('中国历年奖牌数与GDP变化')
    fig.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_corr_heatmap(df, cols, save_path=None):
    corr = df[cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('相关性热力图')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_wordcloud(text_series, save_path=None):
    text = ' '.join(text_series.dropna().astype(str))
    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update([
        'want', 'be', 'lot', 'get', 'make', 'go', 'see', 'take', 'would', 'could', 'should', 
        'really', 'much', 'many', 'one', 'two', 'three', 'also', 'may', 'might', 'can', 'will',
        'im', 'like', 'just', 'exercise', 'fit'
    ])
    font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
    wc = WordCloud(font_path=font_path, width=800, height=400, background_color='white', stopwords=custom_stopwords).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('词云图')
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_gdp_hist(merged_df, save_path=None):
    plt.figure(figsize=(10, 6))
    merged_df['GDP_num'].dropna().plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('GDP（美元）')
    plt.ylabel('国家数')
    plt.title('各国GDP分布直方图')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_medal_boxplot(merged_df, save_path=None):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=merged_df['medal_count'])
    plt.ylabel('奖牌总数')
    plt.title('各国奖牌数箱线图')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_happiness_bar(happiness_df, top_n=20, save_path=None):
    if 'Ladder score' in happiness_df.columns:
        score_col = 'Ladder score'
        country_col = 'Country name'
    elif 'Score' in happiness_df.columns:
        score_col = 'Score'
        country_col = 'Country or region'
    elif 'Happiness score' in happiness_df.columns:
        score_col = 'Happiness score'
        country_col = 'Country'
    else:
        return

    top = happiness_df.sort_values(score_col, ascending=False).head(top_n)
    plt.figure(figsize=(12, 6))
    plt.bar(top[country_col], top[score_col], color='mediumseagreen')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('国家/地区')
    plt.ylabel('幸福度')
    plt.title(f'幸福度前{top_n}国家/地区')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

    bottom = happiness_df.sort_values(score_col, ascending=True).head(top_n)
    plt.figure(figsize=(12, 6))
    plt.bar(bottom[country_col], bottom[score_col], color='salmon')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('国家/地区')
    plt.ylabel('幸福度')
    plt.title(f'幸福度后{top_n}国家/地区')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path.replace('.png', '_bottom.png'))
    plt.show()

def plot_happiness_hist(happiness_df, save_path=None):
    if 'Ladder score' in happiness_df.columns:
        score_col = 'Ladder score'
    elif 'Score' in happiness_df.columns:
        score_col = 'Score'
    elif 'Happiness score' in happiness_df.columns:
        score_col = 'Happiness score'
    else:
        return
    plt.figure(figsize=(10, 6))
    happiness_df[score_col].dropna().plot(kind='hist', bins=20, color='gold', edgecolor='black')
    plt.xlabel('幸福度')
    plt.ylabel('国家数')
    plt.title('全球幸福度分布直方图')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_medal_pie(medal_type_df, country='China', save_path=None):
    row = medal_type_df[medal_type_df['region'] == country]
    if row.empty:
        return
    medals = row.iloc[0][['Gold', 'Silver', 'Bronze']]
    plt.figure(figsize=(6, 6))
    plt.pie(medals, labels=['金', '银', '铜'], autopct='%1.1f%%', colors=['gold', 'silver', '#cd7f32'])
    plt.title(f"{country}奖牌类型占比")
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_gdp_boxplot(merged_df, save_path=None):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=merged_df['GDP_num'])
    plt.ylabel('GDP（美元）')
    plt.title('各国GDP箱线图')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_happiness_gdp_scatter(happiness_df, gdp_df, save_path=None):
    df = happiness_df.merge(gdp_df, left_on='Country', right_on='Country Name', how='left')
    if 'Ladder score' in df.columns:
        score_col = 'Ladder score'
    elif 'Score' in df.columns:
        score_col = 'Score'
    elif 'Happiness score' in df.columns:
        score_col = 'Happiness score'
    else:
        score_col = df.columns[1]
    plt.figure(figsize=(10, 6))
    plt.scatter(df['GDP (purchasing power parity)'], df[score_col], alpha=0.7)
    plt.xlabel('GDP（美元）')
    plt.ylabel('幸福度')
    plt.title('幸福度与GDP关系')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()