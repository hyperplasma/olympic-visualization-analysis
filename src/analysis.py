import pandas as pd

def merge_olympics_gdp(olympics_df, gdp_df, noc_region_path):
    noc_df = pd.read_csv(noc_region_path)
    df = olympics_df.merge(noc_df[['NOC', 'region']], left_on='noc', right_on='NOC', how='left')
    df = df[df['medal'].notna()]
    # 去重：每个国家、每届、每个项目、每种奖牌唯一
    unique_medals = df.drop_duplicates(subset=['year', 'event', 'medal', 'region'])
    medal_count = unique_medals.groupby('region').size().reset_index(name='medal_count')
    merged = medal_count.merge(gdp_df, left_on='region', right_on='Country Name', how='left')
    merged['GDP_num'] = merged['GDP (purchasing power parity)']
    merged['Population_num'] = merged['Population']
    return merged

def medal_type_count(olympics_df, noc_region_path):
    noc_df = pd.read_csv(noc_region_path)
    df = olympics_df.merge(noc_df[['NOC', 'region']], left_on='noc', right_on='NOC', how='left')
    df = df[df['medal'].notna()]
    # 去重：每个国家、每届、每个项目、每种奖牌唯一
    unique_medals = df.drop_duplicates(subset=['year', 'event', 'medal', 'region'])
    medal_pivot = unique_medals.pivot_table(index='region', columns='medal', values='year', aggfunc='count', fill_value=0)
    medal_pivot = medal_pivot.reset_index()
    return medal_pivot

def medal_gdp_corr(merged_df):
    corr_gdp = merged_df['medal_count'].corr(merged_df['GDP_num'])
    corr_pop = merged_df['medal_count'].corr(merged_df['Population_num'])
    return corr_gdp, corr_pop

def merge_with_happiness(medal_df, happiness_df):
    if 'Country' in happiness_df.columns:
        key = 'Country'
    elif 'Country name' in happiness_df.columns:
        key = 'Country name'
    else:
        key = happiness_df.columns[0]
    merged = medal_df.merge(happiness_df, left_on='region', right_on=key, how='left')
    return merged

def china_trend_analysis(olympics_df, gdp_pop_df):
    china_medals = olympics_df[olympics_df['noc'] == 'CHN'].groupby('year').size().reset_index(name='medal_count')
    china_gdp_pop = gdp_pop_df[gdp_pop_df['Country Name'] == 'China']
    return china_medals, china_gdp_pop