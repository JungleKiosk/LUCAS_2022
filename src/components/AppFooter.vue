<script>

import { contacts } from "./../data/contacts.js"
import { projects } from "./../data/projects.js"
import { correlations } from "./../data/correlations.js"

import AboutFooter from "./AboutFooter.vue"
import ContactsFooter from "./ContactsFooter.vue"
import ProjectsFooter from "./ProjectsFooter.vue"
import CorrelationsFooter from "./CorrelationsFooter.vue"

export default {
  name: "AppFooter",
  components: {
    AboutFooter,
    ContactsFooter,
    ProjectsFooter,
    CorrelationsFooter,
  },
  data() {
    return {
      contacts,
      projects,
      correlations,
    }
  },
}
</script>

<template>
  <img class="wave_svg margin-bottom: -1px;" style="height: 90px;" src="../assets/img/decoration/wave.svg" alt="">
  <footer>
    <div class="container" id="Contacts">
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3">
        <AboutFooter></AboutFooter>
        <CorrelationsFooter :blog="correlations"></CorrelationsFooter>
        <ProjectsFooter :pages="projects"></ProjectsFooter>
        <ContactsFooter :contacts="contacts"></ContactsFooter>
      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->
  </footer>
</template>