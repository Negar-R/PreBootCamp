n = int(input())
list_of_colors = list(map(int, input().split()))

min_color = 100
# key = color, value = number of markers

answer = 0
markers = {}

for color in list_of_colors:
    if color not in markers.keys():
        markers[color] = 1
    else:
        markers[color] += 1

print("this is our result : ", markers)

for key , value in markers.items():
    if value <= min_color:
        min_color = value
    if key >= answer :
        answer = key

for key ,value in markers.items():
    if value == min_color:
        if key < answer :
            answer = key
            
print("this is ans : ", answer)