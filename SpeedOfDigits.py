def track_digit_changes(increment=70, iterations=100):
    """
    Track how digit count changes when continuously adding a number.
    초기값 0에서 시작해서 특정 값을 계속 더하면서 자릿수 변화를 추적합니다.
    
    Args:
        increment: Number to add repeatedly / 반복해서 더할 숫자 (기본값: 70)
        iterations: Number of iterations / 반복 횟수
    """
    current = 0
    previous_digits = 1  # 0 is 1 digit / 0의 자릿수는 1
    
    print(f"Initial value: 0 (Digit count: 1)")
    print(f"초기값: 0 (자릿수: 1)")
    print(f"\nDigit changes when adding {increment}:")
    print(f"{increment}을(를) 더할 때마다 자릿수 변화:")
    print("-" * 70)
    
    digit_change_count = 0
    
    for i in range(1, iterations + 1):
        current += increment
        current_digits = len(str(current))
        
        # Check if digit count has changed / 자릿수 변화가 있었는지 확인
        if current_digits != previous_digits:
            print(f"Iteration {i:3d}: {current:10d} | Digits: {previous_digits} → {current_digits} ✓ (CHANGED!)")
            print(f"반복 {i:3d}: {current:10d} | 자릿수: {previous_digits} → {current_digits} ✓ (변화!)")
            digit_change_count += 1
            previous_digits = current_digits
        else:
            # Display every 10 iterations when no change / 변화 없으면 10번마다 한 번씩만 표시
            if i % 10 == 0:
                print(f"Iteration {i:3d}: {current:10d} | Digits: {current_digits} (no change)")
                print(f"반복 {i:3d}: {current:10d} | 자릿수: {current_digits} (변화 없음)")
    
    print("-" * 70)
    print(f"\nTotal iterations: {iterations}")
    print(f"Digit changes occurred: {digit_change_count} times")
    print(f"\n총 반복 횟수: {iterations}회")
    print(f"자릿수 변화 횟수: {digit_change_count}회")
    return digit_change_count


# Example: Start from 0 and add numbers repeatedly
# 예시: 0에서 시작해서 숫자를 반복해서 더함
if __name__ == "__main__":
    print("=" * 70)
    print("DIGIT GROWTH ANALYSIS / 자릿수 증가 분석")
    print("=" * 70 + "\n")
    
    # Test with 70 / 70으로 테스트
    track_digit_changes(increment=70, iterations=200)
