#coding=utf-8
from qiniu import Auth,put_file,etag
import qiniu.config
import requests 
import base64
import json
from PIL import Image
import os
#上传
def upload(bucket,path,filename,key,url):
    try:
        token = key.upload_token(bucket, filename, 3600)
        print('正在上传..')
        reform,inform = put_file(token, filename, path)
        if reform != None:
            print '已经成功地将{}->>{}'.format(filename,bucket)
            print "正在处理您的图片..."
            url=url + '/' + filename
            path=path.split('/')[-1]

    except Exception,e:
        print '上传失败，错误信息：',e

#调用API
def apiget(urlbucket,url):
    try:
        url=urlbucket + '/001.jpg' + '?face-analyze/verification/url/' + url
        #标准对比的图片地址，名称为001.jpg
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception,e:
        print e
        print("网络发生故障，请重试..")

#base64 Encode
def base64encode(url):
    try:
        print "正在加密链接.."
        enurl=base64.urlsafe_b64encode(bytes(url, "utf-8"))
        print "加密完成"
        enurl=str(enurl)
        enurl=enurl.split("'")[1]
        return enurl
    except:
        print "这里出现了一个问题，请重试.."

#PIL 图片压缩
def pilresize(per,path):
    im=Image.open(path)
    imsize=im.size
    sizex=int(imsize[0]*per)
    sizey=int(imsize[1]*per)
    im=im.resize((sizex,sizey))
    im.save('trans.jpg','JPEG')
    print '图片压缩完成，输出成功' 
    print '{}->>({},{})'.format(imsize,sizex,sizey)

def pilwork(path):
    try:
        size=os.path.getsize(path)
        size = float(size)
        kb=size/1024
        per=10/kb
        pilresize(per,path)
    except:
        print "请检查您的地址是否输入错误" 


#JSON分析
def jsonanal(jtext):
    print("正在分析,请稍后..")
    rj=json.loads(jtext)
    stat=rj['status']
    confi=rj['confidence']
    return stat + ',' +str(confi)

#主体
def main():
    #填写你的 AK 和 SK
    accesskey = input('请输入您在七牛云的AccessKey：')
    secretkey = input('请输入您在七牛云的SecretKey：')

    #鉴定身份
    keyq=Auth(accesskey,secretkey)

    #所要操作的空间
    bucketname =input("请输入要操作的空间(公开)名字：")

    #所要操作空间的外链地址
    urlbucket = input("请输入空间所绑定的域名或者默认外链地址：")

    #判定操作类型
    while 1:
        order=input('请输入你需要进行的操作：')
        mode=order.split(' ')[0]
        if mode == '识别':
            path=order.split(' ')[1]
            fname=path.split('/')[-1:][0]
            unrl=urlbucket+'/trans.jpg'
            print('正在压缩图片.请稍后..')
            #调用函数
            pilwork(path)  #压缩图片
            print("正在上传token,请稍后..")
            upload(bucketname,'./trans.jpg','trans.jpg',keyq,urlbucket) #上传文件
            enurl=base64encode(unrl)   #base64加密
            jtext=apiget(urlbucket,enurl) #调用七牛api并得到返回的json数据
            result=jsonanal(jtext)  #分析返回的json，得到最终相似度
            if result.split(',')[0] == 'invalid':
                print('识别发生了错误')
            else:
                if eval(result.split(',')[1]) >= 0.7:
                    print("识别成功，鉴定为本人，相似度为{:.1f}".format(eval(result.split(',')[1])*100))
                else:
                    print("识别成功，鉴定不是本人，相似度过低")
        if mode == '退出':
            print("欢迎您的使用..")
            break

#终端提示显示
print("+----------------------------------------+")
print("|        欢迎使用七牛的人脸识别功能      |")
print("+----------------------------------------+")
print("|本程序须知：                            |")
print("|1.本程序测试图片为杨幂的人像,见face.jpg |")
print("|2.您需要提供服务的Accesskey，Secretkey  |")
print("|3.您需要提供 bucket名字和bucket外链地址 |")
print("+----------------------------------------+")
print("|使用方法:                               |")
print("|1.识别输入格式： 识别 图片位置(包括后缀)|")
print("|2.退出输入格式： 退出                   |")
print("+----------------------------------------+")
main()

作者：七牛云
链接：https://juejin.im/post/59719caef265da6c4741cdd7
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。