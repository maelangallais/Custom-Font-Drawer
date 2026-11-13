list="10000000"
char=""
buffer=""
hex_val=["A","B","C","D","E","F"]
dec_val=[10,11,12,13,14,15]

def bin_to_dec(bin_num):
    global dec_num
    r=len(bin_num)-1
    for str in reversed(bin_num):
        if str=="1":dec_num+=2**r
        r-=1

def dec_to_hex(dec_num):
    global hex_num
    buffer=[]
    if dec_num==0:hex_num+="0"
    while dec_num!=0:
        buffer.append(dec_num%16)
        dec_num=dec_num//16
    for string in reversed(buffer):
        for i in range(6):string=hex_val[i]if string==dec_val[i]else string
        hex_num+=str(string)

def convert():
    global dec_num,char,hex_num
    n=dec_num=0;bin_num=hex_num=""
    for val in reversed(buffer):
        if val!=";":bin_num+=val
        n+=1
        if n==4:bin_to_dec(bin_num),dec_to_hex(dec_num);n,bin_num,dec_num=0,"",0
    if len(bin_num)<4 and bin_num!="":bin_to_dec(bin_num),dec_to_hex(dec_num)
    if len(hex_num)<2:hex_num+="0"*(2-len(hex_num))
    hex=""
    for string in reversed(hex_num):hex+=string
    char+=hex

rep=0
len_list=0
for string in list:
    if string==";" and rep==0:char+=str(len(buffer))+";"
    if string==";":convert();buffer="";rep+=1
    buffer+=string
convert()

print("\""+char+"\"")