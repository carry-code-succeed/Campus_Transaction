#!/bin/sh
# 校易小程序后台管理功能
echo "#######输入数字使用功能#######"
echo "1：git pull"
echo "2：启动模块"
echo "3：停止模块"
echo "4：重启模块"
echo "5：修复git pull分支"
echo "6：一键pull并重启模块"
echo "9：重新查看此菜单"
echo "0：退出"
echo "##########################"
while [ "$num" != "0" ]
do
	echo -n "请输入数字："
	read num
	if [ "$num" = "1" ] ;then
		echo `CTgit.sh`
	elif [ "$num" = "2" ] ;then
		echo `start-CT.sh`
	elif [ "$num" = "3" ] ;then
		echo `stop-CT.sh`
	elif [ "$num" = "4" ] ;then
		echo `rs-CT.sh`
	elif [ "$num" = "5" ] ;then
		echo `rb.sh`
	elif [ "$num" = "6" ] ;then
                	echo `uprs.sh`
	elif [ "$num" = "9" ] ;then
		echo "#######输入数字使用功能#######"
		echo "1：git pull"
		echo "2：启动模块"
		echo "3：停止模块"
		echo "4：重启模块"
		echo "5：修复git pull分支"
		echo "6：一键pull并重启模块"
		echo "9：重新查看此菜单"
		echo "0：退出"
		echo "##########################"
	fi
done
echo "结束"





