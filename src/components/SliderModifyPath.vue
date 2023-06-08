<script>


import img_cards_1 from '../assets/img/third_step/gep_ultimate_path.png'
import img_cards_2 from '../assets/img/third_step/shortest_path_modify.png'
import img_cards_3 from '../assets/img/third_step/gep_view_mode_1.png'


 
export default {
    data() {
        return {
            img_cards_1: img_cards_1,
            img_cards_2: img_cards_2,
            img_cards_3: img_cards_3,
            cards: [
                {
                    img_vr: img_cards_1,
                    txt_img_vr: '3D view'
                },
                {
                    img_vr: img_cards_2,
                    txt_img_vr: 'QGIS view'
                },
                {
                    img_vr: img_cards_3,
                    txt_img_vr: 'Ground view'
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

        <div class="col-md-1 col-6">
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

        <div class="col-12 col-lg-8 col-md-8 px-5">

            <div class="bg-transparent border-0 text-center">
                <div class="cont_img_vr">
                    <img class="rounded-3 cardinal_vr" :src="cards[currentIndex].img_vr"
                        alt="cardinal zone in of Verona QGIS" />
                </div>
            </div>


        </div>
    </div>
</template>

<style></style>