from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.structures import Instances

import cv2
import os

CLASSE_GATOS = 15
DIRETORIO = "./base_dados/"


class DetectNet:
    def __init__(self) -> None:
        self.cfg = get_cfg()

        self.cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.80  
        
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
        self.predictor = DefaultPredictor(self.cfg)
        return

    def processa_video(self, filename, path):
        caminho_arquivo = path + filename
        cap = cv2.VideoCapture(caminho_arquivo)
        occurrences = 0
        while(True):
            ret, frame = cap.read()
            if (frame is None):
                break

            if self.existem_gatos(frame):
                print(f"{filename} possui gatos")
                return

        print(f"{filename} não possui gatos")

    def existem_gatos(self, frame) -> bool:
        deteccoes = self.predictor(frame)
        instancias = deteccoes["instances"].to("cpu")
        instancias = instancias[instancias.pred_classes == CLASSE_GATOS]
        return len(instancias) >= 1

def main():
    detectnet = DetectNet()

    lista_arquivos = os.listdir(DIRETORIO)
    total = len(lista_arquivos)

    for index, nome_arquivo in enumerate(lista_arquivos):
       print(f"{index+1}/{total} - " + nome_arquivo)
       detectnet.processa_video(nome_arquivo, DIRETORIO)

if __name__ == "__main__":
    main()