# Materiais e Componentes

<div class="video-frame"><iframe src="https://youtube.com/embed/shorts/s1-IYc2nubc" title="Teste integrado do Jurandi com drone" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>

A seleção dos componentes priorizou flutuabilidade, integridade estrutural, resistência ao ambiente aquático e capacidade de processamento para navegação autônoma.

## Especificações principais

| Subsistema | Componente | Especificação |
|---|---|---|
| Cascos | Tubos de PVC | 200 mm de diâmetro × 1 m de comprimento |
| Berço | Perfis de alumínio | 1,0 × 0,8 m |
| Deck | Chapa de acrílico | 1,02 × 1,16 m; fixação M8 |
| Controle | Pixhawk 6C | IMUs internas e fusão sensorial EKF |
| Energia | Bateria LiPo Gens Ace | 4S; 14,8 V nominal |
| Cabeamento | Fio de silicone | 22 AWG |

## Estrutura mecânica

### Cascos e berço

Os dois cascos usam tubos de PVC com defletores angulados de 45° na proa e tampões herméticos na popa. O berço de perfis de alumínio sustenta o convés, combinando rigidez, baixo peso e resistência à corrosão.

::::{grid} 2
:gutter: 2

:::{grid-item}
```{figure} images/casco_catamara.jpg
:alt: Casco do catamarã construído com tubo de PVC
Casco tubular de PVC.
```
:::
:::{grid-item}
```{figure} images/berco_aluminio.jpg
:alt: Berço estrutural montado com perfis de alumínio
Berço estrutural de alumínio.
```
:::
::::

### Deck de acrílico

A chapa plana funciona como convés dielétrico, base do invólucro estanque e heliponto rígido. A carga de impacto é distribuída pelo berço por fixações com parafusos e porcas M8.

```{figure} images/deck_acrilico.jpg
:alt: Catamarã Jurandi na água com o deck de acrílico e a eletrônica embarcada visíveis
:class: report-figure

Deck de acrílico instalado no Jurandi durante ensaio em piscina.
```

### Fixação e suportes internos

Cintas de nylon de 500 mm ancoram os cascos ao berço e mitigam a torção longitudinal. Suportes internos modelados em CAD e impressos em PETG isolam a eletrônica das vibrações.

::::{grid} 2
:gutter: 2

:::{grid-item}
```{figure} images/abracadeiras_nylon.jpg
:alt: Abraçadeiras de nylon utilizadas na fixação estrutural
Abraçadeiras de fixação estrutural.
```
:::
:::{grid-item}
```{figure} images/suportes_fixacao.jpg
:alt: Suportes internos modelados em CAD e impressos em 3D
Suportes internos impressos em 3D.
```
:::
::::

## Eletrônica, potência e propulsão

### Controle e energia

A Pixhawk 6C executa navegação, controle PID e fusão sensorial. O módulo Holybro PM07 regula a alimentação, distribui potência e mede corrente e tensão. Uma bateria LiPo 4S fornece a reserva energética.

::::{grid} 3
:gutter: 2

:::{grid-item}
```{figure} images/pixhawk_6c.png
:alt: Controladora de voo Pixhawk 6C
Controladora Pixhawk 6C.
```
:::
:::{grid-item}
```{figure} images/bateria_power_module.jpg
:alt: Módulo de gerenciamento de potência Holybro PM07
Módulo de potência PM07.
```
:::
:::{grid-item}
```{figure} images/lipo_4s.jpg
:alt: Bateria de polímero de lítio Gens Ace 4S
Bateria LiPo 4S.
```
:::
::::

### Comunicação e acionamento

O cabeamento de silicone 22 AWG combina flexibilidade, resistência térmica e baixa impedância. O rádio estabelece comunicação bidirecional MAVLink com a GCS. ESCs com BLHeli acionam os motores submersíveis em ambos os sentidos.

::::{grid} 2
:gutter: 2

:::{grid-item}
```{figure} images/cabo_silicone.jpg
:alt: Cabo flexível de silicone utilizado nas interconexões
Cabeamento de silicone 22 AWG.
```
:::
:::{grid-item}
```{figure} images/modulo_telemetria.jpg
:alt: Rádio transceptor usado no enlace de telemetria
Rádio de telemetria MAVLink.
```
:::
:::{grid-item}
```{figure} images/esc_motores.jpeg
:alt: Controladores eletrônicos de velocidade usados nos motores
Controladores eletrônicos de velocidade.
```
:::
:::{grid-item}
```{figure} images/motores_propulsao.jpg
:alt: Motores brushless submersíveis usados na propulsão
Propulsores submersíveis.
```
:::
::::

## Software e firmware

A navegação pode utilizar ArduRover ou PX4. O planejamento por *waypoints*, a calibração dos sensores e o monitoramento remoto são realizados pelo Mission Planner ou QGroundControl.

```{figure} images/interface_gcs.jpg
:alt: Interface da estação de controle em solo usada para configurar a embarcação
:class: report-figure

Interface da Estação de Controle em Solo (GCS).
```
