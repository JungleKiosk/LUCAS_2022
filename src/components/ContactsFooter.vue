<script>
export default {
  name: "ContactFooter",
  props: {
    contacts: Object,
  },
  methods: {
    getLogoPath: function (name) {
      return new URL(`../assets/img/${name}`, import.meta.url).href
    }
  },

}
</script>

<template>
  <section class="contacts col">

    <ul>
    <h5>Contacts</h5>
      <!-- <p class="address m-0">{{ `${contacts.country}, ${contacts.state} ${contacts.houseNumber}, ${contacts.street}, ${contacts.state}` }}</p> -->
      <p class="phone_numbers my-3">
        Tel.: {{ contacts.tel }}
        <br>
        <!-- Tel.: {{ contacts.tel_2 }} -->
      </p>
      <p class="email m-0">{{ contacts.email }}</p>
  
      <div class="container">
        <div class="row justify-content-between">
          <div class="col-6 col-lg-6 my-4">
            <div class="d-flex">
              <div class="px-1" v-for="logo in contacts.logos" :key="logo.img_logo">
                <a :href="logo.url" target="_blank">
                  <img :src="getLogoPath(logo.img_logo)" :alt="logo.img_logo">
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

    </ul>

  </section>
  <!-- /.col -->
</template>
 