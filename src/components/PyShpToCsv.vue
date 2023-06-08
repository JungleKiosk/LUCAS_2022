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


        <button class="btn text-light zoom-effect lucas_link my-4" @click="showCode = !showCode">{{ showCode ? 'hide code'
            : 'Show code' }}</button>
        <div class="col-12 col-md-6 bg-black border-1 border-light px-3 px-md-5">
            <div v-if="showCode">
                <pre>
                        <code class="language-python">

myDir = ('C:/Users/NameUsers/.../csv_folder')

for vLayer in iface.mapCanvas().layers():
    QgsVectorFileWriter.writeAsVectorFormat( vLayer, 
        myDir + vLayer.name() + ".csv",delimiter=",", "utf-8", 
        vLayer.crs(),"csv")
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