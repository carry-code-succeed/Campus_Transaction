#!/bin/sh
# 定时重启mysql和模块功能
while [ "1" != "0" ];do
	i = 1
	echo "第$i次重启"
	echo `service mysql restart`
	echo `date +%Y-%m-%d-%X`
	restart-CT.sh
#	定时30分钟
	sleep 30m
done