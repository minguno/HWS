# 0425_homework

## 1. T/F

1. let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다. **(F)**
   - var 변수는 재선언, 재할당이 모두 가능, let은 재할당 가능 재선언 불가능, const는 재선언 재할당 모두 불가능하다.
2. "값이 없음"을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다. **(F)**
   - null은 null 객체가 반환된다.
3. for ... in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 활용하는 경우에 주로 활용한다. **(F)**
   - 주로 객체의 속성들을 순회할 때 사용된다. 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없어 권장되지 않는다.
4. '==' 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false를 반환한다. **(F)**
   - 타입이 달라도 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교한다.

## 2. 코드 작성

```javascript
const numbers = [1, 2, 3, 4, 5]
```

- for ... of 문을 사용하여 배열의 각 요소를 출력하시오.

  ```javascript
  for (let number of numbers) {
      console.log(number)
  }
  ```

- for ... of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생성하시오.

  ```javascript
  for (let number of numbers) {
      number = number + 10
      consol.log(number)
  }
  ```

- for ... of 문을 사용하여 배열의 각 요소들 중 홀수 요소 들로만 구성된 새로운 배열을 생성하시오.

  ```javascript
  for (let number of numbers) {
      if (number % 2 == 1) {
          console.log(number)
      }
  }
  ```

- for ... of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오.

  ```javascript
  let sum = 0
  
  for (let number of numbers) {
      sum += number
  }
  
  console.log(sum)
  ```