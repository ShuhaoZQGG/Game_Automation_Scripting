import pyautogui
import time 
print(pyautogui.size())
print(pyautogui.position())

'''
This is a game scripting for 一梦江湖野花采集
Suitable for resolution (width = 3240, height = 2160)
Make sure to maximize the Program and close the "搜索" and all the tabs in "搜索“ in the 地图
Don't stay around the 采集点 before running the program
'''

#open 地图
pyautogui.click(3019,157)
time.sleep(1)
#open 世界
pyautogui.click(3096,1924)
time.sleep(1)
#click 江南
pyautogui.click(2698,774)
time.sleep(1)
#click 搜索
pyautogui.click(79,905)
time.sleep(1)

#click 采草
pyautogui.click(704,1086)
time.sleep(1)

#click 野花
pyautogui.click(822,1483)
time.sleep(1)

#go to the position
pyautogui.click(2266,757)
time.sleep(10)


timeout = time.time() + 60*10
while time.time() < timeout:
    #click "采集"
    #measure time elaps ~= 6s
    pyautogui.click(2413,1473)
    time.sleep(7)
    
    #选择工具
    #采集 time elapse ~=6s
    #野花刷新 time ~= 17 s
    pyautogui.click(2077,1255)
    time.sleep(4)

    #学习配方
    pyautogui.click(2552,1094)
    time.sleep(3)

    #确定学习
    pyautogui.click(2099,1367)
    time.sleep(3)

# 444 个野花 2021/7/28 1:23
# run 10 mins
# 556 个野花
# 10分钟内采集112个野花



    





