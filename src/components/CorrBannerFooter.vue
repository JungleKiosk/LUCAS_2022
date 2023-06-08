<script>
export default {
  name: "ArticlePreview",
  props: {
    item: Object,
  },
  methods: {
    getImageUrl(image) {
      return new URL(`/src/assets/img/${image}`, import.meta.url).href
    }
  }
}
</script>

<template>
  <li>
    <a class="d-flex align-items-center" :href="item.link" target="_blank">
      <img class="w-25 me-3 my-3 flex-shrink-0 rounded-0" :src="getImageUrl(item.img)" alt="Correlation projects">
      <div class="text">
        <h6>{{ item.title }}</h6>
        <span>{{ item.date }}</span>
      </div>
      <!-- /.text -->
    </a>
  </li>
</template>
