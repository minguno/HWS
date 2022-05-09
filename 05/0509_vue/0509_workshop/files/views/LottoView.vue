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
