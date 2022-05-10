# 0510_homework

## 1. T/F

- Vue는 컴포넌트 간 양방향 데이터 흐름을 지향하기 때문에 부모, 자식 컴포넌트 간의 데이터 전달 및 수정이 자유롭다. **(F)**
  - 단방향 데이터 흐름을 지향하여 컴포넌트 간 수직 관계를 갖고있기 때문에 전달 및 수정이 까다롭다.
- v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시 전달받은 함수를 실행한다. **(T)**
- 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 이벤트를 보내고, 자식 컴포넌트는 emit을 통해 부모 컴포넌트에게 데이터를 전달한다. **(T)**

## 2. Vue는 SPA Framework

하위 컴포넌트가 부모의 상태를 변경하기 용이한 양방향 데이터 흐름의 경우 앱의 데이터 흐름을 추적하기가 어려워 코드의 유지보수가 어렵게 되기 때문이다.

## 3. .navtive 수식어의 역할

태그가 다르다면 문제가 없지만 같은 태그 중에서 click 했을 때 발생하는 이벤트 자체를 호출하고 싶을 때 사용하는 수식어이다. Vue3에서는 `.native`가 사라진다. 

## 4. 코드 작성

- TodoListInput 컴포넌트의 버튼을 누르면 add-todo 이벤트가 발생한다. 이벤트 발생 시 data의 inputData 값도 함께 전달한다.
- TodoList 컴포넌트에서 add-todo 이벤트를 청취하면, onAddTodo 메서드를 실행한다.
- onAddTodo 메서드에서는 TodoListInput 컴포넌트에서 전달받은 값을 console.log 함수를 통해 출력한다.

```vue
// TodoListInput.vue

<template>
  <div>
    <input type="text" v-model="inputData">
    <button @click="onClick">추가</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListInput',
  data: function () {
    return {
      inputData: '',
    }
  },
  methods: {
    onClick: function () {
      this.$emit('add-todo', this.inputData)
    },
  },
}
</script>
```

```vue
// TodoList.vue

<template>
  <div>
    <todo-list-input add-to-do="onAddTodo"></todo-list-input>
  </div>
</template>

<script>
import TodoListInput from './components/TodoListInput.vue'
    
export default {
  name: 'MyTodoList',
  components: {
    TodoListInput,
  },
  methods: {
    onAddTodo(value) {
      console.log(value)
    },
  },
}
</script>
```

