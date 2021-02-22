from pipelines import pipeline
import wikipedia



def filter_length_answers(json_result):
    result = []
    for qa_pair in json_result:
        lenght_of_answer = len(qa_pair["answer"]) 
        if(lenght_of_answer> 30):
            continue
        result.append(qa_pair)
    return result

nlp = pipeline("question-generation")

topic = input("Give a Topic: ")
topics = print(wikipedia.search(topic))
topic = input("Choose a Topic: ")

summary = wikipedia.summary(topic)
summary = summary.replace("\n", "")

json_result = nlp(summary)

json_result = filter_length_answers(json_result)

for idx, qa_pair in enumerate(json_result):
    print("Question "+ str(idx + 1) + ":")
    print(qa_pair["question"] + "\n")
    print("Press Enter to see the answer\n")
    input()
    print("Answer: " + qa_pair["answer"] + "\n")
    print("---------------------------")

