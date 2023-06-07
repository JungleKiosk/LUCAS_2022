<script>



export default {
    name: "MainMenu",
    data() {
        return {
        }
    },
    props: {
        menu: Array
    }
}
</script>

<!-- @mouseover="option.clicked = true"
            @mouseleave="option.clicked = false" -->
<template>
    <a :href="`#${option.id}`" class="linkpage-center" v-for="(option, index) in menu">
        <button class="border border-0 bg-transparent deskopt_version" :class="{ 'active_option': option.clicked }"
            type="button" aria-expanded="false">
            {{ option.title }}
        </button>
    </a>
</template>

