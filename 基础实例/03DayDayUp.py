#Q1  每天进步/退步 1‰
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

#Q2  工作日进步1％，周末退步1％
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)
print("工作日的力量：{:.2f}".format(dayup))

#Q3  Q2模式下工作日每天要努力多少才能和每天努力1％一样
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup *(1-0.01)
        else:
            dayup = dayup *(1 +df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
