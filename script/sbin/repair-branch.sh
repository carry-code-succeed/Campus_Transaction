#!/bin/sh
# 修复git pull分支
echo "-------修复git pull--------"
cd /root/Campus_Transaction
git fetch origin
git clean -f
git reset --hard origin/master
echo "-------修复完成--------"
/root/Campus_Transaction/script/sbin/set-permissions.sh