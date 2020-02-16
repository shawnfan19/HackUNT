<template>
  <v-app>
    <StateFarm></StateFarm>
  </v-app>
</template>

<script>
import StateFarm from './components/StateFarm';

export default {
  name: 'App',

  components: {
    StateFarm,
  },

  data: () => ({
    //
  }),
};
</script>
