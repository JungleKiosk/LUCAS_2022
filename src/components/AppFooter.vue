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
  <footer>
    <div class="container" id="Contacts">
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3">
        <AboutFooter></AboutFooter>
        <ContactsFooter :contacts="contacts"></ContactsFooter>
        <ProjectsFooter :pages="projects"></ProjectsFooter>
        <CorrelationsFooter :blog="correlations"></CorrelationsFooter>
      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->
  </footer>
</template>