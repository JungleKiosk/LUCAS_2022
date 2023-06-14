
fn= 'C:/enter_your_path/.../name_file.shp'

py1=QgsVectorLayer(fn,'','ogr')

pv=py1.dataProvider()

pv.addAttributes([QgsField('id',QVariant.Double,"double",10,1),QgsField('length_Km',QVariant.Double,"double",10,2),QgsField('time',QVariant.Double,"double",10,2),QgsField('km_L',QVariant.Double,"double",10,2),QgsField('fuel_eurL',QVariant.Double,"double",10,2),QgsField('CO2_gkm',QVariant.Double,"double",10,2)])

py1.updateFields()

id=QgsExpression('1+$id')
length_Km=QgsExpression('$length/1000')
time=QgsExpression('("length_Km"/50)*60')
km_L=QgsExpression('100/4.6')
fuel_eurL=QgsExpression('(("length_Km"*2)/"km_L")')
CO2_gkm=QgsExpression('("length_Km"*105)')


cntext=QgsExpressionContext()
cntext.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(py1))

with edit(py1):
    for f in py1.getFeatures():
        cntext.setFeature(f)
        f['id']=id.evaluate(cntext)
        py1.updateFeature(f)
with edit(py1):
    for f in py1.getFeatures():
        cntext.setFeature(f)
        f['length_Km']=length_Km.evaluate(cntext)
        py1.updateFeature(f)
with edit(py1):
    for f in py1.getFeatures():
        cntext.setFeature(f)
        f['time']=time.evaluate(cntext)
        py1.updateFeature(f)
with edit(py1):
    for f in py1.getFeatures():
        cntext.setFeature(f)
        f['km_L']=km_L.evaluate(cntext)
        py1.updateFeature(f)
with edit(py1):
    for f in py1.getFeatures():
        cntext.setFeature(f)
        f['fuel_eurL']=fuel_eurL.evaluate(cntext)
        py1.updateFeature(f)
with edit(py1):
    for f in py1.getFeatures():
        cntext.setFeature(f)
        f['CO2_gkm']=CO2_gkm.evaluate(cntext)
        py1.updateFeature(f)