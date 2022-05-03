# 0502_homework

## 1. True or False

- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다. **(T)**
  - 자바스크립트의 메인 thread인 이벤트 루프는 single threaded이나, 실행될 때는 웹 브라우저나 NodeJS 같은 multi-threaded 환경에서 실행되기 때문에 비동기 작업을 통해 하나의 작업에 소요되는 런타임 동안 다음 코드를 불러올 수 있다.
- `setTimeout`은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다. **(F)**
  - Call Stack은 동작을 수행해야 될 작업이 쌓이고 (push) 차례대로 실행 (pop) 하는 곳으로 Web API에게 작업을 넘긴 후 Call Stack에서 제거된다.

## 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

동기 함수는 순차적, 직렬적으로 task를 수행하고 비동기는 병렬적으로 수행한다.

동기는 요청 후 응답을 받아야만 다음 동작이 이루어지므로 어떤 작업이 수행중이라면 다음 작업은 대기하게 된다. 데이터 양이 큰 앱일 수록 실행속도가 기하급수적으로 느려질 수 있기 때문에 setTimeout, setInterval 혹은 AJAX를 사용하여 비동기적으로 state (data)를 처리하면 앱이 과부하 걸리지 않게 해주는 역할이다.

## 3. axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드를 작성하라.

```js
axios.get('https://api.example.com/data')
  .then(function (response) {
    console.log(response.data)
})
```

