<script>
import AppHeader from './components/AppHeader.vue';
import AppMain from './components/AppMain.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  data() {
    return {
      loadingXtime: true
    };
  },
  components: {
    AppHeader,
    AppMain,
    AppFooter
  },
  methods: {
    loadingPage() {
      setTimeout(() => {
        this.loadingXtime = false
      }, 2800)
    },
    changeTheme(newTheme) {
      document.documentElement.setAttribute('data-theme', newTheme)
    }
  },
  mounted() {
    const anchorTags = document.querySelectorAll('a[href="#"]');
    anchorTags.forEach(a => {
      a.addEventListener('click', event => {
        event.preventDefault();
      });
    });

    this.loadingPage()
  }
}

</script>

<template>
  <div v-if="loadingXtime">
    <div class="container container_loading">
      <div class="row justify-content-center">
        <div class="col-9 col-lg-3 col-md-6 text-center px-5 py-5 rounded-5">
          <h1 class="splash_page p-4">My<span class="txt_title_thin">FLOW</span> </h1>
          <div class="logo_container">
            <img class="gap splash_page" src="./assets/img/800px-QGIS_logo_minimal.svg.png" alt="Main_logo">
            <img class="gap splash_page" src="./assets/img/python-5.svg" alt="Main_logo">
            <img class="gap splash_page" src="./assets/img/icons8-google-maps.svg" alt="Main_logo">
            <img class="gap splash_page" src="./assets/img/Google_Earth_icon.svg.png" alt="Main_logo">
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-show="!loadingXtime">

    <AppHeader></AppHeader>
    <AppMain></AppMain>
    <AppFooter></AppFooter>

  </div>
</template>




<style lang="scss" scoped>
.container_loading {
  margin-top: 10rem;
}

.logo_container img {
  width: 50%;
}

.gap {
  padding-left: 3rem;
}

.logo_container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;

  .splash_page {
    opacity: 1;
    animation: wakeup 1.5s linear both;
  }

}

@keyframes wakeup {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}
</style>
