<template>
  <div>
    <iframe 
      :src="videoUrl" 
      frameborder="0"
    >
    </iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
      required: false,
    },
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>