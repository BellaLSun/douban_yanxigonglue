import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import json
#  pip install pyplotz
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Droid Sans Fallback']
import matplotlib.pyplot as plt


# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
# plt.rcParams['font.family']=['STFangsong']
# https://github.com/isuhao/jieba


def ciyun(filepath):
    comment = []
    with open(filepath, 'r') as f:
        rows = f.readlines()
        for row in rows:
            comment.append(row.split(','))

    comment2 = json.dumps(comment, ensure_ascii=False)  # 转码显示中文
    print("comment2", comment2)
    comment_after_split = jieba.cut(str(comment2), cut_all=False)

    # 查看分词效果
    wl_space_split = " ".join(comment_after_split)
    print("wl_space_split", wl_space_split)
    # 以上都运行无误

    # 导入背景图
    backgroud_Image = plt.imread('1.jpg')  # 读取图片数据
    stopwords = STOPWORDS.copy()
    # 可以加多个屏蔽词
    stopwords.add("剧情")
    stopwords.add("一部")
    stopwords.add("一个")
    stopwords.add("没有")
    stopwords.add("什么")
    stopwords.add("有点")
    stopwords.add("这部")
    stopwords.add("这个")
    stopwords.add("不是")
    stopwords.add("真的")
    stopwords.add("感觉")
    stopwords.add("觉得")
    stopwords.add("还是")
    # stopwords.add("女主")
    # stopwords.add("皇后")
    # stopwords.add("贵妃")
    # stopwords.add("于妈")
    stopwords.add("就是")
    stopwords.add("可以")

    # 设置词云参数
    # 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状

    wc = WordCloud(
        background_color='white',
        mask=backgroud_Image,
        font_path='DroidSansFallback.ttf',
        stopwords=stopwords,
        max_font_size=400,
        random_state=50)
    wc.generate_from_text(wl_space_split)
    img_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=img_colors)

    # 保存结果到本地

    wc.to_file('yanxi_wordcloud.jpg')


print("《延禧宫略》：")
ciyun('yanxi5.txt')

