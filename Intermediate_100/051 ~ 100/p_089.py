def move(world_map, moving):
    x,y = 0,0
    for i,m in enumerate(world_map):
        if 1 in m:
            x,y = m.index(1),i
    world_map[y][x] = 0
    for i in moving:
        if i==1 and world_map[y-1][x]!=2:
            y-=1
            
        elif i==2 and world_map[y+1][x]!=2:
            y+=1
            
        elif i==3 and world_map[y][x-1]!=2:
            x-=1
            
        elif i==4 and world_map[y][x+1]!=2:
            x+=1
    world_map[y][x] = 1
    for i in world_map:
        print(i)
    return [x,y]