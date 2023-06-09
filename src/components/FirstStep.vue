<script>
export default {
    data() {
        return {};
    },

}

</script>

<template>
    <main> 



        <div class="container my_flow py-4" id="1">
            <div class="row justify-content-center g-3">

                <div class="col-12 col-lg-8">
                    <h1> <span class="txt_steps">First Step: </span><span class="txt_title_thin">extrapolate the points</span></h1>
         
                    <p>In April 2022 I was assigned LUCAS points, falling within the administrative boundaries of the
                        province
                        of Verona (city in the Veneto region). These were in KML format.</p>
                    <p>
                        Loading the file in Google Earth Pro (GEP) I immediately noticed that the file presented not only
                        the points
                        of the province but of
                        all of Veneto, Trentino, Friuli-VG, a part of Lombardy and Emilia-Romagna; immediately arose there
                        need to extrapolate the points assigned to me in the province of Verona.

                    </p>
                    <p>
                        Furthermore, it should be considered that the LUCAS points are distributed in a pseudo-randomized
                        manner on a
                        2km x 2km grid; they could therefore fall into areas that are difficult to reach: wooded areas with
                        high
                        slopes, areas surrounded by agricultural canals that can only be reached via field roads, private
                        properties,
                        roads with no-passage...
                    </p>
                    <p>
                        To optimize daily trips (minimize the surprise effect in the open field) it is advisable to remotely
                        control a
                        map of suitability for physically reaching the LUCAS point, with the final aim of creating a travel
                        agenda
                        with the relative daily routes: this is possible using the Google My Maps service.
                    </p>
                    <p>
                        Below is the Google Earth Pro image of the aforementioned LUCAS points and the link to access the
                        travel map
                        report:

                    </p>
                </div>

                

                <div class="col-12 col-lg-8 col-md-9">

                    <div class="cont_img_vr text-center">
                        <img width="100%" class="rounded-4" src="../assets/img/first_step/lucas_2022_KML.png" alt="">
                    </div>

                </div>

                <!-- <div class="line"></div> -->


                <div class="col-12 col-lg-8 ">


                    <p>To extrapolate the 208 LUCAS points from the KML file it was necessary to consult the <a
                            class="txt_primary color_txt_link text-decoration-underline" href="https://idt2.regione.veneto.it/" target="_blank">Geoportal of
                            the Veneto region</a> , download the maps relating to the borders
                        administrative files in shape file format, so as to be able to include only the points of interest,
                        excluding
                        all the others.

                    </p>

                </div>

                <div class="col-12 col-lg-7 col-md-6 py-3 ">
                    <img class="rounded-3 " width="100%" src="../assets/img/first_step/geoportal_veneto_region.png" alt="">
                </div>

                <div class="col-12 col-lg-8 ">

                    <p>
                        I performed the procedure in QGIS environment with Geoprocessing tools; from the shape files
                        of the provinces and municipalities of the Veneto I have extrapolated those of Verona. Below
                        are the representative images of the shape files in QGIS (note Canvas and Layers to understand the
                        use of shape files)
                    </p>

                </div>

                <strong class="text-center">Veneto region shape file</strong>

                <div class="col-12 col-md-6 py-3 d-flex">
                    <img class="rounded-3 text-center" width="100%" src="../assets/img/first_step/shp_veneto_1.png" alt="">
                </div>

                <strong class="text-center">Select Verona Provincial Border Attribute Table -> export to shape file (Layer
                    in light green)</strong>

                <div class="col-12 col-md-6 py-3 d-flex">
                    <img class="rounded-3" width="100%" src="../assets/img/first_step/shp_verona_2.png" alt="">
                </div>

                <div class="col-12 col-lg-8 ">

                    <p>Now it remains to use the Verona borders layer as a mask to perform the clipping on the LUCAS points
                        layer. <br> First, however, it was necessary to transform the KML file into a shape file: loading it
                        in QGIS and saving it in ESRI shapefile format. <br> In the image you can see the mask of the
                        province of Verona on the entire shape file of the LUCAS points.
                    </p>

                </div>

                <div class="col-12 col-lg-8 col-md-6 py-3 d-flex">
                    <img class="rounded-3" width="100%" src="../assets/img/first_step/kml_to_shp.png" alt="">
                </div>

                <div class="col-12 col-lg-8 ">

                    <p>
                        Subsequently, I extrapolated with Clip Geoprocessing the points falling only in the province of
                        Verona.
                        By opening the Attribute Table I confirmed the number of points (circled in red "Features
                        Total:208")
                    </p>

                </div>

                <div class="col-12 col-lg-8 col-md-6 py-3 d-flex">
                    <img class="rounded-3" width="100%" src="../assets/img/first_step/clipping_points.png" alt="">
                </div>



            </div>


        </div>


    </main>
</template>

<style>

</style>