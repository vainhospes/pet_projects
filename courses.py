rect_width, rect_height, w, h = map(int, input().split())

# здесь пишите программу
rectangles = (rect_width//w) * (rect_height//h)
print(rectangles)

total = 0