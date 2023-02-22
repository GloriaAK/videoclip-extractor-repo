import pysrt
subs = pysrt.open("TestFiles/I_LOVE_TO_SLEEP_twoSS.srt")

# for i in subs:
#     # print(sub.text)
#     ace123 = i.text
#     aa = ace123[0:5]
#     print(aa)
#
# ace123 = subs.text
# for i in subs.text:
#     if i == len(ace123[0:5])


listings = subs.text.split()
print(listings)

