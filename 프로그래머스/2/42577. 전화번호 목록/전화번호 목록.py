
def solution(phone_book):
    # 문자열 기준 정렬 -> 직후 번호의 접두어랑 다르면 그 후도 다르다
    phone_book = sorted(phone_book)
    for idx in range(len(phone_book) - 1):
        if phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:
            return False
    return True
        
    
