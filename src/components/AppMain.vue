<script>

import JumboTron from './Jumbotron.vue';
import PostJumbo from './PostJumbo.vue';
import Intro from './Intro.vue';
import FirstStep from './FirstStep.vue';


export default {
    data() {
        return {};
    },
    components: { JumboTron, PostJumbo, Intro, FirstStep },
}

</script>

<template>

  <main>
    <JumboTron></JumboTron>
    <PostJumbo></PostJumbo>
    <Intro></Intro>
    <FirstStep></FirstStep>
    

  </main>
</template>

<style></style>