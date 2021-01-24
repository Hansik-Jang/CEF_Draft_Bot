import discord
import asyncio
import time
import random
import os
from discord.ext import commands
from discord.utils import get

MAX_COUNT = 20
DELETE_AMOUNT = 2
BOT_SLEEP_TIME = 2

bot = commands.Bot(command_prefix='%')

f = open("key.txt", 'r')
key = f.readline()

dice = 0
pin = 0
switch = 0
check = 0
entry = [""]
queue = []
st = []
lw = []
rw = []
cam = []
cm = []
cdm = []
lb = []
cb = []
rb = []
gk = []
wait_st = []
wait_lw = []
wait_rw = []
wait_cam = []
wait_cm = []
wait_cdm = []
wait_lb = []
wait_cb = []
wait_rb = []
wait_gk = []
a_team = []
b_team = []
c_team = []
d_team = []
wait_mem = [""]
wait_temp = []
form = [""]

@bot.event
async def on_ready():
    print('로그인 중')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("'%도움말' | 드래프트봇")
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title="CEF 봇 도움말", description="CEF 봇 명령어 간단 모음집", color=0xff0000)
    embed.add_field(name="모음", value="`도움말`, `도움말2`", inline=False)
    embed.add_field(name="대기실", value="`대기초기화`, `특정번호삭제`, `대기참가`, `대기삭제`, `대기목록`", inline=True)

    embed.add_field(name="분배", value="`사다리`, `드래프트2`, `드래프트4`, `주사위`, `포지션뽑기`", inline=True)
    embed.add_field(name="기타", value="`!clear`, `포메이션`", inline=False)
    embed.set_footer(text="상세 명령어 보는 법 : %명령어 모음, %명령어 대기실, %명령어 분배, %명령어 기타")
    embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")
    await ctx.message.delete()
    await ctx.send(embed=embed)

@bot.command()
async def 명령어(ctx, *, text):
    if text == '모음':
        embed = discord.Embed(title='명령어 모음', discription="", color=0xFF007F)
        embed.add_field(name="%도움말", value="CEF 드래프트봇의 명령어를 출력합니다.", inline=False)
        embed.add_field(name="%도움말2", value="CEF 매니저봇의 명령어를 출력합니다.\n(해당 봇은 아직 제작 및 테스트 과정입니다.)", inline=False)
        embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")
        await ctx.message.delete()
        await ctx.send(embed=embed)
    elif text == '대기실':
        embed = discord.Embed(title='대기실 관련 명령어', discription="", color=0xFF007F)
        embed.add_field(name="%대기초기화", value="대기목록을 초기화합니다.", inline=False)
        embed.add_field(name="%특정번호삭제 숫자", value="현재 대기목록 중 특정 번호의 대기열을 삭제합니다.(스태프 전용)", inline=False)
        embed.add_field(name="%대기참가 포지션", value="대기목록에 포지션으로 참가합니다.(포지션은 명확하게 문자로 작성할 것)", inline=False)
        embed.add_field(name="%대기삭제", value="대기목록에서 본인의 이름과 번호를 삭제합니다.", inline=False)
        embed.add_field(name="%대기목록", value="현재 대기목록을 보여줍니다.", inline=False)
        embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")
        await ctx.message.delete()
        await ctx.send(embed=embed)
    elif text == '분배':
        embed = discord.Embed(title='인원 분배 관련 명령어', discription="", color=0xFF007F)
        embed.add_field(name="%사다리", value="이모지 o을 클릭한 인원들을 포지션 구분 없이 2팀으로 나눕니다.", inline=False)
        embed.add_field(name="%드래프트2", value="이모지 포지션을 선택한 것을 기준으로 2팀으로 분배합니다.\n주의사항 - 첫번째로 선택한 이모지를 기준으로 분배하며, 선택 후에는 수정 및 취소가 불가능합니다.", inline=False)
        embed.add_field(name="%드래프트4", value="이모지 포지션을 선택한 것을 기준으로 4팀으로 분배합니다.\n주의사항 - 첫번째로 선택한 이모지를 기준으로 분배하며, 선택 후에는 수정 및 취소가 불가능합니다.", inline=False)
        embed.add_field(name="%주사위 숫자", value="0부터 입력한 숫자까지의 범위 중 랜덤한 숫자를 출력합니다.(반드시 숫자로 입력)", inline=False)
        embed.add_field(name="포지션뽑기 포지션", value="이모지 o를 클릭한 인원들의 이름으로 자동으로 주사위를 출력합니다.", inline=False)
        embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")
        await ctx.message.delete()
        await ctx.send(embed=embed)
    elif text == '기타':
        embed = discord.Embed(title='기타 기능의 명령어', discription="", color=0xFF007F)
        embed.add_field(name="!clear 숫자", value="현재 채널에서 최근 메시지를 숫자만큼 삭제합니다.", inline=False)
        embed.add_field(name="%포메이션", value="피파21 내 포메이션 중 랜덤하게 하나를 출력합니다.", inline=False)
        embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")
        await ctx.message.delete()
        await ctx.send(embed=embed)

