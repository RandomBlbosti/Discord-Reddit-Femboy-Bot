import discord
import random
from discord.ext import commands
import redditeasy
import urlextract
import html

TOKEN = 'YOUR BOT TOKEN HERE'
bot = commands.Bot(command_prefix='f!')
bot.remove_command('help')
client_id = "YOUR REDDIT CLIENT ID HERE"
client_secret = "YOUR REDDIT SECRET HERE"


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
@commands.is_nsfw()
async def reddit(ctx, arg1: str = None):
    extractor = urlextract.URLExtract()
    reddits = ['feminineboys', 'femboy', "femboy_irl", 'boysinskirts']
    if arg1 is None:
        stopo = True
    else:
        stopo = False
        subreddit = str(arg1)
    if not stopo:
        if subreddit.lower() in reddits or subreddit.lower() == 'polska' or subreddit.lower() == 'polish'::
            if subreddit.lower() == "feminineboys":
                url = "https://styles.redditmedia.com/t5_2vmuo/styles/communityIcon_xt0odp2ips851.jpg?width=256&format=pjpg&s=57fde2ac04bda0c332a88ff433e63c0db6a49033"
            elif subreddit.lower() == "femboy":
                url = "https://styles.redditmedia.com/t5_2titd/styles/communityIcon_zos7vawff2721.PNG?width=256&s=32a55e4de4429ff45cfa9e7e03b07785b269d5f4"
            elif subreddit.lower() == "femboy_irl":
                url = "https://styles.redditmedia.com/t5_124gju/styles/communityIcon_6niwblo40p471.png?width=256&s=7eea38cdf172e2706b509f029849c07519a7c318"
            elif subreddit.lower() == "boysinskirts":
                url = "https://styles.redditmedia.com/t5_2yo2c3/styles/communityIcon_uhleghlsjnf51.png?width=256&s=526c6f47d0942c21e8ddccee8ed1b8d3661ac048"
            elif subreddit.lower() == "polska":
                url = "https://styles.redditmedia.com/t5_2qiqo/styles/communityIcon_3s04zinfgjr41.png?width=256&s=cac5a2cf4a3e18591ec0ea105670ad7f213beaf9"
            elif subreddit.lower() == "polish":
                url = "https://styles.redditmedia.com/t5_2rhyf/styles/communityIcon_jvkebngncnd31.png?width=256&s=6330aceac0d749e574be61b8e00c51a3e8d0afe0"
            red = redditeasy.Subreddit(client_id=client_id,
                                       client_secret=client_secret,
                                       user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61')
            randnum = random.randint(1, 30)
            if randnum <= 9:
                meme = red.get_post(subreddit=subreddit.lower())
            elif 9 < randnum <= 18:
                meme = red.get_new_post(subreddit=subreddit.lower())
            elif 18 < randnum <= 29:
                meme = red.get_top_post(subreddit=subreddit.lower())
            else:
                meme = red.get_controversial_post(subreddit=subreddit.lower())
            if "&" in str(meme.content):
                meme.content = html.unescape(str(meme.content).replace("amp;", ""))
            if "&" in str(meme.title):
                meme.title = html.unescape(str(meme.title).replace("amp;", ""))
            if meme.content is None:
                meme.content = ""
            if "{'mediaCount':" in str(meme.content):
                mediacount = int(str(meme.content)[:16][-1])
                links = extractor.find_urls(str(meme.content))
                fixedlinks = []
                desc = ""
                for i in range(mediacount):
                    fixedlinks.append(links[i])
                for i in fixedlinks:
                    desc += i + "\n"
                embed = discord.Embed(title=meme.title, url=meme.post_url, description=desc, color=0xEC6694)
                embed.set_image(url=fixedlinks[0])
                embed.set_thumbnail(url=url)
                if int(meme.score) >= 0:
                    embed.add_field(name="Upvotes", value=f"{meme.score}")
                else:
                    embed.add_field(name="Downvotes", value=f"{-meme.score}")
            elif extractor.find_urls(str(meme.content)):
                embed = discord.Embed(title=meme.title, url=meme.post_url, description=meme.content, color=0xEC6694)
                embed.set_image(url=str(extractor.find_urls(meme.content)[0]) if str(
                    extractor.find_urls(meme.content)[0]).startswith("https") or str(
                    extractor.find_urls(meme.content)[0]).startswith(
                    "http") else f'http://{extractor.find_urls(meme.content)[0]}')
                embed.set_thumbnail(url=url)
                if int(meme.score) >= 0:
                    embed.add_field(name="Upvotes", value=f"{meme.score}")
                else:
                    embed.add_field(name="Downvotes", value=f"{-meme.score}")
            else:
                embed = discord.Embed(title=meme.title, url=meme.post_url, description=meme.content, color=0xEC6694)
                embed.set_thumbnail(url=url)
                if int(meme.score) >= 0:
                    embed.add_field(name="Upvotes", value=f"{meme.score}")
                else:
                    embed.add_field(name="Downvotes", value=f"{-meme.score}")
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                "Femboy subreddit not recognised!")
    elif stopo:
        subreddit = random.choice(reddits)
        if subreddit.lower() == "feminineboys":
            url = "https://styles.redditmedia.com/t5_2vmuo/styles/communityIcon_xt0odp2ips851.jpg?width=256&format=pjpg&s=57fde2ac04bda0c332a88ff433e63c0db6a49033"
        elif subreddit.lower() == "femboy":
            url = "https://styles.redditmedia.com/t5_2titd/styles/communityIcon_zos7vawff2721.PNG?width=256&s=32a55e4de4429ff45cfa9e7e03b07785b269d5f4"
        elif subreddit.lower() == "femboy_irl":
            url = "https://styles.redditmedia.com/t5_124gju/styles/communityIcon_6niwblo40p471.png?width=256&s=7eea38cdf172e2706b509f029849c07519a7c318"
        elif subreddit.lower() == "boysinskirts":
            url = "https://styles.redditmedia.com/t5_2yo2c3/styles/communityIcon_uhleghlsjnf51.png?width=256&s=526c6f47d0942c21e8ddccee8ed1b8d3661ac048"
        red = redditeasy.Subreddit(client_id=client_id,
                                   client_secret=client_secret,
                                   user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                              'like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61')
        randnum = random.randint(1, 30)
        if randnum <= 9:
            meme = red.get_post(subreddit=subreddit.lower())
        elif 9 < randnum <= 18:
            meme = red.get_new_post(subreddit=subreddit.lower())
        elif 18 < randnum <= 29:
            meme = red.get_top_post(subreddit=subreddit.lower())
        else:
            meme = red.get_controversial_post(subreddit=subreddit.lower())
        if "&" in str(meme.content):
            meme.content = html.unescape(str(meme.content).replace("amp;", ""))
        if "&" in str(meme.title):
            meme.title = html.unescape(str(meme.title).replace("amp;", ""))
        if meme.content is None:
            meme.content = ""
        if "{'mediaCount':" in str(meme.content):
            mediacount = int(str(meme.content)[:16][-1])
            links = extractor.find_urls(str(meme.content))
            fixedlinks = []
            desc = ""
            for i in range(mediacount):
                fixedlinks.append(links[i])
            for i in fixedlinks:
                desc += i + "\n"
            embed = discord.Embed(title=meme.title, url=meme.post_url, description=desc, color=0xEC6694)
            embed.set_image(url=fixedlinks[0])
            embed.set_thumbnail(url=url)
            if int(meme.score) >= 0:
                embed.add_field(name="Upvotes", value=f"{meme.score}")
            else:
                embed.add_field(name="Downvotes", value=f"{-meme.score}")
        elif extractor.find_urls(str(meme.content)):
            embed = discord.Embed(title=meme.title, url=meme.post_url, description=meme.content, color=0xEC6694)
            embed.set_image(url=str(extractor.find_urls(meme.content)[0]) if str(
                extractor.find_urls(meme.content)[0]).startswith("https") or str(
                extractor.find_urls(meme.content)[0]).startswith(
                "http") else f'http://{extractor.find_urls(meme.content)[0]}')
            embed.set_thumbnail(url=url)
            if int(meme.score) >= 0:
                embed.add_field(name="Upvotes", value=f"{meme.score}")
            else:
                embed.add_field(name="Downvotes", value=f"{-meme.score}")
        else:
            embed = discord.Embed(title=meme.title, url=meme.post_url, description=meme.content, color=0xEC6694)
            embed.set_thumbnail(url=url)
            if int(meme.score) >= 0:
                embed.add_field(name="Upvotes", value=f"{meme.score}")
            else:
                embed.add_field(name="Downvotes", value=f"{-meme.score}")
        await ctx.send(embed=embed)


bot.run(TOKEN)
