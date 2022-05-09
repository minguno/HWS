# 0509_homework

## 1. T/F

- Vue의 Life Cycle Hook에서 created Hook은 Vue template에 작성한 요소들이 DOM에 모두 그려지는 시점에 실행된다. **(T)**
- npm은 Node Package Manager의 약자이며, npm을 통해 설지한 package 목록은 package.json 파일에 자동으로 작성된다. **(F)**
  - `package-lock.json`에 저장된다.
- Vue CLI를 통해 만든 프로젝트는 브라우저가 아닌 node.js 환경이기 때문에 DOM 조작이나 Web API 호출 등 Vanilla JS에서의 기능을 사용할 수 없다. **(F)**
  - 사용 가능하다.

## 2. Vue router의 history mode

HTML History API를 사용해서 router를 구현한 것으로, 브라우저의 히스토리 (방문 기록)을 남기지만 실제 페이지는 이동하지 않고 새로고침도 않되는 기능을 지원한다.

## 3. Vue Life Cycle Hook을 참고하여 Vue application 실행 시 console 창에 출력되는 메세지

```html
<script>
export default {
  name: 'HelloWorld',
  created: function () {
    console.log('created!')
  },
  mounted: function () {
    console.log('mounted!')
  },
  updated: function () {
    console.og('updated!')
  },
}
</script>
```

```typescript
created!
mounted!
```



