# -*- coding: utf-8 -*- 
'''
Created on 2013年11月23日

@author: tunghsu/vosp
'''
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.template import  Context
from django.template.loader import get_template
from django.db.models import Count
from dbase.models import Merchant_Unit, Website_Unit, Item_Unit, City, Merchant_Category, Item_Category, Avatar_Base
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
import os, mimetypes
from django.core.files.storage import default_storage

def homepage(request):
    line = {}
    matrix = []
    NUM =  1
    seq = Item_Unit.objects.order_by('id')
    #print seq
    title = '网站主页'
    for i in range(0,NUM):
        line['id'] = seq[i].id
        line['name'] = Item_Unit.objects.get(id = line['id']).name
        line['detail']  = Item_Unit.objects.get(id = line['id']).detail
        line['price'] = Item_Unit.objects.get(id = line['id']).price
        line['m_name'] = Merchant_Unit.objects.get(mid = Item_Unit.objects.get(id = line['id']).mid).name
        line['since'] = Item_Unit.objects.get(id = line['id']).since
        line['link'] = Item_Unit.objects.get(id = line['id']).link
        line['m_link'] = Merchant_Unit.objects.get(mid = Item_Unit.objects.get(id = line['id']).mid).link
        matrix.append(dict(line))
    return render_to_response('index.html', {'title': title, 'matrix':matrix})