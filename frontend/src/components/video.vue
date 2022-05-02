<template>
  <v-card class="mx-auto mt-5" width="600" height="200">
    <v-card-title
      class="text-left mt-2"
      style="text-overflow: ellipsis; white-space: nowrap; overflow: hidden"
      >{{ video.title }}</v-card-title
    >
    <v-card-subtitle>
      <!-- <v-chip v-for="(t, key) in tags" :key="key" color="primary"
        >#{{ t }}</v-chip
      ><v-chip>...</v-chip> -->
      <br />
      Speaker: {{ video.main_speaker }}
      <br />
      Duration: {{ time }}
      <br />
      Published Date: {{ date }}
    </v-card-subtitle>
    <v-card-actions class="mb-5">
      <v-btn
        text
        color="blue lighten-2"
        class="mb-5"
        @click="gotoVideo(video.title)"
        >View Video</v-btn
      >
      <br />
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ["video"],
  data() {
    return {
      time: null,
      date: null,
      tags: [],
    };
  },
  methods: {
    gotoVideo(videoTitle) {
      this.$router.push({
        path: `/video/${videoTitle}`,
      });
    },
  },
  mounted() {
    this.time = Math.floor(this.video.duration / 60);
    this.date = this.video.published_date;
    if (this.video.tags.length > 3) {
      this.tags = this.video.tags.slice(0, 3);
    }
  },
};
</script>
