"""英制单位英寸与公制单位厘米互换"""
value=float(input("请输入长度："))
unit=input("请输入单位：（in/cm）")
if unit=="in":
    print('%.2f英寸=%.2f厘米'%(value,(value*2.54)))
elif unit=="cm":
    print('%.2f厘米=%.2f英寸'%(value,value/2.54))
else:
    print('请输入有效单位')