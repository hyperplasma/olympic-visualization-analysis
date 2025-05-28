import pandas as pd

def clean_olympics_results(filepath):
    df = pd.read_csv(filepath)
    # 只保留有奖牌的记录
    df = df[df['medal'].notna()]
    # 标准化国家代码
    df['noc'] = df['noc'].str.upper()
    # 只保留主要字段
    df = df[['year', 'type', 'discipline', 'event', 'noc', 'medal']]
    return df

def clean_gdp_population(filepath):
    df = pd.read_csv(filepath)
    # 标准化国家名
    df['Country Name'] = df['Country Name'].str.strip()
    # 清洗GDP字段，去除$和,，转为float
    df['GDP (purchasing power parity)'] = pd.to_numeric(
        df['GDP (purchasing power parity)']
        .replace('[\$,]', '', regex=True)
        .replace('unknown', None)
        .str.replace(' ', ''),
        errors='coerce'
    )
    # 清洗人口字段，去除,，转为float
    df['Population'] = pd.to_numeric(
        df['Population']
        .replace(',', '', regex=True)
        .replace('unknown', None),
        errors='coerce'
    )
    # 只保留主要字段
    df = df[['Country Name', 'Country Code', 'GDP (purchasing power parity)', 'Population']]
    return df

def clean_happiness(filepath):
    df = pd.read_csv(filepath)
    # 标准化国家名
    if 'Country name' in df.columns:
        df['Country'] = df['Country name']
    elif 'Country' not in df.columns and 'Country or region' in df.columns:
        df['Country'] = df['Country or region']
    # 只保留主要字段
    keep_cols = [col for col in df.columns if 'Country' in col or 'GDP' in col or 'Happiness' in col or 'Score' in col]
    df = df[keep_cols]
    return df

if __name__ == "__main__":
    # 检查奥运奖牌数据清洗
    olympics_df = clean_olympics_results("./data/Olympics-Dataset-master/clean-data/results.csv")
    print(olympics_df.head())

    # 检查经济数据清洗
    gdp_df = clean_gdp_population("./data/2020-All Country_data_GDP, Population, Electricity-consumption and many more.csv")
    print(gdp_df.head())

    # 检查幸福报告数据清洗
    happiness_df = clean_happiness("./data/Exploring-World-Happiness-main/Resources/2020.csv")
    print(happiness_df.head())