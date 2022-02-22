from email import parser
import pandas as pd
import codeforces_api
import time


parser = codeforces_api.CodeforcesParser()
cf_api = codeforces_api.CodeforcesApi()

i = 0

df = pd.read_csv("csv_files/prob_rec_csv_file_yo_2.csv")
# print(df)
rated_list = []
for k in range(1):
    print(df.iloc[k]['User_Name'])
    list = []
    Su = []
    correct = 0.0
    total = 1.0
    user_submissions = cf_api.user_status(
        df.iloc[k]['User_Name'], start=1, count=100)

    print(type(user_submissions))  # returns a class <list>

    for i in user_submissions:

        print("user_srbmission for loop ran")
        # time.sleep(5)

        if i.id > df.iloc[k]['Submission_Id']:

            ta = i.problem.tags
            # print(ta)//debugger to see tafuq is ta
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
                print(z, "<---hey its the line that prints z--->", j, "\n")
                if z == j:
                    total = total+1
                    if i.verdict == 'OK':
                        correct = correct+1
                    break

    rated_list.append(correct/total)
    time.sleep(2)
