import json
import emoji
from matplotlib import pyplot as plt
from collections import defaultdict

reaction_map = {"ð\x9f\x98¢": emoji.emojize(":crying_face:"),
                "ð\x9f\x98\x86": emoji.emojize(":grinning_squinting_face:"),
                "ð\x9f\x91\x8d": emoji.emojize(":thumbs_up:"),
                "ð\x9f\x98®": emoji.emojize(":face_with_open_mouth:"),
                "ð\x9f\x92\x97": emoji.emojize(":growing_heart:"),
                "ð\x9f\x98\xa0": emoji.emojize(":angry_face:"),
                "â\x9d¤": emoji.emojize(":red_heart:")}

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

print(reaction_map)
print(messages[0])
reactions = defaultdict(lambda : 0)
for msg in messages:
    try:
        for reaction in msg["reactions"]:
            reactions[reaction_map[reaction["reaction"]]] += 1
    except KeyError:
        pass

print(reactions)

x = []
for react in reactions.keys():
    x.append((react, reactions[react]))

x = sorted(x, key=lambda x:-x[1])

plt.xkcd()
fig, ax = plt.subplots()
rects = ax.bar([i[0] for i in x], [i[1] for i in x])
plt.xticks(rotation=45, ha="right")
plt.ylabel("number of reactions")
plt.title("Most popular reactions in Savage Squad")
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