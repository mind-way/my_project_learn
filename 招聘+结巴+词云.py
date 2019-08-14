import openpyxl
from openpyxl import load_workbook
import jieba
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 一、读取文件
# 1.1 读取excel文件
wb = load_workbook(r'E:\练习文件\项目文件\安居客所有新楼盘信息.xlsx')
wb.guess_types = True   # 猜测格式类型
sheet2 = wb.get_sheet_by_name('安居客新楼盘信息')

# 1.2 文件需要处理部分存储为txt文档，也可以直接赋值给变量，此处这么写的目的是避免大文件直接赋值到变量（可调整读取量）
with open(r'E:\练习文件\项目文件\安居客成都所有新楼盘词频信息.txt','w',encoding='utf-8') as f:
    # 读取第三列
    for column in sheet2['D']:
        # print(column.value)
        f.writelines(str(column.value)+'\n')

# 1.3 从txt中提取文本信息
with open(r'E:\练习文件\项目文件\安居客成都所有新楼盘词频信息.txt','r',encoding='utf-8') as f2:
    content = f2.read()
# print(content)
# 二、结巴分词部分
# 2.1 自定义词典
jieba.load_userdict(r'E:\练习文件\项目文件\anjudict.txt')

# 2.2 设置停用词
jieba.analyse.set_stop_words(r'E:\练习文件\项目文件\anju-stop.txt')

# 2.3 精确模式
# jb_cut = jieba.cut(content,cut_all=False)
# print('/'.join(jb_cut))

# 2.4 提取关键词并保存
with open(r'E:\练习文件\项目文件\安居客成都所有新楼盘词频信息.txt','w',encoding='utf-8') as f3:
    tags = jieba.analyse.extract_tags(content,topK=100,withWeight=True)
    keywords = {}
    for v,n in tags:
        keywords[v] = n
        print('%s:%s'%(v,n))
        f3.writelines('%s:%s'%(v,n)+'\n')

# 三、提供背景图,通过numpy处理
path_img = r'E:\练习文件\图片\词云用图\cd1.jpg'
bg_img = np.array(Image.open(path_img))

# 四、词云部分
wordcloud = WordCloud(
    # 设置字体路径            # msyh.ttc(微软雅黑)/msyhl.ttc(微软雅黑-细)/msyhbd.ttc(微软雅黑-细)/simhei.ttf(黑体)
    font_path=r'C:\Windows\Fonts\simhei.ttf',   # simsun.ttc(宋体)/stxihei.ttf(华文细黑)/SIMLI.ttf(隶书)/stcaiyun.ttf(华文彩云)
    # 设置背景色，高宽
    background_color='white',mask=bg_img,max_font_size=130,min_font_size=4).generate_from_frequencies(keywords)
# 加载背景图片，执行
image_colors = ImageColorGenerator(bg_img)
plt.imshow(wordcloud.recolor(color_func=image_colors),interpolation='bilinear')
plt.axis('off')
plt.show()