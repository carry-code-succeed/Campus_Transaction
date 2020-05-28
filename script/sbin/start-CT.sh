#!/bin/sh
# 启动模块
echo "-------启动模块--------"
echo "启动管理员模块"
nohup python3 -u /root/Campus_Transaction/script/python/Administrator_module.py > /root/CAMPUS_TRANSACTION/log/Administrator_module.log 2>&1 &
echo "启动上下架模块"
nohup python3 -u /root/Campus_Transaction/script/python/Upper_and_lower_rack_module.py > /root/CAMPUS_TRANSACTION/log/Upper_and_lower_rack_module.log 2>&1 &
echo "启动登录注册模块"
nohup python3 -u /root/Campus_Transaction/script/python/User_Registration_Login_module.py > /root/CAMPUS_TRANSACTION/log/User_Registration_Login_module.log 2>&1 &
echo "启动查询模块"
nohup python3 -u /root/Campus_Transaction/script/python/Query_module.py > /root/CAMPUS_TRANSACTION/log/Query_module.log 2>&1 &
echo "启动测试模块"
nohup python3 -u /root/Campus_Transaction/script/python/testpic.py > /root/CAMPUS_TRANSACTION/log/testpic.log 2>&1 &
# echo "启动定时重启mysql和模块功能"
# nohup timed-restart-mysql.sh  > /root/CAMPUS_TRANSACTION/log/timed-restart-mysql.log 2>&1 &
echo "-------启动完成--------"
