import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

cl = LineClient(authToken='ECjjCWf5SYMo0tL5R4Pf.WJG8gHJjlIgjNsfQBB647W.SDH+3WenpJV/1QJxTDAt4jnm8snHweCnB0LkC6OyVek=')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient(authToken='EChVJY1UHa7jS2LbTzQ6.nILq0sdil+6eOXNAhcVSzG.F6tIzG1Om5jFJQze/X20HTYJPSqiMkJJzbB1Iz+zFR0=')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

kk = LineClient(authToken='ECi9Wc1JwC9kO6vPJfK6.H2zEHts4H+R/wj20+gKqvG.S86tyeK+NWSPX4xzVtiloOgys+767J6WxeviJdW7oRk=')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

kc = LineClient(authToken='EC7MHC6t32z2Zlk7W2tb.SlIqkZQyuLBjLJTmNqFQsW.ZEJL6eDNQlTrNUoP02PDNuRr0QmnwCnOobnspbVq1nc=')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))

kc4 = LineClient(authToken='ECiCAmMG0IRE8CtGSWN6.yd1yT9E88tk61hgidxYQPG.wsfh6gzyNo1ZHSRGA3t6owJgPm7CRoBRpixzGxEe1cw=')
kc4.log("Auth Token : " + str(kc4.authToken))
channel4 = LineChannel(kc4)
kc4.log("Channel Access Token : " + str(channel4.channelAccessToken))

kc5 = LineClient(authToken='ECwMrdEbWPTyuVBMg8T2.RCpl5hd1yKmymyWwsMlVCG.urUk2mD3k8+dPjoESOeJN9NiWkB1HZPwDXS8Fu560Xg=')
kc5.log("Auth Token : " + str(kc5.authToken))
channel5 = LineChannel(kc5)
kc5.log("Channel Access Token : " + str(channel5.channelAccessToken))

kc6 = LineClient(authToken='ECpDGw0pPtWIyveriY18.IF9rY3IW3AzIWg1da96xca.jMM44eQmrq/bUIgu4V9N1JsCQzAaNsGIiesgJ5UXhrk=')
kc6.log("Auth Token : " + str(kc6.authToken))
channel6 = LineChannel(kc6)
kc6.log("Channel Access Token : " + str(channel6.channelAccessToken))

kc7 = LineClient(authToken='ECCnBB1sUxBPC5HPqMz8.XP+BrsGNqEaYSGzPsTSoIa.oG8Os43DrgfRHD3NfDxURsg00cgKfzc9/cg1DLyJpRo=')
kc7.log("Auth Token : " + str(kc7.authToken))
channel7 = LineChannel(kc7)
kc7.log("Channel Access Token : " + str(channel7.channelAccessToken))

kc8 = LineClient(authToken='ECppNbwqZDgvwl9Rf4Nd.V+ghEvSc3aRjpPV16Yafpq.C1xgl8U0095pnA8eevXGIw3WeAOwFWUh1wSExxJwT3U=')
kc8.log("Auth Token : " + str(kc8.authToken))
channel8 = LineChannel(kc8)
kc8.log("Channel Access Token : " + str(channel8.channelAccessToken))

kc9 = LineClient(authToken='EC6P93eeMJqBuYDnd0Dc.nZiAFaHfAPZ1IAEdRAwOpa./DMROaQLOX1u2tj2SeRIlXrj7I1NuFMwKGE6lge+Q9o=')
kc9.log("Auth Token : " + str(kc9.authToken))
channel9 = LineChannel(kc9)
kc9.log("Channel Access Token : " + str(channel9.channelAccessToken))


poll = LinePoll(cl)
call = cl
creator = ["uc2383c1a18c92e21899d216a6dbeb8ef"]
owner = ["uc2383c1a18c92e21899d216a6dbeb8ef"]
admin = ["uc2383c1a18c92e21899d216a6dbeb8ef"]
staff = ["uc2383c1a18c92e21899d216a6dbeb8ef"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
C4mid = kc4.getProfile().mid
C5mid = kc5.getProfile().mid
C6mid = kc6.getProfile().mid
C7mid = kc7.getProfile().mid
C8mid = kc8.getProfile().mid
C9mid = kc9.getProfile().mid

KAC = [cl,ki,kk,kc,kc4,kc5,kc6,kc7,kc8,kc9]
ABC = [ki,kk,kc,kc4,kc5,kc6,kc7,kc8,kc9]
ppop = [ki,kk,kc,kc4,kc5,kc6,kc7,kc8,kc9]
Bots = [mid,Amid,Bmid,Cmid,C4mid,C5mid,C6mid,C7mid,C8mid,C9mid]
Dpk = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []
leave = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kc4.getProfile().displayName
responsename5 = kc5.getProfile().displayName
responsename6 = kc6.getProfile().displayName
responsename7 = kc7.getProfile().displayName
responsename8 = kc8.getProfile().displayName
responsename9 = kc9.getProfile().displayName



settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":True,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "autoJoin":True,
    "autoAdd":True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":True,
    "sticker":False,
    "selfbot":True,
    "mention":"",
    "Respontag":"",
    "welcome":"",
    "leave":"",
    "comment":"Auto Like ⚔คนติดบอท⚔",
    "message":"💀• Aüto Blöck Messagë •💀\n ออโต้บล็อค: By..⚔คนติดบอท⚔",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน \n %02d ชั่วโมง \n %02d นาที  \n %02d วินาที \n ' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน \n %02d ชั่วโมง \n %02d นาที  \n %02d วินาที \n' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = " \n\n  \n. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n    ".format(str(cl.getGroup(to).name))
                except:
                    no = "\n ความสำเร็จ"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "เออเล่อ\n" + str(error))
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "\n  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\n กลุ่ม "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n     ".format(str(cl.getGroup(to).name))
                except:
                    no = "\n"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "\n ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n".format(str(cl.getGroup(to).name))
                except:
                    no = "\n"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] เออเล่อ\n" + str(error))


def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " \n  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nกลุ่ม  "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n    ".format(str(cl.getGroup(to).name))
                except:
                    no = "\nความสำเร็จ "
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "เออเล่อ\n" + str(error))


