# Moyo Fagbuyi, Margie Cao, Tim Ng
# Systems Level Programming
# SoftDev
# K04 -- Python dictionairies and random selection
# 2024-09-13
# time spent: 40/60

def pop():
    keys = list(krewes.keys())
    #keys -> lists of period
    keysLen = len(keys)
    x = random.randint(0, keysLen - 1)
    #x -> random int to get a random period
    vals = list(krewes.get(keys[x]))
    # vals -> list of students from the period
    valsLen = len(vals)
    y = random.randint(0, valsLen - 1)
    # y -> random int to get random student
    print(vals[y])
    
krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }
ducks = {4:[], 5:[]}

pd$$$devo$$$ducky@@@pd$$$devo$$$ducky@@@pd$$$devo$$$ducky@@@