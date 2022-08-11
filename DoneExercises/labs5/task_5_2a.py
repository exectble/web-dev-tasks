# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
x=input('Введите ip и маску:')
x=x.split('.')
ip1=x[0]
ip2=x[1]
ip3=x[2]


mask=x[3]
mask=mask.split('/')
ip4=mask[0]
ip4=int(ip4)

mask1=mask[1]

ms='1'*int(mask1)+'0'*(32-int(mask1))

ms1=ms[:8]
m1=int(ms1,2)

ms2=ms[8:16]
m2=int(ms2,2)

ms3=ms[16:24]
m3=int(ms3,2)

ms4=ms[24:]
m4=int(ms4,2)

ip1=int(ip1) & m1
ip2=int(ip2) & m2
ip3=int(ip3) & m3
ip4=ip4 & m4





ip_template = '''
     IP address:
     {:<8} {:<8} {:<8} {:<8}
     {:08b} {:08b} {:08b} {:08b}
     '''
print(ip_template.format(ip1, ip2, ip3, ip4, int(ip1), int(ip2), int(ip3), int(ip4)))
mask_template = '''
     Mask:
     /{}
     {:<8} {:<8} {:<8} {:<8}
     {:08b} {:08b} {:08b} {:08b}
     '''
print(mask_template.format(mask1,m1, m2, m3, m4, int(m1), int(m2), int(m3), int(m4)))  