@bot.command()
async def dice(ctx):
    await ctx.send(ctx.author.display_name + "  /  " + str(random.randrange(1, 7)))


@bot.command(pass_context=True)
async def 대기초기화(ctx):
    if str(ctx.message.channel) != "대기순서":
        await ctx.send("대기순서 채널에 작성해주세요")
        time.sleep(BOT_SLEEP_TIME)
        #await ctx.channel.purge(limit=DELETE_AMOUNT)
    else:
        wait_mem.clear()
        wait_mem.append("")
        await ctx.send(ctx.author.mention + "님이 경기 대기실을 초기화하였습니다.")
        time.sleep(BOT_SLEEP_TIME)
        #await ctx.channel.purge(limit=DELETE_AMOUNT)


@bot.command()
@commands.has_role("스태프")
async def 번호삭제(ctx, *, text):
    role_names = [role.name for role in ctx.author.roles]
    if '스태프' in role_names:
        del_wait = ""
        in_num = int(text)
        try:
            if text == 0:
                await ctx.send("0번은 제거할 수 없습니다.")
                time.sleep(BOT_SLEEP_TIME)
                #await ctx.channel.purge(limit=DELETE_AMOUNT)
            else:
                del_wait = wait_mem[in_num]
                del wait_mem[in_num]
                await ctx.send(ctx.author.display_name + " 님이 " + del_wait + "님을 대기열에서 삭제하였습니다.")
                time.sleep(BOT_SLEEP_TIME)
                #await ctx.channel.purge(limit=DELETE_AMOUNT)
        except:
            await ctx.send("정확한 번호를 입력해주세요")
    else:
        await ctx.send("대기순서 채널에 작성해주세요")


