# 0428_homework

## 1. True or False

- EventTarget.addEventListener(type, listener)에서 listener 위치에 콜백 함수를 정의한다. 이때 콜백 함수의 첫 번째 매개변수에는 발생한 이벤트에 대한 정보를 담고 있는 Event 객체가 전달된다. **(T)**
- event.preventDefault 메서드를 통해 이벤트의 기본 동작을 취소할 수 있다. **(T)**

## 2. DOM Event

- `click`: 클릭 시 발생
- `mouseover`: 마우스가 특정 객체 위로 올려졌을 시 발생
- `mouseout`: 마우스가 특정 객체 밖으로 나갔을 때 발생
- `keydown`: 키를 눌렀을 때 발생
- `keyup`: 키에서 손을 뗐을 때 발생
- `load`: 문서의 로드가 완료 되었을 때 발생
- `scroll`: 스크롤 했을 때 발생
- `change`: 변동이 있을 시 발생
- `input`: input 태그 안에 들어있는 데이터가 변동되는 경우에 실행

## 3. 코드 작성

```javascript
const button = document.querySelector('button')

button.addEventListener('click', function () {
    console.log('Button clicked!')
})
```

