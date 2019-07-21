import random,json,os,operator
from quiz import getLevelLen
scoring={}
def load_json_to_python():
    global scoring
    if os.path.exists("scoring.json"):
        scoring_file=open("scoring.json","r")
        scoring = json.load(scoring_file)
        scoring_file.close()
    else:
        for i in range(getLevelLen()):
            scoring["Level_"+str(i+1)]={}


def load_python_to_json():
    global scoring
    scoring_file=open("scoring.json","w")
    scoring_file.write(json.dumps(scoring))
    scoring_file.close()

def save_scoring(level,score,name):
    global scoring
    if (name in scoring["Level_"+str(level)] and scoring["Level_"+str(level)][name]<score) or (name not in scoring["Level_"+str(level)]):
        scoring["Level_"+str(level)][name]=score
        print("Your new score is:"+str(score))


def display_scoring(level):
    print("""
        SCORING FOR LEVEL {}
        ____________________
    """.format(level))
    sorted_d = sorted(scoring["Level_"+str(level)].items(), key=operator.itemgetter(1), reverse=True)
    for k,v in sorted_d:
        print("\t\t{}________{}".format(k,v))