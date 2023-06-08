<script>
import CorrBannerFooter from "./CorrBannerFooter.vue"

export default {
  name: "BlogFooter",
  components: {
    CorrBannerFooter,
  },
  props: {
    blog: Array,
  },
}
</script>

<template>
  <section class="correlations col">
    <h5>Correlations</h5>
    <ul>
      <CorrBannerFooter v-for="n in 2" :key="blog[n - 1].title + blog[n - 1].date" :item="blog[n - 1]"></CorrBannerFooter>
    </ul>
  </section>
  <!-- /.col -->
</template>
 