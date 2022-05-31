import cv2
from random import randint
import json
from pathlib import Path

### Nombre del video a cargar
filename = Path(__file__).parent / "input.mkv"  
### Nombre del archivo a guardar
output_filename ='tracking.mp4'
### Cargo el Json con los objetos y condiciones iniciales
pathJson = Path(__file__).parent / "initial_conditions.json"
archivo = open(pathJson)
Objetos_Ini = json.load(archivo)
#### Creo instancia Multitracker
multi_tracker = cv2.legacy.MultiTracker_create()


######## Funcion
### Toma como  argumentos el Json con los objetos de interes
def main(Objetos):
    try:
        # Cargo el video
        cap = cv2.VideoCapture(str(filename))
        success, frame = cap.read()

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        result = cv2.VideoWriter(output_filename, fourcc,
                                 int(cap.get(cv2.CAP_PROP_FPS)),
                                 (frame.shape[1], frame.shape[0]))

        Rectangulo = []
        colores = []
        id_list = []

        if success:

            ## Tomo del Json los objetos
            for obj_t in Objetos:
                Rectangulo.append(obj_t['coordinates'])
                colores.append(
                    (randint(1, 255), randint(1, 255), randint(1, 255)))
                id_list.append(obj_t['object'] + ": " + str(obj_t['id']))

            for bbox in Rectangulo:
                multi_tracker.add(cv2.legacy.TrackerCSRT_create(), frame, bbox)

            for f in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
                success, frame = cap.read()

                if success:

                    porcentaje=round(((f+1)/int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))*100,0)
                    print("\rEspere por favor, Procesando Video...... %d" %porcentaje,"%", end='')    

                    success, bboxes = multi_tracker.update(frame)

                    # Dibujo rectangulos y textos
                    for i, bbox in enumerate(bboxes):
                        point_1 = (int(bbox[0]), int(bbox[1]))
                        point_2 = (int(bbox[0] + bbox[2]),
                                   int(bbox[1] + bbox[3]))
                        cv2.rectangle(frame, point_1, point_2, colores[i],5)
                        xm = int(
                            int(point_1[0]) +
                            abs(int(point_1[0]) - int(point_2[0])) / 2)
                        ym = int(
                            int(point_1[1]) +
                            abs(int(point_1[1]) - int(point_2[1])) / 2)
                        cv2.putText(frame, id_list[i], (xm, ym),
                                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
                    result.write(frame)

                else:
                    break

        cap.release()
        result.release()
        print("\nProceso Terminado!!")
    except Exception as e:
        print("Se encontro un error: ", e)
    finally:
        pass

if __name__ == "__main__":
    main(Objetos_Ini)