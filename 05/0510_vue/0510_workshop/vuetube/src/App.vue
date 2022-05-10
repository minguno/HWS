<template>
  <div id="App">
    <h1>Vuetube</h1>
    <TheSearchBar @on-search="onSearch"/>

    <VideoDetail 
      v-if="Object.keys(video).length" 
      :video="video"
    />

    <VideoList 
      :videos="videos"
      @on-click-video="onClickVideo"
    />
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

import axios from 'axios'


export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function() {
    return {
      videos: [],
      video: {}, //VideoListItem에서 click한 비디오 저장할 데이터
    }
  },
  methods: {
    // 비동기 방식
    async onSearch(keyword) {

      const YOUTUBE_SEARCH_BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
      const YOUTUBE_API_KEY = 'AIzaSyAX3dU3C9uQ-Evy-UYhSCkeAWEbMdjKsOE'
      
      const params = {
        key: YOUTUBE_API_KEY,
        part: 'snippet',
        q: keyword,
      }

      // https://..../search?key=...&part=snippet&q=keyword 로 GET 요청을 보내기
      // 뒤에가 Promise 객체일 때만 await 사용 가능
      const response = await axios.get(YOUTUBE_SEARCH_BASE_URL, { params },)
      
      const videos = response.data.items
      this.videos = videos
    },

    onClickVideo(video) {
      this.video = video
    },
  },
}
</script>

<style>
h1 {
  color: rgb(226, 35, 35);
}
</style>