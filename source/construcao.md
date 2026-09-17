# Construção e Integração

O processo de construção do Jurandi foi dividido na montagem mecânica estrutural e na integração e configuração de baixo nível dos sistemas eletrônicos e de propulsão.

## Montagem Mecânica e Estrutural

A construção da estrutura física priorizou a modularidade e a resistência mecânica, garantindo uma plataforma rígida para a navegação:

* **Fabricação dos Cascos:** Os cascos cilíndricos foram construídos a partir de tubos de PVC. Para assegurar a estanqueidade total, acoplou-se um tampão de vedação na popa e um joelho de 45° na proa de cada tubo. A união definitiva das peças foi realizada por meio de soldagem química com adesivo plástico para PVC (Krona).
* **Estruturação do Berço:** A armação que forma o berço metálico foi montada utilizando perfis de alumínio. O esquadro e a rigidez foram garantidos pelo uso de cantoneiras metálicas (junções em L) e conectores customizados em PETG (manufaturados via impressão 3D FDM). Todo o conjunto foi fixado por uniões parafusadas.
* **Acoplamento do Convés (Deck):** A chapa superior de acrílico foi submetida a perfurações de precisão para alinhamento com a estrutura inferior e fixada mecanicamente ao berço metálico utilizando conjuntos de parafusos e porcas M8.
* **Ancoragem e Suportes de Propulsão:** Os motores *brushless* foram parafusados a suportes hidrodinâmicos customizados, impressos em 3D. A fixação conjunta dos cascos de PVC e dos suportes dos motores ao berço de alumínio foi realizada através de abraçadeiras de nylon de alta tenacidade. O roteamento das cintas foi feito passando entre a chapa de acrílico e o berço metálico, abraçando simultaneamente a estrutura de alumínio e os tubos de PVC. Utilizou-se uma média de 16 abraçadeiras tensionadas por casco para consolidar todo o monobloco.

## Integração Eletrônica e Modularização

A arquitetura eletrônica foi projetada para suportar o ambiente marinho e facilitar manutenções locais:

* **Cabeamento e Conexões:** O chicote elétrico dos propulsores foi estendido utilizando cabos de silicone de especificação 22 AWG, que oferecem alta flexibilidade mecânica e resistência térmica. Para modularizar o sistema e permitir a desconexão rápida dos motores, as terminações das fases foram soldadas a conectores cilíndricos de alta corrente tipo *Bullet* (*Bullet Connectors*).
* **Acondicionamento Estanque:** Toda a eletrônica de controle e potência — incluindo a FCU Pixhawk 6C, o módulo de telemetria, o módulo de potência PM07 Holybro e a bateria LiPo 4S da Gens Ace — foi inserida e organizada no interior de um invólucro polimérico vedado (uma caixa adaptada tipo *Tupperware*). Esse compartimento atua como uma central eletrônica (E-box) blindada contra ingresso de água e maresia.
* **Isolamento Sensorial:** No interior do compartimento estanque, a controladora Pixhawk 6C foi posicionada o mais próximo possível do centro de gravidade (CG) da embarcação e assentada sobre espumas amortecedoras elastoméricas, isolando a Unidade de Medida Inercial (IMU) das vibrações de alta frequência geradas pelos propulsores.
* **Mitigação de Interferências:** O módulo de GPS e a bússola externa foram instalados no topo de uma haste elevada (mastro), distanciando os magnetômetros dos campos eletromagnéticos transientes induzidos pelos cabos de potência dos motores e da bateria. As conexões de rádio e telemetria foram ancoradas nas portas seriais e RC IN dedicadas da FCU.

## Configuração de Firmware (BLHeli e Pixhawk)

Uma das etapas críticas da integração foi a parametrização dos ESCs. Para que um ASV no formato catamarã tenha boa manobrabilidade usando *Skid Steering* (controle vetorial pela diferença de rotação dos motores modulares), os propulsores precisam operar dinamicamente em ambos os sentidos (avante e reverso).

1. **Flash do Firmware BLHeli:** O firmware BLHeli nativo dos ESCs foi atualizado e reconfigurado para o modo bidirecional (*Bidirectional Mode*). Essa parametrização estabelece que o sinal de controle neutro (largura de pulso PWM em torno de 1500 µs) mantenha o rotor estático. Sinais de largura superior induzem torque positivo (avante), enquanto larguras inferiores revertem a comutação das fases (ré).
2. **Calibração da Pixhawk 6C:** Executou-se a calibração rigorosa do acelerômetro, giroscópio e da bússola através da GCS, estabelecendo os tensores de correção do referencial inercial para navegação de superfície precisa.
3. **Mapeamento de Matriz de Motores (Mixer):** Os canais de rádio frequência foram assinalados para vetorização de aceleração e guinada (*throttle/yaw*). Ajustou-se a matriz de mixagem nativa da controladora para o *frame* "Rover/Boat", traduzindo comandos de direção em diferenciais de potência assimétricos entre o motor de bombordo e estibordo.