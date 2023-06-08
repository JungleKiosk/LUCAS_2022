<script>

import JumboTron from './Jumbotron.vue';
import PostJumbo from './PostJumbo.vue';
import Intro from './Intro.vue';
import FirstStep from './FirstStep.vue';
import SecondStep from './SecondStep.vue';
import ThirdStep from './ThirdStep.vue';



export default {
    data() {
        return {};
    },
    components: { JumboTron, PostJumbo, Intro, FirstStep, SecondStep, ThirdStep },
}

</script>

<template>

  <main>
    <JumboTron></JumboTron>
    <PostJumbo></PostJumbo>
    <Intro></Intro>
    <FirstStep></FirstStep>
    <SecondStep></SecondStep>
    <ThirdStep></ThirdStep>


  </main>
</template>

<style></style>