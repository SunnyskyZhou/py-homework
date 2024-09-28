coal_total=29.5
truck1=4
coal_left=coal_total-truck1*3

truck2=2.5
chance=coal_left / truck2

print("煤的总重(单位：吨)为：",coal_total)
print("第一次运送后，剩下的煤的总重为：",coal_left)
print("第二批卡车的最大载重(单位：吨)为：",truck2)
print("第二次运送需要的次数为：",int(chance))