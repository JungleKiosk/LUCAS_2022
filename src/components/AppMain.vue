<script>

import JumboTron from './Jumbotron.vue';
import PostJumbo from './PostJumbo.vue';
import Intro from './Intro.vue';
import FirstStep from './FirstStep.vue';
import SecondStep from './SecondStep.vue';
import ThirdStep from './ThirdStep.vue';
import FourthStep from './FourthStep.vue';
import CutterPage from './CutterPage.vue';
import LastStep from './LastStep.vue';
import Conclusion from './Conclusion.vue';
import ConclusionLogos from './ConclusionLogos.vue';

export default {
  data() {
    return {};
  },
  components: {
    JumboTron,
    PostJumbo,
    Intro,
    FirstStep,
    SecondStep,
    ThirdStep,
    FourthStep,
    CutterPage,
    LastStep,
    Conclusion,
    ConclusionLogos },
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
    <FourthStep></FourthStep>
    <CutterPage></CutterPage>
    <LastStep></LastStep>
    <Conclusion></Conclusion>
    <ConclusionLogos></ConclusionLogos>

  </main>
</template>

<style></style>