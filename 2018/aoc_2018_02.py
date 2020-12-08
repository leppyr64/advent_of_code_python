from string import ascii_lowercase

def find_count(s, n):
    for c in ascii_lowercase:
        cnt = 0
        for x in s:
            if x == c:
                cnt = cnt + 1
        if cnt == n:
            return(1)
    return(0)

def compare_two(a, b):
    ndiff = 0
    for i in range(26):
        if a[i] != b[i]:
            ndiff = ndiff + 1
    return (ndiff == 1)
            

txt = "umdryebvlapkozostecnihjexg,amdryebalapkozfstwcnrhjqxg,umdcyebvlapaozfstwcnihjqgg,ymdryrbvlapkozfstwcuihjqxg,umdrsebvlapkozxstwcnihjqig,umdryibvlapkohfstwcnfhjqxg,umdryebvqapkozfatwcnihjqxs,umzrpebvlapkozfshwcnihjqxg,fmhryebvlapkozfstwckihjqxg,umdryebvlahkozfstwcnizjrxg,qmdryebvlapkozfslwcnihgqxg,umdiyebjlapknzfstwcnihjqxg,umdryebvlapkoqfstwcaihvqxg,cmdryebvlapkpzfstwcnihjvxg,umdryebvlakkozfstwcgihjixg,umdryebvlasjozfstwcnihqqxg,umdryebvladkozfsvwcnifjqxg,umdrlebvlapaozfstwcniwjqxg,umdryebvlhpkozrstwsnihjqxg,umdryebvcapkozfqtwcnihjrxg,ubdrykbvlapkowfstwcnihjqxg,umdryebvldpkozfstwcnihtqsg,umdryebvlapaozyutwcnihjqxg,umdryibvlapkozfstdfnihjqxg,umdryebvlapgozkstwznihjqxg,umdrxebvlapkozfstwcngxjqxg,umdryekvlapkozfstwclchjqxg,nmdryebvlapkozjsewcnihjqxg,umdryebvyapkozfstfcniheqxg,umdfyebvlapkozfstwcnhhjpxg,umdryelylupkozfstwcnihjqxg,smdryebvlqpkozfstwcnihjdxg,umdryebvlapaozfsuwcnihjqxc,umdryebvlrzkozrstwcnihjqxg,umdbycbvlapkojfstwcnihjqxg,umdryebvlapkonfstwpnirjqxg,uecryebvlapkozfstwcnihpqxg,uqdryebvltpkozfstwcnihrqxg,umdryebvlqsknzfstwcnihjqxg,cmdryebvlapkocfstwcvihjqxg,umdrkebvlapkozqsfwcnihjqxg,umdryabveapkoifstwcnihjqxg,ummrnehvlapkozfstwcnihjqxg,umdryebvlxpkozfstwqnihjtxg,umdryebvlagkozastwcnihjqxh,umdryebvlatkozzhtwcnihjqxg,umdryebvlcpkozfstwrnihjqvg,umdryebvlapkozfsnwcnrhjcxg,umdzyebvlypkozfstwcnibjqxg,nmdryebvlvpkozbstwcnihjqxg,uwdryebvlipkozfstwcnihvqxg,umdraebvlavkozfstwcnihjqwg,umdeyebvlspbozfstwcnihjqxg,umdryxlvlapkozfstwcnihjqxu,umdryegvlapkqzfstwcnirjqxg,umdrupbvlapkozfstwcnihjqog,imxryebvlapkxzfstwcnihjqxg,umdrfebvlapkozowtwcnihjqxg,umdreebvlapkozmstwczihjqxg,undryebdlapkozbstwcnihjqxg,umdryebvlapkpzfetwcnihjqxb,ymdnyebvlapkozfstwinihjqxg,umdryebvaapkozfstwcnihyqqg,umdryebvlapkzzwsrwcnihjqxg,umdrkebvlapkmzfskwcnihjqxg,umdrmebvlapkozfsvwcnidjqxg,umdlyehvlapkozfstwcnihjqkg,umnryebvlrpkozfstwjnihjqxg,uqdryebvlapxozfsawcnihjqxg,vmdruebvlapkozfstwcnihjqqg,umdryabviapkozistwcnihjqxg,umdryebvlapkzzfstwfnihkqxg,uvdryebvlapkozfsxwcuihjqxg,umdlhebvlapkozfstwcnvhjqxg,umdreebvlapkopfstjcnihjqxg,umdryebvlazkomfstwynihjqxg,kmdryebulapkoznstwcnihjqxg,umdryebvxakkozfstwinihjqxg,ukdryobvlapkozistwcnihjqxg,umdryebveapkozfstwcnthjqgg,mmdrtebvlapcozfstwcnihjqxg,umdryebvlapkolistwnnihjqxg,umdryebxlapkozfatwcnihjqxx,uxdryebvlapkozfstwhniheqxg,ufdryebvzapkozfstwcnbhjqxg,amdryhbvlapkozfstwcnifjqxg,umqryebvlaphozfstwcnihjqxn,umdryebvlapkosfstfcnihjqxe,gmkryebvlapkozfstwcnihjmxg,umdrnebvlkpkozfstwcnihjnxg,umdryebvrapkozfstmcndhjqxg,umdryebvmapkozfstichihjqxg,umdryesvnapkozestwcnihjqxg,umeryhbvlapkozfstfcnihjqxg,umdryedvbapkozfstwcnihqqxg,umdryebllapzozfstwcnihjvxg,umdcyebvlzdkozfstwcnihjqxg,umdrybbvlapkbvfstwcnihjqxg,umdrytbglapkozfsthcnihjqxg,umdryebvlkpkozfsteclihjqxg,umdntebvlapkmzfstwcnihjqxg,lkdryebveapkozfstwcnihjqxg,ymdryubvlapkozfstwbnihjqxg,tmrryebvlapkozfstwcnqhjqxg,umdryeovlaekonfstwcnihjqxg,umiryeuvlapkozfstwcnihjwxg,umdryebvlspvozwstwcnihjqxg,umdrtebvlapkoznxtwcnihjqxg,umvryebvlaphozfstwcnahjqxg,umdryebvlapkozfstinniajqxg,umdryebqlapkozfctwcnihjqxx,umdryebvlapkbzfptwcnihjqvg,umdryabviapkozistwcnihjqxd,umdryrbvlapkezfstscnihjqxg,umhryebvlapkozfstacnihxqxg,umdxyelvlapkozfitwcnihjqxg,umdryevvuapkozfstwcnihtqxg,uydrypbvxapkozfstwcnihjqxg,umdryebvlapkopfstwcnihzqxo,uedryebvlapkozistwceihjqxg,umdiyebvlapkozfgtwcnihjqxv,ymdryebvlapkozfsticniqjqxg,umbrkebvlapkozfslwcnihjqxg,umdryebliapkozbstwcnihjqxg,umvryebolapkozfstwcnihjqig,umdryeavbackozfstwcnihjqxg,umdryfbvlapsozfstwcnihaqxg,umdqyebvlapkozfjtgcnihjqxg,umdrjebvlaqkozfstwcyihjqxg,umdryebklaqkozrstwcnihjqxg,umdryebvpapkozfstwcpihjqjg,uydryebhlawkozfstwcnihjqxg,umdyyebvlapkozfstwcykhjqxg,umdryebvlapkozfstwcnitjnxh,umdzyebvlapkozfstwcnehyqxg,mmcryebvlapkozfstwinihjqxg,umdryebvlapuozfstwmvihjqxg,umdryfbvlapkozqstwcnihjmxg,umdryebslapsozfhtwcnihjqxg,umdtyemvlapmozfstwcnihjqxg,umdrxevvlapkozfytwcnihjqxg,umdahebvlapjozfstwcnihjqxg,umdryebvlapkozfstacnivjqxb,umdryebvlzpkozfjtwcnihjyxg,umdryebvlaqkozfstwcnisjqxu,umdrydbvlapkozfsuwcnihjlxg,umdryebvlapkomrstwcnihjqkg,umdryebvlapcozfstmcnwhjqxg,umdryebvlahkozfstwcibhjqxg,gmdrzebvlapkozlstwcnihjqxg,umdryebvlapkezfsswcnrhjqxg,umdryebvlapkoqfitwcgihjqxg,umdrnebvlapkozfsiwcninjqxg,umdryebvlapkozfsrwckohjqxg,umdryebtlapkomfstwcnihjexg,umdryxbvlapjozfstwcnihoqxg,umdpyebvlapkosustwcnihjqxg,umdryebvlapkvzfawwcnihjqxg,umhnyebvlaikozfstwcnihjqxg,umdryebvlagkozfstvknihjqxg,uodryebjlapkoxfstwcnihjqxg,umdryefdlapkozfstwcnyhjqxg,umprmebvtapkozfstwcnihjqxg,umdhyebvlapoozfstwcnihjqgg,uddryebvidpkozfstwcnihjqxg,umdryebtlapkozfetwfnihjqxg,umdbyebolapkozfstwcoihjqxg,umdryebvlapkonfstwcnihjpxo,umdryebvlapkohfstwcnihjqwk,umdryebolalkkzfstwcnihjqxg,updryebvxapkozfstwcnshjqxg,umdryebvlapkovfktwcnuhjqxg,umdrqrbvlppkozfstwcnihjqxg,umdrylgvlapkozfstwrnihjqxg,umdryebvlapkozfstxcnihbqig,uvdryeevlappozfstwcnihjqxg,zmdryebvlapkozfstwcnihqqxt,umdryebvlapvozfstwenihiqxg,umdryebvlbpkozfsgwcnihjlxg,umdryhbvlapkozfstwcnihtqxw,umdreecvlapkozwstwcnihjqxg,umwryebvlapkoztsmwcnihjqxg,ukdryebvfapkozrstwcnihjqxg,umdrylbdlamkozfstwcnihjqxg,umdryebvlapoozwsmwcnihjqxg,umdryebvlapkozfqtwcnnzjqxg,umdryekvlapktzfstwcnohjqxg,umdryebvlapkozfstwcnihjwqo,umdrrebflapkogfstwcnihjqxg,umdryevvlapkozfztwctihjqxg,umdrybbvlapkozfstwcnihxaxg,umdryebvlapkozfsowcnphjqag,smdryebvlapbozfitwcnihjqxg,umdryebvtapiozfstwcnihjqxe,umdryebjlakkozfstwccihjqxg,umdryebvlapdozfshwckihjqxg,umnryebvlapiozfstwcnihlqxg,umdrycbvlapkjzfsnwcnihjqxg,umdryebvyaprozjstwcnihjqxg,ucdryebvlapkozfstwomihjqxg,umdryebvlagklzfstwcnihjqyg,umdryebvladkozfstwcnihjqjh,umdrwebvlapkozfstwdnicjqxg,umdryebvlapkmzfstwcniheqxr,umdryebvlapkjzfstwcviheqxg,umdrvebvlapkozfstwcbihjqmg,umdrfebvlapkoffstwcnihsqxg,umdryebvtarkazfstwcnihjqxg,umdryebvlapkozfstwcfihjcng,umdryebvlapkktostwcnihjqxg,uedryeevlapkozfstwcniijqxg,bmdryebylapkozfstwcnihjqog,umdryebvlmpkoztstwcnihjqeg,umdryepvlarkohfstwcnihjqxg,uwdryebvlapklzfstzcnihjqxg,umdryebklapkozfsswcbihjqxg,umdtyeavlapkozfstwsnihjqxg,umdryebvaapkozfhtfcnihjqxg,umdrpebvlapuozfstwvnihjqxg,umdryebvlapkozffmwcniijqxg,uqdpyebvlapkozfstwfnihjqxg,umdryebvlapuozdstwcnihjhxg,tmdryhbvlapkozfptwcnihjqxg,umdryevvmapkozfstwcnihjgxg,umdryeuvlapmozfstwcnihjwxg,umdryebqlzpkozfbtwcnihjqxg,umdryebvsapkozystwcniqjqxg,imdryebvlapkozfscwinihjqxg,umdryebvlzpkozustwcnmhjqxg,umdrypbvlapbozfsnwcnihjqxg,bmdryebvlapqoznstwcnihjqxg,umdrfebvlapaozfstwcnihxqxg,umdiyebvxapkozfstwcnchjqxg,umdrygbvlapkozfstwcnizjqxz,amdryedvlapkozfstwcnihfqxg,umdryebvvapzozfstwcnihjgxg,undryebvlapkzzfstjcnihjqxg,umdryvbvlapgozfrtwcnihjqxg,umdrkebvlapkozfstwcnihihxg,umdryebvrppkozfsowcnihjqxg,umdryebvlapktzfsdwclihjqxg,otdrdebvlapkozfstwcnihjqxg,mmdryebvlazkozfxtwcnihjqxg,umdryebvlapkozfsbwtnihjqxa,imqryebvrapkozfstwcnihjqxg,umdryebvlrpkozfscwcnihjqlg,uedryebvlapkoznsvwcnihjqxg,umdryebvlqpkozfstscnihjqxj,umerycbvlapkozfstwcnihjqxh,umdkykbvlapjozfstwcnihjqxg"
words = txt.split(",")

total_pair = 0
total_triple = 0
for s in words:
    total_pair += find_count(s, 2)
    total_triple += find_count(s, 3)
print(total_pair, total_triple)

for s1 in words:
    for s2 in words:
        if compare_two(s1, s2) == 1:
            print(s1, s2)