def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"เวลา "+datetime.strftime(timeNow,'%H:%M:%S')+" \nกลุ่ม "+str(len(gid))+"\nเพื่อน "+str(len(teman))+"\n หมดอายุ ใน "+hari+"\n เวอร์ชั่นบอท  BOT DS 5.4.2 ( Sept 04 2018 14:52:22) \nวันที "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n เวลาการล็อคอิน   \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = """
☦═ই☬ই═☦ help  ↬  เรียกดูคำสั่ง
☦═ই☬ই═☦ self on  ↬  เปิดเซล
☦═ই☬ই═☦ self off  ↬  ปิดเซล
☦═ই☬ই═☦ status ↬  เช็คตั้งค่า
☦═ই☬ই═☦ me  ↬  คท
☦═ই☬ই═☦ mid  ↬  เช็คmid
☦═ই☬ই═☦ Mid @  ↬  ดึงmid
☦═ই☬ই═☦ Info  @  ↬  ดึงรูป&คท&mid
☦═ই☬ই═☦ เช็ค  ↬  เช็คบอท
☦═ই☬ই═☦ แทค  ↬  แทคทุกคนในกลุ่ม
☦═ই☬ই═☦ sp  ↬  เช็คความเร็ว
☦═ই☬ই═☦ Botadd @  ↬  เพิ่มบอท
☦═ই☬ই═☦ Botdell @  ↬  ลบรายการบอท
☦═ই☬ই═☦ staff:on  ↬  เพิ่มแอดโดยคท
☦═ই☬ই═☦ staff:repeat  ↬  ลบแอดโดยคท
☦═ই☬ই═☦ bot:on ↬  เพิ่มบอทโดยคท
☦═ই☬ই═☦ bot:repeat  ↬  ลบบอทโดยคท
☦═ই☬ই═☦ bot bye  ↬  สั่งตัวเองออก
☦═ই☬ই═☦ Ban @  ↬  บชดำ
☦═ই☬ই═☦ Unban @ ↬  บชขาว
☦═ই☬ই═☦ ban:on  ↬  บชดำโดยคท
☦═ই☬ই═☦ unban:on  ↬  บชขาวโดยคท
☦═ই☬ই═☦ banlist  ↬  เช็คดำ
☦═ই☬ই═☦ clearban  ↬  ล้างดำ
☦═ই☬ই═☦ sidere on    ↬  เปิดระบบอ่าน
☦═ই☬ই═☦ sidere off    ↬  ปิดระบบอ่าน
☦═ই☬ই═☦ kickalls @    ↬  เตะคนแท็กได้ไม่จำกัด


☦═ই☬ই═☦ เวอร์ชั่น    ↬  เช็คเวอร์บอท
☦═ই☬ই═☦ go    ↬  บินกลุ่ม
☦═ই☬ই═☦ ตั้งรันแท็ก: _s ↬  ตั้งค่ารันแท็ก
☦═ই☬ই═☦ รันแท็ก @    ↬  รันแท็ก
☦═ই☬ই═☦ วันเกิด: _d    ↬  ตั้งวันเกิด
☦═ই☬ই═☦ @@    ↬  แท็ก
☦═ই☬ই═☦ เช็คแอด   ↬  เช็คคทแอด
☦═ই☬ই═☦ ลบแชท   ↬  ลบแชทบอท
☦═ই☬ই═☦ ฝาก:: __   ↬  ประกาศกลุ่ม
☦═ই☬ই═☦ คำสั่ง   ↬  ดูคำสั่งที่ตั้ง
☦═ই☬ই═☦ ตั้งคำสั่ง __   ↬  ตั้งคำสั่ง
☦═ই☬ই═☦ ลบคำสั่ง   ↬  ลบที่ตั้ง
☦═ই☬ই═☦ เช็คเพื่อน   ↬  เช็คชื่อเพื่อน
☦═ই☬ই═☦ เช็คกลุ่ม   ↬  เช็คจำนวนห้อง
☦═ই☬ই═☦ ปิดลิ้งค์   ↬  ทำการเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์  ↬  ทำการปิดQR
☦═ই☬ই═☦ อัพลิ้งค์  ↬  ทำการอัพQR
☦═ই☬ই═☦ เปลี่ยนรูปกลุ่ม  ↬  รูปกลุ่มเปลี่ยน
☦═ই☬ই═☦ ออน  ↬  เช็คเวลาล็อค
☦═ই☬ই═☦ เปลี่ยนชื่อ __  ↬  เปลี่ยนชื่อ
☦═ই☬ই═☦ บอท ↬  เช็คชื่อบอท
☦═ই☬ই═☦ แอดมิน  ↬  เช็คจำนวนคนคุม
☦═ই☬ই═☦ ป้องกัน   ↬  เช็คระบบป้องกันแยก
☦═ই☬ই═☦ รายงานตัว  ↬  เช็คบอท
☦═ই☬ই═☦ เชิญบอท  ↬  เชิญบอทที่หาย
☦═ই☬ই═☦ กุออก  ↬  สั่งตัวเองออก
☦═ই☬ই═☦ ออกหมด __ ↬  สั่งบอทออก
☦═ই☬ই═☦ คลิ้กกเข้า  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้กออก  ↬  สั่งคลิ้กออก
☦═ই☬ই═☦ ความเร็ว  ↬  เช็คความเร็ว
☦═ই☬ই═☦ เชิญโทร  ↬  เชิญมาโทร
☦═ই☬ই═☦ เตะ @  ↬  สั่งเตะ
☦═ই☬ই═☦ เพิ่มแอด @  ↬  เพิ่มแอดมิน
☦═ই☬ই═☦ ตั้งแอด @  ↬  เพิ่มแอดมิน
☦═ই☬ই═☦ ลบแอด @  ↬  ลบแอดออก
☦═ই☬ই═☦ ลบแอดมิน @  ↬  ลบแอดออก
☦═ই☬ই═☦ เพิ่มแอดมิน  ↬  โดยคท
☦═ই☬ই═☦ ลบคนคุมบอท  ↬  โดยคท
☦═ই☬ই═☦ หยุดการเพิ่ม  ↬  หยุดการเพิ่มแอด
☦═ই☬ই═☦ คทแอดมิน ↬  เช็คคทแอด
☦═ই☬ই═☦ คทแอด ↬  เช็คคทแอด
☦═ই☬ই═☦ คทบอท ↬  เช็คคทบอท
☦═ই☬ই═☦ ตั้งเชิญโทร: _s  ↬  ตั้งเลขเชิญ

☦═ই☬ই═☦ ตั้งแอด @  ↬  ตั้งแอดมิน
☦═ই☬ই═☦ เพิ่มแอด @  ↬  ตั้งแอดมิน
☦═ই☬ই═☦ ลบรายการแอด @  ↬  ลบแอด
☦═ই☬ই═☦ ลบแอดมิน @  ↬  ลบแอด
☦═ই☬ই═☦ เพิ่มแอ ดมินบอท1  ↬  เพิ่มแอด คท
☦═ই☬ই═☦ ลบคนคุมบอทออก1  ↬  ลบแอดคท
☦═ই☬ই═☦ หยุดการเพิ่ม1  ↬  ปิดการเพิ่มแอด
☦═ই☬ই═☦ ดำ @  ↬  ทำดำยาว
☦═ই☬ই═☦ ขาว @  ↬  ทำขาวยาว
☦═ই☬ই═☦ เพิ่มดำ  ↬  บชดำโดยคท
☦═ই☬ই═☦ เพิ่มขาว  ↬  บชขาวโดยคท
☦═ই☬ই═☦ เช็คบชดำ  ↬  เช็คดำ
☦═ই☬ই═☦ คทดำ  ↬  เช็คดำ
☦═ই☬ই═☦ คทดำ1  ↬  เช็คดำ

☦═ই☬ই═☦ ป้องกันบอทลบ   ↬  ป้องกันjs
☦═ই☬ই═☦ คลิ้กเข้า  ↬  สั่งเข้า
☦═ই☬ই═☦ คลิ้กออก  ↬  สั่งออก
☦═ই☬ই═☦ ออกหมด __   ↬  สั่งคลิ้กออก
☦═ই☬ই═☦ คลิ้ก1   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก2  ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก3   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก4   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก5   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก6   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก7   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก8   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก9   ↬  คลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก   ↬  คลิ้กเข้า

☦═ই☬ই═☦ ตั้งค่า    ↬  เช็คตั้งค่า
☦═ই☬ই═☦ ทักทาย เปิด  ↬  เปิดทัก
☦═ই☬ই═☦ ทักทาย ปิด  ↬  ปิดทัก
☦═ই☬ই═☦ ป้องกันลิ้งค์ เปิด  ↬  เปิดกันQR
☦═ই☬ই═☦ ป้องกันลิ้งค์ ปิด  ↬  ปิดกันQR
☦═ই☬ই═☦ ป้องกันการเตะ เปิด  ↬  เปิดกันลบ
☦═ই☬ই═☦ ป้องกันการเตะ ปิด  ↬  ปิดกันลบ
☦═ই☬ই═☦ ป้องกันการเข้า เปิด  ↬  เปิดกันคนเข้า
☦═ই☬ই═☦ ป้องกันการเข้า ปิด  ↬  ปิดกันคนเข้า
☦═ই☬ই═☦ ป้องกันการเชิญ เปิด  ↬  เปิดกันเชิญ
☦═ই☬ই═☦ ป้องกันการเชิญ ปิด↬  ปิดกันเชิญ
☦═ই☬ই═☦ ป้องกันการยก เปิด ↬  เปิดกันยกเลิก
☦═ই☬ই═☦ ป้องกันการยก ปิด ↬  ปิดกันยกเลิก
☦═ই☬ই═☦ ป้องกันบอทลบ เปิด ↬  เปิดกันjs
☦═ই☬ই═☦ ผี เปิด  ↬  เปิดระบบคลิ้กผี
☦═ই☬ই═☦ ผี ปิด  ↬  ปิดระบบคลิ้กผี
☦═ই☬ই═☦ ระบบป้องกันทั้งหมด เปิด  ↬  เปิดทั้งหมด
☦═ই☬ই═☦ ระบบป้องกันทั้งหมด ปิด  ↬  ปิดทั้งหมด
☦═ই☬ই═☦ เตะแท็ก เปิด  ↬  เปิดแท็กเตะ
☦═ই☬ই═☦ เตะแท็ก ปิด  ↬  ปิดแท็กเตะ
☦═ই☬ই═☦ เช็คคท เปิด   ↬  เปิดเช็คคท
☦═ই☬ই═☦ เช็คคท ปิด   ↬  ปิดเช็คคท
☦═ই☬ই═☦ แท็ก เปิด   ↬  เปิดระบบแท็ก
☦═ই☬ই═☦ แท็ก ปิด   ↬  ปิดระบบแท็ก
☦═ই☬ই═☦ เข้าออโต้ เปิด   ↬  เปิดเข้าอัตโนมัติ
☦═ই☬ই═☦ เข้าออโต้ ปิด   ↬  ปิดเข้าอัตโนมัติ
☦═ই☬ই═☦ ออกแชท เปิด   ↬  กันแชทรวม
☦═ই☬ই═☦ ออกแชท ปิด   ↬  ปิดกันแชทรวม
☦═ই☬ই═☦ ออโต้แอด เปิด   ↬  แอดมีข้อความ
☦═ই☬ই═☦ ออโต้แอด ปิด   ↬  ปิดแอดมีข้อความ
☦═ই☬ই═☦ เช็คติ้ก เปิด   ↬  เช็คติ้ก
☦═ই☬ই═☦ เช็คติ้ก ปิด   ↬  ปิดเช็คติ้ก
☦═ই☬ই═☦ ตั๋ว เปิด   ↬  เข้าโดยลิ้งค์
☦═ই☬ই═☦ ตั๋ว ปิด   ↬  ปิดเข้าโดยลิ้งค์

☦═ই☬ই═☦ ตั้งข้อความแอด __   ↬  ตั้งข้อความ
☦═ই☬ই═☦ ตั้งคนเข้า __  ↬  ตั้งทักเข้า
☦═ই☬ই═☦ ตั้งระบบออก __  ↬  ตั้งทักออก
☦═ই☬ই═☦ ตั้งแท็ก __   ↬  ตั้งข้อความ
☦═ই☬ই═☦ ตั้งสแปม __   ↬  ตั้งข้อความ
☦═ই☬ই═☦ ตั้งอ่าน __   ↬  ตั้งข้อความ
☦═ই☬ই═☦ เช็คข้อความแอด   ↬  เช็คข้อความ
☦═ই☬ই═☦ เช็คทักเข้า   ↬  เช็คข้อความ
☦═ই☬ই═☦ เช็คแท็ก   ↬  เช็คข้อความ
☦═ই☬ই═☦ เช็คสแปม   ↬  เช็คข้อความ
☦═ই☬ই═☦ เช็คการอ่าน   ↬  เช็คข้อความ

☦═ই☬ই═☦ เช็คกลุ่ม1   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม2   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม3   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม4   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม5   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม6   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม7   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม8   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เช็คกลุ่ม9   ↬  เช็คห้องคลิ้ก
☦═ই☬ই═☦ เปิดลิ้งค์1   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์2   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์3   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์4   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์5   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์6   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์7   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์8   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ เปิดลิ้งค์9   ↬  คลิ้กเปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์1   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์2   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์3   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์4   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์5   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์6   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์7   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์8   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ ปิดลิ้งค์9   ↬  คลิ้กปิดQR
☦═ই☬ই═☦ เปลี่ยนชื่อ1 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ2 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ3 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ4 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ5 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ6 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ7 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ8 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อ9 __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ เปลี่ยนชื่อผี __  ↬  เปลี่ยนชื่อคลิ้ก
☦═ই☬ই═☦ คลิ้ก1  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก2  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก3  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก4  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก5  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก6  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก7  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก8  ↬  สั่งคลิ้กเข้า
☦═ই☬ই═☦ คลิ้ก9  ↬  สั่งคลิ้กเข้า

หมายเหตุ1  ตรงหลังคำสั่งที่มี เครื่องหมาย __ คือให้ไส่ข้อความ 
หมายเหตุ2  ตรงหลังคำสั่งที่มี เครื่องหมาย _s คือให้ไส่เลข
หมายเหตุ3  ตรงหลังคำสั่งที่มี เครื่องหมาย _d คือให้ไส่เลขวันทีตัวอย่าง 2018-09-05
	"""
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = """
	"""
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            cl.reissueGroupTicket(op.param1)
                                            X = cl.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"คุณไม่ได้รับอนุญาตให้เชิญ \n กลุ่ม " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if C4mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc4.acceptGroupInvitation(op.param1)
                        ginfo = kc4.getGroup(op.param1)
                        kc4.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc4.acceptGroupInvitation(op.param1)
                        ginfo = kc4.getGroup(op.param1)
                        kc4.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if C5mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc5.acceptGroupInvitation(op.param1)
                        ginfo = kc5.getGroup(op.param1)
                        kc5.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc5.acceptGroupInvitation(op.param1)
                        ginfo = kc5.getGroup(op.param1)
                        kc5.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if C6mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc6.acceptGroupInvitation(op.param1)
                        ginfo = kc6.getGroup(op.param1)
                        kc6.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc6.acceptGroupInvitation(op.param1)
                        ginfo = kc6.getGroup(op.param1)
                        kc6.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if C7mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc7.acceptGroupInvitation(op.param1)
                        ginfo = kc7.getGroup(op.param1)
                        kc7.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc7.acceptGroupInvitation(op.param1)
                        ginfo = kc7.getGroup(op.param1)
                        kc7.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if C8mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc8.acceptGroupInvitation(op.param1)
                        ginfo = kc8.getGroup(op.param1)
                        kc8.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc8.acceptGroupInvitation(op.param1)
                        ginfo = kc8.getGroup(op.param1)
                        kc8.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))
            if C9mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc9.acceptGroupInvitation(op.param1)
                        ginfo = kc9.getGroup(op.param1)
                        kc9.sendMessage(op.param1,"สวัสดี " +str(ginfo.name))
                    else:
                        kc9.acceptGroupInvitation(op.param1)
                        ginfo = kc9.getGroup(op.param1)
                        kc9.sendMessage(op.param1,"สวัสดี " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kc10.cancelGroupInvitation(op.param1,[_mid])
                        kc10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.cancelGroupInvitation(op.param1,[_mid])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        group = kc4.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kc4.cancelGroupInvitation(op.param1,[_mid])
                                            kc4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            group = kc5.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                kc5.cancelGroupInvitation(op.param1,[_mid])
                                                kc5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                group = kc6.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    kc6.cancelGroupInvitation(op.param1,[_mid])
                                                    kc6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    group = kc7.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        kc7.cancelGroupInvitation(op.param1,[_mid])
                                                        kc7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        group = kc8.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            kc8.cancelGroupInvitation(op.param1,[_mid])
                                                            kc8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            group = kc9.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for _mid in gMembMids:
                                                                kc9.cancelGroupInvitation(op.param1,[_mid])
                                                                kc9.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                cl.sendContact(op.param1, op.param2)
                cl.sendImageWithURL(op.param1, image)
        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n  " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
#                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.prevenARoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.prevenARoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"ระบบป้องกันระบบ JS")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"ระบบป้องกันระบบ JS")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"ระบบป้องกันระบบ JS")
                else:
                    pass
            except:
                pass
#-------------------------------------------------------------------------------                
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in wait["blacklist"]:
                                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    if op.param3 not in wait["blacklist"]:
                                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                            kc7.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = ki.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.updateGroup(G)
                                                            Ticket = ki.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = ki.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            ki.updateGroup(G)
                                                            Ticket = ki.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                cl.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    cl.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                        cl.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                            kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                            cl.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                cl.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    cl.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        cl.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            cl.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                            kc7.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kk.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.updateGroup(G)
                                                            Ticket = kk.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kk.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kk.updateGroup(G)
                                                            Ticket = kk.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                                ki.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                            kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ki.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                            kc7.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.updateGroup(G)
                                                            Ticket = kc.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc.updateGroup(G)
                                                            Ticket = kc.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                                kk.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kk.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                        kk.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                            kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                            kk.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                kk.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kk.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kk.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kk.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                            kc7.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = cl.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                            cl.updateGroup(G)
                                                            Ticket = cl.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = cl.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            cl.updateGroup(G)
                                                            Ticket = cl.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                                kc.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                            kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if C4mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc5.kickoutFromGroup(op.param1,[op.param2])
                        kc5.inviteIntoGroup(op.param1,[op.param3])
                        kc4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kc4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc4.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                        kc4.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                            kc7.inviteIntoGroup(op.param1,[op.param3])
                                            kc4.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                kc4.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    kc4.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc4.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc5.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                                            kc5.updateGroup(G)
                                                            Ticket = kc5.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc5.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc5.updateGroup(G)
                                                            Ticket = kc5.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                kc4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc4.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                            kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc4.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc4.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc4.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc4.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc4.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if C5mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc4.kickoutFromGroup(op.param1,[op.param2])
                        kc4.inviteIntoGroup(op.param1,[op.param3])
                        kc5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kc5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc5.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                        kc5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                            kc7.inviteIntoGroup(op.param1,[op.param3])
                                            kc5.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                kc5.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    kc5.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc5.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc4.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc4.kickoutFromGroup(op.param1,[op.param2])
                                                            kc4.updateGroup(G)
                                                            Ticket = kc4.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc4.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc4.updateGroup(G)
                                                            Ticket = kc4.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                kc5.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc5.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc5.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc5.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc5.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc5.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc5.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc5.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if C6mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc7.kickoutFromGroup(op.param1,[op.param2])
                        kc7.inviteIntoGroup(op.param1,[op.param3])
                        kc6.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc6.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kc6.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc6.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc5.kickoutFromGroup(op.param1,[op.param2])
                                        kc5.inviteIntoGroup(op.param1,[op.param3])
                                        kc6.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc4.kickoutFromGroup(op.param1,[op.param2])
                                            kc4.inviteIntoGroup(op.param1,[op.param3])
                                            kc6.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                kc6.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    kc6.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc6.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc7.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc7.kickoutFromGroup(op.param1,[op.param2])
                                                            kc7.updateGroup(G)
                                                            Ticket = kc7.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc7.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc7.updateGroup(G)
                                                            Ticket = kc7.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc7.kickoutFromGroup(op.param1,[op.param2])
                                                                kc7.inviteIntoGroup(op.param1,[op.param3])
                                                                kc6.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc6.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc6.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc6.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc6.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc6.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc6.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc6.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if C7mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc6.kickoutFromGroup(op.param1,[op.param2])
                        kc6.inviteIntoGroup(op.param1,[op.param3])
                        kc7.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc7.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kc7.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc7.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc5.kickoutFromGroup(op.param1,[op.param2])
                                        kc5.inviteIntoGroup(op.param1,[op.param3])
                                        kc7.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc4.kickoutFromGroup(op.param1,[op.param2])
                                            kc4.inviteIntoGroup(op.param1,[op.param3])
                                            kc7.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                kc7.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc9.kickoutFromGroup(op.param1,[op.param2])
                                                    kc9.inviteIntoGroup(op.param1,[op.param3])
                                                    kc7.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc7.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc6.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc6.kickoutFromGroup(op.param1,[op.param2])
                                                            kc6.updateGroup(G)
                                                            Ticket = kc6.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc6.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc6.updateGroup(G)
                                                            Ticket = kc6.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                kc7.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc7.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc7.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc7.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc7.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc7.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc7.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc7.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if C8mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc9.kickoutFromGroup(op.param1,[op.param2])
                        kc9.inviteIntoGroup(op.param1,[op.param3])
                        kc8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kc8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc8.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc5.kickoutFromGroup(op.param1,[op.param2])
                                        kc5.inviteIntoGroup(op.param1,[op.param3])
                                        kc8.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc4.kickoutFromGroup(op.param1,[op.param2])
                                            kc4.inviteIntoGroup(op.param1,[op.param3])
                                            kc8.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                kc8.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                    kc8.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc8.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                            kc9.updateGroup(G)
                                                            Ticket = kc9.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc9.updateGroup(G)
                                                            Ticket = kc9.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                kc8.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc8.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc8.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kk7.kickoutFromGroup(op.param1,[op.param2])
                                                                            kk7.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc8.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc8.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc8.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc8.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc9.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc8.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if C9mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc8.kickoutFromGroup(op.param1,[op.param2])
                        kc8.inviteIntoGroup(op.param1,[op.param3])
                        kc9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kc9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc9.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc5.kickoutFromGroup(op.param1,[op.param2])
                                        kc5.inviteIntoGroup(op.param1,[op.param3])
                                        kc9.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc4.kickoutFromGroup(op.param1,[op.param2])
                                            kc4.inviteIntoGroup(op.param1,[op.param3])
                                            kc9.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                kc6.inviteIntoGroup(op.param1,[op.param3])
                                                kc9.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                    kc7.inviteIntoGroup(op.param1,[op.param3])
                                                    kc9.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kc9.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = kc8.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc8.kickoutFromGroup(op.param1,[op.param2])
                                                            kc8.updateGroup(G)
                                                            Ticket = kc8.reissueGroupTicket(op.param1)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = kc8.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc8.updateGroup(G)
                                                            Ticket = kc8.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                kc9.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc9.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    try:
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc9.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        try:
                                                                            kk7.kickoutFromGroup(op.param1,[op.param2])
                                                                            kk7.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc9.acceptGroupInvitation(op.param1)
                                                                        except:
                                                                            try:
                                                                                kc4.kickoutFromGroup(op.param1,[op.param2])
                                                                                kc4.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc9.acceptGroupInvitation(op.param1)
                                                                            except:
                                                                                try:
                                                                                    kc5.kickoutFromGroup(op.param1,[op.param2])
                                                                                    kc5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc9.acceptGroupInvitation(op.param1)
                                                                                except:
                                                                                    try:
                                                                                        kc6.kickoutFromGroup(op.param1,[op.param2])
                                                                                        kc6.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc9.acceptGroupInvitation(op.param1)
                                                                                    except:
                                                                                        try:
                                                                                            kc8.kickoutFromGroup(op.param1,[op.param2])
                                                                                            kc8.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc9.acceptGroupInvitation(op.param1)
                                                                                        except:
                                                                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                        kc4.findAndAddContactsByMid(op.param1,admin)
                                        kc4.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                            kc5.findAndAddContactsByMid(op.param1,admin)
                                            kc5.inviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                kc6.findAndAddContactsByMid(op.param1,admin)
                                                kc6.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                    kc7.findAndAddContactsByMid(op.param1,admin)
                                                    kc7.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                        kc8.findAndAddContactsByMid(op.param1,admin)
                                                        kc8.inviteIntoGroup(op.param1,admin)
                                                    except:
                                                        try:
                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                            kc9.findAndAddContactsByMid(op.param1,admin)
                                                            kc9.inviteIntoGroup(op.param1,admin)
                                                        except:
                                                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,staff)
                                    kc.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        kc4.kickoutFromGroup(op.param1,[op.param2])
                                        kc4.findAndAddContactsByMid(op.param1,staff)
                                        kc4.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            kc5.kickoutFromGroup(op.param1,[op.param2])
                                            kc5.findAndAddContactsByMid(op.param1,staff)
                                            kc5.inviteIntoGroup(op.param1,staff)
                                        except:
                                            try:
                                                kc6.kickoutFromGroup(op.param1,[op.param2])
                                                kc6.findAndAddContactsByMid(op.param1,staff)
                                                kc6.inviteIntoGroup(op.param1,staff)
                                            except:
                                                try:
                                                    kc7.kickoutFromGroup(op.param1,[op.param2])
                                                    kc7.findAndAddContactsByMid(op.param1,staff)
                                                    kc7.inviteIntoGroup(op.param1,staff)
                                                except:
                                                    try:
                                                        kc8.kickoutFromGroup(op.param1,[op.param2])
                                                        kc8.findAndAddContactsByMid(op.param1,staff)
                                                        kc8.inviteIntoGroup(op.param1,staff)
                                                    except:
                                                        try:
                                                            kc9.kickoutFromGroup(op.param1,[op.param2])
                                                            kc9.findAndAddContactsByMid(op.param1,staff)
                                                            kc9.inviteIntoGroup(op.param1,staff)
                                                        except:
                                                            pass

                return


        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52114132","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"เช็คไอดีและลิ้งค์ติ้กเกอร์\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nLink Sticker" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"ชื่อ   " + msg.contentMetadata["displayName"] + "\nMID  " + msg.contentMetadata["mid"] + "\nตัส   " + contact.statusMessage + "\nลิ้งค์รูป http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nLink Sticker" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"คอนแทคที่คุณลงมาได้เป็นสมาชิกบอทแล้ว")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"เพิ่มสมาชิก bot เรียบร้อยแล้ว")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"นำออกจากสมาชิก bot เรียบร้อยแล้ว")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"คอนแทคที่ลงมาไม่ได้เป็นสมาชิกของบอท")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"คอนแทคที่ลงมาได้เป็นแอดมินบอทแล้ว")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"เพิ่มพนักงานเรียบร้อยแล้ว")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"ลบพนังงานเรียบร้อย")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"คอนแทคที่คุณลงมาไม่ได้เป็นพนังงานของบอท")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"คอนแทคที่ส่งมา คือ คอนแทคแอดมิน")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"เพิ่มแอดมินเรียบร้อย")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"ลบแอดมินเรียบร้อย")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"ผู้ติดต่อไม่ได้เป็นผู้ดูแลระบบ")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"ผู้ติดต่ออยู่ในรายการดำที่ไม่อนุญาต")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"เพิ่มลงในบัญชีดำของผู้ใช้เรียบร้อยแล้ว")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"ลบเรียบร้อยแล้วจากบัญชีดำของผู้ใช้")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"คอนแทคที่คุณลงมาไม่ได้อยู่ในรายการดำ")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"คทติดบชดำ")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"บชดำ")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"ลบเรียบร้อยแล้วจากผู้ใช้ Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"ไม่มีที่อยู่ติดต่อใน Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "เพิ่มรูปภาพสำเร็จแล้ว")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "ได้ทำการเปลี่ยนรูปห้องเรียบร้อย")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif C4mid in Setmain["ARfoto"]:
                            path = kc4.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][C4mid]
                            kc4.updateProfilePicture(path)
                            kc4.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif C5mid in Setmain["ARfoto"]:
                            path = kc5.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][C5mid]
                            kc5.updateProfilePicture(path)
                            kc5.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif C6mid in Setmain["ARfoto"]:
                            path = kc6.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][C6mid]
                            kc6.updateProfilePicture(path)
                            kc6.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif C7mid in Setmain["ARfoto"]:
                            path = kc7.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][C7mid]
                            kc7.updateProfilePicture(path)
                            kc7.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif C8mid in Setmain["ARfoto"]:
                            path = kc8.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][C8mid]
                            kc8.updateProfilePicture(path)
                            kc8.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif C9mid in Setmain["ARfoto"]:
                            path = kc9.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][C9mid]
                            kc9.updateProfilePicture(path)
                            kc9.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc4.updateProfilePicture(path4)
                     kc4.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc5.updateProfilePicture(path5)
                     kc5.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc6.updateProfilePicture(path6)
                     kc6.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc7.updateProfilePicture(path7)
                     kc7.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc8.updateProfilePicture(path8)
                     kc8.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")
                     kc9.updateProfilePicture(path9)
                     kc9.sendMessage(msg.to, "เปลี่ยนโฟลต์รูปโปรไฟล์เรียบร้อยแล้ว")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "ปิดระบบการตอบของเซลบอทเรียบร้อย")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "ปิดระบบการตอบของเซลบอทเรียบร้อย")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "status"or text.lower() == 'ตั้งค่า':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "⚔คนติดบอท⚔\n"
                                if wait["sticker"] == True: md+="เช็คติ้กเกอร์ เปิด\n"
                                else: md+="เช็คติ้กเกอร์ ปิด\n"
                                if wait["contact"] == True: md+="เช็คคท เปิด\n"
                                else: md+="เช็คคท ปิด\n"
                                if wait["talkban"] == True: md+="ลงบชดำโดยคท เปิด\n"
                                else: md+="ลงบชดำโดยคท ปิด\n"
                                if wait["Mentionkick"] == True: md+="แท็กเตะ เปิด\n"
                                else: md+="แท็กเตะ ปิด\n"
                                if wait["detectMention"] == True: md+="แท็ก เปิด\n"
                                else: md+="แท็ก ปิด\n"
                                if wait["autoJoin"] == True: md+="เข้าออโต้ เปิด\n"
                                else: md+="เข้าออโต้ ปิด\n"
                                if wait["autoAdd"] == True: md+="ออโต้แอด เปิด\n"
                                else: md+="ออโต้แอด ปิด\n"
                                if msg.to in welcome: md+="ทักทาย เปิด\n"
                                else: md+="ทักทาย ปิด\n"
                                if wait["autoLeave"] == True: md+="ออกแชทรวม เปิด\n"
                                else: md+="ออกแชทรวม ปิด\n"
                                if msg.to in protectqr: md+="ป้องกันลิ้งค์ เปิด\n"
                                else: md+="ป้องกันลิ้งค์ ปิด\n"
                                if msg.to in protectjoin: md+="ป้องกันการเข้าร่วม เปิด\n"
                                else: md+="ป้องกันการเข้าร่วม ปิด\n"
                                if msg.to in protectkick: md+="ป้องกันการเตะ เปิด\n"
                                else: md+="ป้องกันการเตะ ปิด\n"
                                if msg.to in protectcancel: md+="ป้องกันยกเลิก เปิด\n"
                                else: md+="ป้องกันยกเลิก ปิด\n"
                                if msg.to in protectinvite: md+="ป้องกันเชิญ เปิด\n"
                                else: md+="ป้องกันเชิญ ปิด\n"
                                if msg.to in protectantijs: md+="ป้องกันบอทลบ JS เปิด\n"
                                else: md+="ป้องกันบอทลบ JS ปิด\n"  
                                if msg.to in ghost: md+="ระบบคลิ้กนอกเข้า เปิด\n"
                                else: md+="ระบบคลิ้กนอกเข้า ปิด\n"                                   
                                cl.sendMessage(msg.to, md+"\nวันที  "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")

                        elif cmd == "เช็คแอด" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"คทแอดผู้ดูแลระบบ") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "เวอร์ชั่น" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "Sai Selfbot \n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif text.lower() == "go":
                          ytoo = random.choice(ppop)
                          g = cl.getGroup(msg.to)						 
                          gmembs = len(g.members)
                          xxyy = [i.mid for i in g.members if i.mid not in Bots]
                          for u in xxyy:
                              ytoo.kickoutFromGroup(g.id,[u])
                          #kk.leaveGroup(msg.to)
                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
								   								   	   
                        elif cmd == "เช็ค":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': C4mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': C5mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': C6mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': C7mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': C8mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': C9mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)


                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kc4.removeAllMessages(op.param2)
                                   kc5.removeAllMessages(op.param2)
                                   kc6.removeAllMessages(op.param2)
                                   kc7.removeAllMessages(op.param2)
                                   kc8.removeAllMessages(op.param2)
                                   kc9.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "ลบบอท1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kc4.removeAllMessages(op.param2)
                                   kc5.removeAllMessages(op.param2)
                                   kc6.removeAllMessages(op.param2)
                                   kc7.removeAllMessages(op.param2)
                                   kc8.removeAllMessages(op.param2)
                                   kc9.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"ลบแชทคลิ้กเรียบร้ออย")
                               except:
                                   pass

                        elif cmd.startswith("ฝาก:: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"\n" + str(pesan))

                        elif text.lower() == "คำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, " " + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("ตั้งคำสั่ง "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "ไม่สามารถเปลี่ยนคีย์")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "คำสั่งที่ถูกตั้ง \n {}".format(str(key).lower()))

                        elif text.lower() == "ลบคำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "ได้ทำการลบคำสั่งที่ตั้งเรียบร้อย")

                        elif cmd == "รีบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "รอการรีบูทระบบใหม่ทั้งหมด")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "รอการรีบูท")
                            
                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "βӪ₮₤ЇŊ€ \n" +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, " Grup Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nâ‚-âž£Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "Fams Grup Info\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kc4.leaveGroup(i)
                                    kc5.leaveGroup(i)
                                    kc6.leaveGroup(i)
                                    kc7.leaveGroup(i)
                                    kc8.leaveGroup(i)
                                    kc9.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "เช็คเพื่อน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"   รายชื่อเพื่อนในไลน์\n \n"+ma+" \nจำนวน"+str(len(gid))+" คน")

                        elif cmd == "เช็คกลุ่ม1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")
							   
                        elif cmd == "เช็คกลุ่ม2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc4.getGroupIdsJoined()
                               for i in gid:
                                   G = kc4.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc4.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม5":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc5.getGroupIdsJoined()
                               for i in gid:
                                   G = kc5.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc5.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม6":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc6.getGroupIdsJoined()
                               for i in gid:
                                   G = kc6.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc6.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม7":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc7.getGroupIdsJoined()
                               for i in gid:
                                   G = kc7.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc7.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม8":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc8.getGroupIdsJoined()
                               for i in gid:
                                   G = kc8.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc8.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")

                        elif cmd == "เช็คกลุ่ม9":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc9.getGroupIdsJoined()
                               for i in gid:
                                   G = kc9.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "  " + str(a) + ". " +G.name+ "\n"
                               kc9.sendMessage(msg.to,"    รายการกลุ่ม \n‘\n"+ma+"\nจำนวน"+str(len(gid))+" กลุ่ม")


                        elif cmd == "เปิดลิ้งค์":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "เปิดลิ้งค์OK")

                        elif cmd == "เปิดลิ้งค์1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kk.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kk.updateGroup(X)
                                   kk.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc.updateGroup(X)
                                   kc.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc4.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc4.updateGroup(X)
                                   kc4.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์5":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc5.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc5.updateGroup(X)
                                   kc5.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์6":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc6.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc6.updateGroup(X)
                                   kc6.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์7":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc7.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc7.updateGroup(X)
                                   kc7.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์8":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc8.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc8.updateGroup(X)
                                   kc8.sendMessage(msg.to, "เปิดลิ้งค์OK")
								   
                        elif cmd == "เปิดลิ้งค์9":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc9.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kc9.updateGroup(X)
                                   kc9.sendMessage(msg.to, "เปิดลิ้งค์OK")

                        elif cmd == "ปิดลิ้งค์":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ปิดลิ้งค์OK")

                        elif cmd == "ปิดลิ้งค์1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kk.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kk.updateGroup(X)
                                   kk.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc.updateGroup(X)
                                   kc.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc4.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc4.updateGroup(X)
                                   kc4.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์5":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc5.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc5.updateGroup(X)
                                   kc5.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์6":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc6.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc6.updateGroup(X)
                                   kc6.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์7":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc7.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc7.updateGroup(X)
                                   kc7.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์8":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc8.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc8.updateGroup(X)
                                   kc8.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "ปิดลิ้งค์9":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kc9.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kc9.updateGroup(X)
                                   kc9.sendMessage(msg.to, "ปิดลิ้งค์OK")
								   
                        elif cmd == "อัพลิ้งค์":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ชื่อกลุ่ม "+str(x.name)+ "\nลิ้งค์กลุ่ม   http://line.me/R/ti/g/"+gurl)

