import time
import codeforces_api
import pandas as pd

parser = codeforces_api.CodeforcesParser()
cf_api = codeforces_api.CodeforcesApi()

test = cf_api.problemset_recent_status(1000, problemset_name="")
id_list=[]
tags_list=[]
user_list=[]
problemrating_list=[]
user_rating_list = []
problemindex_list = []
imp=[]
math=[]
greedy=[]
dp=[]
bit=[]
con=[]
sot=[]
ds =[]
bt=[]
grp=[]
bs=[]
dfs=[]
tree=[]
str=[]
nt=[]
com=[]
geo=[]
tp=[]
dsu=[]
sp=[]
prb=[]
dc=[]
hs=[]
games=[]
fw=[]
it=[]
mat=[]
sss=[]
fft=[]
gm=[]
ts=[]
ep=[]
mm=[]
sat=[]
ct=[]
sch=[]

for i in test:
    ta = (i.problem.tags)
    check = i.author.members
    # print(i.id,':')
    id_list.append(i.id)
    problemrating_list.append(i.problem.rating)
    ta.sort()
    tags_list.append(ta)
    cnt = 0
#seprating the problem tags==================================
    if "implementation" in ta:
        imp.append(1)
    elif "implementation" not in ta:
        imp.append(0);    
    if "math" in ta:
        math.append(1) 
    elif "math" not in ta: 
        math.append(0)   
    if "bitmasks" in ta:
        bit.append(1)
    elif "bitmasks" not in ta: 
        bit.append(0)   
    if "constructive algorithms" in ta:
        con.append(1)
    elif "constructive algorithms" not in ta: 
        con.append(0)   
    if "greedy" in ta:
        greedy.append(1) 
    elif "greedy" not in ta:
        greedy.append(0) 
    if "dp" in ta:
        dp.append(1)
    elif "dp" not in ta:
        dp.append(0)
    if "sortings" in ta:
        sot.append(1)      
    elif "sorting" not in ta:
        sot.append(0) 
    if "data structures" in ta:
        ds.append(1)
    elif "data structures" not in ta:
        ds.append(0)
    if "brute force" in ta:
        bt.append(1)
    elif "brute force" not in ta:
        bt.append(0) 
    if "graphs" in ta:
        grp.append(1)
    elif "graphs" not in ta:
        grp.append(0)
    if "binary search" in ta:
        bs.append(1)
    elif "binary search" not in ta:
        bs.append(0)    
    if "dfs and similar" in ta:
        dfs.append(1)
    elif "dfs and similar" not in ta:
        dfs.append(0)    
    if "trees" in ta:
        tree.append(1)
    elif "trees" not in ta:
        tree.append(0)    
    if "string" in ta:
        str.append(1)
    elif "string" not in ta:
        str.append(0)    
    if "number theory" in ta:
        nt.append(1)
    elif "number theory" not in ta:
        nt.append(0)    
    if "combinatorics" in ta:
        com.append(1)
    elif "combinatorics" not in ta:
        com.append(0)    
    if "geometry" in ta:
        geo.append(1)
    elif "geometry" not in ta:
        geo.append(0)    
    if "two pointers" in ta:
        tp.append(1)
    elif "two pointers" not in ta:
        tp.append(0)    
    if "dsu" in ta:
        dsu.append(1)
    elif "dsu" not in ta:
        dsu.append(0)    
    if "shortest paths" in ta:
        sp.append(1)
    elif "shortest paths" not in ta:
        sp.append(0)    
    if "probabilities" in ta:
        prb.append(1)
    elif "probabilities" not in ta:
        prb.append(0)    
    if "divide and conquer" in ta:
        dc.append(1)
    elif "divide and conquer" not in ta:
        dc.append(0)    
    if "hashing" in ta: 
        hs.append(1)
    elif "hashing" not in ta:
        hs.append(0)    
    if "games" in ta:
        games.append(1)
    elif "games" not in ta:
        games.append(0)    
    if "flows" in ta:
        fw.append(1)
    elif "flows" not in ta:
        fw.append(0)    
    if "interactive" in ta:
        it.append(1)
    elif "interactive" not in ta:
        it.append(0)    
    if "matrices" in ta:
        mat.append(1)
    elif "matrices" not in ta:
        mat.append(0)    
    if "string suffix structures" in ta:
        sss.append(1)
    elif "string suffix structures" not in ta:
        sss.append(0)    
    if "fft" in ta:
        fft.append(1)
    elif "fft" not in ta:
        fft.append(0)    
    if "graph matchings" in ta:
        gm.append(1)
    elif "graph matchings" not in ta:
        gm.append(0)
    if "ternary search" in ta:
        ts.append(1)
    elif "ternary search" not in ta:
        ts.append(0)    
    if "expression parsing" in ta:
        ep.append(1)
    elif "expression parsing" not in ta:
        ep.append(0)
    if "meet-in-the-middle" in ta:
        mm.append(1)
    elif "meet-in-the-middle" not in ta:
        mm.append(0)    
    if "2-sat" in ta:
        sat.append(1)
    elif "2-sat" not in ta:
        sat.append(0)    
    if "chinese remainder theorem" in ta:
        ct.append(1)
    elif "chinese remainder theorem" not in ta:
        ct.append(0)    
    if "schedules" in ta:
        sch.append(1)
    elif "schedules" not in ta:
        sch.append(0)    




    for j in check:
        user_list.append(j.handle)

try:
    users = cf_api.user_info(user_list)
except:
    cnt+=1
for i in users:
    try:
        user_rating_list.append(i.rating)
    except:
        user_rating_list.append(0)
a = ({'Submission_Id':id_list,'User_Rating' :user_rating_list,'User_Name' :user_list,'Tags':tags_list,'Problem_Rating':problemrating_list, 'Implementation': imp , 'Maths': math, 'Greedy': greedy, 'dp': dp,
'Sorting': sot, 'Bitmasks': bit, 'Constructive Algo': con, 'Data Structure': ds, 'Brute force':bt,'Graph':grp,'Binary Search':bs,'dfs and similar':dfs,'Trees':tree,'String': str,'Number Theory':nt,'Combinatorics':com,'Geometry':geo,'Two Pointers':tp,'dsu':dsu,'Shortest Paths':sp,'Probabilities':prb,'Divide and Conquer':dc,'Hashing':hs,'Games':games,'Flows':fw,'Interactive':it,'Matrices':mat,
'String Suffix Structures':sss,'fft':fft,'Graph Matchings':gm,'Ternary Search':ts,'Expression Parsing':ep,'Meet-in-the-Middle':mm,'2-sat':sat,'Chinese Remainder Theorem':ct,'Schedules':sch})
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
compression_opts = dict(method='zip',
                        archive_name='ProbRecco.csv')  
df.to_csv('IEProject.zip', index=False,
          compression=compression_opts)
