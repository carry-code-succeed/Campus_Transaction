#!/bin/sh
# 定时重启mysql和模块功能
declare -i i
i=1
while [ "1" != "0" ];do
	echo "第$i次重启"
	i=i+1
	echo `service mysql restart`
	echo `date +%Y-%m-%d-%X`
	restart-CT.sh
#	定时30分钟
	sleep 30m
done