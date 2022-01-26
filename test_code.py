import time
import codeforces_api
import pandas as pd

parser = codeforces_api.CodeforcesParser()
cf_api = codeforces_api.CodeforcesApi()

test = cf_api.problemset_recent_status(1000, problemset_name="")

# lists for data collection======================================
id_list = []
tags_list = []
user_list = []
problemrating_list = []
user_rating_list = []
problemindex_list = []

# driver program to create the code==============================
for i in test:
    ta = i.problem.tags
    check = i.author.members
    # print(i.id,':')
    id_list.append(i.id)
    problemrating_list.append(i.problem.rating)
    tags_list.append(ta)
    cnt = 0
    for j in check:
        user_list.append(j.handle)

try:
    users = cf_api.user_info(user_list)
except:
    cnt += 1
for i in users:
    try:
        user_rating_list.append(i.rating)
    except:
        user_rating_list.append(0)

# panda buizness is going on=====================================
a = ({'Submission_Id': id_list, 'User_Rating': user_rating_list,
     'User_Name': user_list, 'Tags': tags_list, 'Problem_Rating': problemrating_list})
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
compression_opts = dict(method='zip',
                        archive_name='ProbRecco.csv')
# conversion to csv==============================================
df.to_csv('IEProject.zip', index=False,
          compression=compression_opts)

# program end====================================================