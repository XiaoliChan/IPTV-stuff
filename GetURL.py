import json, argparse, sys, os, textwrap

def SortResult(sourceFile, outFile, urlType):
    f = open(sourceFile, 'r')
    f2 = open(outFile, 'w')
    f2.write('#EXTM3U name="CMCC IPTV"' + '\n')
    f2.close()
    urlDict = json.loads(f.read())
    channelList = urlDict['channels']
    for channelDict in channelList:
        for channelDictKey,channelDictValue in channelDict.items():
            if channelDictKey == 'params':
                subChannelDict = channelDict[channelDictKey]
                urlResult = SortIPTVSubChannel(subChannelDict,urlType=urlType)
                if urlResult != 'none' and channelDict['subTitle'] !='' :
                    writeResult(outFile,subTitle=channelDict['subTitle'],urlResult=urlResult,channelDict=channelDict)
    f.close()

def SortIPTVSubChannel(subChannelDict,urlType):
    url = ''
    if subChannelDict[urlType] != '' :
        url = subChannelDict[urlType]
    else:
        url = 'none'
    return url

def writeResult(outFile,subTitle,urlResult,channelDict):
    f2 = open(outFile, 'a')
    subTitle = '#EXTINF:-1,' + channelDict['subTitle']
    f2.write(subTitle + '\n')
    f2.write('http://192.168.1.1:8888/rtp/' + urlResult.strip('rtp://|udp://') + '\n')
    f2.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help = True, description = "This is a script use to convert CMCC-IPTV official live sources "
                                    "format to udpxy format. \n"
                                    "Example: python3 GetURL.py -f getAllChannel.json -t zteurl -o iptv.m3u",
                                    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-f', '--file', action='store', help='Specify IPTV-sources file.')
    parser.add_argument('-t', '--type', action='store', help='Specify IPTV channel, hwurl is for HUAWEI url, zteurl is for ZTE url')
    parser.add_argument('-o', '--outfile', action='store', help='Specify output file name you want to save.')

    if len(sys.argv) == 1:
        print(parser.print_help())
        sys.exit(1)

    options = parser.parse_args()

    if os.path.exists(options.file) == False:
        print("[-] File not existed, maybe you got a typo!")
    elif options.type not in ['hwurl','zteurl']:
        print("[-] Wrong type!")
    else:
        SortResult(sourceFile=options.file, urlType=options.type, outFile=options.outfile)
        print("[+] Convert finished!")