@bot.command()
async def 대기참가(ctx, *, text):
    if str(ctx.message.channel) != "대기순서":
        await ctx.send("대기순서 채널에 작성해주세요")
        time.sleep(BOT_SLEEP_TIME)
        await ctx.channel.purge(limit=DELETE_AMOUNT)
    else:
        try:
            for i in range(0, len(wait_mem)):
                if ctx.author.display_name in wait_mem[i]:
                    check_overlap = 1
                    break
                else:
                    check_overlap = 0

            if check_overlap == 0:
                wait_mem.append(ctx.author.display_name + "/" + text)

                await ctx.send(content=f"{ctx.author.display_name}님\n"
                                       f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                time.sleep(BOT_SLEEP_TIME)
                #await ctx.channel.purge(limit=DELETE_AMOUNT)


            else:
                await ctx.send("중복 등록이므로 불가합니다.")
                time.sleep(BOT_SLEEP_TIME)
                #await ctx.channel.purge(limit=DELETE_AMOUNT)

        except:
            print("aaa")


@bot.command()
async def 대기삭제(ctx):
    if str(ctx.message.channel) != "대기순서":
        await ctx.send("대기순서 채널에 작성해주세요")
        time.sleep(BOT_SLEEP_TIME)
        await ctx.channel.purge(limit=DELETE_AMOUNT)
    else:
        try:
            for i in range(0, len(wait_mem)):
                if wait_mem[i].startswith(ctx.author.display_name):
                    wait_mem.remove(wait_mem[i])
                    await ctx.send(ctx.author.display_name + "삭제되었습니다")
                    time.sleep(BOT_SLEEP_TIME)
                    #await ctx.channel.purge(limit=DELETE_AMOUNT)
        except:
            await ctx.send(content=f"{ctx.author.display_name} 님은 대기열에 없습니다.")
            time.sleep(BOT_SLEEP_TIME+3)
            #await ctx.channel.purge(limit=DELETE_AMOUNT)


@bot.command()
async def 대기목록(ctx):
    alert = ""
    try:
        for i in range(1, len(wait_mem)):
            alert = alert + f"{i} . " + wait_mem[i] + "\n"

        if alert == "":
            await ctx.send("대기열이 존재하지 않습니다. 등록해주세요.")
        else:
            await ctx.send("대기목록 \n")
            await ctx.send("```" + alert + "```")
    except:
        await ctx.send("대기열에 아무도 없습니다.")



@bot.command()
async def 사다리(ctx, DRAFT_COUNT: int = 20):  # Comment 1 after the code
    ladder_agree = []
    ladder_team_a = []
    ladder_team_b = []

    ladder = await ctx.send("사다리 팀 분배에 참여하시겠습니까?")
    await ladder.add_reaction("⭕")

    guide_text = await ctx.send("카운트 : " + str(DRAFT_COUNT) + " 초")
    while DRAFT_COUNT >= 1:
        DRAFT_COUNT -= 1
        await guide_text.edit(content=f"카운트 : {DRAFT_COUNT} 초")
        await asyncio.sleep(1)

    await guide_text.edit(content="집계완료")
    ladder = await ctx.channel.fetch_message(ladder.id)
    ladder_agree = [u.mention for u in await ladder.reactions[0].users().flatten() if u != bot.user]

    # If only one person enters, there is no point in sorting
    # Check comment 2 and 3 after the code
    if len(ladder_agree) > 1:
        while len(ladder_agree) > 0:
            if len(ladder_agree) > 0:
                temp1 = random.choice(ladder_agree)
                ladder_team_a.append(temp1)
                ladder_agree.remove(temp1)

            if len(ladder_agree) > 0:
                temp2 = random.choice(ladder_agree)
                ladder_team_b.append(temp2)
                ladder_agree.remove(temp2)

        text = ""
        for i in range(0, len(ladder_team_a)):
            text = text + ladder_team_a[i] + ", "
        await ctx.send("\n\n A팀 : " + text)

        text2 = ""
        for i in range(0, len(ladder_team_b)):
            text2 = text2 + ladder_team_b[i] + ", "
        await ctx.send("\n\n B팀 : " + text2)
    else:
        await ctx.send("선택한 인원이 적습니다.")


@bot.command()
async def 포지션뽑기(ctx, *, text):
    pos_choose = []
    choose_time = 5
    mes = await ctx.send(content=f"'{text}'할 사람 뽑기")
    await mes.add_reaction("⭕")

    guide = await ctx.send("카운트 : " + str(choose_time) + " 초")
    while choose_time >= 1:
        await guide.edit(content=f"카운트 : {choose_time} 초")
        await asyncio.sleep(1)
        choose_time -= 1


    choose = await ctx.channel.fetch_message(mes.id)
    pos_choose = [u.mention for u in await choose.reactions[0].users().flatten() if u != bot.user]

    if len(pos_choose) == 1:
        await ctx.send(content=f"{text} 포지션 할 사람은 {pos_choose[0]}입니다.")
    elif len(pos_choose) == 0:
        await ctx.send("선택한 사람이 없습니다.")
    else:
        for i in range(0, len(pos_choose)):
            await ctx.send(content=f"{pos_choose[i]}의 주사위 : {random.randint(1,100)}")


@bot.command()
async def 주사위(ctx, *, num):
    dice = random.randint(0, int(num))
    await ctx.send(content=f"{ctx.author.mention} : {dice}")


@bot.command()
async def 포메이션(ctx):
    cd = await ctx.send("포메이션을 랜덤으로 뽑습니다")
    time.sleep(1)
    for i in range(0, 3):
        j = 3 - i
        await cd.edit(content=f"카운트다운 : {j}초")
        time.sleep(1)
        if j == 1:
            form = ["3-1-4-2", "3-4-1-2", "3-4-2-1", "3-4-3 다이아몬드", "3-4-3 플랫", "3-5-1-1", "3-5-2", "4-1-2-1-2 좁게", "4-1-2-1-2 넓게", "4-1-3-2",
                    "4-1-4-1", "4-2-2-2", "4-2-3-1 넓게", "4-2-3-1 좁게", "4-2-4", "4-3-1-2", "4-3-2-1",
                    "4-3-3 가짜 공격수", "4-3-3 공격", "4-3-3 수비", "4-3-3 홀딩", "4-3-3 플랫", "4-4-1-1 공격", "4-4-1-1% 미드필드",
                    "4-4-2 홀딩", "4-4-2 플랫", "4-5-1 공격", "4-5-1 플랫",
                    "5-2-1-2", "5-2-2-1", "5-3-2", "5-4-1 플랫", "5-4-1 다이아몬드"]
            sel_form = random.choice(form)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=f"선정된 포메이션 : {sel_form}")


#@bot.command()
#async def 삭제(ctx, limit):
#   await ctx.channel.purge(limit=limit)

