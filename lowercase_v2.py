from math import ceil
from kandinsky import fill_rect as fr

a="5;0E010F11111F"
b="6;2020202E312121322C"
c="5;070810100807"
d="5;0101010F111111110F"
e="5;0E111F10110E"
f="6;0708083E0808080808"
g="6;1F22223C203E21211E"
h="5;1010101E1111111111"
i="4;01000F0101010101"
j="4;01000F010101010101010E"
k="6;202020222428342221"
l="5;1C0404040404040403"
m="7;764949494949"
n="5;1E1111111111"
o="5;0E111111110E"
p="5;1E111111111E101010"
q="5;0F111111110F010101"
r="5;171810101010"
s="5;0E100C06010E"
t="5;08081F0808080807"
u="5;11111111130D"
v="5;11110A0A0404"
w="7;49495D555522"
x="5;110A04040A11"
y="7;412222141408081870"
z="5;1F020404081F"
A="7;081C14143E222241"
B="5;1E11111E1111111E"
C="5;0708101010100807"
D="6;3C2221212121223C"
E="5;1F10101E1010101F"
F="5;1F10101E10101010"
G="6;0F1020202321110F"
H="5;1111111F11111111"
I="5;1F0404040404041F"
J="5;1F0101010101110E"
K="6;2224283824242221"
L="5;101010101010101F"
M="7;6363555549494141"
N="5;1119191515131311"
O="7;1C2241414141221C"
P="5;1E1111111E101010"
Q="7;1C2241414141221C080C"
R="5;1E1111111E141211"
S="5;0E11100C0201110E"
T="7;7F08080808080808"
U="5;111111111111110E"
V="5;1111110A0A0A0404"
W="7;4141414949555522"
X="7;6322140808142263"
Y="5;11110A0A04040404"
Z="5;1F0102040408101F"
n0="5;0E1111151511110E"
n1="5;0C0404040404041F"
n2="5;0E1101010204081F"
n3="5;0E11010E0101110E"
n4="5;02060E0A121F0202"
n5="5;1F10101E0101011E"
n6="5;0F18101E1111110E"
n7="5;1F01020604040404"
n8="5;1F11111F1111111F"
n9="5;0E1111110F01031E"
sp="00"
ap="1;010101"
gl="3;050505"
cm="3;03010204"
dp="1;010000000001"
dt="1;01"
ep="1;0101010101010001"
ip="5;0E1101010204040004"
def lp():return"5;0103020404040404020301"
def rp():return"5;1018080404040404081810"
def pc():return"7;2352240808122562"
def bd():return"7;7F"
def pl():return"5;04041F0404"
def mn():return"5;1F"
def tm():return"5;0404150E0A11"
def dd():return"5;0102020204040408080810"
def eq():return"5;1F001F"
def lb():return"5;0704040404040404040407"
def rb():return"5;1C0404040404040404041C"
def lc():return"5;03040404040C0404040403"
def rc():return"5;1804040404060404040418"
def la():return"5;03060C180C0603"
def ra():return"5;180C0603060C18"
def cp():return"3;020000000003010204"
def pi():return"7;7F2222222223"
def sr():return"7;030202040404642C181808"
def rg():return"5;0D16"
def bs():return"5;10100808040402020101"
def ca():return"5;040A0A11"
def ii():return"7;36494936"
def ar():return"7;0804027F020408"
def br():return"1;010101010101010101010101"
def dg():return"3;070507"
def ml():return"5;04041F0404001F"
def at():return"7;0C32214749494520310E"
def ht():return"6;12123F12123F1212"
def ad():return"7;18242418314A443B"
def dl():return"5;04040E11100E01110E04"
def uk():return"6;3F332D2D2D2D333F"
aa="01;10"
ga="10;01"
ac="010;101"
dr="101"
cd="010;001;110"

red,green,blue=(255,0,0),(0,255,0),(0,0,255)
black,white,grey=(0,)*3,(255,)*3,(150,)*3
yellow,purple=(255,255,0),(255,0,255)
alt=dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '\",:.!?()%_+-*/=[]{}<>;π√~^∞→|°±@#&$\\",[
[a,10],[b,10],[c,10],[d,10],[e,10],[f,10],[g,13],[h,10],[i,10],[j,13],[k,10],[l,10],[m,10],[n,10],[o,10],[p,13],[q,13],[r,10],[s,10],[t,10],[u,10],[v,10],[w,10],[x,10],[y,13],[z,10],
[A,10],[B,10],[C,10],[D,10],[E,10],[F,10],[G,10],[H,10],[I,10],[J,10],[K,10],[L,10],[M,10],[N,10],[O,10],[P,10],[Q,12],[R,10],[S,10],[T,10],[U,10],[V,10],[W,10],[X,10],[Y,10],[Z,10],
[n0,10],[n1,10],[n2,10],[n3,10],[n4,10],[n5,10],[n6,10],[n7,10],[n8,10],[n9,10],
[sp,14],[ap,5],[gl,5],[cm,13],[dp,10],[dt,10],[ep,10],[ip,10],
[lp(),12],[rp(),12],[pc(),10],[bd(),12],[pl(),9],[mn(),7],[tm(),9],[dd(),12],[eq(),8],[lb(),12],[rb(),12],[lc(),12],[rc(),12],[la(),10],[ra(),10],[cp(),13],
[pi(),10],[sr(),11],[rg(),7],[ca(),6],[ii(),9],[ar(),10],[br(),13],[dg(),5],[ml(),10],[at(),12],[ht(),10],[ad(),10],[dl(),11],[bs(),12]]))
acl=["à","â","ä","é","è","ê","ë","î","ï","ô","ö","ù","û","ü","ÿ","ç"]
dif={"à":["a",ga],"â":["a",ac],"ä":["a",dr],"é":["e",aa],"è":["e",ga],"ê":["e",ac],"ë":["e",dr],"î":["i",ac],"ï":["i",dr],"ô":["o",ac],"ö":["o",dr],
"ù":["u",ga],"û":["u",ac],"ü":["u",dr],"ÿ":["y",dr],"ç":["c",cd]}

