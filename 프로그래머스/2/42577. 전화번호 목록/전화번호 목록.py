# 문자열 기준 정렬 -> 짧고 앞순위로 오름차순
#               -> temp가 temp 다음의 머릿말이 아니면 더 볼 필요 X
def solution(phone_book):
    phone_book.sort()
        
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return True


