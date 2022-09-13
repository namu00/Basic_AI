data = input().split()
data_set = set(data)
data_dict = {}
for key in data_set:
    data_dict[key] = data.count(key)

print(f'{max(data_dict, key=data_dict.get)}(이)가 총 {max(data_dict.values())}표로 반장이 되었습니다.')