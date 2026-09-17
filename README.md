# 🚤 Projeto Jurandi: Veículo de Superfície Autônomo (ASV)

**🔗 Versão Interativa do Site (Local):** [Acessar Documentação Sphinx](file:///home/yavellyn/relatorio-jurandi/build/html/apresentacao.html)
*(Nota: Links locais `file:///` funcionam apenas ao visualizar o documento no seu próprio computador, sendo bloqueados por segurança caso clicados diretamente pelo site do GitHub).*

---

## Apresentação e Objetivos

[![Teste do Catamarã Jurandi](https://img.youtube.com/vi/ryNO8USSduo/maxresdefault.jpg)](https://www.youtube.com/watch?v=ryNO8USSduo)

O projeto **Jurandi** consiste no desenvolvimento de um Veículo de Superfície Autônomo (ASV — *Autonomous Surface Vehicle*) em formato de catamarã. Desenvolvido na Universidade Federal da Paraíba (UFPB) com o apoio financeiro da CAPES, o projeto busca inovar na integração tecnológica entre robótica marinha e aérea.

Os ASVs são plataformas robóticas essenciais para operações complexas em ambientes aquáticos, viabilizando tarefas como monitoramento da qualidade da água, mapeamento batimétrico e inspeções visuais contínuas, mitigando a exposição de operadores humanos a áreas de risco. Especificamente, a construção do Jurandi tem como finalidade principal atuar como uma base móvel autônoma para o pouso e decolagem de Veículos Aéreos Não Tripulados (VANTs/drones) sobre a água. Essa integração cria uma arquitetura colaborativa híbrida, potencializando missões que demandam interação direta e contínua entre os domínios aéreo e aquático.

### Objetivo Geral
Construir, integrar e validar o hardware e o software de controle do catamarã Jurandi, estabelecendo uma plataforma robótica autônoma, funcional e dinamicamente estável para navegação de precisão.

### Objetivos Específicos
* **Integração de Hardware:** Estruturar a montagem mecânica e integrar de forma coesa a controladora de voo Pixhawk 6C ao sistema de propulsão.
* **Configuração de Firmware:** Parametrizar o firmware BLHeli nos Controladores Eletrônicos de Velocidade (ESCs) para assegurar o acionamento preciso e responsivo dos motores.
* **Telemetria e Comunicação:** Estabelecer um link de rádio robusto para o envio de dados em tempo real e operação segura via Estação de Controle em Solo (GCS - *Ground Control Station*).
* **Testes de Campo:** Validar a dinâmica de locomoção, a estabilidade de flutuabilidade e a confiabilidade na resposta aos comandos de navegação em um ambiente aquático real.

*(Exemplo de como colocar uma imagem no Markdown:)*
![Catamarã Jurandi em Teste](images/jurandi_1.jpg)

## Materiais e Componentes

[![Teste Jurandi com Drone](https://img.youtube.com/vi/8dZGqTz3dco/maxresdefault.jpg)](https://www.youtube.com/watch?v=8dZGqTz3dco)

Para o desenvolvimento do catamarã Jurandi, realizou-se a seleção criteriosa de componentes de hardware e software, visando assegurar a flutuabilidade adequada, integridade estrutural e o processamento computacional robusto exigido para a navegação autônoma de superfície.

### Estrutura Mecânica 

* **Casco do Catamarã:** Estrutura de duplo casco projetada para otimizar a estabilidade hidrodinâmica e minimizar o coeficiente de arrasto. Cada casco é constituído por um tubo de cloreto de polivinila (PVC) com 200 mm de diâmetro e 1 m de comprimento, dotado de defletores angulados (joelhos de 45°) na proa para corte de marolas e tampões de vedação hermética na popa.
![Casco de PVC](./images/casco_catamara.jpg)

* **Berço do Catamarã:** Armação metálica de alta rigidez em formato de paralelepípedo, confeccionada com perfis estruturais de alumínio. Destinada à sustentação do convés principal, apresenta dimensões de 1,0 x 0,8 m, garantindo leveza e resistência à corrosão.
![Berço de Alumínio](./images/berco_aluminio.jpg)

* **Deck do Catamarã:** Chapa de acrílico plana com dimensões de 1,02 x 1,16 m. Atua primariamente como convés dielétrico para a acomodação do invólucro estanque de componentes eletrônicos e como heliponto rígido para a aterrissagem dos drones, distribuindo a carga de impacto uniformemente pelo berço metálico através de fixações com parafusos e porcas M8. 
![Deck de Acrílico](./images/deck_acrilico.jpg)

* **Abraçadeiras de Fixação Estrutural:** Cintas de nylon de alta tenacidade com 500 mm de comprimento. Empregadas para ancorar mecanicamente os cascos tubulares ao berço de alumínio, mitigando a torção longitudinal e consolidando o monobloco estrutural.
![Abraçadeiras de Nylon](./images/abracadeiras_nylon.jpg)

* **Suportes de Acomodação Interna:** Componentes projetados via modelagem CAD 3D paramétrica e manufaturados por manufatura aditiva (impressão 3D FDM). Recomenda-se a utilização de polímeros com elevada resistência térmica e mecânica, como o PETG, garantindo o isolamento contra vibrações da eletrônica embarcada no ambiente marinho.
![Suportes CAD 3D](./images/suportes_fixacao.jpg)

### Eletrônica, Potência e Propulsão

* **Controladora de Voo (FCU):** Unidade de processamento modular Pixhawk 6C. Encarregada da execução dos algoritmos de navegação autônoma, malhas de controle PID e fusão avançada de dados sensoriais (EKF) a partir de suas IMUs internas amortecidas e magnetômetro.
![Controladora Pixhawk 6C](./images/pixhawk_6c.png)

* **Módulo de Gerenciamento de Potência (PMU):** Placa de distribuição de potência Holybro PM07. Desempenha o papel crítico de fornecer regulação de tensão contínua e redundante para a controladora de voo e periféricos, além de realizar a amostragem em tempo real da corrente drenada e da tensão total do sistema para a telemetria.
![Power Module PM07](./images/bateria_power_module.jpg)

* **Acumulador de Energia:** Bateria de Polímero de Lítio (LiPo) de 4 células (4S - 14.8V nominal) da fabricante Gens Ace. Dimensionada para suportar altas taxas de descarga contínua impostas pelos propulsores marítimos, garantindo a reserva energética necessária para missões de média a longa duração.

* **Cabeamento e Interconexões de Sinal:** Cabeamento lógico e de potência secundária estruturado com fios isolados em silicone flexível de bitola 22 AWG. Esta especificação assegura elevada resiliência térmica, baixa impedância ôhmica para correntes moderadas e excelente imunidade à fadiga mecânica gerada pela vibração contínua dos motores.

* **Rádio Transceptor de Telemetria:** Módulo de RF configurado para o estabelecimento de um link de dados bidirecional criptografado via protocolo MAVLink, permitindo o monitoramento telemétrico e intervenções de controle em tempo real pela Estação de Controle em Solo (GCS).
![Módulo de Telemetria](./images/modulo_telemetria.jpg)

* **Controladores Eletrônicos de Velocidade (ESCs):** Módulos de comutação trifásica dedicados ao acionamento dos motores. Operam suportando protocolos digitais de alta frequência (como DShot) e modulação PWM padrão, com suporte a correntes de pico elevadas.
![ESCs BLHeli](./images/esc_motores.jpeg)

* **Propulsores Submersíveis:** Motores *brushless* de baixo KV, intrinsecamente marinizados e vedados (proteção IP avançada). Projetados para operar submersos, oferecem tração hidrodinâmica eficiente através de hélices otimizadas e são altamente resistentes à corrosão hídrica.
![Motores Brushless](./images/motores_propulsao.jpg)

### Software e Firmware

* **Firmware de Propulsão:** Firmware BLHeli gravado nos ESCs para viabilizar parametrização avançada. Essencial para ativar a operação bidirecional (reversão de empuxo) dos motores, característica mandatória para a manobrabilidade em modo *Skid Steering* do catamarã.
![Configuração de Firmware](./images/firmware_config.jpg)

* **Sistemas de Navegação e GCS:** Operação regida pelos stacks ArduRover ou PX4 na controladora Pixhawk. O monitoramento remoto, planejamento de rotas por *waypoints* georreferenciados e a calibração de malhas sensoriais são conduzidos via software Mission Planner ou QGroundControl.
![Interface GCS](./images/interface_gcs.jpg)

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

## Resultados e Conclusões

O desenvolvimento e integração do catamarã Jurandi demonstraram a viabilidade do uso da Pixhawk 6C em conjunto com ESCs configurados com firmware BLHeli para aplicações marinhas autônomas.

### Resultados Alcançados
A arquitetura de hardware escolhida proporcionou comunicação estável via telemetria e controle responsivo da propulsão. O ajuste bidirecional dos motores foi fundamental para a manobrabilidade do catamarã na água.

### Dificuldades Encontradas
Grande parte das dificuldades foram advindas de detalhes técnicos dos componentes eletrõnicos, que geralmente poderiam dar algumas incompatibilidades ou até não funcionar como o espera. Além disso, as configurações ou conflito de configurações por parte da controladora de voô Pixhawk 6C durante a configuração no QGroundControl foram as partes que mais tornaram o projeto desafiante. Da parte mecânica, tudo correu bem, sem muitas compplicações, visto que foi feito de forma bastante metódica.

### Trabalhos Futuros
Para as próximas etapas do projeto, sugere-se:
* Otimização dos parâmetros de controle PID para navegação em linha reta mais suave.
* Integração de sensores adicionais (ex: sonar, câmera, ou sensores de qualidade da água).
* Execução de missões autônomas de longo alcance para mapeamento de áreas.