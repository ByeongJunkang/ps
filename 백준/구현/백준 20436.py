keyboard = {"q": [0,0],"w":[0,1],"e":[0,2],"r":[0,3],"t":[0,4],
            "a":[1,0],"s":[1,1],"d":[1,2],"f":[1,3],"g":[1,4],
            "z":[2,0],"x":[2,1],"c":[2,2],"v":[2,3]}

keyboard_right = {"y":[0,5], "u":[0,6],"i":[0,7],"o":[0,8],"p":[0,9]
                  ,"h":[1,5],"j":[1,6],"k":[1,7],"l":[1,8]
                  ,"b":[2,4],"n":[2,5],"m":[2,6]}
left,right = input().split()
goal = input()
ans = len(goal)
for letter in goal:
    if letter in keyboard:
        tmp = keyboard[letter]
        goal_x,goal_y = tmp[0],tmp[1]
        left_loc = keyboard[left]
        left_x,left_y = left_loc[0],left_loc[1]
        dis1 = abs(goal_x - left_x) + abs(goal_y - left_y)
        ans += dis1
        left = letter
    else:
        tmp = keyboard_right[letter]
        goal_x,goal_y = tmp[0],tmp[1]
        right_loc = keyboard_right[right]
        right_x, right_y = right_loc[0],right_loc[1]
        dis2 = abs(goal_x - right_x) + abs(goal_y - right_y)
        right = letter
        ans+=dis2
print(ans)
