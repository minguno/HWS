# 0511_homework

## 1. T/F

- Vue  프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다. **(F)**
  - 반드시 아니고 할 필요 없다. 필요할 때만 Vuex를 다운받아 사용한다.
- mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다. **(T)**
- mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다. **(F)**
  - mutations가 store.commit, actions가 store.dispatch로 호출한다.
- state는 data의 역할, getters는 computed와 유사한 역할을 담당한다. **(T)**

## 2. Vuex: State, Getters, Mutations, Actions

- state: 중앙에서 관리하는 모든 상태 정보 (data)
- mutations: 실제로 state를 변경하는 유일한 방법
- getters: state를 변경하지 않고 활용하여 계산을 수행 (computed 속성과 유사)
- actions: mutations를 commit()으로 호출하며 컴포넌트에선 dispatch()에 의해 호출 (비동기 로직 가능)

## 3. Todo App 관련 코드를 Vuex의 Store로 변환

```vue
<script>
export default {
  name: 'TodoList',
  data: function() {
    return {
      todoList: [],
      status: 'all',
    }
  },
  computed: {
    todoListByStatus: function() {
      return this.todoList.filter((todo) => {
        // status 값에 따라 todoList를 필터링한다.
      })
    },
  },
  methods: {
    addTodo: function() {
      // 새로운 todo를 todoList에 추가한다.
    },
  },
}
</script>
```

```js
// index.js

export default new Vuex.Store({
  state: {
  todoList: [],
  status: 'all',
  },
  getters {
    todoListByStatus: function(state) {
      // ...
    },
  },
  mutations: {
    addTodo: function(state) {
      // ...
    },
  },
})
```



