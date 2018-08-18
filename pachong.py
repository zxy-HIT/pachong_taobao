import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import time
import random
import json
import math

# 创建一个文件存储评论及其他数据
myfile = open("tm_fz_gn_1_1_1.txt","a")
# 共获取四个变量，评论者昵称，是否超级会员，评论时间，评论内容
print("评论者昵称","是否超级会员","评论时间","comment",sep='|',file=myfile)
stop = random.uniform(0.5,2)

# 获取页数
try:
    url0 = "https://rate.tmall.com/list_detail_rate.htm?itemId=529355863153&spuId=524522272&sellerId=92688455&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvfpvkvFWvUvCkvvvvvjiPPsFZtj3CRFzvgjljPmPOgj3bP2Fvtj1HPszOQjtU9phv2Hifj7kbzHi4cUSSzT6CvvDvp%2FHZw9CC0K0rvpvooZl17EZvpBIU4q01DdUgL2EL9phvHHiaBOmzjHi47Tr%2BtssScVa4%2BaGBdphvmZChnDL4vhhbtQwCvva47rMNMm76dphvhyDWWDkfvhhvVzkY%2BX4ARhQAZT6CvvDvpdWp69CCaLOtvpvhphvvvUhCvv14cUzMPa147DiF5n%2FrvpvEphbthvwvphkT3QhvChCCvvvtvpvhphvvv2yCvvBvpvvvvphvCyCCvvvvvvyCvh1vRjyvItDTmmxBlwyzhmx%2FwZ3lYb8rwZyaWXxreEIaUmx%2F1RoKHkx%2FwZ3lYb8rwZpaWXxrV8tYVC%2Bda4AAdcHUjLVDYCAfJhl%2BVd0DkphvCyEmmv9fj8yCvv3vpvoxESfW%2BqyCvm3vpvC9vvCvvZCvjPQvvhPGphvwv9vvBj1vpCsGvvChXhCvjPQvvhBy2QhvCvvvMM%2F5vpvhphvhHUhCvv14cEzMja147DifNr%2FCvpvZ7DsXMlzw7Di4OrF5jjlfhxusz69tvpvhphvvv86CvvDvpAwUIpCC4QmCvpvW7DMRzsFw7Dif3FbNdphvmZCH2pL9vhHSRghCvv14OwhpDa147DKZjnGtvpvhphvvv86CvvDvp0XZqQCChaVrvpvEphZvZWpvpLFz9phv2Hia%2FgvOzHi47MXFzghCvv147saIA3147DAnJa%2FCvpvZ7D0X9ENw7DiaGrP5PUCfAHiMz1h%3D&needFold=0&_ksTS=1534594196848_2879&callback=jsonp2880"
    req0 = urllib.request.Request(url0)
    req0.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    html0 = urllib.request.urlopen(req0,timeout=500).read()
    html0 = bytes.decode(html0,encoding="UTF-8")
    print(type(html0))
    #'''
    # 下面这一步是因为这个json不是标准的json，json是一个完完全全的字典，而这个json是在类似json1234()这个结构的括号中，打开看看这个json你就懂了，所以需要用正则表达式去获取真实的json（即字典）
    # '''
    js0 = re.search('{"rateDetail(.*)',html0).group()[:-1]
    # 将json主要内容存入content
    content0 = json.loads(js0)
    content = content0['rateDetail']
    # print(content.keys())
    # print(json.dumps(content0, sort_keys=True, indent=2))
    #尾页
    lastpage = int(content['paginator']['lastPage'])
except:
    print("获取尾页失败，默认爬取99页")
    lastpage = 99

# 构造循环遍历每一页
for i in range(1,lastpage):
    try:
        url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=529355863153&spuId=524522272&sellerId=92688455&order=3&currentPage='+str(i)+'&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvfpvkvFWvUvCkvvvvvjiPPsFZtj3CRFzvgjljPmPOgj3bP2Fvtj1HPszOQjtU9phv2Hifj7kbzHi4cUSSzT6CvvDvp%2FHZw9CC0K0rvpvooZl17EZvpBIU4q01DdUgL2EL9phvHHiaBOmzjHi47Tr%2BtssScVa4%2BaGBdphvmZChnDL4vhhbtQwCvva47rMNMm76dphvhyDWWDkfvhhvVzkY%2BX4ARhQAZT6CvvDvpdWp69CCaLOtvpvhphvvvUhCvv14cUzMPa147DiF5n%2FrvpvEphbthvwvphkT3QhvChCCvvvtvpvhphvvv2yCvvBvpvvvvphvCyCCvvvvvvyCvh1vRjyvItDTmmxBlwyzhmx%2FwZ3lYb8rwZyaWXxreEIaUmx%2F1RoKHkx%2FwZ3lYb8rwZpaWXxrV8tYVC%2Bda4AAdcHUjLVDYCAfJhl%2BVd0DkphvCyEmmv9fj8yCvv3vpvoxESfW%2BqyCvm3vpvC9vvCvvZCvjPQvvhPGphvwv9vvBj1vpCsGvvChXhCvjPQvvhBy2QhvCvvvMM%2F5vpvhphvhHUhCvv14cEzMja147DifNr%2FCvpvZ7DsXMlzw7Di4OrF5jjlfhxusz69tvpvhphvvv86CvvDvpAwUIpCC4QmCvpvW7DMRzsFw7Dif3FbNdphvmZCH2pL9vhHSRghCvv14OwhpDa147DKZjnGtvpvhphvvv86CvvDvp0XZqQCChaVrvpvEphZvZWpvpLFz9phv2Hia%2FgvOzHi47MXFzghCvv147saIA3147DAnJa%2FCvpvZ7D0X9ENw7DiaGrP5PUCfAHiMz1h%3D&needFold=0&_ksTS=1534594196848_2879&callback=jsonp2880'
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
        html = urllib.request.urlopen(req,timeout=500).read()
        html = bytes.decode(html,encoding="UTF-8")
        js = re.search('{"rateDetail(.*)', html).group()[:-1]
        infos0 = json.loads(js)
        infos = infos0['rateDetail']['rateList']
        tiaoshu = 0
        for info in infos:
            try:
                tiaoshu += 1
                time.sleep(stop)
                ss = "正在爬取第%d页的第%d条评论,共%d页" % (i,tiaoshu,lastpage)
                print(ss)
                # 用户姓名
                try:
                    user_name = info['displayUserNick'].strip().replace('\n','')
                except:
                    user_name = ""
                # 是否黄金会员
                try:
                    user_status = info['goldUser'].strip().replace('\n','')
                except:
                    user_status = ""
                # 评论时间
                try:
                    comment_date = info['rateDate'].strip().replace("\n","")
                except:
                    comment_date = ""
                # 评论内容
                try:
                    comment = info['rateContent'].strip().replace("\n","").replace('\t','')
                except:
                    comment = ""
                print(user_name,user_status,comment_date,comment,sep='|',file=myfile)
            except:
                sss = '爬取第%d页的第%d条评论失败,跳过爬取' % (i,tiaoshu)
                print(sss)
                pass
    except:
        print("该产品url获取失败，请检查")
myfile.close()