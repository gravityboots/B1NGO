from functools import wraps
import os
import shutil
from datetime import datetime

from data import SESSIONS, SOLVES, CHALLENGES, STATUS, TEAMS

from flask import Flask
from flask import render_template, request, redirect, abort



# initialisation



app = Flask(__name__, static_folder="assets", static_url_path="")
print(f"Server started up at {datetime.now()}")


# data parser used in the admin page table display
@app.context_processor
def utility_processor():

    def filter_challenge_status(team, status):
        return ', '.join([chalcode for chalcode, metadata in SOLVES[team].items() if metadata['status']==status])
    
    def filter_team_systems(team):
        return '<br>'.join([system for system in SESSIONS if SESSIONS[system]==team])

    return dict(filter_challenge_status=filter_challenge_status, filter_team_systems=filter_team_systems)


def check_session(endpoint):

    @wraps(endpoint)
    def wrapper(*args, **kwargs):
        if request.remote_addr not in SESSIONS:
            return redirect('/login', code=302)
        return endpoint(*args, **kwargs)
    
    return wrapper



# webpages



# bingo home page
@app.route("/")
@check_session
def home_page():
    print(request.method)
    return render_template(
        'index.html', 
        team=SESSIONS[request.remote_addr],
        teams=TEAMS,
        solved=SOLVES[SESSIONS[request.remote_addr]],
        statuses=STATUS,
        challenges=[CHALLENGES[0:5],CHALLENGES[5:10],CHALLENGES[10:15],CHALLENGES[15:20],CHALLENGES[20:25]],
    )


# login page (for identifying team)
@app.route("/login", methods=["GET","POST"])
def login_page():
    if (ip:=request.remote_addr) in SESSIONS:
        return render_template(
            'login-retry.html',
            team=TEAMS[SESSIONS[ip]],
        )
    
    if request.method == 'POST':
        print(request.form)
        SESSIONS[request.remote_addr] = request.form.get('team', '')
        return redirect('/')

    return render_template(
        'login.html', 
        teams=TEAMS,
    )


# admin panel (for approving bingo challenge submissions)
@app.route("/admin", methods=["GET"])
def admin_page():
    if request.remote_addr not in ['localhost', '127.0.0.1']:
        abort(403) # Access Denied

    return render_template(
        'admin.html',
        statuses=STATUS,
        teams=TEAMS,
        chalcodes=[c[0] for c in CHALLENGES],
    )


# participants' challenge submission review page (admin panel redirect)
@app.route("/admin/submission", methods=["GET", "POST"])
def submission_review_page():
    if request.remote_addr not in ['localhost', '127.0.0.1']:
        abort(403) # Access Denied

    if request.method == 'GET':
        # display submission details with option to accept or reject
        try:
            # For GET params (visible in the URL), use request.args not request.form
            path = f"""submissions/{request.args.get('team')}/{request.args.get('challenge')}.txt"""
            with open(path, 'r') as f:
                code = f.read()
        except:
            return render_template('submission-missing.html'), 404 # Text and status

        return render_template('submission.html',
                    team=request.args.get('team'),
                    chalcode=request.args.get('challenge'),
                    subtime=SOLVES[request.args.get('team')][request.args.get('challenge')]['time'],
                    code=code,
                )

    elif request.method == 'POST':
        # save judge's verdict
        if request.form.get('accept'):
            SOLVES[request.args.get('team')][request.args.get('challenge')]['status'] = STATUS.ACCEPTED
        elif request.form.get('reject'):
            SOLVES[request.args.get('team')][request.args.get('challenge')]['status'] = STATUS.REJECTED
        elif request.form.get('hold'):
            SOLVES[request.args.get('team')][request.args.get('challenge')]['status'] = STATUS.UNDER_REVIEW
        else:
            SOLVES[request.args.get('team')][request.args.get('challenge')]['status'] = None

        return render_template('submission-post.html')


# bingo challenge page
@app.route("/challenge/<chalcode>", methods=['GET'])
@check_session
def challenge_page(chalcode):
    for i in range(len(CHALLENGES)):
        if CHALLENGES[i][0]==chalcode: c_i = i

    statusOrNone = SOLVES[SESSIONS[request.remote_addr]].get(chalcode, {}).get('status')
    c_name = CHALLENGES[c_i][1]
    c_info = CHALLENGES[c_i][2]

    prevcode = ''
    path = f"""submissions/{SESSIONS[request.remote_addr]}/{chalcode}.txt"""
    if os.path.isfile(path):
        with open(path, 'r') as f:
                prevcode = f.read()

    return render_template(
        'challenge.html',
        prevcode=prevcode,
        chalcode=chalcode,
        chalname=c_name,
        instructions=c_info,
        warnstatus=statusOrNone,
        statuses=STATUS
    )


# bingo post challenge submission page (user end)
@app.route("/submit/<chalcode>", methods=['POST'])
@check_session
def result_page(chalcode="0"):
    # Access any form field with `request.form[fieldname]` : <input name="..."
    code = request.form['submission']
    team = SESSIONS[request.remote_addr]
    print(f"\tForm Recieved for challenge {chalcode}! System: {team} ({request.remote_addr})\n")

    savepath = f'submissions/{team}/{chalcode}.txt'
    if not os.path.isdir(d:=f'submissions/{team}'):
        os.mkdir(d)
    with open(savepath, 'w') as f:
        f.write(code.replace('\r\n','\n'))

    SOLVES[team][chalcode] = {
        'time': datetime.now().isoformat(' '),
        'status': STATUS.UNDER_REVIEW
    }

    return render_template('challenge-post.html')


# bingo help page
@app.route("/help")
def help_page():
    return render_template('help.html')



# run



if __name__ == '__main__':
    try:
        # if os.path.isdir('submissions'): shutil.rmtree('submissions')
        if not os.path.isdir('submissions') : os.mkdir('submissions')
        app.run('0.0.0.0',777)
    finally:
        print(f"Server closed at {datetime.now()}")
