def get_highscores(name) :
    o = open("scores.txt",'r')
    a = o.readlines()
    o.close()
    scores = {}
    
    def get_topten(dic):
        t = [None,None]
        for i in dic :
            if dic[i] >t[1] :
                t = [i,dic[i]]
        return t
    def get_my_rank(me,dic) :
        rank = 1
        score = dic[me]
        for i in dic :
            if dic[i] > score :
                rank += 1
        return rank

    
    for i in a :
        for j in range(len(i)) :
            if i[j] == ":" :
                break
        
        scores[i[:j]] = int(i[j+1:])

    top_ten = []
    my_score = scores[name]
    my_rank = get_my_rank(name,scores)
    for i in range (10 ) :
        top_ten.append(get_topten(scores))
        del scores[get_topten(scores)[0]]
        if len(scores) == 0 :
            break
    if len(scores) < 10 :
        for i in range(10 - len(scores)) :
            top_ten.append(["",""])
    

    print """------------------------------------------------------------------------------------------
                                HIGH  SCORES
-------------------------------------------------------------------------------------------
 1)  %-20s\t\t\t%5s
 2)  %-20s\t\t\t%5s
 3)  %-20s\t\t\t%5s
 4)  %-20s\t\t\t%5s
 5)  %-20s\t\t\t%5s
 6)  %-20s\t\t\t%5s
 7)  %-20s\t\t\t%5s
 8)  %-20s\t\t\t%5s
 9)  %-20s\t\t\t%5s
 10) %-20s\t\t\t%5s


 You :  Rank = %s    Score = %s"""%(top_ten[0][0],top_ten[0][1],top_ten[1][0],top_ten[1][1],top_ten[2][0],top_ten[2][1],top_ten[3][0],top_ten[3][1],
                                    top_ten[4][0],top_ten[4][1],top_ten[5][0],top_ten[5][1],top_ten[6][0],top_ten[6][1],top_ten[7][0],top_ten[7][1],
                                    top_ten[8][0],top_ten[8][1],top_ten[9][0],top_ten[9][1],my_rank,my_score)





