# Apresentação e Objetivos

<video src="./source/_static/jurandi_test_video_2.mp4" controls="controls"></video>

O projeto **Jurandi** consiste no desenvolvimento de um Veículo de Superfície Autônomo (ASV — *Autonomous Surface Vehicle*) em formato de catamarã. Desenvolvido na Universidade Federal da Paraíba (UFPB) com o apoio financeiro da CAPES, o projeto busca inovar na integração tecnológica entre robótica marinha e aérea.

Os ASVs são plataformas robóticas essenciais para operações complexas em ambientes aquáticos, viabilizando tarefas como monitoramento da qualidade da água, mapeamento batimétrico e inspeções visuais contínuas, mitigando a exposição de operadores humanos a áreas de risco. Especificamente, a construção do Jurandi tem como finalidade principal atuar como uma base móvel autônoma para o pouso e decolagem de Veículos Aéreos Não Tripulados (VANTs/drones) sobre a água. Essa integração cria uma arquitetura colaborativa híbrida, potencializando missões que demandam interação direta e contínua entre os domínios aéreo e aquático.

## Objetivo Geral
Construir, integrar e validar o hardware e o software de controle do catamarã Jurandi, estabelecendo uma plataforma robótica autônoma, funcional e dinamicamente estável para navegação de precisão.

## Objetivos Específicos
* **Integração de Hardware:** Estruturar a montagem mecânica e integrar de forma coesa a controladora de voo Pixhawk 6C ao sistema de propulsão.
* **Configuração de Firmware:** Parametrizar o firmware BLHeli nos Controladores Eletrônicos de Velocidade (ESCs) para assegurar o acionamento preciso e responsivo dos motores.
* **Telemetria e Comunicação:** Estabelecer um link de rádio robusto para o envio de dados em tempo real e operação segura via Estação de Controle em Solo (GCS - *Ground Control Station*).
* **Testes de Campo:** Validar a dinâmica de locomoção, a estabilidade de flutuabilidade e a confiabilidade na resposta aos comandos de navegação em um ambiente aquático real.

*(Exemplo de como colocar uma imagem no Markdown:)*
![Catamarã Jurandi em Teste](images/jurandi_1.jpg)

# Materiais e Componentes

<video src="./source/_static/jurandi_and_drone_1.mp4" controls="controls"></video>

Para o desenvolvimento do catamarã Jurandi, realizou-se a seleção criteriosa de componentes de hardware e software, visando assegurar a flutuabilidade adequada da embarcação e o processamento computacional robusto exigido para a navegação autônoma.
## Estrutura Mecânica 

* **Casco do Catamarã:** Estrutura de duplo casco projetada para garantir estabilidade hidrodinâmica. Cada casco é constituído por um tubo de PVC com 200 mm de diâmetro e 1 m de comprimento, contendo um joelho de 45° acoplado em uma extremidade (proa) e um tampão de vedação na outra (popa).
![Casco de PVC](./images/casco_catamara.jpg)

* **Berço do Catamarã:** Armação metálica em formato de paralelepípedo, confeccionada com perfis de alumínio, destinada à sustentação do convés (deck) de acrílico. Apresenta dimensões de 1,0 x 0,8 m.
![Berço de Alumínio](./images/berco_aluminio.jpg)

* **Deck do Catamarã:** Chapa de acrílico com dimensões de 1,02 x 1,16 m, que atua como convés para acomodação do invólucro de componentes eletrônicos e como plataforma de pouso para os drones. A fixação ao berço de alumínio foi realizada utilizando parafusos e porcas M8. 
![Deck de Acrílico](./images/deck_acrilico.jpg)

* **Abraçadeiras de Nylon:** Com 500 mm de comprimento, foram empregadas para fixar firmemente os cascos ao berço de alumínio, consolidando o acoplamento estrutural entre cascos, berço e convés.
![Abraçadeiras de Nylon](./images/abracadeiras_nylon.jpg)

* **Suportes de Fixação:** Componentes modelados em CAD e manufaturados sob medida (via impressão 3D) para a acomodação e fixação segura da eletrônica embarcada.
![Suportes CAD 3D](./images/suportes_fixacao.jpg)

