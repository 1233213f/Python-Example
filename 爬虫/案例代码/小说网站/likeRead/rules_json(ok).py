import json

rules = {
    "xbiquge":{
        "title":'//div[@id="list"]//dd//text()',
        "urlList":'//div[@id="list"]//dd/a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"http://www.xbiquge.la/",
        "chapter":'//div[@id="content"]/text()',
        "code":"utf-8"
    },
    "dawen":{
        "title":'//ul[@id="listsss"]//a/text()',
        "urlList":'//li[@id="chapter"]//a/@href',
        "book_name":'//div[@class="top"]//h3//text()',
        "realm":"",
        "chapter":'//div[@class="art_con"]/dd[not(@data-id="999")]//text()',
        "code":"utf-8"
    },
    "biquge":{
        "title":'//div[@id="list"]//dd//text()',
        "urlList":'//div[@id="list"]//dd/a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"",
        "chapter":'//div[@id="content"]/text()',
        "code":"utf-8"
    },
    "ikuaiyan":{
        "title":'//div[@class="container border3-2 mt8 mb20"]//a//text()',
        "urlList":'//div[@class="container border3-2 mt8 mb20"]//a/@href',
        "book_name":'//div[@class="w100"]//h1/text()',
        "realm":"http://www.ikuaiyan.com",
        "chapter":'//div[@class="border3-2"]//p/text()',
        "code":"utf-8"
    },
    'booksky':{
        "title":'//div[@class="card mt20 fulldir"]//ul[@class="dirlist three clearfix"]//li/a/text()',
        "urlList":'//ul[@class="dirlist three clearfix"]//li/a/@href',
        "book_name":'//div[@class="header line"]//h1/text()',
        "realm":"http://www.booksky.cc",
        "chapter":'//div[@class="content"]//text()',
        "code":"utf-8"
    },
    '9biquge':{
        "title":'//div[@id="list"]//dd//a/text()',
        "urlList":'//div[@id="list"]//dd//a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"https://www.9biquge.com",
        "chapter":'//div[@id="content"]//text()',
        "code":"utf-8"
    },
    'jjwxc':{
        "title":'//tr[@itemprop="chapter"]//span[@itemprop="headline"]//a[not(@id)]/text()',
        "urlList":'//tr[@itemprop="chapter"]//span[@itemprop="headline"]//a[not(@id)]/@href',
        "book_name":'//h1//span[@itemprop="articleSection"]/text()',
        "realm":" ",
        "chapter":'//div[@class="noveltext"]/text()',
        "code":"utf-8"
    },
    'taiuu':{
        "title":'//div[@class="book_list"]//li//a/text()',
        "urlList":'//div[@class="book_list"]//li//a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"",
        "chapter":'//div[@id="htmlContent"]/text()',
        "code":"gbk"
    },
    'shouda8':{
        "title":'//div[@class="link_14"]//dd//a/text()',
        "urlList":'//div[@class="link_14"]//dd//a/@href',
        "book_name":'//div[@class="bookname"]//h1/text()',
        "realm":"https://www.shouda8.com",
        "chapter":'//div[@id="content"]//text()',
        "code":"utf-8"
    },
    '13800100':{
        "title":'//div[@class="bd"]/ul/li/a/text()',
        "urlList":'//div[@class="bd"]/ul/li/a/@href',
        "book_name":'//div[@class="cate-tit"]//h2/text()',
        "realm":"https://www.13800100.com/",
        "chapter":'//div[@class="page-content FXLNmHSE"]/div//text()',
        "code":"utf-8"
    },
    '31xs':{
        "title":'//div[@id="list"]//dd//text()',
        "urlList":'//div[@id="list"]//dd/a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"http://www.31xs.com/",
        "chapter":'//div[@id="content"]/text()',
        "code":"utf-8"
    },
    '52ggd':{
        "title":'//div[@class="inner"]//dd/a/text()',
        "urlList":'//div[@class="inner"]//dd/a/@href',
        "book_name":'//div[@class="btitle"]//h1/text()',
        "realm":"",
        "chapter":'//div[@id="BookText"]/text()',
        "code":"gbk"
    }
}
with open('rules.json', 'w', encoding='utf-8') as fp:
    json.dump(rules, fp, ensure_ascii=False) 