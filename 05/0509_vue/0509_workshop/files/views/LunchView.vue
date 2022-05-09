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