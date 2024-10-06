import time
import subprocess
import systemcontrol as sy
import os
import shutil
import tkinter as tk
from tkinter import messagebox
import threading
from datetime import datetime
def prompt():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo("DropboxAssistant[v3]",
                        '欢迎使用DropboxAssistant\n此程序已启动 请'
                        '不要重复点击exe文件')
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo("DropboxAssistant[v3]",
                        '此程序适合搭配dropbox使用\n可以自动执行本地python脚本以及一些简'
                        '单的终端操作\n操作细则可查看文件夹内readme.txt.')
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("DropboxAssistant[v3]", '目前已为您自动创建DropboxAssistant\n其中'
                                    '的run和save文件夹分别用于运行指令以及保存结果\n请保证此程序与DropboxAssistant'
                                    '位于同一目录')
class Assistant():
    def __init__(self):
        self.begin_path = os.getcwd()
        name, run, save = 'DropboxAssistant', 'run', 'save'
        self.assistant_path = sy.create_folder(self.begin_path, name)
        self.run_path = sy.create_folder(self.assistant_path, run)
        self.save_path = sy.create_folder(self.assistant_path, save)
        readme_path = self.assistant_path +'\\' + 'readme.txt'
        exist = os.path.exists(readme_path)
        if exist:
            pass
        else:
            sy.create_readme(readme_path)


        self.deal_text = True
        os.chdir(self.save_path)


        self.activate = True
        self.pause = False
        self.haschange_path = []
        self.haschange_time = []
        self.input_stream = []
        self.run_file = []

        self.PauseName = 'SystemPause'
        self.StopName = 'SystemStop'
        self.StartName = 'SystemStart'
        self.CheckTime = 1
        self.StartTime = 60


        if exist:
            pass
        else:
            prompt()



    def change_run_path(self,new_path):
        self.search_path = new_path
    def change_save_path(self,new_path):
        self.save_path = new_path
    def search_dir(self,path):
        sy.AllFile(path)

    def AllThread(self):
        Name = []
        for thread in threading.enumerate():
            Name.append(thread.name)
        return Name

    def run_pyscript(self,filename):
        print('run the script: ' + filename)
        textname = filename.replace('.py', '.txt')
        savepath = self.save_path + '\\' + textname
        runpath = self.run_path + '\\' + filename
        sy.create_file(savepath + ' is running')
        try:
            sy.run_python_script(runpath, savepath)
        except:
            print('wrong')
        try:
            os.remove(savepath + ' is running')
        except:
            pass
        print(filename + ' has been complete')

        # print(self.input_stream)
    def system_function(self,filename):
        filepath = self.run_path + '\\' + filename
        lines = sy.readlast(filepath)
        if len(lines)>0:
            ask = lines[-1]
            message = None
            if ask == ':':
                pass
            else:
                message = self.dealwith_text(ask)
            if message is not None:
                print(message)
                sy.writelast(filepath,message)
            else:
                pass
        else:
            pass
    def dealwith_text(self,ask):
        print('[SystemFile].txt is running')
        message = '已成成功执行'
        try:
            if ask == '获取地址':
                message = os.getcwd()
            elif '获取目录' in ask:
                path = ask.replace('获取目录', '')
                messagelist = sy.AllFile(path)
                message = sy.switch_list_to_str(messagelist)
            elif '查找文件' in ask:

                str = ask.replace('查找文件', '').split(',')
                try:
                    message = sy.search_files(str[0], str[1])
                except:
                    message = '系统错误'
                if message == None:
                    message = '未能成功找到文件'
                else:
                    pass
            elif '全盘搜索' in ask:
                name = ask.replace('全盘搜索', '')
                try:
                    message = sy.searchGolbal(name)
                except:
                    message = '系统错误'
                if message == None:
                    message = '未能成功找到文件'
                else:
                    pass
            elif '运行文件' in ask:
                path = ask.replace('运行文件', '')
                try:
                    subprocess.run(path)
                except:
                    message = '未能成功运行文件'
            elif '移动文件' in ask:
                path = ask.replace('移动文件', '')
                try:
                    shutil.move(path, self.save_path)
                except:
                    message = '未能成功移动文件'
            elif '查看线程' in ask:
                messagelist = self.AllThread()
                message = sy.switch_list_to_str(messagelist)
            elif ask == '查看进程':
                sy.show_allprocesses(self.save_path)
                message = '所有进程以保存至process.txt文件'
            elif '搜索进程' in ask:
                pid = ask.replace('搜索进程', '')
                sy.show_allprocesses(self.save_path,pid)
                message = '所有进程以保存至process.txt文件'
            elif '杀死进程' in ask:
                pid = int(ask.replace('杀死进程', ''))
                message = sy.kill_process(pid)
            elif '改变刷新时间' in ask:
                time = ask.replace('改变刷新时间', '')
                try:
                    self.CheckTime = int(time)
                except:
                    message = "请在文字后直接输入刷新时间，如'改变刷新时间t'(t为时间)"
            elif '改变重启时间' in ask:
                time = ask.replace('改变重启时间', '')
                try:
                    self.StartTime = int(time)
                except:
                    message = "请在文字后直接输入刷新时间，如'改变刷新时间t'(t为时间)"
            elif ask == '关闭计算机':
                os.system("shutdown /s /t 0")
            elif ask == '重启计算机':
                os.system('shutdown /r /t 0')
            else:
                message = ('未能回答此问题。目前只可实现\'获取地址\''
                           ',\'获取目录\',\'查找文件\',\'全盘搜索\''
                           ',\'运行文件\',\'移动文件\',\'改变刷新时间\''
                           '\'改变重启时间\',\'关闭计算机\'功能')
                pass
        except:
            message = '未知问题，请重新输入'
        print('running has completed')
        return message
    def clean_system_command(self, filename):
        if filename in [self.StopName, self.StartName, self.PauseName]:
            os.remove(self.run_path + '\\' + filename)
        else:
            pass
    def system_pause(self):
        self.pause = True
        print("system pause")
        sy.create_file(self.save_path + '\\' + self.PauseName)
    def system_start(self):
        self.pause = False
        print("system star")
        try:
            os.remove(self.save_path + '\\' + self.PauseName)
        except:
            pass
    def system_stop(self):
        self.activate = False
        self.pause = True
        print("system stop")
        sy.create_file(self.save_path + '\\' + self.StopName)
    def system_restart(self,filename):
        if filename == self.StartName:
            self.system_start()
        elif filename == self.StopName:
            self.system_stop()
        else:
            pass
    def dealwith(self,filename):
        tem = True
        #System Controller
        if filename == self.StopName:
            self.system_stop()
        elif filename == self.PauseName:
            self.system_pause()
        elif filename == self.StartName:
            self.system_start()
        #Some Functional Command
        elif '.py' in filename and 'test' in filename:
            task = lambda: self.run_pyscript(filename)
            thread = threading.Thread(target=task,name=filename)
            thread.start()

        elif self.deal_text and '[SystemFile]' in filename and '.txt' in filename:
            self.deal_text = False
            self.system_function(filename)
            self.deal_text = True




        else:
            tem = False
            pass

        #Collect Command
        if tem:
            self.input_stream.append(filename)
        else:
            pass



    def change(self,path):
        dir_stat = os.stat(path).st_mtime
        if path not in self.haschange_path:
            self.haschange_path.append(path)
            self.haschange_time.append(dir_stat)
            return True
        else:
            index = self.haschange_path.index(path)
            if self.haschange_time[index] == dir_stat:
                #print(time.ctime(dir_stat))
                #print(time.ctime(self.haschange_time[index]))
                return False
            else:
                self.haschange_time[index] = dir_stat
                return True
    def loop(self):
        while self.activate:
            while not self.pause:
                for filename in os.listdir(self.run_path):
                    filepath = os.path.join(self.run_path,filename)
                    if self.change(filepath):
                        self.dealwith(filename)
                        self.clean_system_command(filename)
                    else:
                        pass
                time.sleep(self.CheckTime)
            else:
                time.sleep(self.StartTime)
            for filename in os.listdir(self.run_path):
                self.system_restart(filename)








if __name__ == '__main__':
    #run_path = 'C:\\Users\\13299\Dropbox\\test\\run_path'
    #save_path = 'C:\\Users\\13299\Dropbox\\test\\save_path'


    #run_path = 'C:\\Users\\AMA\\Dropbox\\test\\run_path'
    #save_path = 'C:\\Users\\AMA\\Dropbox\\test\\save_path'
    ai = Assistant()
    ai.loop()







