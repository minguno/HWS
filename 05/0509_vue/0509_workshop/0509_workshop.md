# 0509_workshop

## 결과 화면

### Lunch

![image-20220510024511962](C:\Users\meh\AppData\Roaming\Typora\typora-user-images\image-20220510024511962.png)

### Lotto

![image-20220510024530139](C:\Users\meh\AppData\Roaming\Typora\typora-user-images\image-20220510024530139.png)

## Codes

### App.vue

```vue
<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'LunchView' }">Lunch</router-link> |
      <router-link :to="{ name: 'LottoView' }">Lotto</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#margin {
  margin: 100px;
}
</style>
```

### LunchView.vue

```vue
<template>
  <div>
    <div id="margin">
      <h1>점심메뉴</h1>
      <button @click="pickMenu">Pick Lunch</button>
      <p>{{ pickedMenu }}</p>
    </div>

    <div id="margin">
      <h2>로또를 뽑아보자</h2>
      <button @click="gotoLotto">Pick Lotto</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  data: function() {
    return {
      menu: ['라자냐', '치킨 마크니', '5찬 정식', '까르보나라', '굴라쉬 수프', '칠리 콘 카르네 & 마늘 바게트'],
      pickedMenu: '',
    }
  },
  methods: {
    pickMenu: function () {
      this.pickedMenu = _.sample(this.menu)
    },
    gotoLotto: function () {
      location.href = "/lotto/6"
    }
  }
}
</script>

<style>

</style>
```

### LottoView.vue

```vue
<template>
  <div>
    <h1>로또</h1>
    <button @click="pickNumbers">Get Lucky Numbers</button>
    <p>{{ numbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data: function() {
    return {
      numbers: ""
    }
  },
  methods: {
    pickNumbers() {
      // const pick = this.$route.params.lottoNum
      // this.numbers = _.sortBy(_.sampleSize(_.range(1, 46), pick)
      // 초기화
      this.numbers = ""
      for (let i=0; i<6; i++) {
        this.numbers += (String(_.sample(_.range(1, 46))) + " ")
      }
    }
  }
}
</script>

<style>

</style>
```

