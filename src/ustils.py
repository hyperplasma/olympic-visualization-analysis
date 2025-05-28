def standardize_country_name(name):
    """
    国家名标准化（可根据需要补充映射表）
    """
    mapping = {
        'United States': 'United States of America',
        'Russia': 'Russian Federation',
        # 可继续补充
    }
    return mapping.get(name, name)