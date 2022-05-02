<template>
  <div>
    This is video page: {{ $route.params.videotitle }}
    {{ relatedTalks }}
  </div>
</template>

<script>
export default {
  setup() {},
  data() {
    return {
      relatedTalks: [],
    };
  },
  mounted() {
    this.$store.state.curpage = "Find Your Topic";
    var vm = this;
    const fd = new FormData();
    fd.append("title", vm.$route.params.videotitle);
    this.$http.post("getrelated", fd).then(async function (response) {
      console.log("Load Related Page");
      var talks = response.data;
      vm.relatedTalks = talks;
    });
  },
};
</script>
