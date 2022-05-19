try:
        usera = open('tool/useragent.json',>
        printer(Panel(f'''{A2}{usera}''',ti>
        input('\n   %s[ %sKembali %s]'%(J,P>
        tampilan_menu()
    except Exception as e:kecuali(e)

###----------[ DUMP ID PUBLIC ]---------- #>
def publik():
    global file_dump
    try:
        try:
            token  = open('login/token.json>
            cookie = {'cookie':open('login/>
        except:
            print('\n%s[%s•%s] %sCookies In>
            time.sleep(3)
            login()
        print('       %s[%s•%s] %sContoh : >
        tid = input('       %s[%s•%s] %sID >
        file_dump = 'dump/%s.json'%(tid[0])
        try:os.remove(file_dump)
        except:pass
        for id in tid :
            try:
                url = ("https://graph.faceb>
                with requests.Session() as >
                    jso = json.loads(xyz.ge>
                    if len(gabung_sandi) !=>
                        for x in range(Post>
                            open(file_dump,>
                    else:
                        for d in jso["frien>
                            try:open(file_d>
                            except:continue
            except Exception as e:kecuali(e)
        jum = open(file_dump,'r').read().sp>
        print('       %s[%s•%s] %sBerhasil >
