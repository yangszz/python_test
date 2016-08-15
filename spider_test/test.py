# -*- coding:utf-8 -*-

import re



page = u'''
<ul class="s_tjcp"><li class="s_cxtjcp_li">
<a href="/CaiPu/2c91f538d058dbeb.htm" title="水煮肉片的做法详细步骤">水煮肉片</a>&nbsp;猪里脊肉(或者牛柳),蒜苗,芹菜,自己</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/29f1b9dd703049eb.htm" title="酸菜炖排骨的做法详细步骤">酸菜炖排骨</a>&nbsp;排骨,酸菜(我用的是酸菜鱼酸菜)</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/e9a63692a82538d1.htm" title="牛腩炖萝卜的做法详细步骤">牛腩炖萝卜</a>&nbsp;牛腩(腰窝)300克,白萝卜400克</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/b16db60f3f60a515.htm" title="地三鲜的做法详细步骤">地三鲜</a>&nbsp;土豆1个,茄子2个,青椒1个</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/56791cce7e99389e.htm" title="豆角炖肉的做法详细步骤">豆角炖肉</a>&nbsp;猪后肘肉,土豆,豆角</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/18d3e062f16694af.htm" title="青椒炒肉丝的做法详细步骤">青椒炒肉丝</a>&nbsp;猪肉(鸡,鸭,鹅肉均可)四两切细丝后</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/e63e4d35b9e8b062.htm" title="牛肉火锅的做法详细步骤">牛肉火锅</a>&nbsp;面条(标准粉)500克,牛肉(瘦)80</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/f80af132edd95802.htm" title="铁板鱿鱼的做法详细步骤">铁板鱿鱼</a>&nbsp;鱿鱼(鲜)400克</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/ec47c54763d33c05.htm" title="粉蒸排骨的做法详细步骤">粉蒸排骨</a>&nbsp;料酒,花椒,生抽,豆瓣(最好用郫县豆瓣</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/1f960be551a1fd21.htm" title="茄子炒肉的做法详细步骤">茄子炒肉</a>&nbsp;里脊肉,茄子</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/6eea7a60325775dd.htm" title="蒸鸡蛋的做法详细步骤">蒸鸡蛋</a>&nbsp;鸡蛋300克</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/31193bab05d4fdfd.htm" title="荷包蛋的做法详细步骤">荷包蛋</a>&nbsp;鸡蛋1个或数个,酱油,糖适量。</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/156ee9d37d4e2964.htm" title="酱牛肉的做法详细步骤">酱牛肉</a>&nbsp;牛腱子肉1块(约1000g),黄酱100</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/6adbdfe3960baf34.htm" title="红烧羊肉的做法详细步骤">红烧羊肉</a>&nbsp;崇明羊，暂块2，3斤,土豆，切滚刀块2</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/02d590865f571b47.htm" title="绿豆莲藕章鱼清汤的做法详细步骤">绿豆莲藕章鱼清汤</a>&nbsp;绿豆100克,章鱼干2只,莲藕</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/e85bf48bdbe50383.htm" title="剁椒皮蛋烧土豆的做法详细步骤">剁椒皮蛋烧土豆</a>&nbsp;土豆,剁椒,皮蛋</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/e20d7ab25e330058.htm" title="快手微波菜--鸡丁萝卜干的做法详细步骤">快手微波菜--鸡丁萝卜干</a>&nbsp;萝卜干一份,鸡腿一只</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/7f182c6c66559a8b.htm" title="百里香咸蛋烤蟹的做法详细步骤">百里香咸蛋烤蟹</a>&nbsp;花蟹,咸蛋</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/43f15dedcf66d694.htm" title="拌鱿鱼花的做法详细步骤">拌鱿鱼花</a>&nbsp;鱿鱼(鲜)400克</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/8836b4e49cca23bd.htm" title="麻酱扁豆的做法详细步骤">麻酱扁豆</a>&nbsp;扁豆400克,麻酱50克,蒜泥15克</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/7d9d714ec2b4ef34.htm" title="素炒苦瓜的做法详细步骤">素炒苦瓜</a>&nbsp;苦瓜,辣椒末,榨菜末,精盐,味精,酒</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/9baa801c1961619f.htm" title="埃及式煮蚕豆的做法详细步骤">埃及式煮蚕豆</a>&nbsp;蚕豆1000克。</li>
<li class="s_cxtjcp_li">
<a href="/CaiPu/848b7175b639b97e.htm" title="汆紫蟹菜心汤的做法详细步骤">汆紫蟹菜心汤</a>&nbsp;螃蟹500克,白菜500克</li></ul></div></div><div class="clears"></div></div>
<div id="footer">
<a href="/About/AboutUs.htm">关于我们</a> - <a href="/About/mzsm.htm">免责声明</a> - <a href="/About/TouGao.htm">我要投稿</a> - <a href="/About/Contact.htm">联系我们</a> - <a href="/About/Feedback.asp">访客留言</a> - <a href="/About/SiteMap.htm">网站地图</a><br />
<a href="http://www.ttmeishi.com">天天美食 www.<strong>TTMeiShi</strong>.com</a> 版权所有 未经授权禁止复制或建立镜像 美食QQ群: 1286717 7835027 7834989 64605712 <br />
<strong>本站提供菜谱大全、美食制作指南、美食视频、美食博客、特色小吃、生活百科信息服务</strong>，别忘了告诉您的朋友哟 ^_^
</div><div class="clears" style="display:none;">
<script type="text/javascript" src="http://s2.ttmeishi.com/js/count.js"></script>

'''



items = re.findall( r'/CaiPu/.*\.htm', page)
for item in items:
    print item
