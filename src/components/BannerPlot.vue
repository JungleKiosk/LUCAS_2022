<script>

import { stackArray } from "../data/myStack.js"

export default {
    name: 'BannerPlot',
    data() {
        return {
            stackArray
            /* currentColumn: 1, */

        }
    }, methods: {
        getImagePath: function (name) {
            return new URL(`../assets/img/${name}`, import.meta.url).href
        }/* ,
        toggleCard(stack) {
            this.cards.forEach((card, i) => {
                if (stack === i) {
                    card.isOpen = !card.isOpen;
                    card.selected = true; // on "selected"
                } else {
                    card.isOpen = false;
                    card.selected = false; // off "selected" 
                }
            });
        },
        animateBackground() {
            setInterval(() => {
                this.currentColumn = (this.currentColumn % 4) + 1;
                this.toggleCard(this.currentColumn - 1);
            }, 3000);
        }

    }, mounted() {
        // avvia l'animazione al caricamento della pagina
        this.animateBackground();
    } */
    }
}

</script>

<template>
    <main>

        <!--         <div class="gradient left"></div>
        <div class="gradient right"></div> -->

        <div class="banner bg_banner position-relative">
            <!-- <div class="line_banner_up rounded-5 text-center"></div> -->

            <div class="container py-5">
                <div class="row justify-content-center">
                    <div v-for="stack in stackArray" :key="stack.img"
                        class="stak_card col-6 col-lg-3 col-md-6 text-center px-5 py-5 rounded-5">
                        <div class="container_logos">
                            <img :src="getImagePath(stack.img)" alt="">
                        </div>
                        <!--    <h5 :style="{ color: currentColumn === (stack + 1) ? '#ffcc00' : '', transition: 'color 1s ease' }">  -->
                        <h5>{{ stack.title }}</h5>
                        <p>{{ stack.desc }}</p>
                        <a :href="stack.href" target="_blank">Getting started </a>
                    </div>
                </div>
            </div>

            <!-- <div class="cover_right"></div> -->


            <div class="line_banner_down rounded-5">
            </div>

        </div>

    </main>
</template>

