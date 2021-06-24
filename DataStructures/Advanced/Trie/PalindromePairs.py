"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/
https://leetcode.com/problems/palindrome-pairs/

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# TLE
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#
#         def is_palindrome(w: str) -> bool:
#             m = len(w)
#             m2 = m // 2
#             return w[:m2] == w[-1:m-m2-1:-1]
#
#         n = len(words)
#         result = []
#         for i in range(n):
#             for j in range(i+1, n):
#                 if is_palindrome(words[i] + words[j]):
#                     result.append([i, j])
#                 if is_palindrome(words[j] + words[i]):
#                     result.append([j, i])
#
#         return result

# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#
#         def is_palindrome(w: str) -> bool:
#             m = len(w)
#             i, j = 0, m-1
#             while i < j:
#                 if w[i] != w[j]:
#                     return False
#                 i += 1
#                 j -= 1
#             return True
#
#         n = len(words)
#         result = []
#         for i in range(n):
#             for j in range(i+1, n):
#                 if is_palindrome(words[i] + words[j]):
#                     result.append([i, j])
#                 if is_palindrome(words[j] + words[i]):
#                     result.append([j, i])
#
#         return result
from Common.ResultComparators import compareSets

# Runtime: 876 ms, faster than 39.23% of Python3 online submissions for Palindrome Pairs.
# Memory Usage: 21.4 MB, less than 7.29% of Python3 online submissions for Palindrome Pairs.
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.index = -1
        self.list = []

class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = TrieNode()
        result = []
        for i, w in enumerate(words):
            self.add_word(root, w, i)
        for i, w in enumerate(words):
            self.search(words, i, root, result)
        return result

    def add_word(self, root: TrieNode, w: str, i: int):
        m = len(w)
        for j in range(m-1, -1, -1):
            if self.is_palindrome(w, 0, j):
                root.list.append(i)
            root = root.nodes[w[j]]
        root.list.append(i)
        root.index = i

    def search(self, words: List[str], i: int, root: TrieNode, result: List[List[int]]):
        n = len(words[i])
        for j in range(n):
            if root.index >= 0 and root.index != i and self.is_palindrome(words[i], j, len(words[i])-1):
                result.append([i, root.index])
            root = root.nodes.get(words[i][j], None)
            if not root:
                return

        for j in root.list:
            if i == j:
                continue
            result.append([i, j])

    def is_palindrome(self, w, i, j):
        while i < j:
            if w[i] != w[j]:
                return False
            i += 1
            j -= 1
        return True


tests = [
    [["hdhbaggbjiagiihgidda","jj","ihdebgbhejebgehebda","fddhieigcggecjcjefga","eeabdhhchghj","hedeeggihjcddghhb","hjdihahibjbi","di","dafabiedacdafhd","dehjafibiab","hjdgjcjefibgjcejgfif","f","ebdh","gffgffgaahfibjajjai","ejfdejhggcbjegeccfaa","gdfbhcfi","gfejjbjiddjdgjaj","hedjecihdhhcgcgbcjd","jcgadfaj","adcbfjej","fiec","gbcgbgfdheb","bgcdi","dejfcjbbgh","d","gahfa","fhjiaeiadcchfjdfefci","afjcfhfeg","dighaidhgjjjefag","ccbia","ghbcdbcfgcjjjhbh","hiecjhgijb","idgbcgihc","ajcgieggcdfacjj","fddf","jcgihdgbgehjhga","feaeiddcgcigh","iffabaaafacjc","hbdgeiffcgjecfibec","bfcjdeicdjeadaadia","c","ifbgbddaaigabdhggg","gdcjeheigh","aeddjj","cihjhagbfbijgehcbiae","he","bedbbfejhdjjgb","hacggdbcbac","ggbhjibc","efjhgfdgciichb","ebejcbdagfcihbaecjba","idchei","gahibd","dhhighidddefe","feiedgaejdahi","ichbcbehfjcdch","hiebaie","ahj","hbijd","dideedcdgjeaidjeheji","eaehibaj","ec","da","iiffe","jehjcjajaabbga","hcjacedfddbc","gc","feibcdejchdjggb","fahcifbf","ghiccfcaaegjcbge","jfed","cdgfbbfbcg","iiffeidgiji","bfdfefhejbhdj","iijdjidhiibf","fjhigfdijbedbibgjh","hbid","iafd","fehfg","bffahbfcb","ddbhbhfe","edebciih","ejhehahghec","cbgdggcbe","chihjhbbbgc","eighcidiiaacff","gheb","jffffcebc","cbaidfhfachifhhebdc","cjhgaibbe","jgadieed","gbjigdbbfcjgjgcid","gbbjijhhhcgeg","cbegc","cbjcehjhjd","bjgaacja","cc","cfg","debbddhbejjc","dfiabccdcgabaehcbij","jhj","djdjihejhcdbd","jbcbijcjhaggf","cdhghj","fbfdgcffdfidadj","ejgicfjidbibeeb","fieadaggdfad","hgjceffcfifhaifa","aedhiic","ehfi","bciibegeedfhjhegcf","ahfijag","cjeaicfhjbbecici","ibigfeabacagi","bhidhiichcc","haaafceh","ee","edgeabaehgig","haijagdh","gcdabchaceiijjggeba","jeidbgdgddjjjdecf","jebbbjfhecdefdh","dggfadacjeghabcfda","ejjbbdgjh","ficfaajbcjg","dg","abjchgjie","ddjgbjihdbhhjg","gdhhb","bigghigaiidfhijcbha","addaegbagffcd","jaggabgdhfehffb","jhgdjiacegbebbhabgj","acacadjcee","cicjjeahajcjba","hedbiidifbfji","jegacjccebijb","acc","bicgfdbbei","gjbacjjhfc","agde","hefhdgafbiijc","ifidbahcfibbhicifde","ahgecfjdegaji","dh","jehefhdajbib","i","dgcafiacbefhafdddh","ddf","gafiijhgfhicfjcgjbe","fbggdhidjihbddjef","bcacddbcadggjeccjbb","igajgeggjdba","bbcfbbbdccdfaiibacf","eccfigfd","cdcjigich","abjfcfdfedae","ah","hggafcfhf","e","giaafgddcecahcebffj","dcdejidfbcdbjcc","jdjfdcaeeddffjedga","jhdehdhbdjdad","aechhcdjfg","ibifbdcbbaebdgd","fdfhiaajccaafaaaa","ifjah","hgcefhijjidbcad","caicgiijbjicbhbdcbd","cgcjijhafcbf","efjedigabfej","hegabbfd","bbghbghhdidccadicb","ccieeheg","dbacaciciaia","hjjehjfihhbbiaaf","ceh","ejj","ceaifiddjcfcfgi","geja","diadcadfgje","dihjdjiadcebb","bhe","aefddjbdihia","j","jbegdb","cegbiajhcefcdghj","gjaggcggfad","fcbfa","dfjfjieg","gdfgefheiacee","dfhhfehcjddbhdb","ccehihj","ea","aighfdfhhabjh","dfch","cbahdjgbciigdhi","bdbfceahjc","gj","dhhghgeb","eigachdgdg","fihe","dfjcedadbebidcbh","ddbeeeaf","ai","jiagfbijgdjja","ajjjgbfbcgc","aciiijaajcbf","gjbefcbgijbibjaac","cfjceibacdafhaieebae","bjabfeecbedd","hih","eaaejeeghfaeffg","ffhebgbggj","idhffih","jjjaccgdceiahacii","ddgdhjdbeahdaieefa","ghfhgccaadi","cbehdihh","cdeghijecfaajhcdcci","dibfdbabeeegg","igbahgaefaeajgfe","cchdgaj","iiefb","cifdihdijhhagjjce","ehdchh","adfhcfjfbaeb","dhdidgffbejch","eaaehdabjigd","geaccgbcihhfdidhf","ahdbhfbibhccii","addcaah","gihiiaie","aaiihaac","bchbcihigai","cdhjhbaccidcfgaadjif","ieibcf","ehdeeahjjgj","gb","if","bhaiejjffggbida","fajefdhiaaec","fcjcffjd","dbchefhjii","baeiafjgdehaeafbh","iijcgabgjc","cgcggajbbaeiac","gdahfdihifdbidgfhgf","dfehdbgdf","acadjgceghej","bihbhc","behihifdi","iaifdbiiebj","gdigad","bcbgagaifiejggfff","jjafaffebeida","ccbdaagdfh","aghibjgbbfe","gcjgaidadbdgaba","beahaaifcadfiafciecc","jiadiiajiicfjad","ahg","hijgcbjjcgjebge","dgddahbjdbafjefgifei","dajicahia","ffeifh","bgcgcabibhdjgdfda","gdjgie","jdjhhf","jdhabgifidjfbhagijff","adiac","ceedhbec","ef","dhdcgjgehcjeibfbjgd","fhjhaffbachd","dehfiaficbgdb","gabbehaeafc","fjbhhhbfbgfagaafh","h","jicabbheahfahjice","dec","dbchh","gah","iahfgjgaae","hiec","bgjjgdjfcfbidfdcfedj","bhjbjjdjcjghacicjdha","bheadcgfcjjfaefdighg","adebfajbaajbjibjdf","fghbafa","fcgciiidgaejfhddae","ifgajgijgcheefdfecai","jadfg","ihhiigbied","ejaajbcfjifaahhdbeh","dhdjcifhgidfgbddg","bifhfffjfhffdgfc","eg","fcjida","cgjbjeb","jcffhdaaecgiej","ehgehia","eddfiiied","ijbabagbbdhgdiagacbh","gjejfeci","jbcegdigafcbcajhe","cifgcbjfeaajdj","bbcaifeihhai","fbdbfbfegijjca","ifgeaegejjhchagf","bajegjjbiga","ghcccjcgdijfgdg","jdgjjdeehjhddd","cjbigd","bjdi","hiejf","bjfihieehj","jiecbehjbijaeibaihc","a","djb","dicecbifcicabgdcdag","affccaccgjbaffa","cjfbchejebjddbbdb","fjijfh","add","dbja","gcbjcgedibbhfi","ggdahfejagjbc","cjfcidfehjghg","aiiiajadcggfhgebccej","cdfjbe","dee","dafdcjaifee","abbjcheigdghiddfja","ifbha","aei","bhhahheeajhifcaijc","gaiidgcfijid","aagbhgcgechgaddbc","afiaiejfchhb","aciaadijfagaa","ihfe","eggcjiiabe","hjacbfjb","igggcgdbjaeihjfc","eiaehgjffjfj","agffa","ijbfjddedhhbcf","ccijhhafd","eabifhcafbbij","cgei","hffebjhhjfeafcdh","fhiiaffhfbe","dcbigc","hfadegfaai","aa","ggaibddbehe","ifa","hfcfcidiafdejfehad","befbfea","fa","jhfeadiffchia","cegfaigfcjhiie","hcc","ibhabeijie","jdchabdgbhhdiej","jbhhdfeahbedea","bbgfeidbjibfihddjdbj","eb","ahfbbag","ddhgbbegfjbdhfgifac","ejc","dgdafhbajegdfff","iehfjigaihc","giheghdgebffied","fhj","agcbhd","hcehigehgcggggb","hbaggfdeejfjebe","bfhdffgd","hf","edcjic","jhcg","dhbg","fiabgdcfdgadbcebgaag","hgcjhhiahijeichaeb","dj","ehfic","edajgfiaahfef","hdagfb","diecgcjdjchhd","agdfdicecdchjjifdfg","ifejadagaj","ccdaed","jdgbhijed","defbdddgijfffbcbae","bbecfbc","fchjhcedjbjjjchehjhg","agfhccgchffghdi","fgjjidfgjdg","gfjcbagigfdgddjhcf","babehhihcdhcfeajdch","fhggdccfg","hfafhjbehabjfddbj","eccfj","fjbdhgbcfjjbhegbbgbc","defgeijgacbdigi","bjajhehi","fdahjdcedajgfgjdaiai","hfh","bhffedgfigcaacjfeh","dhcdajfcgiechjc","ghacadjgaeecdccjjgc","cbhccbhfdgfh","ceacfgggebhjfa","ejhhi","fbffdc","gejdhdjdajdabdidjjjd","idffja","gdagd","bjgbfaad","gebdeibichiga","iefbdeaeeeagjfedab","ehbahhbd","gcg","ccafeifdji","cjfdhffcbiagigg","bi","geedcccd","eeebfhjbjcbdb","gebicd","iib","gijf","hedjj","aiajggchjh","cdahfcfcfb","defj","hihabhc","hachfabdbgfci","ejcecfced","ffeeifaiedcjffab","gfibgfegd","djfhcgafdddahg","dbddfbbedghcgb","hiecfjbdeb","ddcdfeahgcacegd","jd","hbihhhcdafgeeeh","gcbbgf","cghfgdcg","efhgbefdcagdfhi","jgahjfhfbbg","hjgdebfdfajb","icggjahgjaaiihbibg","hiheaf","jbeachabddj","iafgejhahhjejg","gfjb","hdgachcbbadjgcdgacge","hejjihigaadagajhag","dhh","ghcd","fgadjjigfiiafhd","ieeffhgichbgaa","bcaibhi","ehiheh","dbgiiehdjigadfaficg","afgabgdffch","ijgeaaiajchcbagid","hif","hgfjjbifcefjdagada","ajdjficegcb","hiij","feh","deec","bcjcecd","habbegd","dahfeeajiafcccgbcadj","dcaedg","edcaejj","hbegdcfcfhicihfi","fag","cabiegcbeigaj","ebhegggcggijbhehga","dfda","ehdcjecedij","bhbfcede","agg","jibbjcadihhcija","bebcfbjfgcaciccfgb","eafecf","djcgc","ehf","ibiggadjieia","iigjdda","hgjceajhebigjfcbcc","bjicijidjcgjdjdfc","hdi","dccgbhajjchb","eadgaahiifg","ffffabigiifigghcggea","bgdaefiahjcihai","jfcfccbaiihcebdgb","cgffigeddgejac","cdjffbffheijdi","gjdgbaacbdbd","ajaeaiceejjbfhfb","jcjeeade","ieafjffagacdcacadi","geeab","ahhefiabc","egajjgjcfcjh","b","cdhedbfbciicbdj","bhafcige","gfcijgdihjce","ghhgbejgejgghbhjebj","jfiaiiafdda","beciabaifhfjgaaghjjh","fbgccdie","eadigbeh","adfaedgaehdaifg","jegbgbaf","gafag","jghajhdbjd","cdedd","ihh","cchjfhhfcahffca","caea","bgdgcejgcdaeicie","efbgihdghjh","ggcaghhe","cggc","ebjihibhbbfjd","afeechgej","dgeidej","fcfjhjc","jdcfgeihabjebi","g","ifg","dehbe","idjaaeibg","hiecgdiiefggfibcddgh","jcaeccbbjdcd","aegbbijaebfc","fdjjc","eggeifjahhdbghgaca","gegaiadicebfcfdj","dbjbhfhgefjgaihbiedf","hbgheibafbhhe","bcjdieidijibjeiae","bjj","bbibhh","addefejeh","feede","edij","fjaacehcbccdgccef","hajhggagbffigbe","fjcj","afddfdciefjifihbdgia","aedhieaiadifdahfc","eadigbdi","afdj","cgbchibiaijif","cjhf","cddjgcajcjdadfd","bbheggdidg","cbgbcjgfjhfgjdeicca","dgibdjbacaefdhggbhfj","acjjgffcfhedifaagc","icaaffdgfcfdieghdbih","bcjfh","cbfhh","hhgjib","icbcjj","efjggdeddhhg","hgjabedfedg","jhibhcbah","ieafgiecaheiifegdic","edcdheghaidd","igje","haihhjjbagede","haehddhdaig","gddadbefij","dcjdb","eea","ic","fjefjdgcagiiabdifb","gfgfg","ceacjehccacgcbfghe","dibbhd","bjcdj","iia","hgbgjcijb","ihf","jhhfffegihfacehai","cffgjaa","ceeebhacacbiiijcfejc","ddefcgadghf","jeaadficdg","fjefacceddhiaehg","hbjc","jaifabhifaefdjafd","faiacagccjegbff","hfehf","igdce","cgff","gjfjfiaiaffbe","aijajdffiiijchehi","fjii","iajbiia","hgiibjaeijfg","jaabiacbfigcjiij","gce","igaac","cjcbhiaehccd","hdadfegeccahcgjba","ggigfhidi","fgebd","gjhbdegiihbddc","jhgheicejjc","egbagabbcifi","cgegg","gbbdeghahdid","bffdgchjadi","dfcgdbifidjjagaj","behffbehhcfjeiehied","gbadbceedcbjcfg","djajhffhifjdhjaieij","edheja","jggejigihifehjfah","adhfffdjadciidghejdg","hihbcgjechagebfjfdje","idedg","dbehgeidgd","jabjf","hdedejcfgiebeebc","bdbajdhdhb","bbbgbhbifabgbijgg","gaaehhhdi","jbjieciababffjageibc","eaeaijehdbfaaddcad","fbda","dfifa","idiajbjiadda","cfchdedeffhfjdaig","cgcbgcheaehehaajeib","cccbhidfjfje","jfabh","haeabffgeghefbd","dibcjh","eiigbfjj","bbihibbhhbjcfcb","cj","dd","hiidebfe","jacefbffjgcccfhebab","ifbjagjeggca","eihj","hjdhjbi","gajd","igehaabddcihjgb","jjgibbd","cafbgeajbdiggg","bcfidjahdcbe","cjffbcibedidbhagghj","deijcajhjdc","cja","hjcagajajcjejj","fad","ceehfeaceif","eihdggijfhjba","bc","eejehjacjafjgij","eabe","ji","ciieeiaahbijdc","ajghiecehgcagf","gdcfedgfeaccjhefi","hcfiaagfjbgfej","feaehdbebhfagehgcfeg","edffhifj","jicej","ijcaijidjceddfdef","ejjaaaiffgbfdgagj","faajf","abigihddcfgjh","ggbfcajgcbjee","bhchjchadjdfjchaiedf","diibaahgfgf","jbdhgchbhfjgah","ijehfgdgggeabcff","ebjjd","acbebeeb","hgcbjicbfdfdaidaacbb","eedfdahajhecbbfdjaae","hhgbghifdieajfehhc","bibda","cgggh","gdbjicagbhafeeghiif","ffiddebjehhifhcbc","habbcdjgdbaiiffjjcic","ddjeehadbgcecahbibh","eiajfhdiafbfhfdifi","ihj","iaedfhijegeiif","gbgccgifggfahfcjdghh","bhh","agjhh","gidcfhfcghgdc","ebdjdgcia","beiggfebghedi","iibafbbj","jcfhjedejfcbchieghf","hdddcdajgfbca","dadfjiiaeeddgjdicbf","dfhbjcgfdeeei","bjbgeeddibgdgig","jjfjehihhj","igbfieicd","hh","cejjbbeg","ijibibifd","ggigbcdeabdiajfibi","ebjdacaihcbbijeadf","djhcjbabdbb","jf","hehchfbcf","cjghfadce","hdfaaiciecbh","dhdchfadebgcccd","acfbjdeffbfhdif","cdcbjhja","ffgbfdejdcecfjfii","aijgbhfchhihgejebige","idgjjfdcehhaddjha","caaigdciafihf","cg","eibijeiibheacejha","feji","fidbidbjjdbdgfid","jbc","hbcjgiedcbjbcbefd","ii","fah","eejcjdbfaefh","hbjeeh","jgigdbgafc","ihjc","dfdaacjjacgciijhcib","ahibbfabidegghefjhg","egigbijh","ahe","bahdieehageejbde","gjgbjejaefdgabgfgahj","ibeahdjhgjhcfejjejib","cb","ihaiiafjgbafgigf","eagj","fib","cedfbdadfiaja","fbdceeca","daf","cjb","hcfbeceidjfdie","ifbi","fdijgifedhcaicjgc","fjcjgfh","iegbfibgfbjfjd","fgaheegcicdab","affcddihfidhb","dibbcb","jhcjehdfjebgbjic","dfd","gfjhhfga","hcifaga","bgaaacaig","iidichgadjijhdbc","edf","jhedg","ebbighfadifg","hgcgffdffedijhhbb","bdehgc","cedeidac","cjbhcihfjfgebf","hgjhhccjecbcbddfgcj","gjibabjddfbjcb","ebhciahde","fcdbfihbaehabjjhi","dgahfaeac","jfhjihagf","jeaeciiagbcjbhhii","jcjieejghfehcf","accheh","ggicdgcgjga","ifeafcdhefdd","ddcdjaeaffe","gacejfadbiibiiifjf","bbhbaheceifjhagbid","fieifeag","cbbicba","daehh","bgbbdaijjfc","bgic","jbicbiibagd","diifadbg","bdgcjagjeb","jghiebchaheh","hgiccb","fafccfagjadjdhhifb","cfdhidgehdgbeacdeeg","cidadhhbhfaiefhhdhj","ihb","ggfehbe","bfaddecjahabcijf","cjbfbgiabf","cebcj","cbgbaaf","gaejcajdgjjigiaabahi","eifeihieheegajicch","ghejcbcjciejcbhiahf","diaddacacggbcf","idhdejgdiajef","jgeejihaeajh","agidcdfdjbgfceecegih","acfiifbfgaifhdbebdig","ihajjgdbajciafbibjij","jjcjachecfa","aefffdgdjchbejbagcj","agdabcachieaih","bddhbgjhge","efaccbjjjgdejfbdbah","feddeghjehag","eehcahgcdedefia","hgddfihgdgidc","iegdai","djjgiehbdjhee","fjaihcjfihgeia","cicjdgcfafcehgbb","eaefeaddae","hchcb","cghjfiaigeabb","beghdhiaiadeacdfbiij","ddjgiaeahec","aadjajga","hjdda","ieibjejfbfcfi","ghhejfi","hjifjjbdcjhajbdgjejh","fjgegdcjciaeiaajih","cahdafdghadfehgfjdh","bgabfgjigbaej","idgfedeebfdebd","hagiccacbegg","fbbhahbb","bge","ijihdgfjhajhfegce","dafdggjbgec","cjafhcbfdgcjje","fbhafe","jbfccb","fei","cbhibjjfajj","geidcb","hjihijjfgeih","hfigjgbbggcc","dfchegbbfiebifdd","gjadjff","ebihefeaaijbfbejec","deaggfaje","idfeaj","jiahgidcfaicjgbjbhbb","idgbhicdjgcgdbeg","dagfja","dbhjeeffhjd","eebeibf","ghedgabaeabd","jcigefjdchidehbg","ifdghchbfcaiegfbieid","hdhififeddghjgghahjj","icgdbdieghhddjibgeb","hcjggbaiiagjfjafeb","jgiiefihccicbd","icbiabheh","gd","jecgdegiabjbebaedhda","edachaahdjb","dgagjggh","djdbhdhfhfgfh","jhaibiiadjbdjfhe","dechchfbghefcdbcjg","dieghajfijicaaheejhd","dfig","gbeifiejajejhjbc","ehhefchfcbac","iehifeeghfcjdbh","cdfj","bihjacaeahbfagib","baeeaehggbhajhejcb","dcdahjed","dhaeabfjhdfcfcbace","ajeahjhiiaiiaibhbi","gaiiiedgefb","hafhegeabecfaga","eehhjjbii","dbdc","dijafhijfeghfcegcjh","ecbeejjiibcjea","eibiiehijibaadjae","dahbccaj","hchhfjjcifjfadgha","cdfbccheaggfdiigbag","ciheegdcagfacgeia","fahj","ccbeg","bbcjjjd","ddgcahffi","bieiaafgdiebjcd","jiffe","jdbcagg","hciebdfahigbf","cd","jcfbjieeahagg","ffaejijcjbfaf","efeaaddgfcbj","hdjehbijgedfej","fb","iefjdcbjd","fche","jaijd","jfbgi","bcddfgfgdgige","igcahjdaef","jedefeahcaahb","aijchgehfih","hcfjjafhjiac","ebjchbiifadjjfei","gbfggciea","eebgj","eefdaebhbhhhhii","cheebfbgiihfadgf","acfcbcjgbejcc","dhjjhieidadfdjijehdd","ajdfgi","hhjjfgagebafdfjihd","ibigjccaididd","faejccibjifcgbdcg","cebggffgafdbfi","hefeecdhh"], [[1, 178], [1, 185], [185, 1], [1, 552], [7, 24], [146, 7], [11, 148], [11, 240], [11, 273], [361, 11], [11, 381], [559, 11], [11, 727], [855, 11], [927, 11], [62, 24], [125, 24], [144, 24], [332, 24], [387, 24], [24, 447], [461, 24], [24, 655], [655, 24], [24, 885], [24, 922], [34, 148], [40, 61], [40, 66], [40, 96], [96, 40], [529, 40], [40, 587], [654, 40], [40, 673], [738, 40], [757, 40], [40, 906], [922, 40], [159, 45], [45, 177], [45, 279], [45, 474], [493, 45], [61, 159], [177, 61], [61, 614], [319, 62], [325, 62], [62, 670], [66, 425], [66, 539], [607, 66], [66, 738], [738, 66], [70, 437], [437, 70], [96, 137], [96, 364], [116, 159], [159, 116], [116, 332], [586, 116], [539, 125], [125, 885], [885, 125], [137, 319], [279, 144], [498, 144], [146, 205], [240, 146], [146, 428], [527, 146], [587, 146], [146, 676], [146, 744], [744, 146], [148, 655], [279, 157], [157, 319], [178, 159], [194, 159], [273, 159], [298, 159], [369, 159], [185, 199], [185, 387], [447, 185], [185, 654], [676, 185], [727, 185], [319, 194], [336, 194], [199, 539], [202, 470], [205, 319], [205, 593], [513, 239], [239, 539], [856, 239], [760, 240], [474, 273], [555, 273], [862, 273], [279, 324], [364, 279], [381, 279], [279, 466], [279, 721], [721, 279], [539, 298], [298, 856], [315, 320], [325, 319], [319, 356], [356, 319], [319, 361], [319, 485], [488, 319], [319, 586], [319, 593], [320, 447], [655, 325], [361, 763], [513, 369], [654, 372], [376, 381], [376, 565], [381, 410], [387, 447], [447, 387], [425, 738], [428, 432], [428, 513], [428, 760], [513, 432], [432, 744], [492, 447], [721, 461], [485, 774], [552, 513], [673, 513], [708, 513], [513, 757], [513, 927], [721, 527], [539, 738], [885, 539], [593, 744], [764, 602], [610, 727], [614, 738], [670, 763], [763, 670], [673, 757], [757, 673], [673, 841], [721, 708], [757, 742]]],
    [["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]]],
    [["bat","tab","cat"], [[0,1],[1,0]]],
    [["a",""], [[0,1],[1,0]]]
]

run_functional_tests(Solution().palindromePairs, tests, custom_check=compareSets)