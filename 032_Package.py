# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# trip_to = vietnam.VeitnamPackage()
# trip_to.detail()

# travel package 안에서 범위를 설정해 줘야 한다.
# 공개 / 비공개에 대한 범위 설정 필요
from travel import *

trip_to = thailand.ThailandPackage()
trip_to.detail()
