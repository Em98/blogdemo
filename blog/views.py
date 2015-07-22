# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
logger = logging.getLogger('blog.views')


# Create your views here.

def index(request):
    # 广告查询
    ad_list = Ad.objects.all()
    # 分类查询
    category_list = Category.objects.all()
    # 文章查询
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 4)     # 2为分页数
    try:
        page = request.GET.get('page', 1)
        article_list = paginator.page(page)   # 返回当前页数据，保存在article_list中，page为第几个页面
        print type(article_list)
    except(InvalidPage, EmptyPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return render(request, 'index.html', locals())

def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }