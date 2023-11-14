"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2023-11-14

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")


Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         h = set()
#         n = len(s)
#         right_hashes = [set()] * n
#         right_hashes[-1].add(s[-1])
#         for i in range(n-2, -1, -1):
#             right_hashes[i] = right_hashes[i+1].copy()
#             right_hashes[i].add(s[i])
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 if s[i] in right_hashes[j+1]:
#                     sh = 1000 * ord(s[i]) + ord(s[j])
#                     if sh not in h:
#                         h.add(sh)
#         return len(h)

# Runtime
# Details
# 3523ms
# Beats 7.48%of users with Python3
# Memory
# Details
# 265.66MB
# Beats 5.26%of users with Python3
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         h = set()
#         n = len(s)
#         left_hashes = [set()] * n
#         left_hashes[0].add(s[0])
#         right_hashes = [set()] * n
#         right_hashes[-1].add(s[-1])
#         for i in range(1, n):
#             left_hashes[i] = left_hashes[i - 1].copy()
#             left_hashes[i].add(s[i])
#         for i in range(n-2, -1, -1):
#             right_hashes[i] = right_hashes[i+1].copy()
#             right_hashes[i].add(s[i])
#         cnt = 0
#         for i in range(1, n-1):
#             chars = left_hashes[i - 1].intersection(right_hashes[i + 1])
#             for c in chars:
#                 sh = ord(c) * 1000 + ord(s[i])
#                 if sh not in h:
#                     h.add(sh)
#                     cnt += 1
#         return cnt


# Runtime
# Details
# 678ms
# Beats 50.33%of users with Python3
# Memory
# Details
# 17.06MB
# Beats 92.65%of users with Python3
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/editorial/?envType=daily-question&envId=2023-11-14
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         letters = set(s)
#         result = 0
#         for c in letters:
#             i, j = s.index(c), s.rindex(c)
#             between = set()
#             for k in range(i+1, j):
#                 between.add(s[k])
#             result += len(between)
#
#         return result


# Runtime
# Details
# 149ms
# Beats 84.54%of users with Python3
# Memory
# Details
# 17.27MB
# Beats 43.97%of users with Python3
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/editorial/?envType=daily-question&envId=2023-11-14
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         return sum(len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s))


# Runtime
# Details
# 735ms
# Beats 47.48%of users with Python3
# Memory
# Details
# 17.32MB
# Beats 24.34%of users with Python3
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/editorial/?envType=daily-question&envId=2023-11-14
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first, last = [-1] * 26, [-1] * 26
        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
        result = 0
        for i in range(26):
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i]+1, last[i]):
                between.add(s[j])
            result += len(between)
        return result


