POSTID = input("POSTID: ")
POSTID = POSTID[:3]
if POSTID in ["010", "011", "012"]:
    print("강북구")
elif POSTID in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")