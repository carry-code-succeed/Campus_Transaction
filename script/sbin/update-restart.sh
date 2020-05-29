#!/bin/sh
# 更新git仓库并重启模块
git-pull.sh
stop-CT.sh
start-CT.sh
