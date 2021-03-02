# -*- coding=utf-8 -*-

# 导入redis sentinel库
from redis.sentinel import Sentinel

# 实例化sentinel对象
sentinel = Sentinel([('localhost', 17001), ('localhost', 17002), ('localhost', 17003)], socket_timeout=0.1)
# 获取主库信息
print(sentinel.discover_master('mymaster'))
# 获取从库信息
print(sentinel.discover_slaves('mymaster'))
# 配置写节点
master = sentinel.master_for('mymaster', socket_timeout=0.1, password='123456')
# 配置从节点
slave = sentinel.slave_for('mymaster', socket_timeout=0.1, password='123456')
# 读写分离测试（字符串拼接）
print('master-mode:', master.set('name', 'olda'))
print('slave-node:', slave.get('name'))
