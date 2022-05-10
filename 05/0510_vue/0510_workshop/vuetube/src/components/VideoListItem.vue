<template>
  <div class="card" @click="onClickVideo">
    <div class="left">
      <img :src="video.snippet.thumbnails.high.url" alt="">
    </div>
    <div class="right">
      <h2 class="title">{{ video.snippet.title }}</h2>
      <p class="desc">{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: false,
    },
  },
  methods: {
    onClickVideo() {
      this.$emit('on-click-video', this.video)
    },
  },
}
</script>

<style>
.card {
  display: flex;
  width: 700px;
  margin: 12px 0px;
}

.card:hover {
  cursor: pointer;
  opacity: 0.7;
}

.left {
  width: 30%;
}

.left > img {
  width: 100%;
}

.right {
  width: 70%;
  padding-left: 15px;
}

.right > .title {
  margin-top: 0;
}

</style>