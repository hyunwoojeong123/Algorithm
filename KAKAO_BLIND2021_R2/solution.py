import requests

url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'
token = '487deeb48fa23d13c20aff4e0aa8799b'
auth_key = ''
nn= [-1,5,60]
tt = [-1,5,10]
di,dj = [0,0,1,-1], [1,-1,0,0]

def start(token,problem):
    uri = url + '/start'
    h = {'X-Auth-Token' : token, 'Content-Type': 'application/json' }
    d = {'problem' : problem}
    #print(uri,h)
    return requests.post(uri, params = d, headers = h).json()

def Locations():
    uri = url + '/locations'
    h = {'Authorization': auth_key, 'Content-Type': 'application/json' }
    return requests.get(uri,headers=h).json()

def Trucks():
    uri = url + '/trucks'
    h = {'Authorization': auth_key, 'Content-Type': 'application/json' }
    return requests.get(uri,headers=h).json()

def Simulate(commands):
    uri = url + '/simulate'
    h = {'Authorization': auth_key, 'Content-Type': 'application/json' }
    d = {"commands" : commands}
    if commands == []:
        d = {"commands" : [{'truck_id' : 0, 'command' : [0]}]}
    return requests.put(uri,json = d,headers=h).json()

def Score():
    uri = url + '/score'
    h = {'Authorization': auth_key, 'Content-Type': 'application/json' }
    return requests.get(uri,headers=h).json()

## 재고가 위험수준인 애를 찾는다.
def find_in_danger(locs, p):
    #print(locs)
    
    N = nn[p]*nn[p]
    res = []
    for i in range(N):
        if locs[i]['located_bikes_count'] < 2:
            res.append(i)
    return res
   

## 두 ID 사이의 거리
def dist(ID1,ID2,p):
    if p == 2:
        n = 60
    i1,j1 = ID1 // nn[p], ID1 % nn[p]
    i2,j2 = ID2 // nn[p], ID2 % nn[p]
    return abs(i1-i2) + abs(j1-j2)

## 트럭 중 거지랑 젤 가까운 트럭 ID를 반환
def find_near_truck(guji,trucks,p,used_truck):
    min_dist = 9999
    near_truck = -1
    for truck in trucks:
        tid = truck['id']
        if used_truck[tid]:
            continue
        tloc = truck['location_id']
        if min_dist > dist(tloc,guji,p):
            min_dist = dist(tloc,guji,p)
            near_truck = truck['id']
    return [near_truck, min_dist]

#거지랑 젤 가까운 안 위험한 애 넣음
def find_near_not_danger(guji,locs,visited_loc,pr):
    q = [guji]
    visited = [[False for j in range(nn[pr])]for i in range(nn[pr])]
    while q:
        p = q.pop(0)
        pi,pj = p // nn[pr], p % nn[pr]
        if locs[p]['located_bikes_count'] >= 3 and not visited_loc[p]:
            return [p,locs[p]['located_bikes_count']]
        for k in range(4):
            ni,nj = pi + di[k],pj+dj[k]
            n = ni*nn[pr]+nj
            if ni < 0 or nj < 0 or ni >= nn[pr] or nj >= nn[pr]:
                break
            if visited[ni][nj]:
                break
                
            visited[ni][nj] = True
            q.append(n)
    return [-1,-1]
        
# 트럭이 이동하는 명령 추가
def move_command(fro,to,pr):
    res = []
    fi,fj = fro//nn[pr],fro%nn[pr]
    ti,tj = to // nn[pr], to % nn[pr]
    # 목적지가 오른쪽
    if fi < ti:
        for i in range(ti-fi):
            res.append(2)
    else:
        for i in range(fi-ti):
            res.append(4)
    # 목적지가 위쪽
    if fj < tj:
        for i in range(tj-fj):
            res.append(1)
    else:
        for i in range(fj-tj):
            res.append(3)
    return res

# commands에 nt가 이동하고 자전거 태우는 커맨드 추가
def make_command(commands,nt,ntpos,not_danger,guji,bikes,pr):
    nt_command = []
    nt_command += move_command(ntpos,not_danger,pr)
    if bikes == 2:
        nt_command += [5,5]
    else:
        nt_command += [5]
    nt_command += move_command(not_danger,guji,pr)
    if bikes == 2:
        nt_command += [6,6]
    else:
        nt_command += [6]
    commands.append({'truck_id':nt,'command':nt_command})

def p(n):
    
    global auth_key
    ret = start(token,n)
    auth_key = ret['auth_key']
    while True:
        ## 재고 위험수준인애 찾음
        locs = Locations()['locations']
        #print(locs)
        indangers = find_in_danger(locs,n)
        #print('locs:' ,locs)
        #print('indangers:', indangers)
        ## 재고 위험한애 없으면 트럭 안 움직임
        if len(indangers) == 0:
            ret = Simulate([])
        ## 재고 위험한 애 있으면
        else:
            commands = []
            ## 재고 위험한 애와 트럭 간의 거리 
            ## 젤 가까운 트럭을 찾는다.
            # 여기서 guji는 location이고
            # nt는 truck의 id이다.
            # nt_to_guji는 nt에서 guji까지 거리다.
            
            trucks = Trucks()['trucks']
            used_trucks = [False for i in range(tt[n])]
            visited_loc = [False for i in range(nn[n]*nn[n])]
            for guji in indangers:
                # 거지가 필요로 하는 자전거 대수를 구한다.
                need_bikes = 2- locs[guji]['located_bikes_count']
                # while need_bikes > 0:
                nt,nt_to_guji = find_near_truck(guji,trucks,n,used_trucks)
                if nt == -1:
                    continue
                ntpos = trucks[nt]['location_id']
                
                # 거지에서 가까운 안 위험한애들을 찾는다.
                not_danger,not_danger_bikes = find_near_not_danger(guji,locs,visited_loc,n)
                if not_danger != -1:
                    # 거리가 6이하고 
                    if dist(nt,not_danger,n) + dist(not_danger,guji,n) <= 6:
                    # not_danger_bikes 가 4 이상이면
                        if not_danger_bikes >= 4:
                            make_command(commands,nt,ntpos,not_danger,guji,2,n)
                            visited_loc[not_danger] = True
                            used_trucks[nt] = True
                            need_bikes -= 2
                        elif not_danger_bikes == 3:
                            make_command(commands,nt,ntpos,not_danger,guji,1,n)
                            visited_loc[not_danger] = True
                            used_trucks[nt] = True
                            need_bikes -= 1
                    # 거리가 8이하이면
                    elif dist(nt,not_danger,n) + dist(not_danger,guji,n) <= 8:
                        make_command(commands,nt,ntpos,not_danger,guji,1,n)
                        visited_loc[not_danger] = True
                        used_trucks[nt] = True   
                        need_bikes -= 1
            print(commands)
            ret = Simulate(commands)
        print(ret)
        if ret['status'] == 'finished':
            print(ret['time'], ret['status'])
            break
    print(n,':' , Score())
   


if __name__ == '__main__':
   #p(1)
   p(2)

## 끝날 때가 되서야 생각이 난 풀이방법
# 트럭들을 구역을 나눠준다.
# 해당 지역에서 위험한 애가 생기면 걔를 차출해서 자전거를 옮기는데 쓴다.