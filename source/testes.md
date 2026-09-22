# Metodologia de Testes

Os testes foram organizados em bancada e em campo para reduzir riscos e verificar progressivamente cada subsistema.

## Testes de bancada

| Verificação | Critério observado |
|---|---|
| Sentido de rotação | Resposta dos motores aos comandos de frente, ré e curvas, validando o BLHeli. |
| Alcance de telemetria | Conexão estável entre a Pixhawk 6C e a Estação de Controle em Solo. |
| Calibração de sensores | Coerência do horizonte artificial e da direção da bússola na GCS. |

## Testes de campo

| Verificação | Critério observado |
|---|---|
| Estanqueidade e flutuabilidade | Distribuição de peso, estabilidade e vedação do compartimento eletrônico. |
| Controle manual | Resposta hidrodinâmica e potência do sistema propulsor nos modos Loiter/Manual. |

```{figure} images/payload_test.jpeg
:alt: Preparação do catamarã Jurandi para um teste de carga e estabilidade
:class: report-figure

Preparação da plataforma para validação experimental.
```

:::{admonition} Sequência de segurança
:class: result-callout
A validação em seco antecedeu a entrada na água, evitando que falhas de acionamento, comunicação ou calibração comprometessem a embarcação.
:::
