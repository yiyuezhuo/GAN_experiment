# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 00:26:30 2017

@author: yiyuezhuo
"""

import urllib
import urllib.request
import urllib.parse
import urllib.error

import time
import socket
import json
import os

__start_amount = 0
time_sleep = 0.1

def url_to_name(url):
    '''url如何编码为path的尾名称，这个不要单独存文件，否则非常麻烦。默认方法是把/替换成..'''
    return url.replace('/','..').replace(':',';')

def get_json(keyword, pn):
    
    search = urllib.parse.quote(keyword)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
            pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
    try:
        time.sleep(time_sleep)
        req = urllib.request.Request(url=url, headers=headers)
        page = urllib.request.urlopen(req)
        data = page.read().decode('utf8')
    except UnicodeDecodeError as e:
        print('-----UnicodeDecodeErrorurl:', url)
    except urllib.error.URLError as e:
        print("-----urlErrorurl:", url)
    except socket.timeout as e:
        print("-----socket timout:", url)
    else:
        return json.loads(data)
    finally:
        page.close()
    return
    

def get_image_by_url(url, root, verbose = True):
    name = url_to_name(url)
    path = os.path.join(root, name)
    if os.path.exists(path):
        if verbose:
            print('skip {}'.format(url))
        return
    try:
        urllib.request.urlretrieve(url, path)
    except:
        print('error {}'.format(url))
    else:
        if verbose:
            print('download {}'.format(url))
    
            
def get_image_by_keyword(keyword, start_pn = 0, end_pn = None, root = None):
    
    root = keyword if root is None else root
    
    if not os.path.exists(root):
        os.mkdir(root)
    
    pn = start_pn
    
    while (end_pn is None) or pn < end_pn:
        dic = get_json(keyword, pn)
        for img in dic['imgs']:
            time.sleep(time_sleep)
            url = img['objURL']
            get_image_by_url(url, root)
        pn += 60
    
    
