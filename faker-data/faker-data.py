# -*- coding: utf-8 -*-
# ！usr/bin/python
# ==========================
from faker import Faker
from faker.providers import internet

fake = Faker()
print('============ > 名字')
print(fake.name())
print('============ > 地址')
print(fake.address())
print('============ > 日期')
print(fake.date())
print('============ > 文本')
print(fake.text())
print('============ > ip')
fake.add_provider(internet)
print(fake.ipv4_private())

print('============ > 图片')
print(fake.image_url(width=None, height=None))

print('============ > 多地区 名字')
fake2 = Faker(['zh_CN']) # , 'en_US', 'ja_JP'])
print('============ > 本地化输出')
print(fake2.name())
print(fake2.address())
print(fake2.text())

