<template>
  <div>
    <v-row class="mx-5 my-5">
      <v-text-field
        hide-details
        single-line
        v-model="searchedVideo"
        @keyup="checkForEnterKey"
      ></v-text-field>
      <v-btn text @click="getVideo()"><v-icon>mdi-magnify</v-icon></v-btn>
    </v-row>
    <v-row class="align-center">
      <videoCard
        class="mx-2"
        v-for="(v, key) in selectedVideos"
        :key="key"
        :video="v"
      />
    </v-row>
  </div>
</template>

<script>
import videoCard from "../components/video.vue";
export default {
  components: {
    videoCard,
  },
  data() {
    return {
      searchedVideo: "",
      selectedVideos: [],
      videos: [],
      videoTitle: [],
    };
  },
  methods: {
    getVideo() {
      if (this.videoTitle.includes(this.searchedVideo)) {
        var ind = this.videoTitle.indexOf(this.searchedVideo);
        this.selectedVideos = [this.videos[ind]];
      } else {
        alert("Not Found");
      }
    },
    checkForEnterKey(event) {
      if (event.keyCode == 13) {
        this.getVideo();
      }
    },
  },
  mounted() {
    this.$store.state.curpage = "Find Your Video";
    var vm = this;
    this.$http
      .get("getvideos/" + vm.$route.params.topicname)
      .then(async function (response) {
        console.log("Load Topic Page");
        var videos = response.data;
        vm.videos = videos;
        var tmp = [];
        for (var v in videos) {
          console.log(videos[v]);

          tmp.push(videos[v]["title"]);
        }
        vm.videoTitle = tmp;
        vm.selectedVideos = vm.videos;
        console.log(vm.videoTitle);
      });
  },
};
</script>
