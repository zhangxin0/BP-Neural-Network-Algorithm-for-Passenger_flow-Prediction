from datetime import datetime
from datetime import timedelta
from get_weather import GetWeather
import requests
import json


class GenRes():
    def gen_dates(self, b_date, days):
        day = timedelta(days=1)
        for i in range(days):
            yield b_date + day * i

    def get_date_list(self, start_date, end_date):  # end_date=None
        """
        获取日期列表
        :param start: 开始日期
        :param end: 结束日期
        :return:
        """
        if start_date is not None:
            start = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is None:
            end = datetime.now()
        else:
            end = datetime.strptime(end_date, "%Y-%m-%d")
        data = []
        for d in self.gen_dates(start, ((end - start).days + 1)):  # 29 + 1
            data.append(d.strftime("%Y%m%d"))
        return data

    def get_month_list(self, start_date, end_date):
        dates = self.get_date_list(start_date, end_date)
        months = []
        for i in dates:
            if i[:7] not in months:
                months.append(i[:7])
        return months

    def get_res(self):
        # last : 2018-04-26
        start_date = '2018-04-27'
        end_date = '2019-08-11'
        date = self.get_date_list(start_date, end_date)  # 两个日期之间的所有日期，包括开始日期， 包括 结束日期
        res = {}
        # print(get_month_list(start_date, end_date)) # 两个日期之间的所有月份，包括开始月份， 包括 结束月份
        get_weather = GetWeather()
        try:
            for d in date:  # d: 20180101
                print(d)
                week_day = datetime.strptime(d, '%Y%m%d').weekday() + 1
                # "正常工作日对应结果为 0, 法定节假日对应结果为 1, 节假日调休补班对应的结果为 2，休息日对应结果为 3"
                url_holiday = f"http://api.goseek.cn/Tools/holiday?date={d}"
                try:
                    holiday = requests.get(url_holiday).json()['data']
                except Exception as e:
                    holiday = 0
                    print("No holiday type was read:")
                    print(e)
                for hour in range(0, 24):
                    if hour >= 0 and hour <= 4:
                        continue
                    h = str(hour)
                    if len(h) < 2:
                        h = '0' + h
                    key = d + h
                    try:
                        weather = get_weather.get_weather(d, h)
                        data = {}
                        data['t'] = weather['t']
                        data['hum'] = weather['hum']
                        data['weather'] = weather['weather']
                        data['wind'] = weather['wind']
                        data['holiday'] = holiday
                        data['week'] = week_day
                        data['date'] = int(key)
                        #print(data)
                        res[key] = data
                    except Exception as e:
                        print(d+h)
                        print("No weather info was get this hour!")
                        print(e)
                        with open('data.json', 'w') as f:
                            json.dump(res, f)
                        continue
        except Exception as e:
            print("Unkown error.")
            with open('data.json', 'w') as f:
                json.dump(res, f)
            print(e)
        return res

get_date = GenRes()
res = get_date.get_res()
# json.dump() 和 json.load() 来编码和解码json data
# Write res to json:
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(res, f)

# Reading data back
# with open('data.json', 'r') as f:
#     data = json.load(f)
# print(data)
