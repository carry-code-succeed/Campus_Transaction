#!/bin/sh
# 校易小程序后台管理功能
# /root/Campus_Transaction/script/sbin/set-permissions.sh
echo "#######输入数字使用功能#######"
echo "1：git pull"
echo "2：启动模块"
echo "3：停止模块"
echo "4：重启模块"
echo "5：修复git pull分支"
echo "6：一键pull并重启模块"
echo "7：打印管理员模块日志文件内容"
echo "8：打印上下架模块日志文件内容"
echo "9：打印注册登录模块日志文件内容"
echo "10：打印查询模块日志文件内容"
# echo "11：打印管理员模块日志文件内容"
echo "99：重新查看此菜单"
echo "0：退出"
echo "##########################"
while [ "$num" != "0" ]
do
	echo -n "请输入数字："
	read num
	if [ "$num" = "1" ] ;then
		echo `git-pull.sh`
	elif [ "$num" = "2" ] ;then
		echo `start-CT.sh`
	elif [ "$num" = "3" ] ;then
		echo `stop-CT.sh`
	elif [ "$num" = "4" ] ;then
		echo `restart-CT.sh`
	elif [ "$num" = "5" ] ;then
		echo `repair-branch.sh`
	elif [ "$num" = "6" ] ;then
                	echo `update-restart.sh`
	elif [ "$num" = "7" ] ;then
		cat ~/CAMPUS_TRANSACTION/log/Administrator_module.log
	elif [ "$num" = "8" ] ;then
		cat ~/CAMPUS_TRANSACTION/log/Upper_and_lower_rack_module.log
	elif [ "$num" = "9" ] ;then
		cat ~/CAMPUS_TRANSACTION/log/User_Registration_Login_module.log
	elif [ "$num" = "10" ] ;then
		cat ~/CAMPUS_TRANSACTION/log/Query_module.log
	elif [ "$num" = "99" ] ;then
		echo "#######输入数字使用功能#######"
		echo "1：git pull"
		echo "2：启动模块"
		echo "3：停止模块"
		echo "4：重启模块"
		echo "5：修复git pull分支"
		echo "6：一键pull并重启模块"
		echo "7：重启mysql数据库"
		echo "7：打印管理员模块日志文件内容"
		echo "8：打印上下架模块日志文件内容"
		echo "9：打印注册登录模块日志文件内容"
		echo "10：打印查询模块日志文件内容"
		echo "99：重新查看此菜单"
		echo "0：退出"
		echo "##########################"
	fi
done
echo "结束"





