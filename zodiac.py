# 白羊座：3月21日～4月19日
# 金牛座：4月20日～5月20日
# 双子座：5月21日～6月21日
# 巨蟹座：6月22日～7月22日
# 狮子座：7月23日～8月22日
# 处女座：8月23日～9月22日
# 天秤座：9月23日～10月23日
# 天蝎座：10月24日～11月22日
# 射手座：11月23日～12月21日
# 摩羯座：12月22日～1月19日
# 水瓶座：1月20日～2月18日
# 双鱼座：2月19日～3月20日


zodiac_name = (u'白羊座', u'金牛座', u'双子座', u'金牛座', u'巨蟹座', u'狮子座', u'处女座',
               u'天秤座', u'天蝎座', u'射手座', u'摩羯座', u'水瓶座', u'双鱼座')

zodiac_days = ((3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23),
               (9, 23), (10, 24), (11, 23), (12, 22), (1, 20), (2, 19))


(money, day) = (2, 15)

zodiac_day = filter(lambda x: x <= (money, day), zodiac_days)
print(zodiac_day)

zodiac_len = len(list(zodiac_day)) % 12

print(zodiac_name[zodiac_len])