hex_val=["A","B","C","D","E","F"]
dec_val=[10,11,12,13,14,15]
def hex_to_bin(hex_num):
 global final_bin
 dec_num,bin_buffer=0,[]
 for string in reversed(hex_num):
  for i in range(6):string=dec_val[i]if string==hex_val[i]else string
  dec_num+=int(string)
  buffer=[]
  while dec_num!=0:
   buffer.append(str(dec_num%2))
   dec_num=dec_num//2
  if len(buffer)<4:
    for _ in range(4-len(buffer)):buffer.append('0')
  bin_num=""
  for string in reversed(buffer):
   bin_num+=string
  bin_buffer.append(bin_num)
 bin_num=""
 for string in reversed(bin_buffer):
  bin_num+=string
 bin_buffer=""
 for n,string in enumerate(reversed(bin_num)):
  if n<len_num:bin_buffer+=string
 bin_num=""
 for string in reversed(bin_buffer):
  bin_num+=string
 if not first_n:final_bin+=";"
 final_bin+=bin_num
def decode_hex(char):
 global len_num,final_bin,first_n
 n,hex_num,len_num,final_bin,first_n=0,"",0,"",True
 for string in char:
  if n==0:len_num+=int(string);n+=1;continue
  if n==1:n+=1;continue
  hex_num+=string
  n+=1
  if n==4:hex_to_bin(hex_num);n,hex_num,first_n=2,"",False
 char=final_bin
 return char
def decode_bin(char):
 rows=char.split(';')
 return[[int(c)for c in row]for row in rows]
def decode_char(char):
  char=decode_hex(char)
  char=decode_bin(char)
  return char
def decode(char):
 rows=char.split(';')
 return[[int(c)for c in row]for row in rows]
def draw(ltr,xf,yf,cc=black,cb=0,tl=1):
 if cb!=0:fr(xf,yf,7*tl,14*tl,cb)
 acc=0
 if ltr in acl:acc,ltr=decode_bin(dif[ltr][1]),dif[ltr][0]
 lst=decode_char(alt[ltr][0])if ltr in alt else decode_char(uk())
 dx,dy=ceil((7-len(lst[0]))/2),alt[ltr][1]-len(lst)if ltr in alt else 2
 for ay in range(len(lst)):
  for ax in range(len(lst[ay])):
   if lst[ay][ax]==1:fr(xf+(ax+dx)*tl,yf+(ay+dy)*tl,tl,tl,cc)
 if acc:
  dx,dy=ceil((7-len(acc[0]))/2),alt[ltr][1]-len(lst)-1-len(acc)if acc!=cd else alt[ltr][1]+1
  dx=dx+1 if acc==decode_bin(cd)or ltr=="i"else dx-1 if acc==decode_bin(ga)else dx
  dy=alt[ltr][1]if acc==decode_bin(cd)else dy+2 if ltr=="i"else dy
  for ay in range(len(acc)):
   for ax in range(len(acc[ay])):
    if acc[ay][ax]==1:fr(xf+(ax+dx)*tl,yf+(ay+dy)*tl,tl,tl,cc)
def write_string(txt,xf,yf,cc=black,cb=0,tl=1):
 rep=rvp=0
 for ch in txt:
  if rep+1<len(txt):
   if txt[rep+1]=="̈":ch="ä"if txt[rep]=="a"else"ë"if txt[rep]=="e"else"ï"if txt[rep]=="i"else"ö"if txt[rep]=="o"else"ü"if txt[rep]=="u"else"ÿ"
   elif txt[rep+1]=="́":ch="é"
   elif txt[rep+1]=="̧":ch="ç"
   elif txt[rep+1]=="̀":ch="à"if txt[rep]=="a"else"è"if txt[rep]=="e"else"ù"
   elif txt[rep+1]=="̂":ch="â"if txt[rep]=="a"else"ê"if txt[rep]=="e"else"î"if txt[rep]=="i"else"ô"if txt[rep]=="o"else"û"
  rep+=1
  if ch in["̈","́","̧","̀","̂"]:continue
  draw(ch,xf+rvp*7*tl,yf,cc,cb,tl)
  rvp+=1
