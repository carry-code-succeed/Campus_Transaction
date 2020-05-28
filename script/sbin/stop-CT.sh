#!/bin/sh
# 关闭模块
echo "-------查找模块进程--------"
NAME=python3
echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "-------关闭模块--------"
for id in $ID
do
kill -9 $id
echo "killed $id"
done
echo "-------关闭完成--------"
