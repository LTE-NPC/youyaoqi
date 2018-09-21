# -*- coding: utf-8 -*-
import json

import scrapy

from youyaoqi.agent_helper import get_random_agent
from youyaoqi.items import YouyaoqiItem


class ComicSpider(scrapy.Spider):
    name = 'comic'
    allowed_domains = ['www.u17.com']
    start_urls = ['http://www.u17.com/comic_list/th99_gr99_ca99_ss99_ob0_ac0_as0_wm0_co99_ct99_p1.html?order=2']

    def start_requests(self):
        data = {
                'data[group_id]': 'no',
                'data[theme_id]': 'no',
                'data[is_vip]': 'no',
                'data[accredit]': 'no',
                'data[color]': 'no',
                'data[comic_type]': 'no',
                'data[series_status]': 'no',
                'data[order]': '2',
                # 'data[page_num]': 1,
                'data[read_mode]': 'no'
        }

        base_url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
        agent = get_random_agent()
        print(agent)

        headers = {
            'Referer': base_url,
            'User-Agent': agent,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.u17.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
        }

        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            print('*' * 30)
            print(page)

            data['data[page_num]'] = str(page)

            yield scrapy.FormRequest(url=base_url, headers=headers, method='POST', formdata=data, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        # print(result)
        for data in result.get('comic_list'):
            item = YouyaoqiItem()
            item['title'] = data.get('name')
            item['cover'] = data.get('cover')
            yield item