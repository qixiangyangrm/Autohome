# Autohome
[Autohome](https://github.com/zhongjiajie/Autohome)基于[Scrapy](https://github.com/scrapy/scrapy)爬虫框架,实现对[汽车之家-文章](http://www.autohome.com.cn/all/)进行定向爬虫，并将抓取的数据存放进[MongoDB](https://github.com/mongodb/mongo)中。后期将对抓取数据进行简单的分析以及NLP的工作。

## 运行环境
* Python 2.7.10
* Scrapy 1.3.2
* MonogDB 3.2.10
* pymongo 3.4.0

## 项目构成


## 使用方式



## 设计概览

### 爬虫设计概览
* Autohome抓取的是[汽车之家-文章](http://www.autohome.com.cn/all/)页面，整个爬虫部分分成四大主题，分别是：文章简介、文章详情、文章评论、评论文章的用户。爬虫的根节点其中四个部分的逻辑如下：
![image](https://github.com/zhongjiajie/Autohome/raw/master/support_file/four_theme/autohome_four_theme.png)

* Autohome基于[Scrapy](https://github.com/scrapy/scrapy)爬虫框架，对四大主题进行抓取，整个流程图如下，其中绿色部分是Scrapy原生框架的逻辑，蓝色部分是[汽车之家-文章](http://www.autohome.com.cn/all/)的爬虫逻辑
![image](https://github.com/zhongjiajie/Autohome/raw/master/support_file/architecture/autohome_architecture.png)

## Features
* 全部基于Scrapy框架实现
* 定义两个Pipeline操作，分别是AutohomeJsonPipeline，即本地json文件；以及AutohomeMongodbPipeline，即存进MongoDB。可以在`setting.py`的`ITEM_PIPELINES`节点中设置启动的Pipeline
* 定义RotateUserAgentMiddleware实现随机的user agent操作，其中所有的User Agent的获取都是在[User Agent String.Com](http://www.useragentstring.com/)中获取的，项目默认是获取Chrome、ChromePlus、Firefox、Safari四个浏览器的UA
* 定义RotateProxyMiddleware实现随机代理操作，代理使用了

## TODO
* 优化模拟登陆的抓取速度及完整度
* 对抓取的结构化数据进行分析
* 对抓取的非结构化数据分析

## Change Log
* 20170531 将原来自定义模块的爬虫程序切换到Scrapy爬虫框架