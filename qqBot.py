from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio
import requests
import json
import pprint
import random
import time
import os
import re
import pickle
import asyncio
import random
import json
import pprint
from hashlib import md5
from graia.application.message.elements.internal import Image
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication
from graia.application.message.elements.internal import At, Plain
from graia.application.session import Session
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, OptionalParam, RequireParam
from graia.application.friend import Friend

def coin():
    txt = ''
    r = requests.get('https://coinmarketcap.com/zh/currencies/shiba-inu/markets/')
    w = re.findall(r'''(?<="priceValue___11gHJ">¥).*?(?=</div><span)''',r.text)
    ppp = 11735667*float(w[0])
    txt += 'shib当前价格为:￥'+w[0]+'\n\n我所持有总价为:￥'+str(ppp)
    r = requests.get('https://coinmarketcap.com/zh/currencies/bitcoin/markets/')
    w = re.findall(r'''(?<="priceValue___11gHJ">¥).*?(?=</div><span)''',r.text)
    txt += '\n\n比特币现价为:￥'+w[0]
    r = requests.get('https://coinmarketcap.com/zh/currencies/ethereum/markets/')
    w = re.findall(r'''(?<="priceValue___11gHJ">¥).*?(?=</div><span)''',r.text)
    txt += '\n\n以太坊现价为:￥'+w[0]
    r = requests.get('https://coinmarketcap.com/zh/currencies/dogecoin/markets/')
    w = re.findall(r'''(?<="priceValue___11gHJ">¥).*?(?=</div><span)''',r.text)
    txt += '\n\nDOGE币现价为:￥'+w[0]
    return txt

def coins(mm):
    txt = ''
    r = requests.get('https://coinmarketcap.com/zh/currencies/'+mm+'/markets/')
    w = re.findall(r'''(?<="priceValue___11gHJ">¥).*?(?=</div><span)''',r.text)
    txt += mm+'现价为:￥'+w[0]
    w = re.sub(',','',w[0])
    tmm = float(w)
    r = requests.get('http://www.zhijinwang.com/huilv/')
    w = re.findall(r'''(?<=<td height="32">).*?(?=</td>)''',r.text,re.DOTALL)
    w = re.findall(r'''[0-9]\.[0-9]*''',w[0])
    txt += '\n\n'+mm+'现价为:$'+str(tmm/float(w[0]))
    return txt

def hl(mm):
    txt=''
    r = requests.get('http://www.zhijinwang.com/huilv/?from='+mm+'&to=CNY&num=100')
    w = re.findall(r'''(?<=<td height="32">).*?(?=</td>)''',r.text,re.DOTALL)
    w = re.findall(r'''[0-9]\.[0-9]*''',w[0])
    txt += mm+'对人民币的汇率为:￥'+w[0]
    return txt

def r6():
    r = requests.get('https://store.steampowered.com/app/359550/Tom_Clancys_Rainbow_Six_Siege/')
    w = re.findall(r'''¥ [0-9]{2}(?=[^0-9])''',r.text,re.DOTALL)
    rr = requests.get('https://store.steampowered.com/app/1238840/Battlefield_1/')
    ww = re.findall(r'''¥ [0-9]{2,3}(?=\s{5,})''',rr.text,re.DOTALL)
    ww = re.findall(r'''(?<=¥ ).*''',ww[0])
    rrr = requests.get('https://store.steampowered.com/app/1238810/_5/')
    www = re.findall(r'''¥ [0-9]{2,3}(?=\s{5,})''',rrr.text,re.DOTALL)
    return '彩六豪华版现价:'+w[0]+'\n\n战地一现价:￥'+ww[0]+'\n\n战地五现价:￥'+www[0]

def kk():
    with open("jwc.txt","r+",encoding='utf-8') as f:
        ptett = int(f.read(4))
    txt = ''
    fl=0
    for page in range(0,10):
        r = requests.get(f'http://jwc.cqu.edu.cn/announcement?page={page}')
        tt = re.findall(r'''(?<=<a href="/node/[0-9]{4}">).*?(?=</a>)''',r.text)
        ls = re.findall(r'''/node/[0-9]{4}''',r.text)
        ti = re.findall(r'''(?<=<span class="field-content views-updated-date">).*?(?=</span>)''',r.text)
        for m in range(len(ls)):
            tet=int(re.sub('/node/','',ls[m]))
            if not fl:
                tett=tet
                fl=1
            if tet<=ptett:
                fo = open("jwc.txt","w",encoding='utf-8')
                fo.write(str(tett)+'\n')
                fo.write(txt)
                fo.close()
                if len(txt)<5:return '无最新消息'
                else:return txt
            else:
                txt+=tt[m]+'\n'
                txt+='http://jwc.cqu.edu.cn'+ls[m]+'\n'*2

def kkb(n):
    txt = ''
    r = requests.get(f'http://jwc.cqu.edu.cn/announcement')
    tt = re.findall(r'''(?<=<a href="/node/[0-9]{4}">).*?(?=</a>)''',r.text)
    ls = re.findall(r'''/node/[0-9]{4}''',r.text)
    for ww in range(n):
        txt+=tt[ww]+'\n'
        txt+='http://jwc.cqu.edu.cn'+ls[ww]+'\n'*2
    return txt

