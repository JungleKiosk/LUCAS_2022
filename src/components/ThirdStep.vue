<script>
import PyClipping from './PyClipping.vue';
import SliderTotalPath from './SliderTotalPath.vue';
import SliderModifyPath from './SliderModifyPath.vue';

/* img street graph */
import img_cards_1 from '../assets/img/third_step/strade_cut_vr.png'
import img_cards_2 from '../assets/img/third_step/strade_veneto_cut_vr.png'
/* img Google Earth Pro */
import img_gep_1 from '../assets/img/third_step/gep_view_mode_1.png'
import img_gep_2 from '../assets/img/third_step/gep_ultimate_path.png'


export default {
    components: { PyClipping, SliderTotalPath, SliderModifyPath },
    data() {
        return {
            img_cards_1: img_cards_1,
            img_cards_2: img_cards_2,
            img_gep_1: img_gep_1,
            img_gep_2: img_gep_2,

            cards: [
                {
                    img_vr: img_cards_1,
                    txt_img_vr: 'Urban road graph (blue) and forest-pastoral (orange) Municipality of Verona'
                },
                {
                    img_vr: img_cards_2,
                    txt_img_vr: 'Urban road graph (blue) and forest-pastoral (orange) Region of Veneto'
                }
            ],
            gep: [
                {
                    img_gep: img_gep_1,
                },
                {
                    img_gep: img_gep_2,
                }
            ],

            currentIndex: 1,
        }
    },
    methods: {
        slideimage() {
            this.currentIndex =
                this.currentIndex === 0 ? this.cards.length - 1 : this.currentIndex - 1
        },

    }
}


</script>

