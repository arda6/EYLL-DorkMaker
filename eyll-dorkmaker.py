from colorama import Fore , init
print(Fore.LIGHTWHITE_EX+"""


'########:::'#######::'########::'##:::'##:'##::::'##::::'###::::'##:::'##:'########:'########::
 ##.... ##:'##.... ##: ##.... ##: ##::'##:: ###::'###:::'## ##::: ##::'##:: ##.....:: ##.... ##:
 ##:::: ##: ##:::: ##: ##:::: ##: ##:'##::: ####'####::'##:. ##:: ##:'##::: ##::::::: ##:::: ##:
 ##:::: ##: ##:::: ##: ########:: #####:::: ## ### ##:'##:::. ##: #####:::: ######::: ########::
 ##:::: ##: ##:::: ##: ##.. ##::: ##. ##::: ##. #: ##: #########: ##. ##::: ##...:::: ##.. ##:::
 ##:::: ##: ##:::: ##: ##::. ##:: ##:. ##:: ##:.:: ##: ##.... ##: ##:. ##:: ##::::::: ##::. ##::
 ########::. #######:: ##:::. ##: ##::. ##: ##:::: ##: ##:::: ##: ##::. ##: ########: ##:::. ##:
........::::.......:::..:::::..::..::::..::..:::::..::..:::::..::..::::..::........::..:::::..::

                                                                cσdєd вч єчll'
""")
site = str(input("ѕítє uzαntıѕı : "))
print("ѕítє uzαntıѕı " + site + " σlαrαk αчαrlαndı.")
inurl = str(input("í̇nurl gírín (ѕql ínj. kullαnmαk í̇çín ѕσnunα $íd= єklєчín   \n ( $ = dєgíşkєn ) :  "))
print("ínurl dєgєrí " + inurl + " σlαrαk αчαrlαndı. ")
intitle = str(input("ѕítє í̇çí αrαmα kєlímєѕí (íntítlє) : "))
print("íntítlє dєğєrí  " + intitle + " σlαrαk αчαrlαndı. ")

soru = str(input("dσrkunuzα íntєхt єklєmєk íѕtєr míѕíníz ? E/h : "))
if soru == 'e':
    intext = str(input("íntєхt dєğєrí gírín : "))
    print("íntєхt dєğєrí " + intext + " σlαrαk αчαrlαndı. ")
    print("")
    print("+-----cσdєd вч єчll'-----+")
    print("")
    print("site:" + site + " " "inurl:" + inurl + " " "intitle:" + intitle + " " "intext:" + intext + "")
    print("")
    print("dσrk hαzırlαndı .")
elif soru == 'h':
    print("")
    print("+-----cσdєd вч єчll'-----+")
    print("")
    print("site:"+site+" " "inurl:"+inurl+ " " "intitle:"+intitle+ "")
    print("")
    print("dσrk hαzırlαndı .")
