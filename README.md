# Robótica

## Introdução

## Projetos
### kalman Filter
Neste projeto inicial, iremos desenvolver um projetinho baseado no tutorial do PySource sobre Kalman Filter. De forma geral, o objetivo é testar e implementar o filtro Kalmar para prever a trajetória de um objeto utilizando Python.

```
    O filtro de Kalman é um algoritmo que faz medições ao longo do </br>
    tempo e cria uma previsão das próximas medições.Isso é usado em muitos </br>
    campos como sensores, GPS, para prever a posição em caso de perda de </br>
    sinal por alguns segundos e é isso que veremos também na visão computacional.
```

Para iniciar o projeto, será necessário a instalação de algumas bibliotecas. A primeira é o OpenCV.
```
    pip install opencv-python
```

Após a instalação da biblioteca OpenCV iremos criar um arquivo chamado kalman.py para a simulção e predição de rotas básicas.
```
    from kalmanFilter import KalmanFilter
    import cv2

    kf = KalmanFilter()

    predicted = kf.predict(50,100)
    predicted = kf.predict(100,100)
    predicted = kf.predict(150,100)
    predicted = kf.predict(200,100)

    print(predicted)
```

Depois podemos melhorar a visualização e simular o movimento de uma bola. Assim conseguimos observar o melhor o desempenho do filtro Kalman. O código está disponível no arquivo ballSimul.py.

Por fim, podemos abordar a implementação deste algoritmo para prever a rota de um objeto real. No exemplo desenvolvido no site PySource é feito o rastreamento da rota de uma laranja. No exemplo que desenvolvi, utilizei uma bola de isopor e realizei a leitura da WebCam. O código está disponível no arquivo ball.py.

## Referências
- https://pysource.com/2021/11/02/kalman-filter-predict-the-trajectory-of-an-object/