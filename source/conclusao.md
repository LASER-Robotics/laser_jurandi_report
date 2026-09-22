# Resultados e Conclusões

O desenvolvimento do Jurandi demonstrou a viabilidade da integração entre a Pixhawk 6C e ESCs com firmware BLHeli em uma plataforma marinha autônoma.

## Resultados alcançados

- Comunicação estável entre a embarcação e a Estação de Controle em Solo.
- Controle responsivo dos propulsores em ambos os sentidos.
- Manobrabilidade por diferença de rotação entre bombordo e estibordo.
- Estrutura modular com flutuabilidade e estabilidade adequadas aos ensaios.

:::{admonition} Síntese
:class: result-callout
O ajuste bidirecional dos motores foi decisivo para a manobrabilidade do catamarã e confirmou a adequação da arquitetura escolhida.
:::

## Dificuldades encontradas

Os principais desafios concentraram-se na integração eletrônica, especialmente na identificação de incompatibilidades de comunicação e alimentação. A parametrização da Pixhawk 6C via QGroundControl exigiu a mitigação de conflitos lógicos no firmware e constituiu a etapa mais complexa. A montagem mecânica, em contrapartida, ocorreu sem intercorrências significativas devido ao planejamento prévio.

## Trabalhos futuros

1. Otimizar os parâmetros PID para uma navegação em linha reta mais suave.
2. Integrar sonar, câmera e sensores de qualidade da água.
3. Executar missões autônomas de longo alcance para mapeamento de áreas.
4. Validar pousos e decolagens repetidos de drones sobre o deck.
