# Fairness checker for dice.
#
#  Output log format is exact the same as on the Eric's Harshbarger site:
#  http://www.ericharshbarger.org/dice/4d12_fairness_report.txt
#
# Dariusz Chilimoniuk, 2017, http://stack.pl

import sys
import hashlib, binascii

def report2dices(diceset, a, b):
    print('-----------------------------------')
    cnt = 0
    score = {}
    for ranking in report2dicesStep(diceset, a, b):
        cnt += 1
        if ranking in score:
            score[ranking] += 1
        else:
            score[ranking] = 1
    print()
    expected_value = list(score.values())[0]
    result = True
    for r in sorted(score):
        print('Ranking [' + r + '] occurs ' + str(score[r]) + ' out of ' + str(cnt) + ' times.')
        if expected_value != score[r]:
            result = False
    return result

def report2dicesStep(diceset, a, b):
    print('Dice Compared: #' + str(a) + ', #' + str(b))
    # how many walls is in a dice
    facecount = len(list(diceset[0]))
    ranking = ''
    cnt = 0
    for b_value in diceset[b-1]:
        for a_value in diceset[a-1]:
            cnt += 1
            print('  Outcome ' + str(cnt) + ': D' + str(a) + '=' + str(a_value) + '  D' + str(b) + '=' + str(b_value) + '  ', end='')
            rankDict = {}
            rankDict[a_value] = 'D' + str(a)
            rankDict[b_value] = 'D' + str(b)  
            ranking = '' 
            for k in sorted(rankDict, reverse=True):
                ranking += rankDict[k] + ','
            ranking = ranking[:-1]
            print('Ranking: ' + ranking)
            yield ranking

def report3dices(diceset, a, b, c):
    print('-----------------------------------')
    cnt = 0
    score = {}
    for ranking in report3dicesStep(diceset, a, b, c):
        cnt += 1
        if ranking in score:
            score[ranking] += 1
        else:
            score[ranking] = 1
    print()
    expected_value = list(score.values())[0]
    result = True
    for r in sorted(score):
        print('Ranking [' + r + '] occurs ' + str(score[r]) + ' out of ' + str(cnt) + ' times.')
        if expected_value != score[r]:
            result = False
    return result

def report3dicesStep(diceset, a, b, c):
    print('Dice Compared: #' + str(a) + ', #' + str(b) + ', #' + str(c))
    # how many walls is in a dice
    facecount = len(list(diceset[0]))
    ranking = ''
    cnt = 0
    for c_value in diceset[c-1]: 
        for b_value in diceset[b-1]:
            for a_value in diceset[a-1]:
                cnt += 1
                print('  Outcome ' + str(cnt) + ': D' + str(a) + '=' + str(a_value) + '  D' + str(b) + '=' + str(b_value)+ '  D' + str(c) + '=' + str(c_value) + '  ', end='')
                rankDict = {}
                rankDict[a_value] = 'D' + str(a)
                rankDict[b_value] = 'D' + str(b)  
                rankDict[c_value] = 'D' + str(c)  
                ranking = '' 
                for k in sorted(rankDict, reverse=True):
                    ranking += rankDict[k] + ','
                ranking = ranking[:-1]
                print('Ranking: ' + ranking)
                yield ranking

def report4dices(diceset, a, b, c, d):
    print('-----------------------------------')
    cnt = 0
    score = {}
    for ranking in report4dicesStep(diceset, a, b, c, d):
        cnt += 1
        if ranking in score:
            score[ranking] += 1
        else:
            score[ranking] = 1
    print()
    expected_value = list(score.values())[0]
    result = True
    for r in sorted(score):
        print('Ranking [' + r + '] occurs ' + str(score[r]) + ' out of ' + str(cnt) + ' times.')
        if expected_value != score[r]:
            result = False
    return result

def report4dicesStep(diceset, a, b, c, d):
    print('Dice Compared: #' + str(a) + ', #' + str(b) + ', #' + str(c) + ', #' + str(d))
    # how many walls is in a dice
    facecount = len(list(diceset[0]))
    ranking = ''
    cnt = 0
    for d_value in diceset[d-1]:
        for c_value in diceset[c-1]: 
            for b_value in diceset[b-1]:
                for a_value in diceset[a-1]:
                    cnt += 1
                    print('  Outcome ' + str(cnt) + ': D' + str(a) + '=' + str(a_value) + '  D' + str(b) + '=' + str(b_value) + '  D' + str(c) + '=' + str(c_value) + '  D' + str(d) + '=' + str(d_value) + '  ', end='')
                    rankDict = {}
                    rankDict[a_value] = 'D' + str(a)
                    rankDict[b_value] = 'D' + str(b)  
                    rankDict[c_value] = 'D' + str(c)  
                    rankDict[d_value] = 'D' + str(d) 
                    ranking = '' 
                    for k in sorted(rankDict, reverse=True):
                        ranking += rankDict[k] + ','
                    ranking = ranking[:-1]
                    print('Ranking: ' + ranking)
                    yield ranking

