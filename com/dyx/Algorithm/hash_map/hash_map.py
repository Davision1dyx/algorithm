hmap: dict = dict()
hmap[123] = "aaa"
hmap[321] = "bbb"
hmap["aaa"] = "ccc"
print(hmap)
name: str = hmap["aaa"]
print(name)
hmap.get("aaa")
hmap.pop("aaa")
print(hmap)
# 遍历
for key,value in hmap.items():
    print(key, "->", value)
for key in hmap.keys():
    print(key)
for value in hmap.values():
    print(value)
hash("aa")
    