#Librerias necesarias para este Script
import arcpy
import pandas as pd

#mantener los Ids globales para entrada y salida, con el fin de preservar
#dichos Ids de la tabla, en el archivo de salida
arcpy.env.preserveGlobalIds = True

#Se crea la funcion principal que contiene todo el Script funcional.
def ScriptTool(capa):
    """ScriptTool function docstring."""

    #se verifica que esta llamando la tabla corriespondiente
    arcpy.AddMessage(f'capa: {capa}')

    #Se crea objeto temporal que aloja los datos que se procesaran 
    #en la proxima linea de codigo
    selectedFeatures = []

    #En esta linea, lo que se hace es recorrer la tabla de objetos con el fin de buscar 
    #el FID de cada una de las filas de la tabla y guardar dichos FID en el objeto 
    #creado anteriormente mediante la condicion "append."
    for row in arcpy.SearchCursor(capa):
        selectedFeatures.append(row.getValue("FID"))

    #Se verifica el contenido del objeto creado, este debe contener los FID de 
    #cada una de las filas de toda la tabla
    arcpy.AddMessage(f'selectedFeatures: {selectedFeatures}')

    #En este paso lo que se hace es modificar el objeto a un arreglo y 
    #transformarlos a String con el fin de poder manipularlos uno por uno
    #Para lograr esto primero definimos que en cada recorrido entre x y selectFeatures
    #estos se separen con ', ' (una coma y un espacio, con el fin de visualicar 
    #de manera mas ordenada los nombres)
    srtFeatures = ', '.join(str(x) for x in selectedFeatures)

    #Se comprueba el arreglo creado
    arcpy.AddMessage(f'srtFeatures: {srtFeatures}')

    # Creo la query para obtener los features seleccionados de la capa.
    expression = """{0} in ({1})""".format(arcpy.AddFieldDelimiters(capa, 'FID'), srtFeatures)


    #Se verifica la tupla creada .... investigar mas esta nueva transformacion de los datos
    arcpy.AddMessage(f'expression: {expression}')

    #Se define una variable fija con el fin de usarla para completar ciertas funciones
    capaAuxiliar = 'capa de testeo'
    
    arcpy.MakeFeatureLayer_management(capa, "lyr") 
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", where_clause=expression)
    arcpy.CopyFeatures_management("lyr", capaAuxiliar)

    
    # Ordeno por el nombre la capa de seleccion
    sort_fields = [["NOM_CON", "ASCENDING"]]
    
    arcpy.Sort_management(capa, capaAuxiliar, sort_fields)



#Ejecutando codigo de importacion de datos de otros modulos, en este caso ArcGIS
if __name__ == '__main__':

    #Lo que indica este comando es que debe capturar la condicion 0 generada por ArcGIS
    #(Para este caso practico es el menu donde se selecciona la tabla a analizar)
    capa: str = arcpy.GetParameterAsText(0)


    #Se llama a la funcion que se creo con anterioridad
    ScriptTool(capa)