def report5dices(diceset, a, b, c, d, e):
    print('-----------------------------------')
    cnt = 0
    score = {}
    for ranking in report5dicesStep(diceset, a, b, c, d, e):
        cnt += 1
        if ranking in score:
            score[ranking] += 1
        else:
            score[ranking] = 1
    print()
    expected_value = list(score.values())[0]
    result = True
    for r in sorted(score):
        print('Ranking [' + r + '] occurs ' + str(score[r]) + ' out of ' + str(cnt) + ' times.')
        if expected_value != score[r]:
            result = False
    return result

def report5dicesStep(diceset, a, b, c, d, e):
    print('Dice Compared: #' + str(a) + ', #' + str(b) + ', #' + str(c) + ', #' + str(d) + ', #' + str(e))
    # how many walls is in a dice
    facecount = len(list(diceset[0]))
    ranking = ''
    cnt = 0
    for e_value in diceset[e-1]:
        for d_value in diceset[d-1]:
            for c_value in diceset[c-1]: 
                for b_value in diceset[b-1]:
                    for a_value in diceset[a-1]:
                        cnt += 1
                        print('  Outcome ' + str(cnt) + ': D' + str(a) + '=' + str(a_value) + '  D' + str(b) + '=' + str(b_value) + '  D' + str(c) + '=' + str(c_value) + '  D' + str(d) + '=' + str(d_value) + '  D' + str(e) + '=' + str(e_value) + '  ', end='')
                        rankDict = {}
                        rankDict[a_value] = 'D' + str(a)
                        rankDict[b_value] = 'D' + str(b)  
                        rankDict[c_value] = 'D' + str(c)  
                        rankDict[d_value] = 'D' + str(d) 
                        rankDict[e_value] = 'D' + str(e)
                        ranking = '' 
                        for k in sorted(rankDict, reverse=True):
                            ranking += rankDict[k] + ','
                        ranking = ranking[:-1]
                        print('Ranking: ' + ranking)
                        yield ranking

def report6dices(diceset, a, b, c, d, e, f):
    print('-----------------------------------')
    cnt = 0
    score = {}
    for ranking in report6dicesStep(diceset, a, b, c, d, e, f):
        cnt += 1
        if ranking in score:
            score[ranking] += 1
        else:
            score[ranking] = 1
    print()
    expected_value = list(score.values())[0]
    result = True
    for r in sorted(score):
        print('Ranking [' + r + '] occurs ' + str(score[r]) + ' out of ' + str(cnt) + ' times.')
        if expected_value != score[r]:
            result = False
    return result

def report6dicesStep(diceset, a, b, c, d, e, f):
    print('Dice Compared: #' + str(a) + ', #' + str(b) + ', #' + str(c) + ', #' + str(d) + ', #' + str(e) + ', #' + str(f))
    # how many walls is in a dice
    facecount = len(list(diceset[0]))
    ranking = ''
    cnt = 0
    for f_value in diceset[f-1]:
        for e_value in diceset[e-1]:
            for d_value in diceset[d-1]:
                for c_value in diceset[c-1]: 
                    for b_value in diceset[b-1]:
                        for a_value in diceset[a-1]:
                            cnt += 1
                            print('  Outcome ' + str(cnt) + ': D' + str(a) + '=' + str(a_value) + '  D' + str(b) + '=' + str(b_value) + '  D' + str(c) + '=' + str(c_value) + '  D' + str(d) + '=' + str(d_value) + '  D' + str(e) + '=' + str(e_value)+ '  D' + str(f) + '=' + str(f_value) + '  ', end='')
                            rankDict = {}
                            rankDict[a_value] = 'D' + str(a)
                            rankDict[b_value] = 'D' + str(b)  
                            rankDict[c_value] = 'D' + str(c)  
                            rankDict[d_value] = 'D' + str(d) 
                            rankDict[e_value] = 'D' + str(e)
                            rankDict[f_value] = 'D' + str(f)
                            ranking = '' 
                            for k in sorted(rankDict, reverse=True):
                                ranking += rankDict[k] + ','
                            ranking = ranking[:-1]
                            print('Ranking: ' + ranking)
                            yield ranking

