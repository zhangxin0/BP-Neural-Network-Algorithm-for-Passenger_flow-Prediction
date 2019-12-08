from datetime import datetime
from datetime import timedelta
from get_weather import GetWeather

class GenRes():
    def gen_dates(self, b_date, days):
        day = timedelta(days=1)
        # print(day)
        for i in range(days):
            # print(b_date + day*i)
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
            # print(d)   # datetime.datetime  类型
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
        start_date = '2018-01-01'
        end_date = '2019-08-11'
        date = self.get_date_list(start_date, end_date)  # 两个日期之间的所有日期，包括开始日期， 包括 结束日期
        week = []
        weather = []
        # print(get_month_list(start_date, end_date)) # 两个日期之间的所有月份，包括开始月份， 包括 结束月份
        for d in date:
            week_day = datetime.strptime(d, '%Y%m%d').weekday() + 1
            week.append(week_day)
            
        return res


get_date = GenRes()
date, week = get_date.get_res()
print(week)
