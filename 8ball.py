import random

eightball = ["● It is certain.", "● It is decidedly so.", "● Without a doubt.", "● Yes definitely.", "● You may rely on it.",
             "● As I see it, yes.", "● Reply hazy, try again.", "● Ask again later.", "● Better not tell you now."
             , "● Don't count on it.", "● My reply is no.", "● My sources say no.", "● Very doubtful"]

answer = input("Ask the 8-ball something (if not type in no): ")

while answer != "no":
    print(random.choice(eightball))
    answer = input("Ask the 8-ball something (if not type in no): ")
