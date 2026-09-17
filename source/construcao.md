# Construção e Integração

O processo de construção do Jurandi foi dividido na montagem mecânica e na configuração de baixo nível dos sistemas eletrônicos.

## Montagem do Hardware
A controladora Pixhawk 6C foi fixada no centro de gravidade da embarcação, utilizando espumas amortecedoras para reduzir a vibração dos motores sobre a IMU. O módulo GPS/Bússola foi posicionado em uma haste elevada para minimizar a interferência eletromagnética gerada pelos cabos de potência dos ESCs.

O sistema de telemetria e o receptor do rádio controle foram conectados nas portas seriais e RC IN da Pixhawk, respectivamente.

## Configuração de Firmware (BLHeli e Pixhawk)
Uma das etapas críticas da integração foi a parametrização dos ESCs. Para que um ASV no formato catamarã tenha boa manobrabilidade usando *Skid Steering* (curva pela diferença de rotação dos motores), os propulsores precisam girar nos dois sentidos (frente e ré).

1. **Flash do BLHeli:** O firmware BLHeli foi gravado e configurado nos ESCs para o modo "Bidirectional". Isso permite que o sinal neutro (PWM em torno de 1500us) mantenha o motor parado, valores superiores girem para frente e inferiores para trás.
2. **Calibração da Pixhawk 6C:** Realizou-se a calibração do acelerômetro e da bússola via GCS, garantindo o alinhamento correto do referencial de navegação.
3. **Mapeamento de Canais:** Os canais do rádio foram mapeados para controle de aceleração e direção, ajustando a mixagem de motores nativa da controladora.