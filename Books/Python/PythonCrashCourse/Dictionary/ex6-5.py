rivers = {
    "nile": "egipt",
    "amazon": "brazil",
    "yangtze": "china",
    "mississippi": "usa",
    "danube": "germany",
    "ganges": "india",
    "volga": "russia",
    "thames": "uk",
}

for k,v in rivers.items():
    print(f"The {k} runs through {v}")

print("\n")
print("Rivers: \n")
for k in rivers.keys():
    print(k)

print("\n")
print("Countries: \n")
for v in rivers.values():
    print(v)
