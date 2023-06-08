<script>

import JumboTron from './Jumbotron.vue';
import PostJumbo from './PostJumbo.vue';
import Intro from './Intro.vue';
import FirstStep from './FirstStep.vue';
import SecondStep from './SecondStep.vue';

export default {
    data() {
        return {};
    },
    components: { JumboTron, PostJumbo, Intro, FirstStep, SecondStep },
}

</script>

<template>

  <main>
    <JumboTron></JumboTron>
    <PostJumbo></PostJumbo>
    <Intro></Intro>
    <FirstStep></FirstStep>
    <SecondStep></SecondStep>


  </main>
</template>

<style></style>