<script>
import PyClipping from './PyClipping.vue';

import img_cards_1 from '../assets/img/second_step/vr_city_clip.png'
import img_cards_2 from '../assets/img/second_step/vr_nord_clip.png'
import img_cards_3 from '../assets/img/second_step/vr_est_clip.png'
import img_cards_4 from '../assets/img/second_step/vr_sud_cli.png'
import img_cards_5 from '../assets/img/second_step/vr_ovest_clip.png'


export default {
    components: { PyClipping },  
    data() {
        return {
            img_cards_1: img_cards_1,
            img_cards_2: img_cards_2,
            img_cards_3: img_cards_3,
            img_cards_4: img_cards_4,
            img_cards_5: img_cards_5,

            cards: [
                {
                    img_vr: img_cards_1,
                    txt_img_vr: 'City'
                },
                {
                    img_vr: img_cards_2,
                    txt_img_vr: 'North'
                },
                {
                    img_vr: img_cards_3,
                    txt_img_vr: 'East'
                },
                {
                    img_vr: img_cards_4,
                    txt_img_vr: 'South'
                },
                {
                    img_vr: img_cards_5,
                    txt_img_vr: 'West'
                }
            ],

            currentIndex: 0,
        }
    },
    methods: {
        nextCard() {
            this.currentIndex =
                this.currentIndex === this.cards.length - 1 ? 0 : this.currentIndex + 1
        },
        prevCard() {
            this.currentIndex =
                this.currentIndex === 0 ? this.cards.length - 1 : this.currentIndex - 1
        },
    }
}

</script>

<template>
    <main>

        <div class="container my_flow py-4" id="2">
            <div class="row justify-content-center ">

                <div class="col-12 col-lg-8">

                    <h2> <span class="txt_steps">Second Step: </span><span class="txt_title_thin">"topological districts”</span></h2>
                    <p>
                        As already announced previously, to obtain a good survey of field data it is good to consider the
                        phenological phases of cultivation and grazing; <br> high density crops per square metre, such as
                        corn or sunflower, do not allow passage to the field in the late summer months. <br> In general,
                        it is good to take care not to damage the crops in the field, this applies to all crops.
                    </p>
                    <p>
                        Therefore, in order to increase the efficiency of my personal organization, <br> I preferred to
                        divide
                        the points into zones
                        with similar orography and <span class="tile text-decoration-underline"
                            title="areas with different agricultural and forestry traditions">socio-economic</span>
                        characteristics.
                    </p>

                    <p>
                        As before, I have extrapolated the boundaries and the points,
                        in order to zoning the points
                        (QGIS geoprocessing clips)
                    </p>
                    <small>Is possible to iterate the clipping process through the use of the Python console in QGIS, click the button to see a practical example</small>
                    <PyClipping></PyClipping>

                    <p>
                        <span class="note">Please note:</span> in the following images the names of the SHPs show the names
                        of the North, East, South and West cardinal points but do not necessarily reflect their boundaries
                        administrations, remains a personal subdivision according to the phenological trends of the crops
                        agriculture and the orography of the territory
                    </p>

                </div>

            </div>

            <div class="row justify-content-center my-3">

                <div class="col-2 col-lg-1 col-md-1 ">
                    <div class="control text-center">
                        <button class="btn btn_arrow"
                            @click="prevCard()"><strong>&leftarrow;</strong></button>
                    </div>
                </div>
                <div class="col-6 col-lg-1 col-md-1  text-center">
                    <p>{{ cards[currentIndex].txt_img_vr }}</p>
                </div>

                <div class="col-2 col-md-1 text-center">
                    <div class="control text-center">
                        <button class="btn btn_arrow"
                            @click="nextCard()"><strong>&rightarrow;</strong></button>
                    </div>
                </div>


            </div>

            <div class="row justify-content-center">

                <div class="col-12 col-lg-9 col-md-12 px-5">

                    <div class="bg-transparent border-0 text-center">
                        <div class="cont_img_vr">
                            <img class="rounded-3 cardinal_vr" :src="cards[currentIndex].img_vr"
                                alt="cardinal zone in of Verona QGIS" />
                        </div>
                    </div>


                </div>
            </div>



        </div>





    </main>
</template>

<style>
.tile {
    color: rgb(255, 140, 0);
}

.note {
    color: #f2b91e;
}

.cardinal_vr {
    width: 100%;
}
</style>