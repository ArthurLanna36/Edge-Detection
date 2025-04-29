# Detecção de Bordas com Sobel Otimizado

Este projeto implementa um detector de bordas baseado no operador Sobel totalmente em Python puro, sem dependências de bibliotecas de otimização de cálculo matricial. O algoritmo é separável em duas passagens para melhorar a eficiência.

## Funcionalidades

- **Separabilidade do Sobel**: cálculo das derivações horizontais e verticais em duas passagens.
- **Normalização de intensidade**: escala automática dos valores de gradiente para o intervalo 0–255.
- **Binarização opcional**: aplicação de um limiar para gerar uma imagem de bordas binária.
- **Medição de desempenho**: exibe o tempo de processamento do núcleo do algoritmo.

## Pré-requisitos

- Python 3.6 ou superior
- [Pillow](https://python-pillow.org/) (PIL)

## Instalação

```bash
pip install Pillow
```

## Uso

```bash
python src/sobel.py data/input.jpg data/output.jpg [limiar]
```

- `<imagem_entrada>`: caminho para o arquivo de entrada (qualquer formato suportado pelo Pillow).
- `<imagem_saida>`: caminho para salvar o mapa de bordas gerado.
- `[limiar]` (opcional): inteiro entre 0 e 255 para binarização das bordas. Se omitido, gera um mapa de tons de cinza proporcional ao gradiente.

### Exemplos

- Gerar mapa de bordas em tons de cinza:
  ```bash
  python optimized_sobel.py input.jpg output.jpg
  ```
- Gerar imagem binária de bordas com limiar 100:
  ```bash
  python optimized_sobel.py input.jpg output.jpg 100
  ```

## Estrutura do Código

- **`separable_sobel(data, width, height)`**: realiza duas passagens separáveis do filtro Sobel.
- **`sobel_edge_detection(input_path, output_path, threshold)`**: coordena a leitura da imagem, chama o algoritmo de Sobel, processa magnitudes, aplica limiar e salva a saída.
- **`print_usage()`**: exibe instruções de uso quando os parâmetros estão incorretos.
- **Bloco principal**: analisa argumentos de linha de comando e invoca `sobel_edge_detection()`.

