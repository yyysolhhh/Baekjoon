def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i + 1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
