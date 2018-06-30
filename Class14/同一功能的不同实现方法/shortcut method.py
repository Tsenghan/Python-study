'''请用已学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码，密码的埋藏点符合以下规律：
    a) 每位密码为单个小写字母
    b) 每位密码的左右两边均有且只有三个大写字母'''

def charinput():
    str_original = r'''ACFlCTLIQlAIVMTqHFkswqbDDHtpgcWaXSSglUYKE
lqNsYCyaQXBzrFUbkAUAWAKrDgDtAlGMBqWQhpEwquZqWZJpslUfMllCwWptqINjrOBTLuPzwvXNbLCx
oFRritKRpJgBOaGPZdkUzvYnvYmAlEsVmKRXqyQUOdCBqLYyboOYeAQNLnkuiDXCiNiksSSRpDMVQQgs
TmYThnppfKSmkpjjceGLaMOvYgsvNkGENKgGtUSzVPlLMeephDKrWGNpAxBqRiCnQIuKwDZurIRsznUp
xhstMWpHdZzqeEnttlAHiWbhbIJpwKBAGsFWthBiwBDKTFzIUamELZJFLbmqOmwBIYBJIofAUyxTLUEm
LcOXzjIHFcfUfEWccbWzhVuIZMdTVsOaNsLTpHjrvFaYTnJUrqaYnUmbobfOXXtkjKjFUEhVNlPWeaIY
uABNuEDKFWiUaqQiBHGsgEmDSKiJKLkkzFWlobXIyUlDzGcwDnEOwwWxgFpebsslmKItazIYctPROSJp
ImDHusQIkoFQSmuqwdcPNERvflfHtkGTrtbQXqZUsazoxmbVTPIuuxKvfALAaGnIuIZwczCcoIRMncBs
timFGHPJPaHMPTLjsBjIwbbzKyghaDTUStzJceaYAneywwpvdiUJifPHtXmAwZPChWsDmwonzeeQCEiB
xWsJLAtrdVEOBxEaYiSabHdUwlXlDOAKzZUwozJoBGvnFttDkXdYdjQSzzhTIPfYpWVFdiFIqSbyPZIi
VoXunBPbAJVMWluPcIfHmjPeHaTyClCvTOucEYEZXbVDiZMsfeuruDGMmQEsHutzvzVmWvCoPRguBiHh
taTeaguPmNuAxzYJLEcdoApfIFBaLUqettjTJNlHZYlJZRRoKXEvFnoUHdPjDuXuTAubGODkHAokpItw
SlEwhjrUSlfMawWlTMciWAzVcgPcqCHIaogokYAWGsvWZzBfJqzxIkCNvHDvBkOMCyeYXzVVuRJLQIOy
BMoVPgFLOagDxyPfWxTtZQNCLOrVVclPzMNYruNUyMOBKxBvinxuGMAAfndhPsROtkOJAAJQSxpmTzXm
CmEwZOhlItvETUneqvdKLghLyREjuJWRFjVVuNMiPuvvmRaEUmjCXDVuMRAvBuHUYGKPXthWISIbueRp
uvxpmqclmrXpAGFrxhJGxQwlrbkHEmcEUooCoPqGzbrCfIWmtUKmzzXvcqbhxKcAwXCNjbJDWDndKiLK
HwaFKyhXJQgHjIaTfIJrkhUpTHJZebRertDigQtDKxGerMRgHWFTrqqZlcBjAUfTZdFlZCAEZnhzgTIy
gJSsWJjFcCVoFonAfKPTOhTxjxTRtzSKLoIOScEwBCDvWFDVGpBOpijqdwvugoYsyuIOZJTcySDrzy
wBxediHOIYgasrUIDsNZcParqTGfTaBZHoSssXGtiCVvLReyoiitzMpsouqUeMHGWwDMgBaQTRkxPwNP
XsvyFVXfjgKuamMTsEsbeKDgAdVndyDleenPBcXWKGPcDsALDajkCEGufvbtyXUZnelqISbQnHphDoTH
RMIxMKclpWSvQHkzRhdAehBVaKYaXRPMpGaeRxvTRVFfewirvIDoGvYTAvKSoMFCLUNVFVKrYMeYtBrS
KgiBOjvliNOHLrmztypGhQjtpEQwzVfpVqsTUPvOCPzgqOuvLXJBQZHLmSwGTxEMgCAbogXombCiBDNX
BvGtXjrGWbWHtNCoRuqIZPhBQXZiNUhbmzOiyByAoMSBvusppiPVibIqmLXwXEVfcEAyNeUxaEZThULu
mkGmoLrpOEktwRluXvOmmfEWxZkxUNIqZKuzbaUmLKBYrXMmdOYLEzljzbSJnqRbSiAFyUNyyieKITkh
mvkKyosXKCaTsXQIKczJmxuqIEKeGGGwZyWTolQynlWngjDzFMlwhJFEmODeycbEfxgSRbIXySfwlhZZ
BUBhKyGBHRzWGRXAzarcmSDORvaOMOqYlcVIMwlHGtrLMhFWioqeKfvsJdTXmfQzavzSzCRrVzLFMaBT
DMOPFJcjzXcPvBkzacRmVKTQAvVobGRBypFHvoUdjvBhwWXVdDjvfJOocyIHbMqZGMaRaaFFnmtvTSkY
nIHbmPAtuEszMDFURBYxcOJXKMvJbfSbhiaacxhxiZBnoHTcFeqXQfjTqpcMKFpvvzkpSxlDxSlhikFZ
XSplcknpxiZfwUwGsrfpBUkevEiwndkKrVpWKufWpLTWXcyyXehOcDfnzgTAkhwOAcaiHqJWzsuAvMyD
pDJgeCdAJMwatRfcpKQGTkwxHracsYOlZeXoGthHIRfDBYzhuGEQRKFRnqSEbWDCJObWSAoSwFzVZEnI
rVBwXibUaTwnSTwRmIwkIgoGPRiOMLOTvnzEBBCfcugYZwGSsHRKCJoRsxxzRkKwnTRcRNfbMGssqmXV
IKYzyWHIsCjdzxiHEtvHaufVgcoqVkqIQertevTUTIVMYlNXCGEUzQowqsFpciURKoUwqCRogxeghOWs
cMnuAathgFvNIVqqXpmdJDJPhXQpZCyNbTYktMyTUtQEBeQBhEZzqHotmYREADhFodlcPmTMutBZyefW
sBmsnUbVnHUGAyaDirMoowBwXnzrmfHJgfpAquFoHTuvQvIJcjqiqVdntXbgwpVywbsKxqUMNxYVxBmQ
OAcxOAVPuJeOgABYEHhevhnUOgCUuTBAhJcUGsasbMInGCbHnHXWDdXijDRkUYFuOytTcMPtWklmTHTR
XFTfcFfSSqFUFbQVCKEjUOLveXtsHrIfkphXyDkRELnaTfuaZUClLqbdpWAREJHJpycYRDjElqlVeNya
kTCjDpvFrdnlXogrDZdQzAYaePDdfvHWdcaQGgrrHKBdMnMYbsikbkffVsITSUhEapmLGQYbHoiKGRcg
GPLeEvmCOAkGIuDBdnYPlzuUmLOfetGXpbTbPjjWCZiOJxlDazSbEPVpnNLDsLiwlgleiCdPezQwnNWT
ECLuRGpfJZlnZtcghLucmvlOZNwXaikbKGmoGZJIcsfNnmaHIcPXiEYDHjLKpVtNsqemAmaiTIzvLqlU
mlcvraikZozZwBoExUkELoiaAbTAkqDhrARHQyAvWvYUjthfWjZqbQNTnkgmySsORxGcxouYcyCSkjmC
fpTGOlFoXWLINurMZdQURRnZCiZqsEKeVVZdFMnaoUepdAdARtUuXTvkGzmpEVNZiYSWJAwkcSKgAWTD
mUNVxVebIiavuOAxWUBkuUkXCYtRoZhVNwCZGlaANNpBvXgSDeLURUdQnQteKAXbGlOLGYYYCzCGjzua
UmrdPYuRrUBvLFfwBGTiABTmpANdPCptqKwWXARMKrtmbggOBDgNkeHzNUCIXUIuOAavRbLTnzNNRgzL
boTJooLJIdVFbbjWNngnzPznJglCLEWqulqzSuAyvqYdivDqxEtYPKTwVheFmDidEOnLqjPHBcjoOVvt
MCDmQfwNxkOPuxiJqLQOPRAGJappmpikgmrvRAlKjFjTlaznQldBJmzSMDvCWghWOgfhfkHFZBNdbmMf
MsaQHrtJQvZuGFCrPVBNSNZBFZRdpmQNZYZXpkGjXRAXhELlxDfGhiXwgAUujQbqUCiKaRIYruNDRDlL
zInUkJBpySRZoqwQlqmoxADBjjtGjFPLTkcexYGwGYlANZQaXNgKkPXUUqlViVzxPxxtMQPqOxTcChCg
dvKNliVwzRfMmSsBFeuePnbmVqvyfdOXnZpUopEqfCMnnXpfZnNYwNKiZFPUWWmNCMibsyQEhiodVjTz
UxsicVsZNMXyvBLrdJxGGeCPEutNCzYBRamXwRlmVdqUTPnUoAWaVDshgTHZhvhVlLZsoqbyqOjJMPac
hHqiCKhgFkDUhUDSwsrEwaBrKhXINTjYmHvsTyFdRHliydbfQtRFZcsSTfcSfqyIgQuXLZnrdAwylBmW
BRbmVwdoNFcnoxMKHaYOhgihIsKitcrgEkfjIOKsDPOadFhMwVSKWeCfxxxfWjgNiGDaiYDtMhCgedOR
nTYoeVrpGsyDIsuKhffqaEqoqfWukaQlcUShYicuZAdoYVGvRchUgcmNwxQGogDvKhyAkIuqHCIXQfXp
CtkSSTXTugolUKfqSzugIOpyHhIlcTjDBTKPqcyaRhmgFdSBkYurnvnukNGVoxpZBFmwIEmehuaUcoeu
btkjJqKcAAqxgrKcoRGuqHVUHqKgEaqRCIXlaTqaUewJBEWnTnTJIDYdLeGUMDfndHPYTAGQbhxreADo
WZtdvbJVnNGRNvlAsqIPlpXSXEZGBdqVyNCCwylcXprVoGqnPXZioKnqbdrYlDhbsTVDJqRQKoPtQXzu
RnrGgCfYfeRRxiihjItxHurPwtYJoObDzlEABeIRxQocvWrJtyWchmZXJdYvTgicUircdiMKYAkNbdKu
gPpzXnTQIZxtIhvfBfjIHRaDXbYExxYBvrejpEaVHlinHlYRrhsbChnAwTKlQtHntqcqiXZwTUEdlsVy
WFdZNRfqzkhWzeKMGmkuKoSkuSZRkddsuBNFVMFLPeUkLwCCDKagNjMZwtHcVcEEKyjAYubHipuqNjaV
JukystpMZrhBgLqRVMpaIPsyAvYIsBDVqKNCMLqLwyhJhuWDdCPBgSzJTLkJvaGPirOFwfuMtkyXeKoZ
rGPRJqXyhdYNOXVSqGvbSPozAbjhpyfgGVuNUYaRQomzrTtzAMJnYnyvDnuBkbVvmYzhlhqmwgCZaGJG
GGRbaFdfnDlUfCfhpDWTkWfpUDuUksJvRFNxVYBKGoxBCdhmYZwyDPzWihcQXgByRbYxWZslVsbuTHTf
vaulICCTRkkiYuYoqFdzuxsqOBkzEJHbNXhSnHYxyeGoEklCeaUVEtjxmXyOEzcpsAhfKCTejxOxwGYh
eLtoPpPINviTCHUsgzSkycIxtvekMaoZkBIyLboyvMxxaqfviBxkSALNjiNYqGTypcZDvHonaVBZCSLp
SjRTsJmDuPwKnYwCdTprFvbXnrhARNToXpryIfEoIwSWIdfSKeOHDYwgyUvwXXpKUKQEiyZxCsTkAjME
hdxShAAUYJTkprXuFITxxJuKMiphRAyAeUFZgknMMLvUaSjiMlGmLARvTMpllxEQyfvEqkcONHVFcaTW
tqcbVrgeTLTGuJsrjZdYrrjtoLKcEfjkIhjzXgEkYhZggujFJuQlVtSqvuejtxAEqjgXrYjmwLkSRmXp
pkTfONxRyAxRYqJccLxuhabwMTWfwLTlzuVGJtVJOXxwKjFIZENpGHwRvTRitDBQBesRYATKhmWmmmbP
EXOzdBHNeghlqpjJFmzXyADNHQNEThWDyMsGsTmyFnywIPvDSIcxHbKQHgmJEcfsPzYvSYIbQjnTAgzF
UfZAbwfgCMRxtmZQQyayJFFhCSVeeUcQzSLWqhENNUpyLZaJsQsFQsPyFIjGtcmoJaFQGKTFtKUBdBBo
xECKHgYSMcBWnzRvPyihfjwyjhTTavfYqOrbrgZDSrwVYFjNsdxLJIigfMgythUoUIVSydOnfhAaesXZ
kfyDztQiBCMHjfEGLFllxfejLJjanZVRENsXhIxSWDgbvHHOAFtHzqdfquGbdQvOFlhDiWpxwEolxbep
fVfpKYGMNIQuOlmtTkNRDFTVMtVkEXYUDZKfEihbxXsSLGDcKSHSMXZxAturZVEQgismVAgMVVatqjBM
rXeHaGdccPJMlqhVAePDyEoIRTLCwJpkNTuOjEKEvXaAGhWmhWPHCBMVPkcPklbGIvzMzOFplRUsvZbE
vScmmoKktOUVOeKBcqVvoSsplqqssDvLiPqucbrxoNkodsbrZnvoDfyNGyUAURseEuJPUWsEiVCNcUNd
sxzoRVpEFuFloqWLumNVJITKXnWnOlGpCaQgTLJYizixXoxAHHbodRtPHBbnSzZRZOmlWKOQqvHWAhDh
cYBGRQsFwyesMILhiwjnvjeMIZnHYHYNrmOahjrVPuRgsxdfgUbKCZAVfcOizDeQLKiFQmQQUlDHnCQe
lMnlLSrtXhmGDqISCgElUrZXbXjGGkdWadBbxzVojGQwyhAbWMhSKFFwoIqJfIDdZjUdfCYFkpDdIuWe
aFIUFhnlsREthBRoaquSzBVVOPABfuAYZpoalZwNfZMPOptcoQYVUdRYlXuYChPAdRJgFgwPyTszSXIe
qHRtMxyNlPGoBfpjxHnNvwIADmJmquLgMQGtpJAyvflZjFwAgIymerCTnVkjvqPKFVRscOqAhqvCqCjw
BBojzXKIdphOVTFKhBpnIWYRfuqvQZgVMaqNBkYKzqGaEnBFKZukSLdPbXNmcZtMeykLwlLbZqaHayOb
IWZvbxEXXnaozCHeyiYMnWqIAwJxhMIPDsgySMKhdBYmdrGdbJOfJralshwvhWlmatTsylewdimJEzph
tuTzSGOkGDPPvltRVJPdHRPBTAsKWncfjjuHdlEVOeZIvVnUFHmyGTFDlMGVyAIdzLocbTXIHYTopIok
UHFAVjEXPlsMoKTriyGnfeTlVzvGhVZzUAWWPdZNdIxKioQylFMJZmSToyRGsDJKJXQxPkINvmoHCVUc
RIjImkWWxTnDLQiXdmHqQrWBuvguUUubGByTRnJfkNWxsSupcfIVgboDWzqYHEfAnIKCfdYUOslfXPax
YnaJfNLqJgcxRjBmRpOYgNpZOpzMOCVIRiiXdIqqFxPJhQqJadKiCesOsZoWGWbbQSVRZUlbNZdzeUTE
nhdMSCKCPbpWZguZHGkLiWCisjqnaLbJpbRFAHPjGbHOXKZQXoQQZohmVqjTcdWNhXEjPlLKnjpwbMPQ
ybzDvGgkybXtbDmjQuyOrMrcYGRGGfuuPXzieaetSBidnSRPsLaXKGcxDkXmHbqMWZJXsQkwtojlxOeU
KSIFdVvNEnOUmIZDdlnwtJcPBlcpRWNTazpzgItwJotSLWZruzrMlSGASMWDwOqTpeYYHaTHCCurPdwB
AWzUtwblZXNrBYdjUoDacvmRVURqOzUPlnFISsZMFPtthnDHSsFgkYfsMtXFuNPhLTleWVrmelyFaemo
bVIhEAxNwOUDQCOCDIBHsQlFxCbHErKiBsvQNjuIGnIzZiwoVTdUZnucSaKdHrxJeGQfTawFJefGJFFa
GHzELfnGBmkZyorbbDDwhvEVeIYIGLPMEuZduqFjbeWbVfzVIRZNXwPLgcYUsevuhEQXfYcJshYnJaWz
iqvlswEBRKNYEJidlzdWnQJpBtyjHYVpkQGzdYkeREqjhmmnUIbGZVnwwaMKqgXfURSICNxdteUSGhGZ
UEEFhWRoTKGRwFmPpZPOsalsrNOlkTdXqGKoWlWkqJvYYrtLiTfhdItMbbhdumSYgCcQVUARnYFWkCsC
jElZxrQHIlbTHFLOnrutlvyxzaSIdkJgeyMUnUmtXfnaIedbAInAuQssOQqBTLbvFRiqKqUSdUEmcRmN
LvAxlgliymfbjTwDSqNTLcAEIerzpUShNKkuehciEAYeGJOFFcOvurJFUyfZhQqzfaneiBcrPhaphSCB
StQiJvtoPhHcLUbriDUIfifVFnNtJfGlmcbQJSXsZfVjpbqnkMllUmHzLvEuSarSlNlNHsWvYlfhjMEA
epYTjoRGZeAAtURFeDfDxTYmOmONuQQBdcdncFGjhHmKlwqmUWoXuIXIxaaXnNThgPGtIlynrUIPLQTG
xXhattDrfBGbZRveKbgjzxJLdYREQlMeLtcIEUoyJocdAfUbymxuFLVjGkOQniiPParqoyQYfDYAQTkM
WLicLxpEFkBbwlKrTyYilKTtYkpVGxtOjYmcBDOrwFhFiGutmpTyTarUbVUeSevBTdaPDpjRkaEmLJMg
WsMhSGfIcBChcqrRKgKpjvGnFipjswgjetRtniMagakbCXAjpzWTtMlgZGCJwGyglpcLebrKWhgwJfWV
qGifWNEpCtjuejHoyVCdIxzMYGnfoslgTNAJdtVBWDVoGLzHSAVBTnhNIvAOExQNiJOIPPiHkdaRbfaP
ixDDoCDOOeAqvQJFxLWDICfGmufyxmaMshbvcrtjqqVtffZTnbtCOQfzRMGwOQEKaAmSWjnYdNgvdkmd
dQmaKZSdqKNrnvJlcyVMKuNWmuoOeyKecgjXbmSqnpjwJEaDYoehEklEgJyiksGxdEKgfYRXQecRZgfe
qKWGc'''
    return str_original
#程序开始
def char2list(str1=''):
    '输入str1为一个字符串，返回为一个经过筛选的列表'
    length = len(str1)
    letters = '' # 所有字母的列表
    for i in range(length):
        if str1[i].isalpha():
            # 已有的就统计数加一
            letters+=str1[i]
    return letters
char_list = char2list(charinput())#修剪字符串，只剩下字母
#奇技淫巧：如果密码是x，密码一定是‘aAAAxAAAa’的格式。
#密码初始化
password = ''
for i in range(len(char_list)):
    #如果第一个是小写字符
    if char_list[i].islower():
        #从该字母开始生成一个长度为9的sub字符串
        sub_list = char_list[i:i+9]
        #如果字符串长度满足要求（避免out of range）
        if len(sub_list) == 9:
            #判断字符串是否是 ：“小大大大小大大大小”
            if (sub_list[4].islower() and sub_list[-1].islower()) and ((sub_list[1:4].isupper())and (sub_list[5:8].isupper())) :
                #满足要求的字符串中，第五个就是密码。将中间的x附加到密码中。
                password+=sub_list[4]
print(password)