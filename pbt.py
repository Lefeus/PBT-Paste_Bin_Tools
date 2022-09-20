import urllib.request
import urllib.parse
import re
from fp.fp import FreeProxy # pip install free-proxy
import click
from pystyle import Colorate, Colors
#from functools import cache

from urllib.request import (build_opener, install_opener, ProxyHandler)
###############################################################################################################################################

dev_key = open("dev-key.txt", "r").read()


@click.group
def cli_commands():
    pass

@click.command()
@click.option("-c", "--code", prompt="[ REQUIRED ] Enter message that you would like to paste.", help="[ REQUIRED ] Enter message that you would like to paste on https://pastebin.com")
@click.option("-p", "--proxy", prompt="[ OPTIONAL ] Enter proxy. Format: [ username:password@host:port ]", help="[ OPTIONAL ] Enter proxy. Format: [ username:password@host:port ]")
def paste(code: str, proxy: str = FreeProxy(rand=True).get()):
    try:
        print(proxy)
        proxy_support = ProxyHandler(proxies={"http": f"{proxy}", "https": f"{proxy}"})
        opener = build_opener(proxy_support)
        install_opener(opener)
        try:
            ip = urllib.request.Request("https://httpbin.org/ip", method="GET")
            ipp = urllib.request.urlopen(ip)
            print(ipp.read().decode())
        except Exception as e:
            print(e)

        site = 'https://pastebin.com/api/api_post.php'
        our_data = urllib.parse.urlencode({"api_dev_key": dev_key, "api_option": "paste", "api_paste_code": code})
        our_data = our_data.encode()
        request = urllib.request.Request(site, method='POST')
        resp = urllib.request.urlopen(request, our_data)
        link = resp.read().decode(resp.headers.get_content_charset())
        rawlink = "https://pastebin.com/raw/" + link[-8:]
        click.echo(rawlink)
        return rawlink
    except Exception as e:
        print(f"Unable to paste. | Exception: {e}")

    

###############################################################################################################################################
@click.command()
@click.option("-u", "--url", prompt="[ REQUIRED ] Enter pastebin url", help="[ REQUIRED ] Enter pastebin url: example: https://pastebin.com/raw/49xfG82x")
def getlinks(url: str):
    alldata = urllib.request.urlopen(url)
    resp = alldata.read().decode(alldata.headers.get_content_charset())
    #print(resp)
    links = re.findall(r'(https?://[^\s]+)', resp)
    click.echo(links)
    return links

###############################################################################################################################################
@click.command()
@click.option("-u", "--url", prompt="[ REQUIRED ] Enter pastebin url", help="[ REQUIRED ] Enter pastebin url: example: https://pastebin.com/raw/49xfG82x")
def getcodewithoutlinks(url: str):
    alldata = urllib.request.urlopen(url=url)
    resp = alldata.read().decode(alldata.headers.get_content_charset())
    text = re.sub(r'http\S+', '', resp)
    click.echo(text)
    #print(text)
    return text








cli_commands.add_command(paste)
cli_commands.add_command(getcodewithoutlinks)
cli_commands.add_command(getlinks)


    # https://pastebin.com/raw/aMpiJJzx

    #print(paste(code="Welcome 1836 https://wieszakware.42web.io"))
    #print(get_code_without_links("https://pastebin.com/raw/aMpiJJzx"))
    #print(get_links("https://pastebin.com/raw/aMpiJJzx"))

if __name__ == "__main__":
    print(Colorate.Vertical(Colors.yellow_to_red, r"""
 ██▓███   ▄▄▄        ██████ ▄▄▄█████▓▓█████  ▄▄▄▄    ██▓ ███▄    █ ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██░  ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓█████▄ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▒██▒ ▄██▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██░█▀  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░▓█  ▀█▓░██░▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░▒▓███▀▒░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░▒░▒   ░  ▒ ░░ ░░   ░ ▒░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░░         ░   ▒   ░  ░  ░    ░         ░    ░    ░  ▒ ░   ░   ░ ░   ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
               ░  ░      ░              ░  ░ ░       ░           ░              ░ ░      ░ ░      ░  ░      ░  
                                                  ░                                                            
         """,1)
    )
    try:
        cli_commands()
    except:
        print(Colorate.Vertical(Colors.green_to_blue, """Please use CLI | pbt --help | Usage pbt [command] --help""", 1))