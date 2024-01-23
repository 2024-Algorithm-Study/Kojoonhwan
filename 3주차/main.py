from collections import deque
def solution(bridge_length, weight, truck_weights):
    i, t = 0, 1
    q, weightsum = deque(), 0
    
    while i < len(truck_weights):
        while i < len(truck_weights) and weightsum + truck_weights[i] <= weight:
            # 트럭무게, 도로를 빠져나온 시간
            q.append( (truck_weights[i], t + bridge_length) )
            weightsum += truck_weights[i]
            
            i += 1
            t += 1
            # 시간이 t가 되어서 트럭이 탈출해야 하는 상황을 처리합니다.
            if q[0][1] == t:
                w, t = q.popleft()
                weightsum -= w
        
        #  트럭이 탈출하는 시점으로 이동합니다.
        if len(q) > 0:
            w, t = q.popleft()
            weightsum -= w
        
    # 큐의 트럭들을 모두 탈출시킵니다.
    while len(q) > 0:
        w, t = q.popleft()
    
    return t