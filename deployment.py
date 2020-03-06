#!/usr/bin/env python

import os, sys

path = '/home/g4user/ros_ws/src/'+sys.argv[1]
os.chdir(path)
os.system('bloom-generate rosdebian --os-name ubuntu --os-version xenial --ros-distro kinetic')

file = open('debian/rules','r')
lines  = file.readlines()
str = 'override_dh_shlibdeps:'
str2 = 'override_dh_auto_install:'
index = 0
first_index = 0
for line in lines:
    index = index + 1
    if str in line:
        first_index = index
    if str2 in line:
        seconed_index = index
del lines[first_index : seconed_index-1 ]
lines.insert(first_index,'\tdh_shlibdeps --dpkg-shlibdeps-params=--ignore-missing-info\n\n')

with open('debian/rules', 'w') as f:
    f.writelines(lines[0:len(lines)])
        
os.system('fakeroot debian/rules binary')
os.system('rm -r debian')
os.system('rm -r obj-x86_64-linux-gnu')

print("\033[1;32mFinish.....\033[0m")

