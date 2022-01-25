# 0120_homework



## 1. 이름 공간 (Namespace)

- `built-in` > `global` > `local`
- 코드의 순서에 따라 다르지 않나요?

## 2. 매개변수와 인자, 그리고 반환

```markdown
~~(1) 함수는 오직 하나의 객체만 반환할 수 있으므로, 'return a, b'와 같이 쓸 수 없다~~
쓸 수 있고, `(a, b)`와 같이 튜플 형태로 반환된다.
```

## 3. 재귀 함수

* 장점
  * 코드가 반복문보다 더 짧고 직관적이여서 가독성이 좋다.
  * 알고리즘 구현에 반복문보다 많이 사용된다.
* 단점
  * 함수가 함수를 반환하는 재귀를 종료 시키는 base case가 반드시 존재하여야 한다.
  * 재귀를 통해 inner 함수가 호출 될 때마다 메모리 공간에 쌓이게 되어 `stack overflow`되거나 프로그램이 느려질 수 있다.
  * 이를 방지하기 위해 python 은 1000번의 재귀를 넘길 시 자체 종료 시킨다.