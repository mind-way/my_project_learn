# 网易云音乐歌曲下载
# python 3.6.5
# author 郭
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import time
import sys
while True:
    # 一、构造URL
    name = input('请输入歌手或者歌曲名：')   #如果name作为参数传递到url,则需要下述语句
    url = 'https://music.163.com/'
    # url_name = parse.quote(name,encoding='utf-8')    # import urllib.parse as parse

    # 二、打开浏览器获取网页信息
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)     # driver.refresh()  # 可刷新网页

    # 三、搜索
    driver.find_element_by_id('srch').clear()
    driver.find_element_by_id('srch').send_keys(name)
    driver.find_element_by_id('srch').send_keys(Keys.ENTER)
    print('搜索成功')
    time.sleep(4)
    iframe = driver.find_element_by_id('g_iframe')
    driver.switch_to.frame(iframe)

    # 四、获取完整网页,通过BeautifulSoup解析网页
    source = driver.page_source
    print('获取网页成功')

    # 五、解析网页并关闭浏览器
    html = bs4.BeautifulSoup(source,'html.parser')
    print('解析网页成功')
    driver.close()

    # 六、获取歌曲id
    N = 1
    song_list = []
    name_list = []
    try:
        song_all = html.find('div',class_='srchsongst').find_all('div',class_='item f-cb h-flag')
        for song in song_all:
            song_id = song.find('a')['data-res-id']
            song_list.append(song_id)
            song_name = song.find('div',class_='td w0').find('b')['title']
            name_list.append(song_name)
            singer = song.find('div',class_='td w1').find('a').text
            album = song.find('div', class_='td w2').find('a').text
            times = song.find_all('div', class_='td')[-1].text
            print('%s、歌曲名:%s    歌手:%s    专辑:%s    歌曲时长:%s'%(N,song_name,singer,album,times))
            N += 1
        print('id清单：%s'%song_list)
        print('获取歌曲清单成功')
    except Exception as e:
        print(e)
        print('获取歌曲基本信息失败！')
    time.sleep(0.5)

    # 七、请求具体的歌曲
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
    while True:
        try:
            song_num = int(input('你想下哪一首歌,任意键结束本次下载，下载请输入数字序号：'))
            id = song_list[song_num-1]
            url = 'http://music.163.com/song/media/outer/url?id='+id+'.mp3'
            # 另一种获取真实下载链接的方法: 进入歌曲链接：url = 'https://music.163.com/#/song?id='+id ,m4a格式，
            # 在该请求页 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=' 可以找到真实链接
            # 真实链接位置：['data'][0]['url']，post请求，涉及加密，破解有难度。
            # 请求歌曲网页，查看响应状态，如果在200-300之间下载歌曲，否则反馈失败信息和响应代码
            res = requests.get(url,headers=headers)
            if 200<= res.status_code <=300:
                print(res.status_code)
                music = res.content
                with open(r'E:\KuGou\%s.mp3'%name_list[song_num-1],'wb') as f:
                    f.write(music)
                    print('下载成功')
            else:
                print('请求失败,响应状态为：%s'%res.status_code)
            time.sleep(0.5)
        except Exception as e:
            print(e)
            print('本次下载未成功！')
            time.sleep(0.5)
        # 确认是否要继续下载
        end = input('是否继续下载，任意键结束，继续请按y:')
        if end != 'y':
            break
        else:
            pass
    time.sleep(0.5)
    # 确认是否要重新搜索
    reserch = input('是否继续搜索新的歌曲，任意键结束，继续请按y:')
    if reserch == 'y':
        continue
    else:
        print('退出程序,输入ctrl+C可以关闭窗口！')
        sys.exit(0)