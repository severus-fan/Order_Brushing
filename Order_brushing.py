import pandas as pd
import numpy as np
import datetime

csv_data = pd.read_csv("order_brush_order.csv")  # 读取csv

csv_data["event_time"] = pd.to_datetime(csv_data["event_time"])  # 转换成日期格式
# 把所有数据按照【用户号+店名】联合分组
for (shopid, userid), group in csv_data.groupby(["shopid", "userid"]):
    if group.shape[0] > 3:  # group大于三条数据，才有刷单可能
        for index, row in group.iterrows():
            st = row.event_time
            if group[(st < group['event_time']) & (group['event_time'] < st + datetime.timedelta(hours=1))].shape[0] > 3:
                print(shopid, userid)
                # break

#               orderid     shopid     userid           event_time
# 0      31411143816483    8834405  188684082  2019-12-30 21:19:03
# 1      31241240213066  156498720   65999766  2019-12-28 22:07:21
# 2      31199268291311  137490922    6840419  2019-12-28 10:27:48
# 3      31162754073727   96757689   69785144  2019-12-28 00:19:14
# 4      31322906493814   52934282  143307391  2019-12-29 20:48:26
# ...               ...        ...        ...                  ...
# 22270  31403777053917     240309      27567  2019-12-30 19:16:17
# 22271  31399325557224   41293031  190817396  2019-12-30 18:02:05
# 22272  31399970387318   10462400   80958696  2019-12-30 18:12:50
# 22273  31504925024665  135054975   18209533  2019-12-31 23:22:05
# 22274  31209167717594  129926387  127668008  2019-12-28 13:12:48


# print(csv_data.event_time[0].year)
# grouped_byshopid = csv_data.groupby('shopid')
# print(csv_data.iloc[0])
# blacklist={'shopid':1,'userid':1}
# print(blacklist)
# csv_data = pd.read_csv("Demo.csv",index_col=0)
