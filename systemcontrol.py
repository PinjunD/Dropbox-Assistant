import os
import subprocess
import csv
import psutil
import logging
import time
import sys
def create_folder(path,name):
    folder_path = path +'\\'+ name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass
    return folder_path


def search_files(name,directory='C:\\'):
    path = None
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file == name:
                    path = root + '\\' + file
                    return path
                else:
                    pass
        else:
            return path
    except:
        return path


def searchGolbal(name):
    root_directory = 'C:\\'
    path = search_files(name,root_directory)
    if path == None:
        root_directory = 'D:\\'
        path = search_files(name,root_directory)
        if path == None:
            root_directory = 'E:\\'
            path = search_files(name,root_directory)
            if path == None:
                root_directory = 'F:\\'
                path = search_files(name,root_directory)
            else:
                pass
        else:
            pass
    else:
        pass
    return path
def read_txt(file_path):
    D = []
    with open(file_path, 'r', encoding='utf-8') as file:
        # 逐行读取文件内容
        lines = file.readlines()
    # 遍历每一行并输出
    for line in lines:
        D.append(line.strip())  # 使用strip()方法去除行末尾的换行符
    return D


def open_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except IOError:
        pass
        return None
def read_csv_file(file_path):
    rows = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
        print(rows)
    return rows

def AllFile(path):
    File = []
    for filename in os.listdir(path):
        File.append(path+'\\'+filename)
    return File

def FindFile(path,text):
    File = []
    for filename in os.listdir(path):
        if text in filename:
            File.append(path+'\\'+filename)
    return File
def create_file(file_path, content=''):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError:
        pass
def run_python_script(run_path,save_path = None):
    try:
        result = subprocess.run(['python', run_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except:
        pass
    with open(save_path, 'w',encoding='utf-8') as f:
        f.write("=== 输出内容 ===\n")
        f.write(result.stdout)
        f.write("\n=== 报错信息 ===\n")
        f.write(result.stderr)
def run_python_code(code):
    try:
        exec(code)
        print("代码执行成功。")
    except Exception as e:
        print(f"代码执行出错: {e}")
def show_allprocesses(path,pid = None):
    processes = psutil.process_iter()
    if pid is None:
        with open(path + '\\' + 'processes.txt', "w", encoding='utf-8') as file:
            for process in processes:
                file.write(f"Process ID: {process.pid}\n")
                file.write(f"Process Name: {process.name()}\n")
                file.write(f"Process Status: {process.status()}\n")
                file.write(f"Process CPU Usage: {process.cpu_percent()}%\n")
                file.write(f"Process Memory Usage: {process.memory_info().rss / 1024 / 1024} MB\n")
                file.write("-" * 40 + "\n")
    else:
        with open(path + '\\' + 'processes.txt', "w", encoding='utf-8') as file:
            for process in processes:
                if pid in process.name():
                    file.write(f"Process ID: {process.pid}\n")
                    file.write(f"Process Name: {process.name()}\n")
                    file.write(f"Process Status: {process.status()}\n")
                    file.write(f"Process CPU Usage: {process.cpu_percent()}%\n")
                    file.write(f"Process Memory Usage: {process.memory_info().rss / 1024 / 1024} MB\n")
                    file.write("-" * 40 + "\n")
                else:
                    pass


def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        return (f"已关闭{pid}.")
    except psutil.NoSuchProcess:
        return (f"没有进程{pid}.")
    except psutil.AccessDenied:
        return (f"进程{pid}拒绝关闭.")
def switch_list_to_str(list_string):
    result = ''
    for string in list_string:
        result += '\n' + string
    return result

def readlast(path):
    lines = ''
    encodings = ['utf-8', 'gbk', 'utf-16']
    for encoding in encodings:
        try:
            with open(path, "r", encoding=encoding) as file:
                lines = file.readlines()
            break  # 如果成功读取文件，则退出循环
        except UnicodeDecodeError:
            pass
    return lines
#self.run_path + '\\' + filename
def writelast(path, message):
    encodings = ['utf-8', 'gbk', 'utf-16']
    for encoding in encodings:
        try:
            with open(path, "a", encoding=encoding) as file:
                file.write('\n回复:' + message + '\n:')
            break  # 如果成功读取文件，则退出循环
        except UnicodeDecodeError:
            continue
def create_readme(path):
    content = ('欢迎使用DropboxAssistant[v3] '
               '以个人信誉担保 本程序不涉及盗取信息'
               '有害系统的恶行行为 请放心使用' 
               '\n\n[说明]保证exe文件与Dropbox'
               'Assistant文件夹位于同一目录 点击exe'
               '即开始程序\n\n[运行python]将需要运行的'
               'python代码添加至run文件夹(文件名中需含'
               'test)即可自动运行 save文件中是默认的地址'
               '自动保存输出的结果 运行时将在save文件夹中'
               '显示XXX is running\n\n[系统功能] 可于'
               'run文件夹创建SystemPause SystemStart'
               ' SystemStop文件分别控制程序的暂停 重启 以及'
               '停止\n\n[系统操作]可与run文件夹创建[SystemFile]'
               '.txt文本框 于其中输入内容实现操作 以下为操作名称'
               '及其功能:\n获取地址 获取save文件夹的位置\n'
               '获取目录+地址 获取地址下所有文件信息\n查找文件'
               '+文件名,磁盘 于磁盘中查找文件\n全盘搜索+文件名 '
               '遍历磁盘查找文件\n运行文件 打开文件\n移动文件+'
               '文件地址 将文件移动至save文件夹\n改变刷新时间+t '
               '用于改变运行频率\n改变重启时间+t 用于改变暂停时检测'
               '的运行频率\n查看线程 查看目前正在运行的线程\n查看'
               '进程 查看目前正在运行的进程\n搜索进程+进程名 搜索指'
               '定的进程\n杀死进程+进程名 关闭进程\n关闭计算机 关闭'
               '电脑\n重启计算机 重启电脑\n以上操作中的'
               '\'+\'仅为表述方便无需打出\n\n[注意事项]\n如果启用'
               'DropboxAssistant[v3].exe的电脑内信息重要 '
               '为防止信息泄露 请不要共享DropboxAssistant或run'
               '文件夹 也不要设计脚本同步run和其他以共享的文件信息'
               '\n\n如有任何建议 可发送邮件至pinjun2000@gmail.com'
               '或直接与本人交流')
    encodings = ['utf-8', 'gbk', 'utf-16']
    for encoding in encodings:
        try:
            with open(path, "a", encoding=encoding) as file:
                file.write(content)
            break  # 如果成功读取文件，则退出循环
        except UnicodeDecodeError:
            continue

#if __name__ == '__main__':
    #save_pyscript('123.txt',lambda: print(3))
    #print(search_files('Dropbox.exe','C:\\'))
    #run_python_script()
    #print(readlast('123.txt'))
    #print(readlast('C:\\Users\\AMA\\Dropbox\\myself\\autoreply\\DropboxAssistant\\run\\[SystemFile].txt'))


