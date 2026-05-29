import time
#Sentence for typing
sentence="Python is easy and fun to learn"
#Show Sentence
print("Type this sentence:")
print(sentence)
#Start time
start_time = time.time()
#User input
typed_text = input("Type your sentence: ")
#End time
end_time = time.time()
#total time
total_time = end_time - start_time
#WPM calculation
words = len(typed_text.split())
minutes=total_time/60
if minutes >0:
    wpm=round(words/minutes)
else:
    wpm=0
#Errors calculation
errors=0
for i in range(min(len(typed_text),len(sentence))):
    if typed_text[i]!=sentence[i]:
        errors+=1
#Extra characters count as errors
errors+=abs(len(sentence) - len(typed_text))
#Output
print("-------Results--------")
print("Time Taken:", round(total_time,2))
print("WPM:", wpm)
print("Errors:", errors)

