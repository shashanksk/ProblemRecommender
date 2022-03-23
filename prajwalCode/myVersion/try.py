from email import parser
import pandas as pd
import codeforces_api
import time


parser = codeforces_api.CodeforcesParser()
cf_api = codeforces_api.CodeforcesApi()

i = 0

df = pd.read_csv("gg.csv")

rated_list = 0
for k in range(20115):

    list = []
    Su = []
    correct = 0.0
    total = 1.0
    try:
        user_submissions = cf_api.user_status(
            df.iloc[k]['User_Name'], start=1, count=100)
    except:
        rated_list = -1
        continue

    try:
        for i in user_submissions:

            if int(i.id) > int(df.iloc[k]['Submission_Id']):

                ta = i.problem.tags

                list.append(ta)
                Su.append(i.id)

            # this is to convert the string to a list
            str = df.loc[k]['Tags']
            str = str.replace(",", "")
            str = str.replace("[", "")
            str = str.replace("]", "")
            str = str.replace("'", "")

            list_1 = str.split()
            # print(list_1, "<--list_1 is")

            for j in list_1:
                ta = i.problem.tags
                for z in ta:
                    if z == j:
                        total = total+1
                        if i.verdict == 'OK':
                            correct = correct+1
                        break
        rated_list = correct/total
        time.sleep(2)
        print("working")

    except:
        print("Hello")
        rated_list = -1

    df = pd.DataFrame(rated_list)

    # append data frame to CSV file
    df.to_csv('try.csv', mode='a', index=False, header=False)

    # print message
    print("Data appended successfully.")
