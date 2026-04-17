#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random
import sys

#Higher Lower Game.
#Who have most followers on iG.

#I don't think this uses some ig API so I will just use a hardcoded dictionary (y)

#just ask an AI to generate names of celebrities
celebrities = ["cristiano ronaldo","lionel messi","kylie jenner","selena gomez","dwayne johnson","ariana grande","kim kardashian","beyonce","khloe kardashian","justin bieber",
"kendall jenner","taylor swift","neymar jr","nicki minaj","jennifer lopez","virat kohli","miley cyrus","kourtney kardashian","kevin hart","demi lovato",
"rihanna","zendaya","tom holland","chris hemsworth","scarlett johansson","robert downey jr","will smith","jason statham","gal gadot","chris evans",
"mark wahlberg","drake","post malone","travis scott","billie eilish","dua lipa","ed sheeran","harry styles","zayn malik","niall horan",
"liam payne","louis tomlinson","shawn mendes","camila cabello","cardi b","megan thee stallion","doja cat","lizzo","bruno mars","usher",
"eminem","kanye west","jay z","snoop dogg","ice cube","the weeknd","bad bunny","j balvin","maluma","karol g",
"shakira","anuel aa","rosalia","becky g","daddy yankee","ozuna","farruko","pitbull","enrique iglesias","ricky martin",
"vin diesel","paul rudd","ryan reynolds","ryan gosling","hugh jackman","jake gyllenhaal","matt damon","ben affleck","leonardo dicaprio","brad pitt",
"angelina jolie","margot robbie","emma stone","emma watson","jennifer lawrence","anne hathaway","natalie portman","keira knightley","cate blanchett","sandra bullock",
"halle berry","nicole kidman","salma hayek","penelope cruz","eva longoria","sofia vergara","jessica alba","jessica chastain","gal gadot","millie bobby brown",
"noah schnapp","finn wolfhard","gaten matarazzo","caleb mclaughlin","sadie sink","timothee chalamet","anya taylor joy","florence pugh","austin butler","jacob elordi",
"zendaya coleman","hunter schafer","sydney sweeney","alexandra daddario","lily collins","hailee steinfeld","madison beer","addison rae","charli d amelio","dixie d amelio",
"bella hadid","gigi hadid","hailey bieber","kourtney kardashian barker","travis barker","machine gun kelly","halsey","ellie goulding","rita ora","ava max",
"clean bandit","calvin harris","david guetta","martin garrix","tiesto","skrillex","diplo","zedd","alan walker","kygo",
"steve aoki","marshmello","deadmau5","porter robinson","madeon","justice","daft punk","pharrell williams","tyler the creator","frank ocean",
"childish gambino","lil nas x","jack harlow","ice spice","central cee","stormzy","skepta","aj tracey","dave","little simz",
"burna boy","wizkid","tems","tiwa savage","davido","diamond platnumz","yemi alade","cassper nyovest","aka rapper","black coffee",
"conor mcgregor","khabib nurmagomedov","israel adesanya","jon jones","anderson silva","ronda rousey","valentina shevchenko","amanda nunes","francis ngannou","alex pereira"]

instagram_followers = {}
guess = ""
score = 0
user_guess = ""
celebrity_one = random.choice(celebrities)
celebrity_two = ""
celebrity_with_more_followers = ""

for c in celebrities:
    instagram_followers[c] = random.randint(1000000,100000000)

def evaluate_win_condition():
    return celebrity_with_more_followers == user_guess

def game():
    global guess,score,user_guess, celebrity_two, celebrity_with_more_followers
    celebrity_two = random.choice(celebrities)
    guess = input(f"Who has more followers? \n "
                  f"{celebrity_one} or {celebrity_two}"
                  f" Type 'A' or 'B': \n")
    if guess.lower() != "a" and guess.lower() != "b":
        print("unknown input existing program... :)")
        sys.exit()
    user_guess = celebrity_one if guess.lower() == "a" else celebrity_two
    celebrity_with_more_followers = celebrity_one if instagram_followers[celebrity_one] > instagram_followers[celebrity_two] else celebrity_two

def finish_game():
    print(f"{celebrity_one} has {instagram_followers[celebrity_one]}! \n")
    print(f"{celebrity_two} has {instagram_followers[celebrity_two]}! \n")
    print(f"you lose, final score: {score}")
    sys.exit()

def main():
    global score, celebrity_one
    print("Higher Lower game! :D")
    while evaluate_win_condition():
        game()
        if not evaluate_win_condition():
           finish_game()
        score += 1
        print("score: ",score)
        celebrity_one = celebrity_with_more_followers
    finish_game()

main()


