import requests
import json


class QQmusic:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        self.sl = []
        self.musicList = []

    # 获取页面
    def getPage(self,url,headers):
        res = requests.get(url,headers = headers)
        res.encoding = 'utf-8'
        return res

    # 获取音乐songmid
    def getSongmid(self):
        num = int(input('请输入获取条数：'))
        # num = 20
        name = input('请输入歌名或歌手：')
        # name = '张学友'
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=%d&w=%s'%(num,name)
        # 搜索音乐
        res = self.getPage(url,headers=self.headers)
        html = res.text
        html = html[9:]
        html = html[:-1]
        # 获取songmid
        js = json.loads(html)
        songlist = js['data']['song']['list']
        for song in songlist:
            print(song)
            songmid = song['songmid']
            name = song['songname']
            self.sl.append((name,songmid))
            print('获取成功songmid')


    # 获取音乐资源，guid是登录后才能获取，nin也是
    def getVkey(self):
        guid = '0712fFoke-7qtZXC'  # input('请输入guid：')
        uin = '1152921504948244261'   # input('请输入uin：')
        for s in self.sl:
            print('开始获取资源')
            # 获取vkey,purl
            name = s[0]
            songmid = s[1]
            keyUrl = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req":{"param":{"guid":" %s"}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"%s","songmid":["%s"],"uin":"%s"}},"comm":{"uin":%s}}'%(guid,guid,songmid,uin,uin)
            res = self.getPage(keyUrl,headers=self.headers)
            html = res.text
            keyjs = json.loads(html)
            purl = keyjs['req_0']['data']['midurlinfo'][0]['purl']
            # 拼凑资源url
            url = 'http://dl.stream.qqmusic.qq.com/' + purl
            self.musicList.append((name,url))
            print('资源地址获取成功')

    #   下载音乐
    def downloadMusic(self):
        for m in self.musicList:
            url = m[1]
            res = self.getPage(url,headers=self.headers)
            music = res.content
            name = m[0] + '.mp3'
            with open(name, 'wb') as f:
                f.write(music)
                print('下载OK')

QQ = QQmusic()
QQ.getSongmid()
QQ.getVkey()
QQ.downloadMusic()