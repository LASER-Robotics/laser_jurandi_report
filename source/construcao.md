# Construção e Integração

A construção do Jurandi foi organizada em uma sequência progressiva: preparação dos cascos, montagem do berço, instalação do deck e dos propulsores, integração eletrônica e, por fim, configuração do controle. Essa ordem facilitou a inspeção de cada subsistema antes dos ensaios em água.

:::{admonition} Critérios adotados
:class: result-callout
A montagem priorizou modularidade, rigidez, estanqueidade, distribuição equilibrada de massa e acesso aos componentes para manutenção.
:::

## Visão geral do processo

| Etapa | Atividade principal | Resultado esperado |
|---|---|---|
| 1 | Preparação e vedação dos cascos | Dois volumes estanques e alinhados |
| 2 | Montagem do berço de alumínio | Estrutura rígida e esquadrejada |
| 3 | Instalação do deck | Convés nivelado e fixado ao berço |
| 4 | Fixação dos propulsores | Motores firmes e posicionados simetricamente |
| 5 | Integração eletrônica | Componentes protegidos e cabeamento modular |
| 6 | Configuração e calibração | Propulsão bidirecional e sensores ajustados |
| 7 | Verificação em bancada | Sistema apto para o primeiro ensaio em água |

## Montagem mecânica e estrutural

### 1. Fabricação dos cascos

Os cascos cilíndricos foram construídos com tubos de PVC de 200 mm de diâmetro e 1 m de comprimento. Em cada tubo, instalou-se um joelho de 45° na proa e um tampão na popa. As uniões foram realizadas com adesivo plástico para PVC, formando volumes fechados e resistentes à entrada de água.

```{figure} images/casco_catamara.jpg
:alt: Casco cilíndrico do Jurandi feito de tubo de PVC com fechamento na extremidade
:class: report-figure

Casco tubular de PVC utilizado na estrutura flutuante.
```

Antes da montagem definitiva, as superfícies de contato devem estar limpas, secas e corretamente encaixadas. A cura do adesivo deve ser respeitada antes do teste de estanqueidade.

### 2. Estruturação do berço

O berço foi montado com perfis de alumínio e dimensões aproximadas de 1,0 × 0,8 m. Cantoneiras metálicas e conectores em PETG impressos em 3D garantiram o esquadro das junções. As uniões parafusadas permitem desmontagem e ajustes sem comprometer os perfis.

```{figure} images/berco_aluminio.jpg
:alt: Berço retangular do catamarã montado com perfis de alumínio e cantoneiras
:class: report-figure

Berço estrutural antes da instalação sobre os cascos.
```

### 3. Acoplamento do deck

A chapa de acrílico de 1,02 × 1,16 m foi marcada e perfurada de acordo com os pontos de fixação do berço. O deck foi então preso à estrutura com parafusos e porcas M8. Além de acomodar o compartimento eletrônico, a chapa cria uma superfície plana para as operações com drones.

```{figure} images/deck_acrilico.jpg
:alt: Catamarã Jurandi na piscina com deck transparente de acrílico instalado sobre os cascos
:class: report-figure

Deck de acrílico instalado e integrado à estrutura do Jurandi.
```

### 4. Ancoragem dos cascos e suportes de propulsão

Os motores *brushless* foram parafusados a suportes hidrodinâmicos impressos em 3D. Os cascos e os suportes foram ancorados ao berço com abraçadeiras de nylon de alta tenacidade. As cintas passam entre a chapa de acrílico e os perfis, envolvendo a estrutura e os tubos de PVC. Utilizou-se uma média de 16 abraçadeiras tensionadas por casco.

:::{admonition} Inspeção mecânica
:class: result-callout
Antes de instalar a eletrônica, verifique o alinhamento dos cascos, o aperto das uniões M8, a tensão uniforme das abraçadeiras e a ausência de contato entre hélices e estrutura.
:::

## Integração eletrônica e modularização

### Arquitetura de interligação

```text
Bateria LiPo 4S
      │
      ▼
Módulo de potência PM07 ─────► Pixhawk 6C ─────► Rádio / GCS
      │                              │
      ├────────► ESC bombordo ─────► Motor bombordo
      └────────► ESC estibordo ────► Motor estibordo
                                     │
                           GPS e bússola externa
```

### Cabeamento e conexões

O chicote dos propulsores foi estendido com cabos flexíveis de silicone 22 AWG. As terminações das fases receberam conectores cilíndricos de alta corrente do tipo *bullet*, permitindo desconectar os motores sem refazer soldas e simplificando inspeções e substituições.

### Acondicionamento estanque

A Pixhawk 6C, o rádio de telemetria, o módulo de potência Holybro PM07 e a bateria LiPo 4S foram organizados em um invólucro polimérico vedado. Esse compartimento central protege a eletrônica contra respingos e umidade e mantém os módulos acessíveis para manutenção.

### Posicionamento dos sensores

A Pixhawk foi posicionada próxima ao centro de gravidade da embarcação e apoiada sobre material amortecedor para reduzir a transmissão de vibrações à Unidade de Medida Inercial. O GPS e a bússola externa foram instalados em uma haste elevada, afastados dos cabos de potência e dos campos magnéticos produzidos pelo sistema propulsor.

## Configuração do firmware

### 1. ESCs e BLHeli

Para permitir manobras por diferença de empuxo (*skid steering*), os ESCs foram configurados no modo bidirecional. O sinal PWM próximo de 1500 µs corresponde ao ponto neutro; valores acima comandam o movimento avante e valores abaixo comandam a ré.

### 2. Calibração da Pixhawk 6C

Acelerômetro, giroscópio e bússola foram calibrados pela Estação de Controle em Solo. Essa etapa estabelece as correções do referencial inercial usadas na estimativa de atitude e na navegação.

### 3. Matriz de motores

A controladora foi ajustada para o *frame* Rover/Boat. A mistura dos comandos de aceleração e guinada distribui potências diferentes entre os motores de bombordo e estibordo, permitindo avanço, recuo e curvas sem leme mecânico.

| Comando | Motor de bombordo | Motor de estibordo |
|---|---|---|
| Avançar | Avante | Avante |
| Recuar | Ré | Ré |
| Curvar a bombordo | Menor empuxo ou ré | Maior empuxo avante |
| Curvar a estibordo | Maior empuxo avante | Menor empuxo ou ré |
| Neutro | Parado | Parado |

## Verificação antes do ensaio em água

- [ ] Cascos vedados e sem indícios de entrada de água.
- [ ] Berço alinhado, parafusos apertados e deck sem folgas.
- [ ] Abraçadeiras tensionadas de forma uniforme.
- [ ] Hélices livres, firmes e sem contato com a estrutura.
- [ ] Cabos identificados, isolados e afastados das partes móveis.
- [ ] Compartimento eletrônico fechado e fixado ao deck.
- [ ] Centro de gravidade conferido com a bateria instalada.
- [ ] Pixhawk, GPS, bússola e rádio reconhecidos pela GCS.
- [ ] Ponto neutro e sentidos de rotação testados com segurança.
- [ ] Comando de parada e procedimento de desarme verificados.

:::{admonition} Segurança
:class: result-callout
Os testes dos propulsores em bancada devem ser realizados com a área das hélices isolada. A embarcação somente deve entrar na água após a confirmação do neutro, do sentido de rotação, da telemetria e da orientação dos sensores.
:::
