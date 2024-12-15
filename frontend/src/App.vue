<template>
  <div id="app">
    <SearchForm />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SearchForm from "./components/searchform.vue";

export default defineComponent({
  name: "App",
  components: {
    SearchForm,
  },
});
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
