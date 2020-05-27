echo "-------分割线--------"
NAME=python3
echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "-------分割线--------"
for id in $ID
do
kill -9 $id
echo "killed $id"
done
echo "-------分割线--------"
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
echo "-------分割线--------"