#================================================ระบบเปลี่ยนชื่อและรุป=================================================================================================================================================================#

                        elif cmd == "เปลี่ยนรูปกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"ส่งรูปภาพ ...")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"ส่งรูปภาพ ...")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"ส่งรูปภาพ ...")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendText(msg.to,"ส่งรูปภาพ ...")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendText(msg.to,"ส่งรูปภาพ ...")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to,"ส่งรูปภาพ ...")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to,"ส่งรูปภาพ ...")

                        elif cmd.startswith("เปลี่ยนชื่อ "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")

                        elif cmd.startswith("เปลี่ยนชื่อ1 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"เปลี่ยนชื่อเป็น   " + string + "")

                        elif cmd.startswith("เปลี่ยนชื่อ2 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")

                        elif cmd.startswith("เปลี่ยนชื่อ3 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")

                        elif cmd.startswith("เปลี่ยนชื่อ4 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc4.getProfile()
                                profile.displayName = string
                                kc4.updateProfile(profile)
                                kc4.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")
								
                        elif cmd.startswith("เปลี่ยนชื่อ5 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc5.getProfile()
                                profile.displayName = string
                                kc5.updateProfile(profile)
                                kc5.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")
								
                        elif cmd.startswith("เปลี่ยนชื่อ6 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc6.getProfile()
                                profile.displayName = string
                                kc6.updateProfile(profile)
                                kc6.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")
								
                        elif cmd.startswith("เปลี่ยนชื่อ7 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc7.getProfile()
                                profile.displayName = string
                                kc7.updateProfile(profile)
                                kc7.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")
								
                        elif cmd.startswith("เปลี่ยนชื่อ8 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc8.getProfile()
                                profile.displayName = string
                                kc8.updateProfile(profile)
                                kc8.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")
								
                        elif cmd.startswith("เปลี่ยนชื่อ9 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc9.getProfile()
                                profile.displayName = string
                                kc9.updateProfile(profile)
                                kc9.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")

                        elif cmd.startswith("เปลี่ยนชื่อผี "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"เปลี่ยนชื่อเป็น  " + string + "")

#==========================================ระบบแท้กและระบบเช็คค่าแยกห้อง&ระบบคลิ้ก By.⚔คนติดบอท⚔=========================================================================================================#

                        elif cmd == "แทค" or text.lower() == 'ðŸ˜†':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "บอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"⚔คนติดบอท⚔\n\n"+ma+"\nจำนวน %s BOT" %(str(len(Bots))))

                        elif cmd == "แอดมิน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"⚔คนติดบอท⚔\n\nSuper admin\n"+ma+"\nAdmin\n"+mb+"\nStaff\n"+mc+"\nจำนวน %s คน" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "ป้องกัน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"⚔คนติดบอท⚔\n\nป้องกันQR \n"+ma+"\nป้องกันการลบ \n"+mb+"\nป้อองกันการเข้า \n"+md+"\nป้องกันการยกเลิก \n"+mc+"\nจำนวน %s กลุ่ม" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "รายงานตัว":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kc4.sendMessage(msg.to,responsename4)
                                kc5.sendMessage(msg.to,responsename5)
                                kc6.sendMessage(msg.to,responsename6)
                                kc7.sendMessage(msg.to,responsename7)
                                kc8.sendMessage(msg.to,responsename8)
                                kc9.sendMessage(msg.to,responsename9)

                        elif cmd == "เชิญบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid,Cmid,Amid,Zmid,C4mid,C5mid,C6mid,C7mid,C8mid,C9mid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                    kc4.acceptGroupInvitation(msg.to)
                                    kc5.acceptGroupInvitation(msg.to)
                                    kc6.acceptGroupInvitation(msg.to)
                                    kc7.acceptGroupInvitation(msg.to)
                                    kc8.acceptGroupInvitation(msg.to)
                                    kc9.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "ป้องกันบอทลบ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"ชื่อห้อง "+str(ginfo.name)+" ป้องกันบอทJS")
                                except:
                                    pass
    
                        elif cmd == "คลิ้กเข้า":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "คลิ้กออก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendText(msg.to, "ไปละนะ "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kc4.leaveGroup(msg.to)
                                kc5.leaveGroup(msg.to)
                                kc6.leaveGroup(msg.to)
                                kc7.leaveGroup(msg.to)
                                kc8.leaveGroup(msg.to)
                                kc9.leaveGroup(msg.to)
                                
                        elif cmd == "bot bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "ไปละนะ "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("ออกหมด "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "ถูกสั่งออกจากผู้ดูแลระบบ")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kc4.leaveGroup(i)
                                        kc5.leaveGroup(i)
                                        kc6.leaveGroup(i)
                                        kc7.leaveGroup(i)
                                        kc8.leaveGroup(i)
                                        kc9.leaveGroup(i)
                                        cl.sendMessage(to,"ระบบคลิ้กถูกสั่งออกจาก " +h + "หมดแล้ว")

                        elif cmd == "คลิ้ก1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "คลิ้ก2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "คลิ้ก3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
								
                        elif cmd == "คลิ้ก4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc4.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc4.updateGroup(G)
								
                        elif cmd == "คลิ้ก5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc5.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc5.updateGroup(G)
								
                        elif cmd == "คลิ้ก6":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc6.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k6c.updateGroup(G)
								
                        elif cmd == "คลิ้ก7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc7.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc7.updateGroup(G)
								
                        elif cmd == "คลิ้ก8":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc8.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc8.updateGroup(G)
								
                        elif cmd == "คลิ้ก9":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc9.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc9.updateGroup(G)

                        elif cmd == "คลิ้กผี":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "คลิ้กผีอออก":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "ความเร็ว":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "ตอบสนองความเร็ว\n\n รับโปรไฟล์ \n   %.10f\n ติดต่อผู้ติดต่อ \n   %.10f\n ในกลุ่ม \n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} วินาที".format(str(elapsed_time)))




                        elif cmd == "sidere on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "เปิดระบบอ่านแบบแท็กอัตโนมัติ\n\nวันที่ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sidere off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "ปิดระบบการอ่านแบบแท็ก\n\nวันที่ "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "ระบบถูกปิดไว้อยู่")


#======================================การตั้งระบบ================================================================================================================================================================================#


                        elif cmd == '@@':
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Alin \n'
                                cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                cl.sendMessage(to, "จำนวนที่สั่งแท็ค {} คน".format(str(len(nama))))

                        elif cmd.startswith("วันเกิด: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"⚔คนติดบอท⚔ \n\n"+"วันเดือนปีเกิด  "+lahir+"\nอายุ "+usia+"\nราศี "+zodiak)

                        elif cmd.startswith("ตั้งรันแท็ก: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendText(msg.to,"คุณได้ตั้งค่าการรันแท็ก " +strnum)

                        elif cmd.startswith("ตั้งเชิญโทร: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"ได้ตั้งค่าการเชิญโทรกลุ่ม จำนวน  " +strnum)

                        elif cmd.startswith("รันแท็ก "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"จำกัดแค่ 1000")
                                        
                        elif cmd == "เชิญโทร":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "เชิญสำเร็จแล้ว {} เชิญกลุ่มการโทร".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"จำนวนเงินเกินขีด จำกัด")



#============================================================================ระบบป้องกัน By.⚔คนติดบอท⚔======================================================================================================================================#


                        elif 'ทักทาย ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ทักทาย ','')
                              if spl == 'เปิด':
                                  if msg.to in welcome:
                                       msgs = "ยินดีต้อนรับสู่ข่าวสารที่ใช้งานอยู่"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบทักทายคนเข้า\nของกลุ่ม " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบทักทายคนเข้าออก\nของกลุ่ม  " +str(ginfo.name)
                                    else:
                                         msgs = "ข่าวสารเกี่ยวกับการต้อนรับไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

                        elif 'ป้องกันลิ้งค์ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันลิ้งค์ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectqr:
                                       msgs = "ป้องกัน URL ที่ใช้งานอยู่"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบป้องกันการเปิดQR \nของกลุ่ม  " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันการเปิด QR\nของกลุ่ม " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกัน URL ไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

                        elif 'ป้องกันการเตะ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันการเตะ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectkick:
                                       msgs = "ป้องกันการลบเปิดอยู่"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบป้องกันการลบ\n ของกลุ่ม  " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันการลบ \nของกลุ่ม " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันการเตะไม่ทำงานf"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

                        elif 'ป้องกันการเข้า ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันการเข้า ','')
                              if spl == 'เปิด':
                                  if msg.to in protectjoin:
                                       msgs = "การป้องกันการเข้าร่วมมีการใช้งานอยู่"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบป้องกันการเข้าร่วม \nของกลุ่ม" +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันการเข้า \n ของกลุ่ม " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันการเข้าไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

                        elif 'ป้องกันการเชิญ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันการเชิญ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectinvite:
                                       msgs = "ป้องกันคำเชิญมีการใช้งานอยู่"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบป้องกันการเชิญ \n ของกลุ่ม " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันการเชิญ\n ของกลุ่ม " +str(ginfo.name)
                                    else:
                                         msgs = "ระบบป้องกันการเชิญไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

                        elif 'ป้องกันการยก ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันการยก ','')
                              if spl == 'เปิด':
                                  if msg.to in protectcancel:
                                       msgs = "ป้องกันการยกเลิกเปิดใช้งานอยู่ในกลุ่มนี้"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดป้องกันการยกเลิกค้างเชิญ \n ของกลุ่ม  " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันการยกเลิก\n ของกลุ่ม " +str(ginfo.name)
                                    else:
                                         msgs = "ระบบป้องกันการยกเลิกค้างเชิญไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

                        elif 'ป้องกันบอทลบ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันบอทลบ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectantijs:
                                       msgs = "เปิดระบบป้องกันบอทลบอยุ่"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบป้องกันบอทลบ \nของกลุ่ม " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องบอทลบ \nของกลุ่ม  " +str(ginfo.name)
                                    else:
                                         msgs = "ระบบป้องกันบอทลบไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                                    
                        elif 'ผี ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ผี ','')
                              if spl == 'เปิด':
                                  if msg.to in ghost:
                                       msgs = "ระบบการเข้าของคลิ้กผีเปิดอยู่"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "เปิดระบบการเข้าคลิ้กนอก \n ของกลุ่ม " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบการเข้าของคลิ้กนอก\nของกลุ่ม  " +str(ginfo.name)
                                    else:
                                         msgs = "ระบบคลิ้กนอกไม่ทำงาน"
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)                                    

                        elif 'ระบบป้องกันทั้งหมด ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ระบบป้องกันทั้งหมด ','')
                              if spl == 'เปิด':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "เปิดระบบป้องกันทั้งหมด \nของกลุ่ม " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "เปิดระบบป้องกันทั้งหมด \nของกลุ่ม " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันทั้งหมด \nของกลุ่ม " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ปิดระบบป้องกันทั้งหมด \nของกลุ่ม " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "⚔คนติดบอท⚔\n" + msgs)

#================================================ระบบเตะคน By.⚔คนติดบอท⚔==============================================================================================================================================#


                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("kickalls " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#====================================================ระบบเพิ่มแอดมินและบช ดำ by.⚔คนติดบอท⚔===============================================================================================================================#
                        elif 'ตั้งระบบออก ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งระบบออก ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไม่สามารถตั้งข้อความคนออกได้")
                              else:
                                  wait["leave"] = spl
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความทักคนออกตามนี้ \n\n {}".format(str(spl)))                                    

                        elif ("ตั้งแอด " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"เพิ่มแอดมินเรียบร้อย")
                                       except:
                                           pass

                        elif ("เพิ่มแอด " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"เพิ่มแอดมินเรียบร้อย")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"เพิ่ม bot เรียบร้อยแล้ว")
                                       except:
                                           pass

                        elif ("ลบรายการแอด " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"ลบออกจากรายการแอดมินเรียบร้อย")
                                       except:
                                           pass

                        elif ("ลบแอดมิน " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"ลบออกจากแอดมินเรียบร้อย")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"ลบออกจากรายการบอท")
                                       except:
                                           pass

                        elif cmd == "เพิ่มแอดมินบอท1" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"กรุณาส่งคอนแทค")

                        elif cmd == "ลบคนคุมบอทออก1" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"กรุณาส่งคอนแทค")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"กรุณาส่งคอนแทค")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kกรุณาส่งคอนแทค")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"กรุณาส่งคอนแทค")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"กรุณาส่งคอนแทค")

                        elif cmd == "หยุดการเพิ่ม1" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"รีเฟรชระบบการเพิ่มแอดสำเร็จแล้ว")

                        elif cmd == "คทแอดมิน" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "คทแอด" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "คทบอท" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#==================================================ส่วนการเปิดปิดระบบ By.⚔คนติดบอท⚔=====================================================================#

                        elif cmd == "เตะแท็ก เปิด" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"เปิดระบบการแท็กเตะ")

                        elif cmd == "เตะแท็ก ปิด" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"ปิดระบบการแท็กเตะ")

                        elif cmd == "เช็คคท เปิด" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"เปิดระบบการเช็คคท")

                        elif cmd == "เช็คคท ปิด" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"ปิดระบบการเช็คคท")

                        elif cmd == "แท็ก เปิด" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"เปิดระบบแท็กมีข้อความ")

                        elif cmd == "แท็ก ปิด" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"ปิดระบบแท็กมีข้อความ")

                        elif cmd == "เข้าออโต้ เปิด" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"เปิดระบบการเข้าออโต้")

                        elif cmd == "เข้าออโต้ ปิด" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"ปิดระบบการเข้าร่ามออโต้")

                        elif cmd == "ออกแชท เปิด" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"เปิดระบบการออกจากเชิยรวม")

                        elif cmd == "ออกแชท ปิด" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"ปิดระบบการออกจากแชทรวม")

                        elif cmd == "ออโต้แอด เปิด" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"เปิดระบบการแอดกลับออโต้&ข้อความ")

                        elif cmd == "ออโต้แอด ปิด" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"ปิดระบบการแอดกลับออโต้&ข้อความ")

                        elif cmd == "เช็คติ้ก เปิด" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"เปิดระบบการเช็ค ID ติ้กเกอร์")

                        elif cmd == "เช็คติ้ก ปิด" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"ปิดระบบการเช็ค ID ติ้กเกอร์")

                        elif cmd == "ตั๋ว เปิด" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"เข้าร่วมตั๋วที่เปิดใช้งาน")

                        elif cmd == "ตั๋ว ปิด" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"เข้าร่วมตั๋วที่ปิดใช้งาน")

