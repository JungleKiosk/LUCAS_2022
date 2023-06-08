<script>


import img_cards_1 from '../assets/img/third_step/path_city.png'
import img_cards_2 from '../assets/img/third_step/path_nord.png'
import img_cards_3 from '../assets/img/third_step/path_est.png'
import img_cards_4 from '../assets/img/third_step/path_sud.png'
import img_cards_5 from '../assets/img/third_step/path_ovest.png'
import img_cards_6 from '../assets/img/third_step/path_all_vr.png'
import img_cards_7 from '../assets/img/third_step/path_all_vr_grafo.png'


export default {
    data() {
        return { 
            img_cards_1: img_cards_1,
            img_cards_2: img_cards_2,
            img_cards_3: img_cards_3,
            img_cards_4: img_cards_4,
            img_cards_5: img_cards_5,
            img_cards_6: img_cards_6,
            img_cards_7:img_cards_7,

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
                },
                {
                    img_vr: img_cards_6,
                    txt_img_vr: 'Paths'
                },
                {
                    img_vr: img_cards_7,
                    txt_img_vr: 'Graph'
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
    <div class="row justify-content-center my-3">

        <div class="col-md-1 col-2">
            <div class="control text-center">
                <button class="btn btn_arrow"
                    @click="prevCard()"><strong>&leftarrow;</strong></button>
            </div>
        </div>
        <div class="col-md-1 col-6 text-center">
            <p>{{ cards[currentIndex].txt_img_vr }}</p>
        </div>

        <div class="col-md-1 col-2 text-center">
            <div class="control text-center">
                <button class="btn btn_arrow"
                    @click="nextCard()"><strong>&rightarrow;</strong></button>
            </div>
        </div>


    </div>

    <div class="row justify-content-center">

        <div class="col-12 col-lg-10 col-md-8 px-5">

            <div class="bg-transparent border-0 text-center">
                <div class="cont_img_vr">
                    <img class="rounded-3 cardinal_vr" :src="cards[currentIndex].img_vr"
                        alt="cardinal zone in of Verona QGIS" />
                </div>
            </div>


        </div>
    </div>
</template>

<style>


</style>