<script>


import img_cards_1 from '../assets/img/fourth_step/csv_pivot_fuel.png'
import img_cards_2 from '../assets/img/fourth_step/csv_pivot_co2.png'
import img_cards_3 from '../assets/img/fourth_step/csv_pivot_km.png'
import img_cards_4 from '../assets/img/fourth_step/csv_time_h.png'

export default {
    data() {
        return {
            img_cards_1: img_cards_1,
            img_cards_2: img_cards_2,
            img_cards_3: img_cards_3,
            img_cards_4: img_cards_4,
            cards: [
                {
                    img_vr: img_cards_1,
                    txt_img_vr: 'Fuel consuption'
                },
                {
                    img_vr: img_cards_2,
                    txt_img_vr: 'CO2 emissions'
                },
                {
                    img_vr: img_cards_3,
                    txt_img_vr: 'Path length'
                }
                ,
                {
                    img_vr: img_cards_4,
                    txt_img_vr: 'Time'
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
    <div class="row justify-content-center my-2">

        <div class="col-md-1 col-2">
            <div class="control text-center">
                <button class="btn btn_arrow"
                    @click="prevCard()"><strong>&leftarrow;</strong></button>
            </div>
        </div>
        <div class="col-lg-3 col-md-3 col-6 text-center">
            <p>{{ cards[currentIndex].txt_img_vr }}</p>
        </div>

        <div class="col-md-1 col-2 text-center">
            <div class="control text-center">
                <button class="btn btn_arrow"
                    @click="nextCard()"><strong>&rightarrow;</strong></button>
            </div>
        </div>


    </div>

    <div class="row justify-content-center slider_csv">

        <div class="col-12 col-lg-12 col-md-8 px-5">

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

.slider_csv{
    margin-bottom: 5rem;
}
.cont_img_vr {
    max-width: 100%;
    height: auto;
}

.cont_img_vr img {
    width: 100%;
    height: auto;
}

</style>