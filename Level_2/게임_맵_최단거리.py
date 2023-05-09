from collections import deque
def solution(maps):

    def bfs(x, y):
        queue=deque()
        queue.append((x,y))

        while queue:
            x,y=queue.popleft()
            dx=[-1,1,0,0]
            dy=[0,0,1,-1]


            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):
                    continue
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    queue.append((nx,ny))
        
        if maps[-1][-1]>1:
            return maps[-1][-1]
        else:
            return -1

    result=bfs(0,0)
    return result