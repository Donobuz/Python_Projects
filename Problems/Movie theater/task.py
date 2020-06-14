# put your python code here
number_of_cinema = int(input())
capacity = int(input())
number_of_viewers = int(input())

if (number_of_cinema * capacity >= number_of_viewers):
    print(True)
else:
    print(False)