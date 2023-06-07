<script>
import { navbarHeaderInfo } from "../data/navbarHeaderInfo.js"
import MainMenu from './MainMenu.vue';

export default {
    name: "AppHeader",
    data() {
        return {
            navbarHeaderInfo,
            headerScroll: true,
            lastPosition: 0,
            shadow_on: false,
            isMobileMenuOpen: false,
            shouldVibrate: false,
            isTopOfPage: true
        }
    },
    components: {
        MainMenu
    },
    methods: {
        toggleMenu() {
            this.isMobileMenuOpen = !this.isMobileMenuOpen;
            if (this.isMobileMenuOpen) {
                this.shouldVibrate = false;
                window.removeEventListener('scroll', this.scrollFunction);
            } else {
                this.shouldVibrate = true;
                window.addEventListener('scroll', this.scrollFunction);
            }
        },

        closeMenu() {
            this.isMobileMenuOpen = false;
            this.shouldVibrate = true;
            window.addEventListener('scroll', this.scrollFunction);
        },
        scrollFunction() {
            this.shadow_on = false;
            const currentPosition = window.pageYOffset;
            if (currentPosition > 0) {
                this.shadow_on = true;
                if (currentPosition > this.lastPosition) {
                    this.headerScroll = false;
                } else {
                    this.headerScroll = true;
                    this.shouldVibrate = true; // Attiva l'effetto di vibrazione quando si scorre verso l'alto
                }
                this.lastPosition = currentPosition;
                this.isTopOfPage = false;
            } else {
                this.shouldVibrate = false; // Disattiva l'effetto di vibrazione quando si torna all'inizio della pagina
                this.isTopOfPage = true;
            }
        }
    },

    mounted() {
        window.addEventListener('scroll', this.scrollFunction);
    }
}

</script>
<template>
    <img id="Start" src="../assets/img/jumbo-overlay.svg" alt="">
    <header class="d-flex justify-content-center align-items-center scroll_upper text-danger"
        :class="headerScroll ? 'header_on' : 'header_off', shadow_on ? ' header_shadow' : ''">
        <nav class="d-md-flex nav_style d-inline"
            :class="{ 'menu-open': isMobileMenuOpen, 'vibrating-menu': shouldVibrate && !isTopOfPage }">

            <button class="menu-button text-center justify-content-center rounded-pill" @click="toggleMenu"
                :class="{ 'vibrating-menu': shouldVibrate && !isTopOfPage }">MENU</button>

            <div class="navbar-content nav_style py-1 px-2" v-show="isMobileMenuOpen">
                <MainMenu :menu="navbarHeaderInfo" />

            </div>

        </nav>
    </header>
</template>

<style lang="scss" scoped>
.header_on {
    animation: on 0.3s linear forwards;
    transition: opacity 0.3s ease-in-out;
}

.header_off {
    animation: off 0.3s linear forwards;
    transition: opacity 0.3s ease-in-out;
}

.header_shadow {
    filter: drop-shadow(0px 0px 10px rgb(0, 174, 142));
    transition: filter 0.3s ease-in-out;
}


@keyframes on {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

@keyframes off {
    from {
        opacity: 1;
    }

    to {
        opacity: 0;
    }
}

.vibrating-menu {
    animation: vibration 1s linear infinite;
}

@keyframes vibration {
    0% {
        transform: translateX(0);
    }

    25% {
        transform: translateX(2px) rotate(-2deg);
    }

    50% {
        transform: translateX(-2px) rotate(2deg);
    }

    75% {
        transform: translateX(2px) rotate(-2deg);
    }

    100% {
        transform: translateX(0);
    }
}
</style>