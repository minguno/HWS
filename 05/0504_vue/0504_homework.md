# 0504_homework

## 1. T/F

- SPA는 Single Pattern Application의 약자이다. **(F)**
  - Single Page Application이다.
- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 이후부터는 페이지 갱신에 필요한 데이터만 전달받는다. **(T)**
- Vue.js에서 말하는 '반응형'은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트되는 것을 의미한다. **(T)**
- 동일한 요소에 v-for와 v-if 두 디렉티브가 함께 작성된 경우, 매 반복 시에 v-if의 조건문으로 요소의 렌더링 여부를 결정한다. **(T)**
- v-bind 디렉티브는 "@", v-on 디렉티브는 ":" shortcut(약어)를 제공한다. **(F)**
  - v-bind가 ":", v-on이 "@" 약어이다.
- v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다. **(F)**
  - 단방향 데이터 바인딩은 값을 바꿀 수 없다.

## 2. MVVM

- M: Model
  - {key: value} 로 이루어진 data
- V: View
  - HTML (DOM)
- VM: ViewModel
  - View와 Model의 중개자

## 3. 코드 작성

```html
<div id="app">
  {{ message }}
</div>

<script>
  const app = Vue ({
    el: '#app',
    data: {
      message: 'Hello World',
    },
  })
</script>
```