<template>
    <main>
        <div class="container my_flow" id="3">
            <div class="row justify-content-center g-3">
                <div class="col-12 col-lg-8">

                    <h2><span class="txt_steps">Third Step: </span> <span class="txt_title_thin">Shortest path to
                            point</span></h2>
                    <p>
                        To optimize travel, I downloaded the cartography from the Geoportal of the Veneto Region, of the
                        urban and forest-pastoral road graph of the
                        Veneto region, extrapolating from the entire regional road graph only the data within the
                        administrative boundaries of Verona. <br> [ same procedure described above: Clip Geoprocessing ]
                    </p>
                    <p>
                        In the same way as described above, I then subdivided the road graphs for each "cardinal topological
                        district" (roads: North, East, South, West). [ Clips
                        Geoprocessing ]
                        Taking advantage of these SHPs, I calculated the shortest routes to reach the LUCAS points, having
                        the Verona railway station as a starting point. <br>
                        I have prepared the routes so as to be able to sample AT LEAST ten LUCAS points a day, trying when
                        possible to develop round-trip routes; In this way I was able to take advantage of the QGIS Python
                        API functions to calculate the parameters of
                        organizational interest: time taken for each journey, fuel consumption and costs, ecological impact
                        in terms of CO2 emissions.
                    </p>

                </div>

                <div class="row justify-content-center my-3">
                    <div class="col-12 col-lg-6 ">
                        <div class="control text-center">
                            <button class="btn text-light zoom-effect lucas_link my-2"
                                @click="slideimage()"><strong>&leftarrow;
                                    Slide image &rightarrow;</strong></button>
                        </div>
                    </div>
                </div>


                <div class="row justify-content-center my-4">

                    <div class="col-12 col-lg-7 col-md-12">
                        <p class="text-center"> <strong>{{ cards[currentIndex].txt_img_vr }}</strong> </p>

                        <div class="fix_card_img_vr">


                            <div class="cont_img_vr">
                                <img class="rounded-3 street_vr_img" :src="cards[currentIndex].img_vr"
                                    alt="cardinal zone in of Verona QGIS" />

                            </div>
                        </div>

                    </div>

                </div>

                <div class="col-12 col-lg-8">
                    <p>
                        With the <span class="txt_primary">Shortest Path</span> Geoprocessing tool it is possible to
                        identify the shortest route between two
                        points, on a road graph layer (Verona road graph shape file).
                    </p>

                    <p>
                        It is important to consider that in general <span class="txt_primary">the shortest route is NOT
                            always the fastest or easiest route:</span>

                        <li>that the route provided by the algorithm requires an incoming road layer</li>
                        <li>It does not consider natural and anthropic obstacles.</li>

                    </p>
                    <p>
                        In fact, analyzing the result, I found myself forced to modify the path with the topological
                        tools of QGIS.<br> The images below show that the distance between the road and the point is only
                        almost
                        100 m, but there is an<span class="txt_primary"> agricultural ditch</span>, which in the
                        spring-summer season could be impenetrable due
                        to
                        vegetation and/or agricultural waters. <br> <br>
                        Furthermore, taking advantage of the Street View Mode function of Google Earth Pro it was possible
                        to
                        get an idea of what could have been found. <br> As you can see, the passage to reach the point was
                        blocked by a building site (for my personal curiosity I passed through it and it was actually
                        there)<br><br>
                    </p>
                </div>

                <div class="row justify-content-center my-3">
                    <div class="col-12 col-lg-8 col-md-12 text-center">
                        <p><strong>Google Earth Pro</strong></p>
                        <img class="rounded-3 gep" src="../assets/img/third_step/gep_p79_viaGalileoGalilei.png" alt="">
                    </div>
                </div>

                <div class="col-12 col-lg-8">
                    <p class="text-center">
                        <br>
                        <br>
                        <br>
                        <span class="txt_note">Please Note: </span> <br> QGIS shortest path algorithm often matches the
                        solution that Google Maps would provide.
                    </p>
                </div>
                <div class="row justify-content-center my-3">
                    <div class="col-12 col-lg-6 col-md-12 text-center">
                        <p><strong>QGIS</strong></p>
                        <img class="rounded-3 my_maps" src="../assets/img/third_step/QGIS_p79_viaGalileoGalilei.png" alt="">
                    </div>
                    <div class="col-12 col-lg-6 col-md-12 text-center">
                        <p><strong>Google Maps</strong></p>
                        <img class="rounded-3 my_maps" src="../assets/img/third_step/MyMaps_via_GB_Zenetti_closed.png" alt="">
                    </div>
                </div>
                <div class="text-dark"></div>
                <br>
                <br>
                <br>
                <br>
                <br>
                <div class="col-12 col-lg-8 text-center">
                    <p>
                        So it was necessary to modify the Shortest Path QGIS layer, looking for an alternative and more
                        feasible
                        way; always with the help of Google Earth Pro.
                    </p>
                    <SliderModifyPath></SliderModifyPath>
                </div>
            </div>
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <div class="container">
            <div class="row justify-content-center">

                <div class="col-12 col-lg-8 text-center">
                    <p>
                        In order, here are two videos that illustrate the route development process:
                    </p>
                </div>

                <div class="container">
                    <div class="row justify-content-center">
                        
                        <div class="col-3 col-lg-1 text-center">
                            <a href="https://www.youtube.com/watch?v=Wbse3awiWEs&list=PLR8J_sq3CKNeNDxQ5qduA0e1RSphD2sfV&index=2" target="_blank">
                                <img class="text-center zoom_yt" src="../assets/img/yt.svg" alt="">
                            </a>
                            <span>Click</span>
                        </div>
                        
                        <div class="col-3 col-lg-1 text-center">
                            
                            <a href="https://www.youtube.com/watch?v=91kFQ2DMe50&list=PLR8J_sq3CKNeNDxQ5qduA0e1RSphD2sfV&index=3" target="_blank">
                                <img class="text-center zoom_yt" src="../assets/img/yt.svg" alt="">
                            </a>
                            <span>Click</span>
                        </div>
                    </div>
                </div>

                <div class="col-12 col-lg-8 text-center">
                    <br>
                    <br>
                    <br>
                    <p>
                        The following images show the final result of processing all the paths:
                    </p>
                    <SliderTotalPath></SliderTotalPath>
                </div>
            </div>
        </div>
    </main>
</template>

<style>
img {
    width: 100%;

}

.gep {
    height: 345px;
}

.my_maps {
    height: 400px;
}

.modify_path {
    height: 500px;
}

.image-container {
    position: relative;
}

.point {
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: red;
    border-radius: 50%;
}

@media only screen and (max-width: 767px) {

    .modify_path,
    .my_maps,
    .gep {
        height: 200px;
        /* imposta un'altezza diversa per i dispositivi mobili */
    }
}
</style>