import pandas as pd

def factor_stat(df):
    n = len(df)

    ret_ari = (df / 100).mean(axis = 0) * 12
    ret_geo = (1 + df / 100).prod()**(12 / n) - 1
    vol = (df / 100).std(axis = 0) * np.sqrt(12)
    sharp = ret_ari/ vol

    stat = pd.DataFrame(
        [ret_ari, ret_geo, vol, sharp],
        index=['연율ㅏ 수ㄱㅠㄹ)산술)', '연율화 수익률(기하)', '연율화 변동성', '샤프지수']).round(4)
    
    stat.iloc[0:3, ] = stat.iloc[0:3, ] * 100

    return stat