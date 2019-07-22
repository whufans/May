#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 11:05
# @Author  : fans
# @File    : Deploy.py
# @Software: PyCharm Community Edition
import sys
from sys import argv
import paramiko
CI_IP='ci.iaskjob.com'   #CI服务器地址
Login_ISA_Key='/back/key/jeson_iaskjob_rsa' #登录ISA的key
Project_IP='172.31.46.37' #工程IP
Project_Login_User='root'   #对应工程机器登录用户
Project_Login_Port='22' #对应工程机器登录端口
Project_Code_File='/tmp/imoocc' #对应工程在CI服务器构建后的执行代码目录
Project_Exclude_File='"/var/cache","/var/tmp","jdbc.profile" ' #不需要向线上同步的文件，如配置文件等等
Project_Backup_Dir='/opt/Jenkins_Backup_Dir' #工程备份目录
Project_Deploy_Path='/opt/imoocc' #工程部署目录
Project_Start_Command='tomcat/bin/catalina.sh start' #工程启动方式
Project_Log_Path='/tmp/imoocc.log' #启动后日志的查看方式

def Gennerate_cmd(Project_Name,CI_IP,Project_Code_File,Project_Exclude_File,Project_Backup_Dir,Project_Deploy_Path,Project_Start_Command,Project_Log_Path):
    cmd = []
    #生成备份命令
    if Project_Backup_Dir:
        #生成备份原有文件
        cmd.append("mkdir -p /opt/")
        cmd.append("rsync -avzP %s %s && touch /tmp/CI_%s_backuptrue"%(Project_Deploy_Path,Project_Backup_Dir,Project_Name))
    #生成关闭原有进程命令
    cmd.append('test -e /tmp/CI_%s_backuptrue && ps -auxgrep "name:%s"grep -v grepawk \'{print $2}\'xargs kill'%(Project_Name,Project_Name))
    #生成命令－确认原来服务已经顺利关闭
    cmd.append('ps -auxgrep "name:%s"grep -v grepawk \'{print $2}\'&& touch /tmp/CI_killSucc  ps -auxgrep "name:%s"grep -v grepawk \'{print $2}\'xargs kill -9'%(Project_Name,Project_Name))
    #生成命令－用于同步新的代码文件
    if Project_Code_File == "":
        cmd.append('test -e "/tmp/CI_%s_killSucc" && rsync -avzP --delete-after --exclude "{%s}" %s::%s %s'%(Project_Name,Project_Exclude_File,CI_IP,Project_Name,Project_Deploy_Path))
    else:
        cmd.append('test -e "/tmp/CI_%s_killSucc" && rsync -avzP --delete-after --exclude "{%s}" %s::%s/%s %s'%(Project_Name,Project_Exclude_File,CI_IP,Project_Name,Project_Code_File,Project_Deploy_Path))
    #生成命令－用于启动服务
    cmd.append(Project_Start_Command)
    #生成命令－查看服务启动后的日志
    cmd.append('tail -n 200 -f %s'%Project_Log_Path)
    #生成命令－清理此次生成的临时文件
    # cmd.append('rm -f /tmp/\*%s\*'%Project_Name)
    return cmd

def Login_Execute_Command(Project_IP,Project_Login_Port,Project_Login_User,Login_ISA_Key,cmds):
    Project_Port = int(Project_Login_Port) if Project_Login_Port else 22
    if Project_IP and Project_Login_User and Login_ISA_Key:
        key = paramiko.RSAKey.from_private_key_file(Login_ISA_Key)
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=Project_IP,port=Project_Port,username=Project_Login_User,pkey=key)
        for cmd_item in cmds:
            stdin,stdout,stderr=s.exec_command(cmd_item)
            print(stdout.read())
        return True
    else:
        return False

def main():
    if len(argv) > 2:
        Config_File = argv[1] if argv[1] else "./Jenkins_Project_Deploy.conf "
        Project_Name = argv[2] if argv[2] else ""
    else:
        print("Error 0:Input argv format error! ./Jenkins_Project_Deploy.py ./test.conf testname")
        sys.exit()
    try:
        # cf = ConfigParser.ConfigParser()
        # cf.read(Config_File)
        # CI_IP = cf.get(Project_Name, "CI_IP")
        # Project_Code_File = cf.get(Project_Name, "Project_Code_File")
        # Project_Exclude_File = cf.get(Project_Name, "Project_Exclude_File")
        # Project_Backup_Dir = cf.get(Project_Name, "Project_Backup_Dir")
        # Project_Deploy_Path = cf.get(Project_Name, "Project_Deploy_Path")
        # Project_Start_Command = cf.get(Project_Name, "Project_Start_Command")
        # Project_Log_Path = cf.get(Project_Name, "Project_Log_Path")
        execute_command = Gennerate_cmd(Project_Name,CI_IP,Project_Code_File,Project_Exclude_File,Project_Backup_Dir,Project_Deploy_Path,Project_Start_Command,Project_Log_Path)
        print("{Step 1: Command collected over!}",execute_command)
        # Project_IP = cf.get(Project_Name, "Project_IP")
        # Project_Login_Port = cf.get(Project_Name, "Project_Login_Port")
        # Project_Login_User = cf.get(Project_Name, "Project_Login_User")
        # Login_ISA_Key = cf.get(Project_Name, "Login_ISA_Key")
    except Exception as e:
        # print("Error 1: %s file open or read error!"%Config_File)
        sys.exit()
    print("{Step 2:Prepare to loging...}",Project_IP)
    result = Login_Execute_Command(Project_IP,Project_Login_Port,Project_Login_User,Login_ISA_Key,cmds=execute_command)
    if result is False:
        print("Error 3:Execute command failed!")
