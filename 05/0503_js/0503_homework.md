# 0503_homework

## 1. True or False

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다. **(T)**
- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다. XHR 객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다.  **(T)**
- axios는 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다. **(F)**
  - XHR 요청을 대체해주는 것이 axios이다.

## 2. Web API, Task Queue, Call Stack 그리고 Event loop에서 어떤 동작이 일어나는가?

```javascript
console.log('Hello SSAFY!')

setTimeout(function () {
    console.log('I am from setTimeout')
}, 1000)

console.log('Bye SSAFY!')
```

```bash
# 출력화면
Hello SSAFY!
Bye SSAFY!
I am from setTimeout
```

1. Call stack에 [console.log('Hello SSAFY!')]가 push 되면 바로 실행되므로 pop 되어 요청이 완수된다.
2. Call stack에 [setTimeout(function)]이 push 되고 다시 pop되어 Web API로 비동기 함수를 처리하러 요청을 보낸다.
3. 그 동안 Call stack에 [console.log('Bye SSAFY!')]가 push 되면서 pop되어 바로 실행되고 run을 마친 Web API에서 console.log('I am from setTimeout')을 다시 Call stack에 push 하면서 제일 마지막으로 실행된다.