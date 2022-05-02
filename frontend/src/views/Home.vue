<template>
  <div class="home">
    <v-row class="mx-5 my-5">
      <v-text-field
        hide-details
        single-line
        v-model="searchedTopic"
        @keyup="checkForEnterKey"
      ></v-text-field>
      <v-btn text @click="getTopic()"><v-icon>mdi-magnify</v-icon></v-btn>
    </v-row>
    <v-row class="mt-5 ml-5">
      <v-col
        ><v-btn
          v-for="(topic, key) in selectedTopics"
          @click="gotoTopic(topic)"
          :key="key"
          >{{ topic }}</v-btn
        ></v-col
      >
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      topics: [],
      selectedTopics: [],
      searchedTopic: "",
    };
  },
  methods: {
    getNums() {
      var number = [];
      for (var i = 0; i < 20; i++) {
        var flag = true;
        var num = Math.floor(Math.random() * 594);
        while (number.includes(num)) {
          num = Math.floor(Math.random() * 594);
        }
        if (flag == true) {
          number.push(num);
        }
      }
      return number;
    },
    gotoTopic(topic) {
      this.$router.push({
        path: `/topic/${topic}`,
      });
    },
    getTopic() {
      if (this.topics.includes(this.searchedTopic)) {
        this.selectedTopics = [this.searchedTopic];
      } else {
        alert("Not Found");
      }
    },
    checkForEnterKey(event) {
      if (event.keyCode == 13) {
        alert(this.searchedTopic);
        this.getTopic();
      }
    },
  },
  mounted() {
    this.$store.state.curpage = "Find Your Topic";
    var vm = this;
    this.$http.get("gettopics").then(async function (response) {
      console.log("Load Main Page");
      var tmp = [];
      var topics = response.data;
      vm.topics = topics;
      var randomInd = vm.getNums();
      console.log(randomInd);
      for (var i in randomInd) {
        tmp.push(topics[i]);
      }
      vm.selectedTopics = tmp;
      console.log(vm.selectedTopics);
    });
  },
};
</script>