def xm():
    r = requests.get('https://stock.finance.sina.com.cn/hkstock/quotes/01810.html')
    w = re.findall(r'''(?<=小米集团-W</a></td><td><span class=).*?(?=</span>)''',r.text,re.DOTALL)
    w = re.findall(r'''[0-9]{2}\.[0-9]*''',w[0])
    return w[0]

def wjf(s):
    s = s.split()
    fo = open('qqk.py','w')
    txt = 'def jf(x):return '+s[0]
    fo.write(txt)
    fo.close()
    fo=open('tem.txt','w')
    fo.write(s[1]+' '+s[2])
    fo.close()
    os.system('python fn.py')
    time.sleep(0.2)
    with open('ans.txt','r') as fo:
        txt = fo.read()
    return txt

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def bdfy(fy,cs):
    appid = '***'
    appkey = '***'
    from_lang = 'auto'
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + fy + str(salt) + appkey)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': fy, 'from': from_lang, 'to': cs, 'salt': salt, 'sign': sign}
    r = requests.post(url, params=payload, headers=headers)
    rr = r.json()
    return rr['trans_result'][0]['dst']

loop = asyncio.get_event_loop()
bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080",
        authKey="***",
        account=***,
        websocket=True
    )
)

@bcc.receiver("FriendMessage")
async def deff(
    message: MessageChain,
    app: GraiaMiraiApplication,
    friend: Friend,
):
    fll=0
    for mme in range(1,10):
        if message.asDisplay().startswith('xx'+str(mme)):
            await app.sendFriendMessage(friend, MessageChain.create([Plain(kkb(mme))]))
            fll=1
    if message.asDisplay().startswith("消息"):
        await app.sendFriendMessage(friend, MessageChain.create([Plain(kk())]))
        fll=1
    if message.asDisplay().startswith("help"):
        await app.sendFriendMessage(friend, MessageChain.create([Plain('coin 快速查询币圈情况\n\nhl加空格加货币缩写（如hl USD）查询实时汇率\n\nbi加空格加虚拟货币全称（如bi bitcoin）查询实时价格\n\njf加空格加表达式加区间（如jf x**3/5+e**x-3*x 0 2）求定积分\n\nfy直接连语种加空格加翻译内容可翻译（如fyen 我爱苹果）')]))
        await app.sendFriendMessage(friend, MessageChain.create([Image.fromLocalFile("C:/Users/Administrator/Desktop/qqBOT/2021-5-6 23.45.52 0000.png")]))
        fll=1
    if message.asDisplay().startswith('steam'):
        await app.sendFriendMessage(friend, MessageChain.create([Plain(r6())]))
        fll=1
    if message.asDisplay().startswith("hl "):
        tmess = re.sub('hl ','',message.asDisplay())
        await app.sendFriendMessage(friend, MessageChain.create([Plain(hl(tmess))]))
        fll=1
    if message.asDisplay().startswith("fy"):
        css = re.sub(' ','',message.asDisplay()[2:5])
        await app.sendFriendMessage(friend, MessageChain.create([Plain(bdfy(message.asDisplay()[5:],css))]))
        fll=1
    if message.asDisplay().startswith("jf "):
        stmess = re.sub('jf ','',message.asDisplay())
        stmess = re.sub('e','2.7182',stmess)
        await app.sendFriendMessage(friend, MessageChain.create([Plain(wjf(stmess))]))
        fll=1
    if message.asDisplay().startswith("ca "):
        ttmess = re.sub('ca ','',message.asDisplay())
        ttmess = re.sub('\s',"",ttmess)
        await app.sendFriendMessage(friend, MessageChain.create([Plain(first_step(ttmess))]))
        fll=1
    if message.asDisplay().startswith("coin"):
        await app.sendFriendMessage(friend, MessageChain.create([Plain(coin())]))
        fll=1
    if message.asDisplay().startswith("bi "):
        tmess = re.sub('bi ','',message.asDisplay()).upper()
        await app.sendFriendMessage(friend, MessageChain.create([Plain(coins(tmess))]))
        fll=1
    if message.asDisplay().startswith("xm"):
        await app.sendFriendMessage(friend, MessageChain.create([Plain('小米当前股价:'+xm())]))
        fll=1
    if message.asDisplay().startswith("creeper"):
        await app.sendFriendMessage(friend, MessageChain.create([Plain("Awwwwwww man?")]))
        fll=1
    if not fll:
        await app.sendFriendMessage(friend, MessageChain.create([Plain("未知指令，输入help获取帮助")]))

'''        await inc.wait(GroupMessageInterrupt(
            group, member,
            custom_judgement=lambda x: x.messageChain.asDisplay().startswith("/confirm")
        ))
        await app.sendGroupMessage(group, MessageChain.creat([
            Plain("执行完毕.")
        ]))
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    await app.sendFriendMessage(friend, MessageChain.create([
        Plain(kk())
    ]))'''
app.launch_blocking()