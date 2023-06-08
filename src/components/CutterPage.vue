

<script>


export default {
    name: 'AppMain',
    data() {
        return { 
            statistics: [
                {   
                    number: '',
                    txt: '',
                    current_hover: false
                },
                {
                    number: '195.31 ',
                    txt: '€ Fuel',
                    current_hover: true
                },
                {
                    number: '223 ',
                    txt: 'Kg CO2',
                    current_hover: false
                },
                {
                    number: '2124 ',
                    txt: 'Km Traveled',
                    current_hover: false
                },
                {
                    number: '42.5 ',
                    txt: 'Hours spent',
                    current_hover: false
                },
                {  
                    number: '',
                    txt: '',
                    current_hover: false
                }
            ]

        }
    }
}

</script>

<template>
    <main id="banner_totals">
        <h1 class="text-center py-3">estimated <span class="txt_primary">Totals</span> </h1>
        <section id="cutter_page">
    
            <div class="container">
                <div class="row justify-content-between align-items-center text-center">
                    <div v-for="statistic in statistics" class="col-12 col-lg-2 col_cutter py-4 count-animation">
                        <span class="number">{{ statistic.number }}</span>
                        <span class="txt">{{ statistic.txt }}</span>
                    </div>
                </div>
    
            </div>
    
    
        </section>

    </main>
</template>

<style lang="scss">
@use '../assets/scss/partials/variables' as *;

main {

    #banner_totals{
        margin-top: 0px;


    }
    #cutter_page {
        background-color: $primary;
        margin-bottom: 300px;

        .number {
            color: $clr_bruise;
            font-size: 2.5rem;
            font-weight: bold;
            display: block;
        }

        .txt {
            
            font-size: 1rem;
            font-weight: bold;
            display: block;
        }

        .col_cutter {
            position: relative;
            display: inline-block;
        }

        .col_cutter:hover:before {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 0;
            height: 0;
            border-radius: 50%;
            background-color: $clr_bruise ;
            opacity: 0.5;
            animation: wave 0.8s linear forwards;
        }

        @keyframes wave {
            0% {
                width: 0;
                height: 0;
                opacity: 0.5;
            }

            100% {
                width: 150px;
                height: 150px;
                opacity: 0;
            }
        }
    }

}

</style>
