<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-btn text @click="gotomain()">
        <h2 class="d-flex align-center">Ted Talks {{ curpage }}</h2>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
  computed: {
    curpage() {
      return this.$store.state.curpage;
    },
  },
  methods: {
    gotomain() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>