def fairness_report(diceset):
    # HEAD
    print('Fairness Report')
    print('DICE COUNT:', len(diceset))
    facecount = len(list(diceset[0]))
    print('FACE COUNT:', facecount)
    for d in range(len(diceset)):
        if len(diceset[d]) != facecount:
            print("ERROR: DIFFERENT FACECOUNT IN DICES ")
            return
        print('D' + str(d+1) + ':', str(diceset[d])[1:-1].replace(' ', ''), end='')
        print()

    # REPORTS
    if len(diceset) == 2:
        result = ( 
                    report2dices(diceset, 1, 2)
                )
    elif len(diceset) == 3:
        # we want run every report
        result1 = report2dices(diceset, 1, 2)
        result2 = report2dices(diceset, 1, 3)
        result3 = report2dices(diceset, 2, 3)
        result4 = report3dices(diceset, 1, 2, 3)
        result = (result1 and result2 and result3 and result4)
    elif len(diceset) == 4:
        result1 = report2dices(diceset, 1, 2)
        result2 = report2dices(diceset, 1, 3)
        result3 = report2dices(diceset, 1, 4) 
        result4 = report2dices(diceset, 2, 3)
        result5 = report2dices(diceset, 2, 4)
        result6 = report2dices(diceset, 3, 4)
        result7 = report3dices(diceset, 1, 2, 3)
        result8 = report3dices(diceset, 1, 2, 4)
        result9 = report3dices(diceset, 1, 3, 4)
        result10 = report3dices(diceset, 2, 3, 4)
        result11 = report4dices(diceset, 1, 2, 3, 4)
        result = (result1 and result2 and result3 and result4 and result5 and 
            result6 and result7 and result8 and result9 and result10 and result11)
    elif len(diceset) == 5:
        result1 = report2dices(diceset, 1, 2)
        result2 = report2dices(diceset, 1, 3)
        result3 = report2dices(diceset, 1, 4) 
        result4 = report2dices(diceset, 1, 5) 
        result5 = report2dices(diceset, 2, 3)
        result6 = report2dices(diceset, 2, 4)
        result7 = report2dices(diceset, 2, 5)
        result8 = report2dices(diceset, 3, 4)
        result9 = report2dices(diceset, 3, 5)
        result10 = report2dices(diceset, 4, 5)
        result11 = report3dices(diceset, 1, 2, 3)
        result12 = report3dices(diceset, 1, 2, 4)
        result13 = report3dices(diceset, 1, 2, 5)
        result14 = report3dices(diceset, 1, 3, 4)
        result15 = report3dices(diceset, 1, 3, 5)
        result16 = report3dices(diceset, 1, 4, 5)
        result17 = report3dices(diceset, 2, 3, 4)
        result18 = report3dices(diceset, 2, 3, 5)
        result19 = report3dices(diceset, 2, 4, 5)
        result20 = report3dices(diceset, 3, 4, 5)
        result21 = report4dices(diceset, 1, 2, 3, 4)
        result22 = report4dices(diceset, 1, 2, 3, 5)
        result23 = report4dices(diceset, 1, 2, 4, 5)
        result24 = report4dices(diceset, 1, 3, 4, 5)
        result25 = report4dices(diceset, 2, 3, 4, 5)
        result26 = report5dices(diceset, 1, 2, 3, 4, 5)
        result = (result1 and result2 and result3 and result4 and result5 and result6 and
                 result7 and result8 and result9 and result10 and result11 and result12 and
                 result13 and result14 and result15 and result16 and result17 and result18 and 
                 result19 and result20 and result21 and result22 and result23 and result24 and
                 result25 and result26)
    elif len(diceset) == 6:
        result1 = report2dices(diceset, 1, 2)
        result2 = report2dices(diceset, 1, 3)
        result3 = report2dices(diceset, 1, 4) 
        result4 = report2dices(diceset, 1, 5)
        result5 = report2dices(diceset, 1, 6)
        result6 = report2dices(diceset, 2, 3)
        result7 = report2dices(diceset, 2, 4)
        result8 = report2dices(diceset, 2, 5)
        result9 = report2dices(diceset, 2, 6)
        result10 = report2dices(diceset, 3, 4)
        result11 = report2dices(diceset, 3, 5)
        result12 = report2dices(diceset, 3, 6)
        result13 = report2dices(diceset, 4, 5)
        result14 = report2dices(diceset, 4, 6)
        result15 = report2dices(diceset, 5, 6)
        result16 = report3dices(diceset, 1, 2, 3)
        result17 = report3dices(diceset, 1, 2, 4)
        result18 = report3dices(diceset, 1, 2, 5)
        result19 = report3dices(diceset, 1, 2, 6)
        result20 = report3dices(diceset, 1, 3, 4)
        result21 = report3dices(diceset, 1, 3, 5)
        result22 = report3dices(diceset, 1, 3, 6)
        result23 = report3dices(diceset, 1, 4, 5)
        result24 = report3dices(diceset, 1, 4, 6)
        result25 = report3dices(diceset, 1, 5, 6)
        result26 = report3dices(diceset, 2, 3, 4)
        result27 = report3dices(diceset, 2, 3, 5)
        result28 = report3dices(diceset, 2, 3, 6)
        result29 = report3dices(diceset, 2, 4, 5)
        result30 = report3dices(diceset, 2, 4, 6) 
        result31 = report3dices(diceset, 2, 5, 6) 
        result32 = report3dices(diceset, 3, 4, 5)
        result33 = report3dices(diceset, 3, 4, 6)
        result34 = report3dices(diceset, 3, 5, 6) 
        result35 = report3dices(diceset, 4, 5, 6) 
        result36 = report4dices(diceset, 1, 2, 3, 4)
        result37 = report4dices(diceset, 1, 2, 3, 5)
        result38 = report4dices(diceset, 1, 2, 3, 6)
        result39 = report4dices(diceset, 1, 2, 4, 5)
        result40 = report4dices(diceset, 1, 2, 4, 6)
        result41 = report4dices(diceset, 1, 2, 5, 6)
        result42 = report4dices(diceset, 1, 3, 4, 5)
        result43 = report4dices(diceset, 1, 3, 4, 6)
        result44 = report4dices(diceset, 1, 3, 5, 6)
        result45 = report4dices(diceset, 1, 4, 5, 6)
        result46 = report4dices(diceset, 2, 3, 4, 5)
        result47 = report4dices(diceset, 2, 3, 4, 6)
        result48 = report4dices(diceset, 2, 3, 5, 6)
        result49 = report4dices(diceset, 2, 4, 5, 6)
        result50 = report4dices(diceset, 3, 4, 5, 6)
        result51 = report5dices(diceset, 1, 2, 3, 4, 5)
        result52 = report5dices(diceset, 1, 2, 3, 4, 6)
        result53 = report5dices(diceset, 1, 2, 3, 5, 6)
        result54 = report5dices(diceset, 1, 2, 4, 5, 6)
        result55 = report5dices(diceset, 1, 3, 4, 5, 6)
        result56 = report5dices(diceset, 2, 3, 4, 5, 6)
        result57 = report6dices(diceset, 1, 2, 3, 4, 5, 6)
        result = (
            result1 and result2 and result3 and result4 and result5 and
            result6 and result7 and result8 and result9 and result10 and
            result11 and result12 and result13 and result14 and result15 and
            result16 and result17 and result18 and result19 and result20 and
            result21 and result22 and result23 and result24 and result25 and
            result26 and result27 and result28 and result29 and result30 and
            result31 and result32 and result33 and result34 and result35 and
            result36 and result37 and result38 and result39 and result40 and
            result41 and result42 and result43 and result44 and result45 and
            result46 and result47 and result48 and result49 and result50 and
            result51 and result52 and result53 and result54 and result55 and
            result56 and result57
        )
    else:
        print()
        print("Error: Supported number of dice: 2, 3, 4, 5 or 6.")
        sys.exit(-1)

    if result == True:
        print('**************')
        print('* OK,  FAIR! *')
        print('**************')
        d1 = str(sorted(diceset[0]))
        h1 = hashlib.blake2b(digest_size=8)
        h1.update(d1.encode('utf-8'))
        d1 += '  #' + h1.hexdigest()

        d2 = str(sorted(diceset[1]))
        h2 = hashlib.blake2b(digest_size=8)
        h2.update(d2.encode('utf-8'))
        d2 += '  #' + h2.hexdigest()

        if len(diceset) >= 3:
            d3 = str(sorted(diceset[2]))
            h3 = hashlib.blake2b(digest_size=8)
            h3.update(d3.encode('utf-8'))
            d3 += '  #' + h3.hexdigest()

        if len(diceset) >= 4:
            d4 = str(sorted(diceset[3]))
            h4 = hashlib.blake2b(digest_size=8)
            h4.update(d4.encode('utf-8'))
            d4 += '  #' + h4.hexdigest()

        if len(diceset) >= 5:
            d5 = str(sorted(diceset[4]))
            h5 = hashlib.blake2b(digest_size=8)
            h5.update(d5.encode('utf-8'))
            d5 += '  #' + h5.hexdigest()
        
        if len(diceset) >= 6:
            d6 = str(sorted(diceset[5]))
            h6 = hashlib.blake2b(digest_size=8)
            h6.update(d6.encode('utf-8'))
            d6 += '  #' + h6.hexdigest()

        #calculate digest identifier of found combination
        h_set = hashlib.blake2b(digest_size=8)
        h_set.update(h1.digest())
        h_set.update(h2.digest())
        if len(diceset) >= 3:
            h_set.update(h3.digest())
        if len(diceset) >= 4:
            h_set.update(h4.digest())
        if len(diceset) >= 5:    
            h_set.update(h5.digest())

        res = 'Dice1: ' + d1 + '\nDice2: ' + d2 + '\n'
        if len(diceset) >= 3:
            res += 'Dice3: ' + d3 + '\n'
        if len(diceset) >= 4:
            res += 'Dice4: ' + d4 + '\n'
        if len(diceset) >= 5:
            res += 'Dice5: ' + d5 + '\n'
        if len(diceset) >= 6:
            res += 'Dice6: ' + d6 + '\n'

        # save found result to file
        f = open('found.' + h_set.hexdigest() + '.txt', 'w')
        f.write(res)
        f.write(' UID: ' + h_set.hexdigest() + '\n')
        f.close()

        #print(res)
    else:
        print('XXXXXXXXXXXXXX')
        print('X  NOT FAIR! X')
        print('XXXXXXXXXXXXXX')

