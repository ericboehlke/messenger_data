import json
from matplotlib import pyplot as plt
from collections import defaultdict

path = "/Users/ericboehlke/Desktop/facebook-ericboehlke98/messages/inbox/SavageSquadREreUNITE_bW7KBKYg6g/"
data = []
for i in range(1, 6):
    with open(path + f"message_{i}.json", "r") as fp:
        data.append(json.load(fp))
        
peopleingroup = data[0]["participants"]
peopleingroup = [i["name"] for i in peopleingroup]
messages = []
for item in data:
    messages += item["messages"]


print(messages[0])
people = defaultdict(lambda : 0)
for msg in messages:
    people[msg["sender_name"]] += 1

print(people)
print(peopleingroup)

x = []
for person in people.keys():
    if person in peopleingroup:
        if person == "Jos\u00c3\u00a9 Zavala":
            x.append(("José Zavala", people[person]))
        else:
            x.append((person, people[person]))

x = sorted(x, key=lambda x:-x[1])

plt.xkcd()
fig, ax = plt.subplots()
rects = ax.bar([i[0] for i in x], [i[1] for i in x])
plt.xticks(rotation=45, ha="right")
plt.ylabel("messages")
plt.title("Messages sent to SavageSquad")
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                f"{int(height)}", 
                ha='center', va='bottom', fontsize=8)
autolabel(rects)
plt.show()