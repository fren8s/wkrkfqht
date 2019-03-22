import discord
import asyncio
import random
import time
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='!명령어 3호기', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕, 나는 자갈봇, 이야!")

    if message.content.startswith('!따라해'):
        learn = message.content.replace('!따라해', "")
        await client.send_message(message.channel, learn + ':heart: ')

    if message.content.startswith('!핑'):
        before = time.monotonic()
        msg = await client.send_message(message.channel, '퐁!')
        ping = (time.monotonic() - before) * 1000
        text = "퐁!  {0}ms ".format((round(ping, 1)))
        await client.edit_message(msg, text)

    if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0]) + 1):
            dice += random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('!고양이'):

        embed = discord.Embed(title='고양이는',description='야옹~',colour=discord.Colour.green())

        urlBase = 'https://loremflickr.com/320/240?lock='

        randomNum = random.randrange(1, 30977)

        urlF = urlBase+str(randomNum)

        embed.set_image(url = urlF)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!강아지'):

        embed = discord.Embed(title='강아지는',description='월월월월',colour=discord.Colour.green())

        urlBase = 'https://loremflickr.com/320/240/dog?lock='

        randomNum = random.randrange(1, 30977)

        urlF = urlBase + str(randomNum)

        embed.set_image(url=urlF)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!뭐먹지?'):
        food = "치킨 햄버거 피자 고기 보쌈 족발"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!투표'):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, "★투표- " + vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```")
            await client.add_reaction(choose, '👍')
   
    if message.content.startswith('!골라'):
        choice = message.content.split(" ")
        choiecnumber =  random.randint(1, len(choice)-1)
        choiceruslt = choice[choiecnumber]
        await client.send_message(message.channel, choiceruslt)

    if message.content.startswith('!팀나누기'):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "-->" + teamname[i])

    if message.content.startswith('!서버'):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, '\n'.join(list))

    if message.content.startswith("!수"):
        content_list = message.content.split(" ")
        content_list = content_list[1:]
        for i in range(0, len(content_list)):
            content_list[i] = int(content_list[i])
        content_list = sorted(content_list)
        await client.send_message(message.channel, content_list[-2])

    if message.content.startswith('!게임'):
        food = "배틀그라운드 오버워치 마인크래프트 좀비고등학교 포트나이트 로블록스"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!메모장쓰기'):
        file = open("자갈봇메모장.txt", "w")
        file.write("오늘까지, 자갈이 괴롭히지 마셈!")
        file.close()

    if message.content.startswith('!메모장읽기'):
        file = open("자갈봇메모장.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith('!시간'):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await client.send_message(message.channel, str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 입니다.")

    if message.content.startswith('!제비뽑기'):

        channel = message.channel

        embed = discord.Embed(title='제비뽑기', description='각 번호별로 번호를 지정합니다.', colour=discord.Colour.blue())

        embed.set_footer(text='끝')

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]
        print(Text.strip())

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List:
                num = random.randrange(0, number)

            List.append(num)
            embed.add_field(name=str(i) + '번째', value=str(num), inline=True)

        print(List)
        await client.send_message(channel, embed=embed)

    if message.content.startswith('!정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(coler=0x00ffbb)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버이름", value=message.author.display_name, inline=True)
        embed.add_field(name="계정생성일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