tests = [
    ["aabca", 3],
    ["adc", 0],
    ["bbcbaba", 4],
    ["swnmktiziarhdvsbqottoksakebbtpzxaevptnqronedeszuugctxnvigkhasprrzcuyhzpahupkajeqvlagpezgxthuvsusvbscmwaqyhfcwnwtxcqguxrxrcayucbpeqbwfnonxybedeyoquvviyradnpioqmhbokpcpxwemkaadaqlquzkrwhfujqqinvmaethrrhrjkacyylgexokvsgjtaxhjdtrbjslncnljyrzwvhwndjslmnhskzygakmuzkpdpomxxxdbgpkekqakblypexjzxyrexpyofttwknslexlhgnbyuxvcfnetczkaxhbzsydqtbutrwwtofdfvmdqodpoqvjeuydxizqbeigomlpuqgxkxozuxzazjnwcrgylkcnozdtxquwagymdefbfrikammqbzjfcorzdiqvpbfmfbhehzhloahllykdfzxxrmiupuqzrwzcsyenjgjzavojajtsvivgsqrgrxbmmbagvaixdhatpuoeuafjtttbnxokyqsalodipizjrsffgsdbezhwnnbtlbspmzpbrdscvvqzwcfwdkcihibekedpkhlrzdipmamhshsybnxuxxcthtvosokuuzdkgsoxjzdjthdmolfkkivkbklabtxcqgaodwppzbtqddpirtljmpgcqekbsldzjvmhivzpditzhhindaospjjfxvtkkwprdmmikazkvviklhwekxafubnajfalrqcmcljlbdgbgilgsztjcvszmbsdycqnokzywkfixofipgrloarbegtmmtogaqoeplgevrpmudowhbwxitvyxlqpeemgyeswqbgeogzbqfunhfhrpnxariicvrdkxllrqfydavuzfeulquxmmfykssakysauaobjapenhqcvquhbxhrwmtnlkjyvlevgkurjwvkygkbogpqfnfpurtvsvpcpslpqiiwpufvulfdfpxccspynqrxihyfaseltzwdfpnxyhvyeklnmwunxdlqqbrzhkbszfsojhtonwharnrqoufrgaqxekdvbwkjdcixtrkhmyyitjmczglabniukndrjkjiexwgupmhdwfnxzauvvwslykbqvgxnkeuibpnapwtfrauqvmmvvomvidgfkhaibftjrhnzomqfgaivtbrleqhqvbgcxptihvaeibctrmnlpycinlgxneansviqwsuhoeqfzltjostekmyfwlsjeprqrjznxtmnhdjjiiqpakddsfmlnpzwfroavtlvwsqlrovzpsbukifnzwoqblfnjbmbpjztqevfgnknwyrkdpreyupqicwoeounkrtndvqmxktzadldmdokpghsrwrplbsbmlpwuwzejlulttvrwciqrtlxjqnqrtnshbjnfziimbxcdfqibkzcqkynbaqwllbwgzuqjngzohxzvlwyvbfdifmrwjyjsexrrgnzufaocoxrqzfecwtbjtnpuamfhjmgedtooqxmtyplliyxbrkoqyxcuhhmsbpvfmlazpsdkrzzuadzqztoqjvdxkldtzkyaztxhvxdwdrzgpbxfllfkjtcwpiqhkhaegwbhkjwdvvcjmdfoujxjpipeerjwvhbfwuviztibsfyzuygomexfamgggjjtcrhvdcgulnpibwaaigmlcfsunbsnzcfccbfmkqyauclbrqihilbqqawvrgvbyetaaebyliqyxaivetcuakaigtoazkxftdddazgzdrbjrcrpbbtghfcfeejzuetgvkhdhnhuplagnlgtspjllrqwgroqemgkuiejyjiwgtkeuwnqkhgujgwsewuyyksriossktwoxtefxtkydcmelqyytofhyhonlrauknhmqqttuccwrncxnfmaaumjmevacnlmosodtodzzkftuleqvtzqksikxecdywpxakonrzcqsjhlqlrkxfipaycjuaksohptcfhhmrvrfrncbougsywmfbgocahrprubixexdowwykoazwpgdyugxyhgebibbmzcvycxjcucscmfdspiwadxraznuccdnwhdmsupzmnmhlpgucxmpczdphgdjwbgxfbplrkkgieitmibdjmvymoshnxlpnzpzaczsilyxfjnxweqcektjjgwmrcwrhvavnykebslvwaqvkprzucddmencjuefoeohnmwnjppahbtgpdjusyjawufzyyeqpyayhqyjmzpmgdowahqxsihpwdttcrhouhwdacnopafizosazmpddfrssgxgspavoyxuphtohotvplqrjdpoabbilgtjxcilcfrbpodfahmkpqwhhumxiwahetxehaacsisiykcnihyyjvojeelgtfdurhefcqxdkbavpkxrplcheddhkotxjgekpmzafdjafvpnhuvadkrboqfqmmpaqepicdvjshmnjzispqxfhuszdgzqmxnbihtvludhtfpxxrzlklbemxkduecsiokbsbdbcmoyaqmlidfmopbdvnhnkxchdiaatlixonxdgsfgirnjpdmzscrfrkowifnbchwvuelhlwwwjumziizxmvritpzglhlevpsvakdakdoinicvbkdlkmpgialugwwbohwrxeuhmowyssaxzsmwjwhrlfqnclryzdgltebosiskksafqrwuvlabdudvvxsnngkgzoftkloauezoksqsjwqgxxwpazxhsbwdqtcofbqxacikmunrsbwfnnqsagbhhbkxirveqcnfiinfqaxnihcvlgcyaxurkpsqfslcnkznkcovkjtnrebwswizfejopkldjjggrunhkrcxsibroglopfvuauievetloqgbjtbiwjhcgumexnomxvqtfwvyumxydwnddtqxfublcbvshfrmxzjrwrlmtvuxyrpmjsluklhpsjwfuapjevhdrrjuqyevptgqaasmgbcmqcxitcbsxkaakosrvxpwxfinsjxpcomcggxnkqwrgewczmdrldniogxxzmdavrtrakbhtuipoifdwkqswsfgxvxjsvfaxbabvpblcaywnbnzfshiwperqfysqkcuknqnvddqnjzthlsglajsbvzajofugwlypqhdoztdkgztjaskmmwnmwdnvfylnrjcrwueyeellnrasfqckveoqrszahpvociqmdipmhoeoyniyxyhucykmpoydywwjcnccznbwjbsehseyoxjmbgadfdtdqbnvahozkqizewkfdojxayqadgeksdsojmuqzsiwruthyyjkumbjxujhyfibjlonvjwftgfhtfyjolekmlkhiewvmnanpguqupfvggzlpinjtuibzaegmtalhxttoslxmdziqxrzaoakizcadsazaeoiixdmgrrgfmwteuscdrohwkelgovjercbjffsjhygtzuvqpicryijtflatdevkflkzdcimzstttgctagdzrkaqbocvgugqibtyiaiqpdvxskfuyyfuvnoyiiyrqbjvkjwdescgmtlmpbshahgxnsqgwjxcaqezmdqikrcrmdxyvxfeclrcbnfqepgobiflucadnlaqjpqsjfgiazaujugmpxtijbpnlkguhpsfkrrhbsduocbgodebtcgjcidcnojgaoftwrnsqfvgorcymgjatphmmbadgsuzxllgjuurvielnccutquhgjpdkivplmglrdtnkdlpkdkvylfajfcowmhzedrythjbhkjmffhrblurerjhfpztfygagioopxyfougaompqkfvtoeyusycqmbifbxbtrpcldemnanlpzkbvilpusrvmhpqbewcdhwuzjtoncyzlmqryskgzfcpzjjvttcppfxncvfwsqxbnyscfvmlmerekurkdvbpngawipbmejhnifsxvgpptdmhtpexuxcvbptiwbtzygmkeyvzskaskoggvsoickupaumkriybpshwpmqxazpwslqxiyyknbfzmylmdmfhaxhqqtycqwvfvkxegixcoqighzwhrrehvtapljxcrnrzkhpocmfosxmivdvzrqnvkbxuafjqepzaygjjpyleejgjocbvuervuuhhqdaletheurofgfjytjxgalvvegojqdiagivpjzwqyuzpwxvwglxwkiicwkblunatuidnlyztpkjzlppgaslwqwwlbwqxczfnuyylimjliqbskacmhosehfzpqlnazyixquksufibvtgeobvneilhadbwwowzlejvnuqtgqotkobkijavactlppcuqahxwdwslntbfidytfhhqgnptsgnrdflkmvxlfdlhjmlrxkylibpxxpvgmujhhghnipwllgvatgkkmawawkjilfcimfubpuqbwtujjnghggzurkgyxwdkzqxraygaztbtvptjkcrpotvzccxntlykbsmlcqqnrhmpkqujxsajdkzpaqbssraesmxwivrqkxbbbwnjihwfpcltighhdephaxwesumfjcxrtkiwmhfzxbrajjgykivjyyujedoiwubphxubezziuvzcltenycfnycxttzybgkgszexcpjmvzwvtcbimfccscgiqjwyibbhalcsxqxkphtikvlthzhutepdywpibhcqtckcsjqrcbtvsndrdtkdvydcvjqeuvojdnqmustaoduqyqmtolseayrxgimduoydjhesbrnyqsdqnajhauvgkjhmluspisawqzpikrfckqjufonylwjsxpvbkykdyvaccsfjxmprlwtqfaitswnutsoyoiptgvtyglopwykfbosdsmvgnnvnuvirdxjrrrwexsxtcfgflninhykxqnpkiomghioicjfyiiuiqysmnlhzbqzkxylidtdqmgfpjitulxplpgsxbyjnevkeatimqehdhothrejoongrbcqnaafxobwwlgunktcigkagekplwyvksmbifywhocrsvjlqrujbzwyzswqrowrlwoceegyjmnhklpvvvcuoocnljborhupefcxqettnqrmlljixmjhpqsqhzlmmikoysvgpxmyshcfpmzrcyqmwtpgrvrsmeymnkciqtmcnwjfrdwnzjautuvmpvjnqkexnxqdfeftuqlhmguzlsgzrmvvghosoznfyjtalevccjrrbctyluhaosenicxetjvgouplrjflzjrjnkmldnhcfuvtpbepximiplwxissktwygzftzrrxrfjqvodvnziyrgsvysudntkycvryuegriejypuoudiqhztlgqjjfjvhyccunwxifxezrdfvqcplylhcuhmcjdabrgggbceefkfnwkhxbozrmcoujtjmrrbkymbovkbhnvffvevruglhpcasrfrkxuozstqfdvzsprdbwockopmahdigpqkdwykaelttonjhawygujgnhrqcklxicixjfriaecbvcxgcinqsoafvwlmmwseinxxhdxsackogqoigkgtlvlwlbkfiyvyulqvvqmgfepkvsitmzziuhhnbhwluvozkwvebpwxjpxukdcmzmhlhtklnudkohiyrtppgrnjkvjppxyskfdkoatlllpmtfovdfmettlrcytzdokeukzqefgrubdqygjuvxvyjzgfxkidinkupcngsbuwgnvinuiczqtnaejiduizkzzjumwyoqlkrbsyegbmxczxozxyuromnmxnfubuuouevmrkhlgtonmacbnirdarsrasmhybhmdwbwgkwitujkrlhvfsbnthoyeaznmxrfnqluwizddmgrisqlcbclpwmdqjobwesjgszlagqfmiexizqjidlfplheauiyhwzzxhvvpedpnoseqyzxsgylumwgehqihxnezjmikshxwqvpotfyqqdmwyqsoabsmmdwkszvdgdakpbtsgvzxrdgyclvkxgyiouwqndpfzpzhueoqvzqikksuucjwaelxtmukasdoosqlvkwqhlmvsirbxegkmdsblyvgoqhgophwtrwuremsifvvcfamhgxrbzlcehmgqoevegjibbgdcasjjnmuygzbdxvrykbpevwdguamnpvvtxxjtsiyyzqwcrwimdylfyqdhgvltdwrwrxsgdwalbbdiokvrklwhrskxntpcchttwtpmnncpauxrkgnknstcvjkpzqrjztnemnayseaqoryheffkanssanbklwtpzjqjhokxgmoyjnkjwimcljbruvfhycbqlpdsdnyltfusmgrcmocuvchmdwdrdjviabipazsrpofwklnmicffuhnubacfehyzmzhlozkzkknmfcpjdeuqbegdxhjtlwyecjobgxwewwabkbocepmoumppjfcdkiovwhedugogoksglmhbyvwxadrqvxupgoacgyuwotvvuqtwjrpxskouhzfcctncwwqiyicseqlpaibjatuuxlhvlfacvjxhmydizpulgfwygqpxnaygcftzheqzbvaetlgbqbmygraankikcikkhblykpwjqpnhgbaqkczxlmtlytfmoiffzancxlotvzhaxghyviplfgrhoksiyfzmrvsjxwtispeqzfkctmvgzfohlxhmsyftojnwzgqwrklcszyhfdtxkyljocwvmdwddasppyjghfpslchzqjawpgrmvcokypdipwbaykbbcyvrtcibbpfgguqndcgbtnrfwrjobryxvwmfybggdrymqqkxjikpdbzowafcskhmbqzfaegdqplexpbwlagfpbofeiunxqklcjplgvoveeeptgrhyutlsonwwbufbgpnimcisprsuxsemmpejcdsgkgekxzkadihnaqiqomuszufvzwijoqdshcbrzzlfndjymlcjosefuojyayspegqdmzvecxrnfelszthjemaqvodmvbreplxqietiirayxachngdlerakzdgatnaxrrwqfluoztdyapwsfkxlkoshgwghgyklgmaohtocsckdyveadcjiapupzktudvsjssduobnozqqgxtywhzeiwfjucxuvirvmsoebclnaggzunuatmvluwixezfyirhtpeiuollpzcruzufstmzlgtrckozwzoxbtwrzeufspjanhltdnpnqfrxhxttsotmwvdcxikbuwfrtwrwdjqywnncuggokgsxaagpqzwyqhhmxrwiczlpvtdqyhgtvzckytgpxfpiqsobvsolninfrirubmivzrmyfzqcrmycxqfrqanfpdfsiaxkpiyitsftzyrkfliridqepbddgmhuiagjjszbzakmbkiyuouuceogrcqmtuvilkxedzqrqjhksgagjviidkslmmouiugdkzopgvansvkjrvdyxoerdojiacuaqxasyrebpfialmecebqrtvpqvtexupcwfmexbbownqlhlbhomoxuxybfervtaczkobhkknithkvksalvgeqxzellmgmxglvshimubldpnlxoenududksstglafmqyaksoafrzkhmwvqdpedetgojzrhvucpzogalydanskwcemqsbvbflojljsqhcbzcyoarbcojsabjhmryfreczexmxumqrrwifpiwztgtjjrqtrehkcufhyuwcxelupflltturlntxtanitvlpbjhsnchpnfvikhbjgioplejgdlpcdrbsjsbnklnozifegvknfvlsqswatxdwgjzmyawhvvnwmuwsdbthzgshhaeglcsxrzwcllmnvidvelylxnqpolmhiglhbhdpzsprfzxrzlsizzpgxnadhzhhpkujdxzkuddxwbymrigaigjddqhgflrvxsxbkqhlwkwucqfsmwomtbkcshqnnjjivcyewredyxnolbyvpkxptenesnhwibcfrvowlutetxfljlhuytodysuedmjagazmovlctkrffqjwtysmilfqwwlqtbiijpfyufqveiylxiegtziixnssfplxlbckznyjpqwkqgkuwjazhrxtltfsqbrhpjmrarlergivrhehmaoibdsfyoadsnctdfjobxozaryjflvfkaqletbijprjspxjmopjjxiqrkoqlhjxvxoqyrdwxdyyxuqnubqcbqehxmsibfurmkqgfnudyesrgscezwhtefugquagesvxjvemioshvpgdxgehaopyufhzzgnjbftqrxlkegvddaecsfcfcphaqybonbjkvedorwaerekovfldtwqmzzssbmarrxccnthiwcsuaxgygjamgnuivmjsjwlfvtfkvrynbqwttixtzzytojubkmaphxwzkpwdtflacrnaamxhbkgffatinmhssoqqgitvmdwiosroihiwfuxyuzxnetloxomkoqdgagggjikuntygkmcbflielkdjhncugclosssxbodhxwwbnetaiiqjjgtngngwuvglzufwrqizwjklazwcyqdmdfnumgdcwzlwfugjubpvqaufasokxjobksgxuahnghwyvaremosowdvpjhtlidctsvsjlmeaakyxxsbzfhpusieidkffehtpsrrbcaoydshrlytgwwuyhhswesqxgsuuxxffenmjkmzdfxkihlsccndszvwyyrnpbsasdzdhkgsccpnbojhthxftunoqisgzrzovslboxqieyetsoaztkopprkaojsfzvqjbhtrdcsvezmvtvabgnbqtksttyfauusoxnhheslsowyekbmhwvkllkrcpeczhmjwufiddezkzffvkygeyyfaxtzlugttfcnddmtjdsftozbuvwkykyfmfzdnjkuugduwfretfavsvtsbopdfyatafgtrqnvfhktcjmoxhfcnsqtrcyokazqhvjhvdjrofqehisqlqzpnjfsdzfuapppxrnffsaepjprzuursdalwtnqtklzmmwvpngojqxanedmecjtgrhozfppxhfoitklrjbbmadwadumfrftetrlsveshngfzlkupaaolsstfweiyltxqfmjjyczuuqafckxurjychtvskyvgmfyglobuxsdyailxceoxtlpxoglggbvnqnktbgnoprhuyeyhwjnpecvrkvnbnbiiqjahufklltprwledizgorszoknyboqbvdnffdosravniaweiwfncwaehjmzcjbtrchopekujwiortpvonclrbaaiypfevyosuyjmxckdpfdthjzbwwvbbzfwbymnjelokcrxzxutsqxzpvylmccobqoxrdrqfrvyfejwnmsdldchrporszvvwsqokozjicdbfknkhcroagukbobpxguoglihwakpvtvxavslilorqxjrmdzcdqaqlwqxewrqhkkcpibkwhdzkmhsxixdurduyctktoltinhywpqukqdjemmrbbjyyfsddefdvkantnqpwlcybuajtffc", 676],
]

run_functional_tests(Solution().countPalindromicSubsequence, tests)
