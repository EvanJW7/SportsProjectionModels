import numpy as np
import pandas as pd
def game_projection(spread0, total, percent_of_bets, favteam, underdog):
    if spread0<0:
        spread = spread0 *-1
    else:
        spread = spread0
    betsfinal = (percent_of_bets)/100
    optimizer = (spread + ((.5 - betsfinal)*30))
    ospread = float(format(optimizer, ".2"))
    x = ((total + ospread)/2)
    y = total - x
    total = x + y
    ospread = x - y
    print(f"\nThe projected outcome of the game is:\n")
    favtotal = f"{favteam.title():<15}{x:>1}"
    print(favtotal)
    dogtotal = f"{underdog.title():<15}{y:>1}"
    print(dogtotal)
    format_ospread = "{:.1f}".format(ospread)
    format_ospread = float(format_ospread)*-1
    if format_ospread <0:
        points_final = round(format_ospread)*-1
        if points_final == 1:
            print(f"\nThe {favteam.title()} are projected to win by about {points_final} point")
        if points_final >1:
            print(f"\nThe {favteam.title()} are projected to win by about {points_final} points")
    if format_ospread>0:
        ospread_final = round(format_ospread)
        if ospread_final == 1:
            print(f"\nUpset Alert! The {underdog.title()} are projected to win by about {ospread_final} point")
        else:
            print(f"\nUpset Alert! The {underdog.title()} are projected to win by about {ospread_final} points")

    print(f"\nOriginal Spread: {spread0}")
    print(f"\bOptimized Spread: {format_ospread}\n")
    #BET SUGGESTION
    print("Bet Suggestion: ")
    bet1 = spread0
    bet2 = format_ospread
    bet = bet1 - bet2
    if bet <=-5 and format_ospread >=4:
        print(f"Bet the moneline on the {underdog.title()}")
    if bet <=-5 and format_ospread <4:
        print(f"Bet the spread on the {underdog.title()}")
    if bet <=-5 and format_ospread <0:
        print(f"Bet the spread on the {underdog.title()}")
    if -5<bet<-3:
        print(f"Bet the spread on the {underdog.title()}")
    if -3<=bet<=3:
        print("Do not bet on this game, there isn't enough edge")
    if 3<bet<5:
        print(f"Bet the moneline on the {favteam.title()}")
    if bet>=5:
        print(f"Bet the spread on the {favteam.title()}")
    start = 0
    f1 = x/4  
    f2 = x/4+ x/4
    f3 = x/4 + x/4 + x/4 
    f4 = x/4 + x/4 + x/4 + x/4
    favteam_points = start, f1, f2, f3, f4
    favteam_points = tuple([float("{0:.2f}".format(n)) for n in favteam_points])
    u1 = y/4
    u2 = y/4+ y/4  
    u3 = y/4 + y/4 + y/4  
    u4 = y/4 + y/4 + y/4 + y/4
    underdog_points = start, u1, u2, u3, u4
    underdog_points = tuple([float("{0:.2f}".format(n)) for n in underdog_points])
    from pandas import DataFrame
    f1 = "{:.1f}".format(f1)
    f2 = "{:.1f}".format(f2)
    f3 = "{:.1f}".format(f3)
    f4 = "{:.1f}".format(f4)
    u1 = "{:.1f}".format(u1)
    u2 = "{:.1f}".format(u2)
    u3 = "{:.1f}".format(u3)
    u4 = "{:.1f}".format(u4)
    boxscore = {
        "1": [f1, u1],
        "2": [f2, u2],
        "3": [f3, u3],
        "4": [f4, u4]
        
    }
    rows = favteam.title(), underdog.title()
    data = pd.DataFrame(boxscore, rows)
    
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize = (12,9))
    Quarter = ['0','15','Halftime','45', '60']
    Points1 = favteam_points
    Points2 = underdog_points
    def getcolor(favteam):
        if favteam == 'cardinals':
            colors = 'red'
        if favteam == 'falcons':
            colors = 'tab:red'
        if favteam == 'panthers':
            colors = 'tab:cyan'
        if favteam == 'bears':
            colors = 'midnightblue'
        if favteam == 'cowboys':
            colors = 'mediumblue'
        if favteam == 'lions':
            colors = 'dodgerblue'
        if favteam == 'packers':
            colors = 'gold'
        if favteam == 'rams':
            colors = 'royalblue'
        if favteam == 'vikings':
            colors = 'darkviolet'
        if favteam == 'saints':
            colors = 'goldenrod'
        if favteam == 'giants':
            colors = 'blue'
        if favteam == 'eagles':
            colors = 'mediumseagreen'
        if favteam == '49ers':
            colors = 'brown'
        if favteam == 'seahawks':
            colors = 'teal'
        if favteam == 'bucs':
            colors = 'maroon'
        if favteam == 'buccaneers':
            colors = 'maroon'
        if favteam == 'football team':
            colors = 'firebrick'
        if favteam == 'washington':
            colors = 'firebrick'
        if favteam == 'ravens':
            colors = 'indigo'
        if favteam == 'bills':
            colors = 'royalblue'
        if favteam == 'bengals':
            colors = 'darkorange'
        if favteam == 'browns':
            colors = 'tab:brown'
        if favteam == 'broncos':
            colors = 'tab:orange'
        if favteam == 'texans':
            colors = 'navy'
        if favteam == 'colts':
            colors = 'deepskyblue'
        if favteam == 'jags':
            colors = 'limegreen'
        if favteam == 'jaguars':
            colors = 'limegreen'
        if favteam == 'chiefs':
            colors = 'orangered'
        if favteam == 'raiders':
            colors = 'slategray'
        if favteam == 'chargers':
            colors = 'lightskyblue'
        if favteam == 'dolphins':
            colors = 'cyan'
        if favteam == 'patriots':
            colors = 'midnightblue'
        if favteam == 'jets':
            colors = 'green'
        if favteam == 'steelers':
            colors = 'black'
        if favteam == 'titans':
            colors = 'mediumturquoise'
        return colors
    
    def getcolor(underdog):
        if underdog == 'cardinals':
            coloru = 'red'
        if underdog == 'falcons':
            coloru = 'tab:red'
        if underdog == 'panthers':
            coloru = 'tab:cyan'
        if underdog == 'bears':
            coloru = 'midnightblue'
        if underdog == 'cowboys':
            coloru = 'mediumblue'
        if underdog == 'lions':
            coloru = 'dodgerblue'
        if underdog == 'packers':
            coloru = 'gold'
        if underdog == 'rams':
            coloru = 'royalblue'
        if underdog == 'vikings':
            coloru = 'darkviolet'
        if underdog == 'saints':
            coloru = 'goldenrod'
        if underdog == 'giants':
            coloru = 'blue'
        if underdog == 'eagles':
            coloru = 'mediumseagreen'
        if underdog == '49ers':
            coloru = 'brown'
        if underdog == 'seahawks':
            coloru = 'teal'
        if underdog == 'bucs':
            coloru = 'maroon'
        if underdog == 'buccaneers':
            coloru = 'maroon'
        if underdog == 'football team':
            coloru = 'firebrick'
        if underdog == 'washington':
            coloru = 'firebrick'
        if underdog == 'ravens':
            coloru = 'indigo'
        if underdog == 'bills':
            coloru = 'royalblue'
        if underdog == 'bengals':
            coloru = 'darkorange'
        if underdog == 'browns':
            coloru = 'tab:brown'
        if underdog == 'broncos':
            coloru = 'tab:orange'
        if underdog == 'texans':
            coloru = 'navy'
        if underdog == 'colts':
            coloru = 'deepskyblue'
        if underdog == 'jags':
            coloru = 'limegreen'
        if underdog == 'jaguars':
            coloru = 'limegreen'
        if underdog == 'chiefs':
            coloru = 'orangered'
        if underdog == 'raiders':
            coloru = 'slategray'
        if underdog == 'chargers':
            coloru = 'lightskyblue'
        if underdog == 'dolphins':
            coloru = 'cyan'
        if underdog == 'patriots':
            coloru = 'midnightblue'
        if underdog == 'jets':
            coloru = 'green'
        if underdog == 'steelers':
            coloru = 'black'
        if underdog == 'titans':
            coloru = 'mediumturquoise'
        return coloru
    
    plt.plot(Quarter, Points1, label = favteam.title(), color = getcolor(favteam), lw = 1, marker = '*', ms = 10)
    plt.plot(Quarter, Points2, label = underdog.title(), color = getcolor(underdog), lw = 1, marker = '*', ms = 10)
    plt.title('Game Spread Projection')
    plt.xlabel('Quarter (in minutes)')
    plt.ylabel('Expected Points')
    plt.legend(fontsize = 'large', loc=9)
    plt.style.use('fivethirtyeight')
    plt.show()
    print("\nBox Score Projection:")
    print(data)
a = float(input("Spread: "))
b = float(input("Over/Under: "))
c = float(input(f"Percent of bets on the favorite: "))
d = input("Favorite: ")
d = d.lower()
e = input("Underdog: ")
e = e.lower()

game_projection(a, b, c, d, e)