## Eletrônica e Propulsão

* **Controladora de Voo (FCU):** Unidade Pixhawk 6C, responsável pelo processamento dos algoritmos de navegação, fusão de dados sensoriais (IMU, magnetômetro) e emissão de sinais de controle.
![Controladora Pixhawk 6C](./images/pixhawk_6c.jpg)

* **Módulo de Telemetria:** Rádio transceptor configurado para comunicação de dados bidirecional em tempo real com a Estação de Controle em Solo (GCS).
![Módulo de Telemetria](./images/modulo_telemetria.jpg)

* **Controladores Eletrônicos de Velocidade (ESCs):** Módulos dedicados ao acionamento e controle de rotação dos motores, operando com suporte a protocolos de alta velocidade (DShot ou PWM).
![ESCs BLHeli](./images/esc_motores.jpg)

* **Propulsores:** Motores *brushless* marinizados (à prova d'água), projetados para garantir tração hidrodinâmica eficiente e resistência à corrosão.
![Motores Brushless](./images/motores_propulsao.jpg)

* **Sistema de Alimentação:** Composto por bateria de Polímero de Lítio (LiPo) e Módulo de Potência (*Power Module*), assegurando a distribuição isolada e segura de tensão elétrica para a controladora e para os propulsores.
![Bateria e Power Module](./images/bateria_power_module.jpg)

## Software e Firmware

* **Firmware de Controle:** BLHeli para a parametrização avançada dos ESCs, e os sistemas ArduRover ou PX4 embarcados na Pixhawk para autonomia de superfície.
![Configuração de Firmware](./images/firmware_config.jpg)

* **Estação de Controle em Solo (GCS):** Software Mission Planner ou QGroundControl, utilizados para o monitoramento telemétrico, planejamento de missões e calibração remota.
![Interface GCS](./images/interface_gcs.jpg)

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

# Metodologia de Testes

Os testes foram divididos em etapas de laboratório e validação em campo para garantir a segurança do equipamento.

## Testes de Bancada (Em seco)
Antes de colocar a embarcação na água, o sistema foi energizado em bancada para as seguintes validações:
* **Sentido de Rotação:** Verificação da resposta dos motores aos comandos do rádio (frente, ré, curva à direita e curva à esquerda) validando a configuração do BLHeli.
* **Alcance de Telemetria:** Teste de conexão entre a Pixhawk 6C e a Estação de Controle em Solo.
* **Calibração de Sensores:** Verificação do horizonte artificial e direção da bússola no Mission Planner/QGroundControl.

## Testes de Campo (Na água)
Os testes práticos consistiram no comissionamento do veículo em ambiente aquático real.
* **Estanqueidade e Flutuabilidade:** Validação da distribuição de peso e vedação do compartimento eletrônico.
* **Controle Manual (Loiter/Manual):** Avaliação da resposta hidrodinâmica do catamarã e da potência do sistema propulsor.
* **Navegação Autônoma (Auto):** *(Descreva aqui se o Jurandi já executou missões de pontos de passagem (waypoints) ou se este é um passo futuro).*

# Resultados e Conclusões

O desenvolvimento e integração do catamarã Jurandi demonstraram a viabilidade do uso da Pixhawk 6C em conjunto com ESCs configurados com firmware BLHeli para aplicações marinhas autônomas.

## Resultados Alcançados
A arquitetura de hardware escolhida proporcionou comunicação estável via telemetria e controle responsivo da propulsão. O ajuste bidirecional dos motores foi fundamental para a manobrabilidade do catamarã na água.

## Dificuldades Encontradas
*(Preencha com os desafios reais do projeto. Exemplos comuns: "Houve dificuldade na calibração da bússola devido ao campo magnético dos motores", ou "O isolamento dos componentes exigiu refações para evitar a entrada de água".)*

## Trabalhos Futuros
Para as próximas etapas do projeto, sugere-se:
* Otimização dos parâmetros de controle PID para navegação em linha reta mais suave.
* Integração de sensores adicionais (ex: sonar, câmera, ou sensores de qualidade da água).
* Execução de missões autônomas de longo alcance para mapeamento de áreas.