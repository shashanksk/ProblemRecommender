# importing Flask and other modules
from flask import Flask, request, render_template
import pickle
import codeforces_api
import random

cf_api = codeforces_api.CodeforcesApi()
# Flask constructor
app = Flask(__name__)


def predict(user_handle, user_pref):
    with open('./IEP_data_save.data', 'rb') as f:
        f_lst = pickle.load(f)
    test = cf_api.user_status(user_handle, 1000)
    problem_set_solved = set()
    p_id = []

    for i in test:
        problem_name = f"{i.problem.contest_id}{i.problem.index}{i.problem.name}"
        p_id.append(i.problem.contest_id)
        problem_set_solved.add(problem_name)
    problem_set_solved = sorted(problem_set_solved)

    value_for_cluster = [0]*1000
    maxx = 0
    minn = 10000
    pos = 1
    f_lst = sorted(f_lst)

    for i in problem_set_solved:
        problem = i
        for x, j in enumerate(f_lst):
            if(problem in j):
                value_for_cluster[x] += 1
                break

    if(user_pref == '1'):
        for i in range(0, len(value_for_cluster)):
            if(maxx < value_for_cluster[i]):
                pos = i
                maxx = value_for_cluster[i]

    elif(user_pref == '2'):
        for i in range(0, len(value_for_cluster)):
            if(minn > value_for_cluster[i]):
                pos = i
                minn = value_for_cluster[i]

    print(value_for_cluster)
    n = random.randint(0, len(f_lst[pos])-1)
    print(pos)
    # print(value_for_cluster)
    return f_lst[pos][n]
# A decorator used to tell the application
# which URL is associated function


@app.route('/', methods=["GET", "POST"])
def predictor():
    if request.method == "POST":
        print(request.form)
        user_handle = request.form.get('user_handle', 'test')
        user_pref = request.form.get('user_pref', 'test')
        # print(user_handle)
        output = predict(user_handle, user_pref)
        return output
    return render_template("form.html")


if __name__ == '__main__':
    app.run()
