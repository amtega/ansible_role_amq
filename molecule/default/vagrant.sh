#!/bin/bash

source /etc/os-release

major_version=$(echo $VERSION_ID | cut -d. -f1)

if [ $major_version -eq 6 ] || [ $major_version -eq 7 ]; then
    # Disable repos mirror list and point to vault

    sed -i -r "s%(^mirrorlist=.*)%#\1%g" /etc/yum.repos.d/*.repo
    sed -i -r "s%#baseurl=http://mirror.centos.org/%baseurl=http://vault.centos.org/%g" /etc/yum.repos.d/*.repo
fi

if [ $major_version -eq 7 ]; then
    test -f /usr/bin/python3 || yum install -y python3
elif [ $major_version -gt 7 ]; then
    test -f /usr/bin/python3 || dnf install -y python3
fi
