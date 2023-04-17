# 딕셔너리로 풀어보기

players=["mumu", "soe", "poe", "kai", "mine"]
callings=["kai", "kai", "mine", "mine"]

players_dict={}
score_dict={}

for i in range(len(players)):
    players_dict[players[i]]=i+1

for i in range(len(players)):
    score_dict[i+1]=players[i]

for j in callings:
    call_player_score=players_dict[j] # 불린 선수의 현재 순위
    pre_player_score=players_dict[j]-1 # 불린 선수가 될 순위
    pre_player=score_dict[pre_player_score] # 역전당한 선수 이름

    players_dict[j]=pre_player_score # 선수(역전한 순위(순위 -1))
    players_dict[pre_player]=call_player_score # 선수(역전당한 순위(순위 +1))

    score_dict[pre_player_score]=j # 순위(불린 선수)
    score_dict[call_player_score]=pre_player # 순위(역전 당한 선수)

print(list(score_dict.values()))

# 너무 정신없게 풀었는데 다시 천천히 생각하면서 풀어보기 딕셔너리 한개로 가능함
# 처음에 푼 list로 풀면 시간초과 나기때문에 딕셔너리로 푸는게 시간이 더 빨랐음