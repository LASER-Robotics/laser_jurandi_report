# Resultados e Conclusões

O desenvolvimento e integração do catamarã Jurandi demonstraram a viabilidade do uso da Pixhawk 6C em conjunto com ESCs configurados com firmware BLHeli para aplicações marinhas autônomas.

## Resultados Alcançados
A arquitetura de hardware escolhida proporcionou comunicação estável via telemetria e controle responsivo da propulsão. O ajuste bidirecional dos motores foi fundamental para a manobrabilidade do catamarã na água.

## Dificuldades Encontradas
Os principais desafios do projeto concentraram-se na integração eletrônica, especificamente na identificação e resolução de incompatibilidades de comunicação e alimentação entre os componentes de hardware embarcados. Adicionalmente, a parametrização da controladora de voo Pixhawk 6C via QGroundControl exigiu a mitigação de diversos conflitos lógicos no firmware, configurando a etapa mais complexa do desenvolvimento. Em contrapartida, a estruturação mecânica foi executada sem intercorrências significativas, resultado do planejamento prévio e da abordagem metódica adotada durante a montagem

## Trabalhos Futuros
Para as próximas etapas do projeto, sugere-se:
* Otimização dos parâmetros de controle PID para navegação em linha reta mais suave.
* Integração de sensores adicionais (ex: sonar, câmera, ou sensores de qualidade da água).
* Execução de missões autônomas de longo alcance para mapeamento de áreas.