import os
def Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_File begin')
    for root, dirs, files in os.walk(window_path):
        for file in files:
            file=os.path.join(root,file)
            print(file)
            cmd = 'E:\STAF\pscp.exe  -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(password=password, window_path=file, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
            os.system(cmd)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_File end')

if __name__ == '__main__':
    window_path = r'E:\AutoDeploy'
    Linux_ip = '172.31.46.37'
    username = 'root'
    password = 'iflytek@206'
    Linux_path = '/home/AutoDeploy'
    Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password)