#====================================ส่วนระบบยัดดำขาว By.⚔คนติดบอท⚔==============================================================================================================================================================#

                        elif ("ดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"เพิ่มบัญชีดำสำเร็จแล้ว")
                                       except:
                                           pass

                        elif ("ขาว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"ลบบัญชีดำสำเร็จแล้ว")
                                       except:
                                           pass

                        elif cmd == "เพิ่มดำ" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"กรุณาส่งคท")

                        elif cmd == "เพิ่มขาว" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"กรุณาส่งคท")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"เพิ่มบัญชีดำสำเร็จแล้ว")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"ลบบัญชีดำสำเร็จแล้ว")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"กรุณาส่งคท")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"กรุณาส่งคท")

                        elif cmd == "banlist" or text.lower() == 'เช็คบชดำ':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"ไม่มีบชดำ")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"รายการดำ\n\n"+ma+"\nรายการบช ดำทั้งหมด" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"ไม่มี")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Talkban User\n\n"+ma+"\nTotal Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "คทดำ" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                    cl.sendMessage(msg.to,"ไม่มีรายการดำ")
                              else:
                                    ma = ""
                                    for i in wait["Talkblacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "คทดำ1" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"ไม่มีบชดำ")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban1':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "ล้างดำ" % len(ragets)
                              cl.sendMessage(msg.to,"ล้างดำ " +mc)

#=========================================================ส่วนระบบตั้งค่าข้อความทั้งหมด By.⚔คนติดบอท⚔=================================================================================================================================#

                        elif 'ตั้งข้อความแอด ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งข้อความแอด ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไม่สามารถเปลี่ยนข้อความได้")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \nคุณได้ตั้งข้อความตอนมีคนแอดตามนี้ \n\n{} ".format(str(spl)))

                        elif 'ตั้งคนเข้า ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งคนเข้า ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไม่สามารถตั้งข้อความคนเข้าได้")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความทักคนเข้าตามนี้ \n\n {}".format(str(spl)))

                        elif 'ตั้งแท็ก ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งแท็ก ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไม่สามารถตั้งข้อความคนแท็กได้")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อคงามที่คุณตั้งตอนคนแท็กตามนี้ \n\n {}".format(str(spl)))

                        elif 'ตั้งสแปม ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งสแปม ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไม่สามารถตั้งข้อความได้")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความสแปมที่คุณตั้งตามนี้ \n\n {} ".format(str(spl)))

                        elif 'ตั้งอ่าน ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งอ่าน ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไม่สามารถตั้งข้อความได้")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ถูกตั้ง ตอนเช็คคนอ่าน ตามนี้ \n\n {} ".format(str(spl)))

                        elif text.lower() == "เช็คข้อความแอด":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ตั้งไว้  \n\n" + str(wait["message"]) + " ")

                        elif text.lower() == "เช็คทักเข้า":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ตั้งไว้  \n\n " + str(wait["welcome"]) + " ")

                        elif text.lower() == "เช็คแท็ก":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ตั้งไว้  \n\n " + str(wait["Respontag"]) + " ")

                        elif text.lower() == "เช็คสแปม":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ตั้งไว้  \n\n " + str(Setmain["ARmessage1"]) + " ")

                        elif text.lower() == "เช็คการอ่าน":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ตั้งไว้  \n\n " + str(wait["mention"]) + " ")

                        elif text.lower() == "ไวรัส":
                            if msg._from in admin:
                               cl.sendContact(to, "u1f41296217e740650e0448b96851a3e2',") 
                        elif text.lower() == "เช็คทักออก":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "⚔คนติดบอท⚔ \n ข้อความที่ตั้งไว้  \n\n " + str(wait["leave"]) + " ")   
#========================================ส่วนระบบการเข้าลิ้งค์ By.Sai==================================================================================================================================================#

                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = kc4.findGroupByTicket(ticket_id)
                                     kc4.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     kc4.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = kc5.findGroupByTicket(ticket_id)
                                     kc5.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     kc5.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group6 = kc6.findGroupByTicket(ticket_id)
                                     kc6.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kc6.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group7 = kc7.findGroupByTicket(ticket_id)
                                     kc7.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc7.sendMessage(msg.to, "Masuk : %s" % str(group.name))
						             group8 = kc8.findGroupByTicket(ticket_id)
                                     kc8.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kc8.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group9 = kc9.findGroupByTicket(ticket_id)
                                     kc9.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc9.sendMessage(msg.to, "Masuk : %s" % str(group.name))
						
    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
