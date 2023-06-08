<script>
export default {
    name: "EndLogos",
}
</script>

<template>
    <div class="container container_endlogos">
<!--         <h1 class="text-center"><span class="txt_primary">Runtime, Frameworks, Libraries, Style</span> be used:</h1> -->
        <div class="row justify-content-center">
            <div class="col-lg-6">
                <div class="container_logos text-center">
                    <a href="https://nodejs.org/en/docs">
                        <img class="img-fluid col-sm-6 col-md-4 col-lg-6 zoom_effect_logos" src="./../assets/img/conc_logos/Nodejs.svg" alt="">
                    </a>
                    <div class="img-fluid col-sm-6 col-md-4 col-lg-6"></div>
                    <a href="https://vitejs.dev/">
                        <img class="img-fluid col-4 col-md-4 col-lg-2 mx-3 zoom_effect_logos" src="./../assets/img/conc_logos/vitejs.svg" alt="">
                    </a>
                    <a href="https://vuejs.org/">
                        <img class="img-fluid col-4 col-md-4 col-lg-2 mx-3 zoom_effect_logos" src="./../assets/img/conc_logos/vuejs.svg" alt="">
                    </a>
                    <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">
                        <img class="img-fluid col-4 col-md-4 col-lg-2 mx-3 my-3 zoom_effect_logos" src="./../assets/img/conc_logos/bootstrap.svg" alt="">
                    </a>
                    <a href="https://docs.npmjs.com/getting-started">
                        <img class="img-fluid col-6 col-md-4 col-lg-4 mx-3 my-3 zoom_effect_logos" src="./../assets/img/conc_logos/npm.svg" alt="">
                    </a>
                    <a href="https://vue-chartjs.org/">
                        <img class="img-fluid col-4 col-md-4 col-lg-2 mx-3 zoom_effect_logos" src="./../assets/img/conc_logos/vue-chartjs.png" alt="">
                    </a>
                    <div class="img-fluid col-sm-6 col-md-4 col-lg-6 my-3"></div>
                    <a href="https://sass-lang.com/">
                        <img class="img-fluid col-4 col-md-4 col-lg-4 my-3 zoom_effect_logos" src="./../assets/img/conc_logos/sass.svg" alt="">
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>


<style>

.container_endlogos{
    margin-top: 20px;
    margin-bottom: 60px;
}

.zoom_effect_logos {
    transition: transform 0.2s ease-in-out;
    transform-origin: center center;
}

.zoom_effect_logos:hover {
    transform: scale(1.1);
}

</style>


