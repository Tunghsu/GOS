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