@bot.command()
async def 드래프트2(ctx):
    #if str(ctx.message.channel) != "드래프트" or "대기순서":
        #await ctx.send("드래프트 채널에 작성해주세요")
    #else:
        switch = 0
        entry.clear()
        entry.append("")
        queue.clear()
        queue.append("")
        st.clear()
        lw.clear()
        rw.clear()
        cam.clear()
        cm.clear()
        cdm.clear()
        lb.clear()
        cb.clear()
        rb.clear()
        gk.clear()
        a_team.clear()
        b_team.clear()

        draft = await ctx.send("포지션을 선택해주세요")
        await draft.add_reaction("<:ST:706530008465932299>")
        await draft.add_reaction("<:LW:706530007937450036>")
        await draft.add_reaction("<:RW:706530008201560156>")
        await draft.add_reaction("<:CM:706530007928930386>")
        await draft.add_reaction("<:CDM:706530008289509466>")
        await draft.add_reaction("<:LB:706530008369463359>")
        await draft.add_reaction("<:CB:706530008113610803>")
        await draft.add_reaction("<:RB:706530008100765707>")
        await draft.add_reaction("<:GK:706530008088182786>")

        cd = await ctx.send("카운트 다운")
        for i in range(0, MAX_COUNT):
            j = MAX_COUNT - i
            await cd.edit(content=f"{j}초 남았습니다.")
            time.sleep(1)
            if j == 1:
                await cd.edit(content="선택 종료")
                for k in range(0, len(entry)):
                    if entry[k].startswith("ST"):
                        st.append(entry[k])
                    if entry[k].startswith("LW"):
                        lw.append(entry[k])
                    if entry[k].startswith("RW"):
                        rw.append(entry[k])
                    if entry[k].startswith("CM"):
                        cm.append(entry[k])
                    if entry[k].startswith("CDM"):
                        cdm.append(entry[k])
                    if entry[k].startswith("LB"):
                        lb.append(entry[k])
                    if entry[k].startswith("CB"):
                        cb.append(entry[k])
                    if entry[k].startswith("RB"):
                        rb.append(entry[k])
                    if entry[k].startswith("GK"):
                        gk.append(entry[k])

                # ST 선발 & 대기열 이동
                try:
                    temp = random.choice(st)
                    a_team.append(temp)
                    st.remove(temp)

                    temp = random.choice(st)
                    b_team.append(temp)
                    st.remove(temp)
                except:
                    print(a_team)

                # LW 선발
                try:
                    temp_lw = random.choice(lw)
                    b_team.append(temp_lw)
                    lw.remove(temp_lw)

                    temp_lw = random.choice(lw)
                    a_team.append(temp_lw)
                    lw.remove(temp_lw)
                except:
                    print(a_team)

                # RW 선발
                try:
                    temp_rw = random.choice(rw)
                    a_team.append(temp_rw)
                    rw.remove(temp_rw)

                    temp_rw = random.choice(rw)
                    b_team.append(temp_rw)
                    rw.remove(temp_rw)
                except:
                    print(a_team)

                # CM 선발 & 대기열 이동
                try:
                    for j in range(0, 2):
                        temp_cm = random.choice(cm)
                        b_team.append(temp_cm)
                        cm.remove(temp_cm)

                        temp_cm = random.choice(cm)
                        a_team.append(temp_cm)
                        cm.remove(temp_cm)
                except:
                    print(a_team)

                # CDM 선발
                try:
                    temp_cdm = random.choice(cdm)
                    a_team.append(temp_cdm)
                    cdm.remove(temp_cdm)

                    temp_cdm = random.choice(cdm)
                    b_team.append(temp_cdm)
                    cdm.remove(temp_cdm)
                except:
                    print(a_team)

                # LB 선발
                try:
                    temp_lb = random.choice(lb)
                    b_team.append(temp_lb)
                    lb.remove(temp_lb)

                    temp_lb = random.choice(lb)
                    a_team.append(temp_lb)
                    lb.remove(temp_lb)

                except:
                    print(a_team)

                # CB 선발
                try:
                    for i in range(0, 2):
                        temp_cb = random.choice(cb)
                        a_team.append(temp_cb)
                        cb.remove(temp_cb)

                        temp_cb = random.choice(cb)
                        b_team.append(temp_cb)
                        cb.remove(temp_cb)
                except:
                    print(a_team)

                # RB 선발
                try:
                    temp_rb = random.choice(rb)
                    b_team.append(temp_rb)
                    rb.remove(temp_rb)

                    temp_rb = random.choice(rb)
                    a_team.append(temp_rb)
                    rb.remove(temp_rb)
                except:
                    print(a_team)

                # GK 선발
                try:
                    temp_gk = random.choice(gk)
                    a_team.append(temp_gk)
                    gk.remove(temp_gk)

                    temp_gk = random.choice(gk)
                    b_team.append(temp_gk)
                    gk.remove(temp_gk)
                except:
                    print(a_team)

                # ST 대기열 정리
                for j in range(0, len(st)):
                    try:
                        queue.append(st[j])
                    except:
                        print(a_team)

                # LW 대기열 정리
                for j in range(0, len(lw)):
                    try:
                        queue.append(lw[j])
                    except:
                        print(a_team)

                # RW 대기열 정리
                for j in range(0, len(rw)):
                    try:
                        queue.append(rw[j])
                    except:
                        print(a_team)

                # CM 대기열 정리
                for j in range(0, len(cm)):
                    try:
                        queue.append(cm[j])
                    except:
                        print(a_team)

                # CDM 대기열 정리
                for j in range(0, len(cdm)):
                    try:
                        queue.append(cdm[j])
                    except:
                        print(a_team)

                # LB 대기열 정리
                for j in range(0, len(lb)):
                    try:
                        queue.append(lb[j])
                    except:
                        print(a_team)

                # CB 대기열 정리
                for j in range(0, len(cb)):
                    try:
                        queue.append(cb[j])
                    except:
                        print(a_team)

                # RB 대기열 정리
                for j in range(0, len(rb)):
                    try:
                        queue.append(rb[j])
                    except:
                        print(a_team)

                # GK 대기열 정리
                for j in range(0, len(gk)):
                    try:
                        queue.append(gk[j])
                    except:
                        print(a_team)

                # 내전 A팀
                temp_a_team = ""
                for j in range(0, len(a_team)+1):
                    try:
                        temp_a_team = temp_a_team + " " + a_team[j]
                        if a_team[j].startswith("ST"):
                            if a_team[j + 1].startswith("LW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LW"):
                            if a_team[j + 1].startswith("RW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RW"):
                            if a_team[j + 1].startswith("CM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CM"):
                            if a_team[j + 1].startswith("CDM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CDM"):
                            if a_team[j + 1].startswith("LB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LB"):
                            if a_team[j + 1].startswith("CB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CB"):
                            if a_team[j + 1].startswith("RB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RB"):
                            if a_team[j + 1].startswith("GK"):
                                temp_a_team = temp_a_team + "\n\n"
                    except:
                        print(temp_a_team)

                await ctx.send("팀 하양 명단 : \n" + temp_a_team)

                # 내전 B팀
                temp_b_team = ""
                for i in range(0, len(b_team)+1):
                    try:
                        temp_b_team = temp_b_team + " " + b_team[i]
                        if b_team[i].startswith("ST"):
                            if b_team[i + 1].startswith("LW"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("LW"):
                            if b_team[i + 1].startswith("RW"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("RW"):
                            if b_team[i + 1].startswith("CM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CM"):
                            if b_team[i + 1].startswith("CDM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CDM"):
                            if b_team[i + 1].startswith("LB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("LB"):
                            if b_team[i + 1].startswith("CB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CB"):
                            if b_team[i + 1].startswith("RB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("GK"):
                            if b_team[i + 1].startswith("RB", ""):
                                temp_b_team = temp_b_team + "\n\n"
                    except:
                        print(temp_b_team)

                await ctx.send("\n\n팀 빨강 명단 :  \n" + temp_b_team)

                temp_w_team = ""
                for i in range(0, len(queue)):
                    try:
                        if queue[i].startswith("ST"):
                            queue[i].replace("ST", "")
                            temp_w_team = temp_w_team + queue[i] + " ST\n"
                        if queue[i].startswith("LW"):
                            queue[i].replace("LW", "")
                            temp_w_team = temp_w_team + queue[i] + " LW\n"
                        if queue[i].startswith("RW"):
                            queue[i].replace("RW", "")
                            temp_w_team = temp_w_team + queue[i] + " RW\n"
                        if queue[i].startswith("CM"):
                            queue[i].replace("CM", "")
                            temp_w_team = temp_w_team + queue[i] + " CM\n"
                        if queue[i].startswith("CDM"):
                            queue[i].replace("CDM", "")
                            temp_w_team = temp_w_team + queue[i] + " CDM\n"
                        if queue[i].startswith("LB"):
                            queue[i].replace("LB", "")
                            temp_w_team = temp_w_team + queue[i] + " LB\n"
                        if queue[i].startswith("CB"):
                            queue[i].replace("CB", "")
                            temp_w_team = temp_w_team + queue[i] + " CB\n"
                        if queue[i].startswith("RB"):
                            queue[i].replace("RB", "")
                            temp_w_team = temp_w_team + queue[i] + " RB\n"
                        if queue[i].startswith("GK"):
                            queue[i].replace("GK", "")
                            temp_w_team = temp_w_team + queue[i] + " GK\n"
                    except:
                        pass

                await ctx.send("\n\n대기 \n" + temp_w_team)


@bot.command()
async def 드래프트4(ctx):
    #if str(ctx.message.channel) != "드래프트":
        #await ctx.send("드래프트 채널에 작성해주세요")
    #else:
        switch = 0
        entry.clear()
        entry.append("")
        queue.clear()
        queue.append("")
        st.clear()
        lw.clear()
        rw.clear()
        cam.clear()
        cm.clear()
        cdm.clear()
        lb.clear()
        cb.clear()
        rb.clear()
        gk.clear()
        a_team.clear()
        b_team.clear()
        c_team.clear()
        d_team.clear()

        draft = await ctx.send("포지션을 선택해주세요")
        await draft.add_reaction("<:ST:706530008465932299>")
        await draft.add_reaction("<:LW:706530007937450036>")
        await draft.add_reaction("<:RW:706530008201560156>")
        await draft.add_reaction("<:CM:706530007928930386>")
        await draft.add_reaction("<:CDM:706530008289509466>")
        await draft.add_reaction("<:LB:706530008369463359>")
        await draft.add_reaction("<:CB:706530008113610803>")
        await draft.add_reaction("<:RB:706530008100765707>")
        await draft.add_reaction("<:GK:706530008088182786>")

        cd = await ctx.send("카운트 다운")
        for i in range(0, MAX_COUNT):
            j = MAX_COUNT - i
            await cd.edit(content=f"{j}초 남았습니다.")
            time.sleep(1)
            if j == 1:
                await cd.edit(content="선택 종료")
                for k in range(0, len(entry)):
                    if entry[k].startswith("ST"):
                        st.append(entry[k])
                    if entry[k].startswith("LW"):
                        lw.append(entry[k])
                    if entry[k].startswith("RW"):
                        rw.append(entry[k])
                    if entry[k].startswith("CM"):
                        cm.append(entry[k])
                    if entry[k].startswith("CDM"):
                        cdm.append(entry[k])
                    if entry[k].startswith("LB"):
                        lb.append(entry[k])
                    if entry[k].startswith("CB"):
                        cb.append(entry[k])
                    if entry[k].startswith("RB"):
                        rb.append(entry[k])
                    if entry[k].startswith("GK"):
                        gk.append(entry[k])

                # ST 선발 & 대기열 이동
                try:
                    temp = random.choice(st)
                    a_team.append(temp)
                    st.remove(temp)

                    temp = random.choice(st)
                    b_team.append(temp)
                    st.remove(temp)

                    temp = random.choice(st)
                    c_team.append(temp)
                    st.remove(temp)

                    temp = random.choice(st)
                    d_team.append(temp)
                    st.remove(temp)
                except:
                    print(a_team)

                # LW 선발
                try:
                    temp_lw = random.choice(lw)
                    b_team.append(temp_lw)
                    lw.remove(temp_lw)

                    temp_lw = random.choice(lw)
                    c_team.append(temp_lw)
                    lw.remove(temp_lw)

                    temp_lw = random.choice(lw)
                    d_team.append(temp_lw)
                    lw.remove(temp_lw)

                    temp_lw = random.choice(lw)
                    a_team.append(temp_lw)
                    lw.remove(temp_lw)
                except:
                    print(a_team)

                # RW 선발
                try:
                    temp_rw = random.choice(rw)
                    c_team.append(temp_rw)
                    rw.remove(temp_rw)

                    temp_rw = random.choice(rw)
                    d_team.append(temp_rw)
                    rw.remove(temp_rw)

                    temp_rw = random.choice(rw)
                    b_team.append(temp_rw)
                    rw.remove(temp_rw)

                    temp_rw = random.choice(rw)
                    a_team.append(temp_rw)
                    rw.remove(temp_rw)
                except:
                    print(a_team)

                # CM 선발 & 대기열 이동
                try:
                    for j in range(0, 2):
                        temp_cm = random.choice(cm)
                        d_team.append(temp_cm)
                        cm.remove(temp_cm)

                        temp_cm = random.choice(cm)
                        a_team.append(temp_cm)
                        cm.remove(temp_cm)

                        temp_cm = random.choice(cm)
                        b_team.append(temp_cm)
                        cm.remove(temp_cm)

                        temp_cm = random.choice(cm)
                        c_team.append(temp_cm)
                        cm.remove(temp_cm)
                except:
                    print(a_team)

                # CDM 선발
                try:
                    temp_cdm = random.choice(cdm)
                    a_team.append(temp_cdm)
                    cdm.remove(temp_cdm)

                    temp_cdm = random.choice(cdm)
                    b_team.append(temp_cdm)
                    cdm.remove(temp_cdm)

                    temp_cdm = random.choice(cdm)
                    c_team.append(temp_cdm)
                    cdm.remove(temp_cdm)

                    temp_cdm = random.choice(cdm)
                    d_team.append(temp_cdm)
                    cdm.remove(temp_cdm)
                except:
                    print(a_team)

                # LB 선발
                try:
                    temp_lb = random.choice(lb)
                    b_team.append(temp_lb)
                    lb.remove(temp_lb)

                    temp_lb = random.choice(lb)
                    c_team.append(temp_lb)
                    lb.remove(temp_lb)

                    temp_lb = random.choice(lb)
                    a_team.append(temp_lb)
                    lb.remove(temp_lb)

                    temp_lb = random.choice(lb)
                    d_team.append(temp_lb)
                    lb.remove(temp_lb)

                except:
                    print(a_team)

                # CB 선발
                try:
                    for j in range(0, 2):
                        temp_cb = random.choice(cb)
                        c_team.append(temp_cb)
                        cb.remove(temp_cb)

                        temp_cb = random.choice(cb)
                        d_team.append(temp_cb)
                        cb.remove(temp_cb)

                        temp_cb = random.choice(cb)
                        a_team.append(temp_cb)
                        cb.remove(temp_cb)

                        temp_cb = random.choice(cb)
                        b_team.append(temp_cb)
                        cb.remove(temp_cb)
                except:
                    print(a_team)

                # RB 선발
                try:
                    temp_rb = random.choice(rb)
                    d_team.append(temp_rb)
                    rb.remove(temp_rb)

                    temp_rb = random.choice(rb)
                    a_team.append(temp_rb)
                    rb.remove(temp_rb)

                    temp_rb = random.choice(rb)
                    b_team.append(temp_rb)
                    rb.remove(temp_rb)

                    temp_rb = random.choice(rb)
                    c_team.append(temp_rb)
                    rb.remove(temp_rb)
                except:
                    print(a_team)

                # GK 선발
                try:
                    temp_gk = random.choice(gk)
                    a_team.append(temp_gk)
                    gk.remove(temp_gk)

                    temp_gk = random.choice(gk)
                    b_team.append(temp_gk)
                    gk.remove(temp_gk)

                    temp_gk = random.choice(gk)
                    c_team.append(temp_gk)
                    gk.remove(temp_gk)

                    temp_gk = random.choice(gk)
                    d_team.append(temp_gk)
                    gk.remove(temp_gk)
                except:
                    print(a_team)

                # ST 대기열 정리
                for j in range(0, len(st)):
                    try:
                        queue.append(st[j])
                    except:
                        print(a_team)

                # LW 대기열 정리
                for j in range(0, len(lw)):
                    try:
                        queue.append(lw[j])
                    except:
                        print(a_team)

                # RW 대기열 정리
                for j in range(0, len(rw)):
                    try:
                        queue.append(rw[j])
                    except:
                        print(a_team)

                # CM 대기열 정리
                for j in range(0, len(cm)):
                    try:
                        queue.append(cm[j])
                    except:
                        print(a_team)

                # CDM 대기열 정리
                for j in range(0, len(cdm)):
                    try:
                        queue.append(cdm[j])
                    except:
                        print(a_team)

                # LB 대기열 정리
                for j in range(0, len(lb)):
                    try:
                        queue.append(lb[j])
                    except:
                        print(a_team)

                # CB 대기열 정리
                for j in range(0, len(cb)):
                    try:
                        queue.append(cb[j])
                    except:
                        print(a_team)

                # RB 대기열 정리
                for j in range(0, len(rb)):
                    try:
                        queue.append(rb[j])
                    except:
                        print(a_team)

                # GK 대기열 정리
                for j in range(0, len(gk)):
                    try:
                        queue.append(gk[j])
                    except:
                        print(a_team)

                # 내전 A팀
                temp_a_team = ""
                for j in range(0, len(a_team)+1):
                    try:
                        temp_a_team = temp_a_team + " " + a_team[j]
                        if a_team[j].startswith("ST"):
                            if a_team[j + 1].startswith("LW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LW"):
                            if a_team[j + 1].startswith("RW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RW"):
                            if a_team[j + 1].startswith("CM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CM"):
                            if a_team[j + 1].startswith("CDM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CDM"):
                            if a_team[j + 1].startswith("LB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LB"):
                            if a_team[j + 1].startswith("CB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CB"):
                            if a_team[j + 1].startswith("RB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RB"):
                            if a_team[j + 1].startswith("GK"):
                                temp_a_team = temp_a_team + "\n\n"
                    except:
                        print(temp_a_team)

                await ctx.send("팀 하양 명단 : \n" + temp_a_team)

                # 내전 B팀
                temp_b_team = ""
                for i in range(0, len(b_team)+1):
                    try:
                        temp_b_team = temp_b_team + " " + b_team[i]
                        if b_team[i].startswith("ST"):
                            if b_team[i + 1].startswith("LW"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("LW"):
                            if b_team[i + 1].startswith("RW"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("RW"):
                            if b_team[i + 1].startswith("CM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CM"):
                            if b_team[i + 1].startswith("CDM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CDM"):
                            if b_team[i + 1].startswith("LB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("LB"):
                            if b_team[i + 1].startswith("CB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CB"):
                            if b_team[i + 1].startswith("RB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("RB"):
                            if b_team[i + 1].startswith("GK", ""):
                                temp_b_team = temp_b_team + "\n\n"
                    except:
                        print(temp_b_team)

                await ctx.send("\n\n팀 빨강 명단 :  \n" + temp_b_team)

                # 내전 C팀
                temp_c_team = ""
                for i in range(0, len(c_team)+1):
                    try:
                        temp_c_team = temp_c_team + " " + c_team[i]
                        if c_team[i].startswith("ST"):
                            if c_team[i + 1].startswith("LW"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("LW"):
                            if c_team[i + 1].startswith("RW"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("RW"):
                            if c_team[i + 1].startswith("CM"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("CM"):
                            if c_team[i + 1].startswith("CDM"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("CDM"):
                            if c_team[i + 1].startswith("LB"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("LB"):
                            if c_team[i + 1].startswith("CB"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("CB"):
                            if c_team[i + 1].startswith("RB"):
                                temp_c_team = temp_c_team + "\n\n"
                        if c_team[i].startswith("RB"):
                            if c_team[i + 1].startswith("GK", ""):
                                temp_c_team = temp_c_team + "\n\n"
                    except:
                        print(temp_c_team)

                await ctx.send("\n\n팀 노랑 명단 :  \n" + temp_c_team)

                # 내전 D팀
                temp_d_team = ""
                for i in range(0, len(d_team)+1):
                    try:
                        temp_d_team = temp_d_team + " " + d_team[i]
                        if d_team[i].startswith("ST"):
                            if d_team[i + 1].startswith("LW"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("LW"):
                            if d_team[i + 1].startswith("RW"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("RW"):
                            if d_team[i + 1].startswith("CM"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("CM"):
                            if d_team[i + 1].startswith("CDM"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("CDM"):
                            if d_team[i + 1].startswith("LB"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("LB"):
                            if d_team[i + 1].startswith("CB"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("CB"):
                            if d_team[i + 1].startswith("RB"):
                                temp_d_team = temp_d_team + "\n\n"
                        if d_team[i].startswith("RB"):
                            if d_team[i + 1].startswith("GK", ""):
                                temp_d_team = temp_d_team + "\n\n"
                    except:
                        print(temp_d_team)

                await ctx.send("\n\n팀 파랑"
                               ". 명단 :  \n" + temp_d_team)

                temp_w_team = ""
                for i in range(0, len(queue)):
                    try:
                        if queue[i].startswith("ST"):
                            queue[i].replace("ST", "")
                            temp_w_team = temp_w_team + queue[i] + " ST\n"
                        if queue[i].startswith("LW"):
                            queue[i].replace("LW", "")
                            temp_w_team = temp_w_team + queue[i] + " LW\n"
                        if queue[i].startswith("RW"):
                            queue[i].replace("RW", "")
                            temp_w_team = temp_w_team + queue[i] + " RW\n"
                        if queue[i].startswith("CM"):
                            queue[i].replace("CM", "")
                            temp_w_team = temp_w_team + queue[i] + " CM\n"
                        if queue[i].startswith("CDM"):
                            queue[i].replace("CDM", "")
                            temp_w_team = temp_w_team + queue[i] + " CDM\n"
                        if queue[i].startswith("LB"):
                            queue[i].replace("LB", "")
                            temp_w_team = temp_w_team + queue[i] + " LB\n"
                        if queue[i].startswith("CB"):
                            queue[i].replace("CB", "")
                            temp_w_team = temp_w_team + queue[i] + " CB\n"
                        if queue[i].startswith("RB"):
                            queue[i].replace("RB", "")
                            temp_w_team = temp_w_team + queue[i] + " RB\n"
                        if queue[i].startswith("GK"):
                            queue[i].replace("GK", "")
                            temp_w_team = temp_w_team + queue[i] + " GK\n"
                    except:
                        pass

                await ctx.send("\n\n대기 \n" + temp_w_team)

'''
@bot.command()
async def 대기실분배2(ctx, num1, num2):
    key = 0
    div = []
    wait_mem_name = []
    wait_mem_pos = []
    alert = ""

    for i in range(1, len(wait_mem)):
        split = wait_mem[i].split('/')
        wait_mem_name[i] = split[0]
        wait_mem_pos[i] = split[1]

        alert = alert + f"{i} . " + wait_mem[i] + "\n"

    await ctx.send("대기목록 \n")
    await ctx.send("```" + alert + "```")
    await ctx.send(content=f"닉네임 : {wait_mem_name}, 포지션 : {wait_mem_pos}")
    key = 1

    if key == 1:
        if num1 == num2:
            for j in range(0, len(wait_mem)-1):
                pass
'''



@bot.event
async def on_reaction_add(reaction, user):
    for i in range(0, len(entry)):
        if user.mention in entry[i]:
            switch = 1
            break
        else:
            switch = 0

    # 사다리타기
    if str(reaction.emoji) == "⭕":
        entry.append("⭕/" + user.mention)

    # 드래프트용
    if switch == 0:  # 스위치가 꺼져있으면
        if user.bot == 1:  # 봇이면 패스
            return None
        if str(reaction.emoji) == "<:ST:706530008465932299>":
            entry.append("ST/" + user.mention)
        if str(reaction.emoji) == "<:LW:706530007937450036>":
            entry.append("LW/" + user.mention)
        if str(reaction.emoji) == "<:RW:706530008201560156>":
            entry.append("RW/" + user.mention)
        if str(reaction.emoji) == "<:CM:706530007928930386>":
            entry.append("CM/" + user.mention)
        if str(reaction.emoji) == "<:CDM:706530008289509466>":
            entry.append("CDM/" + user.mention)
        if str(reaction.emoji) == "<:LB:706530008369463359>":
            entry.append("LB/" + user.mention)
        if str(reaction.emoji) == "<:CB:706530008113610803>":
            entry.append("CB/" + user.mention)
        if str(reaction.emoji) == "<:RB:706530008100765707>":
            entry.append("RB/" + user.mention)
        if str(reaction.emoji) == "<:GK:706530008088182786>":
            entry.append("GK/" + user.mention)


bot.run(key)
