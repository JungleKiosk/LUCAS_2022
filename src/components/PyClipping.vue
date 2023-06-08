<script>

export default {
    data() {
        return {
            showCode: false
        };
    }
}
 
</script>

<template>
    <main>


        <button class="btn text-light zoom-effect lucas_link my-4" @click="showCode = !showCode">{{ showCode ? 'hide code' : 'Show code' }}</button>
        <div class="col-12 col-md-6 bg-black border-1 border-light px-3 px-md-5">
            <div v-if="showCode">
                <pre>
                        <code class="language-python">
<span class="comments"># Python code for clipping point.shp with five poly.shp</span>      

<span class="comments"># Import necessary libraries</span>
<span class="operators">from</span>  qgis.core <span class="operators">import</span>  *
<span class="operators">import</span>  os

<span class="comments"># Set the paths to the shapefiles to clip</span>
points_file = <span class="speach">"C:/usere/.../path/shapefile/points.shp"</span> 
polygons_dir = <span class="speach">"C:/usere/.../path/shapefile/polygons.shp"</span> 

<span class="comments"># Set the output file path and name</span>
output_file = ".../path/to/output/file.shp"

<span class="comments"># Initialize the QGIS application</span>
app = <span class="function">QgsApplication</span>([], <span class="operators">True</span> )
<span class="function">QgsApplication.setPrefixPath</span>(<span class="speach">"/usr"</span>, <span class="operators">True</span>)
<span class="function">QgsApplication.initQgis</span>()

<span class="comments"># Load the points file</span>
points_layer = <span class="function">QgsVectorLayer</span>(points_file, <span class="speach">"points"</span>, <span class="speach">"ogr"</span>)
<span class="operators">if not</span> points_layer.isValid():
print(<span class="speach">"The points file is not valid"</span>)

<span class="comments"># Create an empty list for the clip polygons</span>
polygons_layers = []
<span class="number"></span>
<span class="comments"># Load the polygon files and add them to the list</span>
<span class="operators">for</span>  filename <span class="operators">in</span> <span class="function">os.listdir</span>(polygons_dir):
<span class="operators">if</span> filename.<span class="function">endswith</span>(<span>".shp"</span>):
path =<span class="function">os</span>.path.<span class="function">join</span>(polygons_dir, filename)
layer =<span class="function">QgsVectorLayer</span>(path, filename[:-<span class="number">4</span>],<span class="speach">"ogr"</span>)
<span class="operators">if not</span> layer.isValid():
print(<span class="speach">"The polygon file {} is not valid"</span>.format(filename))
polygons_layers.append(layer)

<span class="comments"># Perform the clip operation for each polygon</span>
<span class="operators">for</span> polygon_layer <span class="operators">in</span> polygons_layers:
<span class="comments"># Create the output file name based on the polygon name</span>
polygon_name = polygon_layer.name()
output_file_polygon = <span class="function">os</span>.path.<span class="function">join</span>(<span class="function">os</span>.path.<span class="function">dirname</span>(output_file), <span class="speach">"{}_{}.shp"</span>.format(<span class="function">os</span>.path.<span class="function">basename</span>(output_file)[:-<span class="number">4</span>], polygon_name))

<span class="comments"># Perform the clip operation</span>
processing.<span class="function">run</span>(<span class="speach">"native:clip"</span>, {
    <span class="speach">'INPUT'</span>: points_layer,
    <span class="speach">'OVERLAY'</span>: polygon_layer,
    <span class="speach">'OUTPUT'</span>: output_file_polygon
})

<span class="comments"># Exit the QGIS application</span>
<span class="function">QgsApplication.exitQgis</span>()
</code>
</pre>
            </div>

        </div>





    </main>
</template>

<style>
.operators {
    color: rgb(0, 195, 255);
}

.speach {
    color: rgb(19, 203, 12);
}

.function {
    color: rgb(225, 61, 230);
}

.comments {
    color: rgb(153, 160, 154);
}

.number {
    color: brown;
}
</style>