<script>


export default {
    data() {

        return {

        };
    }

}



</script>

<template>
    <main>
        <div class="container my_flow margin_final" id="5">
            <div class="row justify-content-center">
                <div class="col-12 col-lg-8">
                    <h2> <span class="txt_steps">Fifth Step: </span><span class="txt_title_thin">import into Google My
                            Maps</span></h2>
                    <p>
                        for personal convenience I prefer to use the mobile phone as a navigator to reach the vicinity of
                        the point
                        Lucas by car. To do this it is necessary to transform the SHP obtained from the previous
                        explanations into KML or
                        another format that can be loaded in the MyMaps Google environment. To do this, you can proceed as
                        described
                        Previously, I prefer to use the MMQGIS plugin.
                    </p>

                    <p>
                        From this arises the need to be able to view the data relating to each point in Google My Maps, in
                        order to be able to better optimize the trips knowing in advance the LUCAS parameters required for
                        each point.
                    </p>

                    <p>
                        Among the material sent to me to carry out the assignment, I used an Excel file to obtain the
                        desired result. In fact, this file contained the ID of each point of my interest and the relative
                        LUCAS parameters to be detected.
                    </p>


                    <div class="line my-5"></div>
                    <h2 class="text-center">But ...</h2>
                    <h4>
                        ... How can you merge an Excel file with the attribute table of a Shapefile?...
                    </h4>
                    <div class="line my-3"></div>

                    <div class="container gif_doc">
                        <div class="row justify-content-center">
                            <div class=" col-12 col-lg-6 my-5">
                                <h3 class="text-center">...with the <span class="txt_title_thin">JOIN </span>algorithm !
                                </h3>
                                <img class="text-center" src="../assets/img/DOC_ready_SVG_GIF.gif" alt="">
                            </div>
                        </div>
                    </div>

                    <p>
                        With the JOINbyFIELD algorithm of QGIS it is possible to satisfy this need. The main rule for
                        using the JOIN by field is that (as the name suggests) there is at least one field in common between
                        two different datasets; that is, with the same header name and records (observations) in both
                        datasets, so the length of the field must be the same in both datasets. If these requirements are
                        not satisfied the algorithm does not work.
                    </p>

                    <p>
                        The following video can better explain the use of the QGIS JOIN algorithm
                    </p>

                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-3 col-lg-2 text-center">
                                <a href="">
                                    <img class="text-center zoom_yt" src="../assets/img/yt.svg" alt="">
                                </a>
                                <span>Click</span>
                            </div>
                        </div>
                    </div>

                    <p>
                        Once the KMLs have been obtained, it is possible to create the personal work map in Google My Maps
                        and on a
                        daily basis
                        update it. Below is my personal map and the legend of the icons

                    </p>

                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-3 col-lg-2 text-center">
                                <a href="">
                                    <img class="text-center zoom_yt" src="../assets/img/yt.svg" alt="">
                                </a>
                                <span>Click</span>
                            </div>
                        </div>
                    </div>


                </div>
            </div>
        </div>

    </main>
</template>

<style>
ul {
    list-style-type: none;
}

li span {
    color: chartreuse;
}

.gif_doc {
    margin-bottom: 10rem;
}

.margin_final {
    margin-bottom: 200px;
}
</style>