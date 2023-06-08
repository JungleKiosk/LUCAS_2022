<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'BarChart',
    components: { Bar },
    data() {
        return {
            chartData: {
                labels: [
                    'North',
                    'East',
                    'South',
                    'West',
                    'City'
                ],
                datasets: [
                    {
                        label: 'CO2 emissions [ Kg / km ] ',
                        backgroundColor: 'rgb(34, 173, 150, 0.5)',
                        borderColor: 'rgb(63, 58, 100, 0.8)',
                        borderWidth: 3,
                        data: [
                            80,
                            44,
                            66,
                            19,
                            15
                        ],
                    },
                ],
            },
            chartOptions: {
                responsive: true,
                indexAxis: 'y',
                scales: {
                    x: {
                        ticks: {
                            color: '#3f3a64',
                        },
                    },
                    y: {
                        ticks: {
                            color: '#3f3a64',
                        },
                    },
                },
            },
        }
    },
}
</script>





<template>
    <div class="container">
        <div class="row">
            <div class="col-12 col-lg-8 col-md-12">
                <div class="card  border border-dark">
                    <div class="card-header bg_primary text-light">
                        <div class="row justify-content-center">
                            <div class="col-8 col-lg-8">
                                <small>Sum by area</small>
                            </div>
                            <div class="col-4 col-lg-4">
                                <small>Next Chart &RightArrow;</small>
                            </div>
                        </div>
                    </div>

                    <div class="card-body bg_chart">
                        <Bar :data="chartData" :options="chartOptions"></Bar>

                    </div>


                </div>

            </div>
        </div>
    </div>
</template>

<style scoped>
.bg_chart {
    background-color:rgb(63, 58, 100, 0.3);
}
</style>