'''
 * Copyright 2024 
 * Licensed under the MIT license 
 * @author txf
 * @date 2024-04-04 09:08:08
'''
import itertools as its

# 自定义密码生成
words = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*?."

# 生成密码本的位数，五位数，repeat=5 自定义密码位数
r = its.product(words, repeat = 8)

# 保存在文件中，追加
dic = open("./pwd.txt", "a")

# i是元组
for i in r:
    # jion空格链接
    dic.write("".join(i))
    dic.write("".join("\n"))
    print("正在生成密码......")
dic.close()
print("密码本已生成")