# ------------------------------------------------

# Example 3 fair dices.
        #[ 1, 6, 8, 11, 15, 16 ],
        #[ 2, 5, 7, 12, 14, 17 ],
        #[ 3, 4, 9, 10, 13, 18 ]

# Another example of three fair dices.
        #[ 1, 6, 9, 10, 15, 16 ],
        #[ 2, 5, 8, 11, 13, 18 ],
        #[ 3, 4, 7, 12, 14, 17 ]

# Example 4 fair dices (well-known as "Go First Dice")
        #[ 1, 8, 11, 14, 19, 22, 27, 30, 35, 38, 41, 48 ],
        #[ 2, 7, 10, 15, 18, 23, 26, 31, 34, 39, 42, 47 ],
        #[ 3, 6, 12, 13, 17, 24, 25, 32, 36, 37, 43, 46 ],
        #[ 4, 5, 9, 16, 20, 21, 28, 29, 33, 40, 44, 45 ]

# Yet Another "Go First Dice", very similar to the genuine:
        #[ 1, 8, 12, 13, 19, 22, 27, 30, 36, 37, 41, 48 ],
        #[ 2, 7, 10, 15, 18, 24, 25, 31, 34, 39, 42, 47 ],
        #[ 3, 6, 9, 16, 20, 21, 28, 29, 33, 40, 43, 46 ],
        #[ 4, 5, 11, 14, 17, 23, 26, 32, 35, 38, 44, 45 ]

# Not fair 6 dice set:
        #[ 1, 12, 13, 24, 25, 36, 37, 48, 49, 60, 61, 72 ],
        #[ 2, 11, 14, 23, 26, 35, 38, 47, 50, 59, 62, 71 ],
        #[ 3, 10, 15, 22, 27, 34, 39, 46, 51, 58, 63, 70 ],
        #[ 4, 9,  16, 21, 28, 33, 40, 45, 52, 57, 64, 69 ],
        #[ 5, 8,  17, 20, 29, 32, 41, 44, 53, 56, 65, 68 ],
        #[ 6, 7,  18, 19, 30, 31, 42, 43, 54, 55, 66, 67 ]

if __name__ == '__main__':
    diceset = [
        [ 1, 8, 11, 14, 19, 22, 27, 30, 35, 38, 41, 48 ],
        [ 2, 7, 10, 15, 18, 23, 26, 31, 34, 39, 42, 47 ],
        [ 3, 6, 12, 13, 17, 24, 25, 32, 36, 37, 43, 46 ],
        [ 4, 5, 9, 16, 20, 21, 28, 29, 33, 40, 44, 45 ]
    ]
    fairness_report(diceset)