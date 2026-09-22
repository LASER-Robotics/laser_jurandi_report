# Relatório Técnico do Projeto Jurandi

<span class="report-kicker">RELATÓRIO TÉCNICO · ASV 001</span>

Desenvolvimento, integração e validação de um **Veículo de Superfície Autônomo (ASV)** em formato de catamarã, concebido como base móvel para operações colaborativas com drones sobre a água.

::::{grid} 3
:gutter: 1

:::{grid-item-card} STATUS
**VALIDAÇÃO EM CAMPO**
:::
:::{grid-item-card} INSTITUIÇÃO
**UFPB · ENGENHARIA**
:::
:::{grid-item-card} FOMENTO
**CAPES**
:::
::::

```{image} images/jurandi.jpg
:alt: Catamarã autônomo Jurandi navegando durante teste em piscina
:class: cover-image
```

## Visão geral

O Projeto Jurandi integra robótica marinha e aérea em uma plataforma modular, estável e preparada para navegação de precisão. O relatório documenta as decisões de hardware, a configuração do sistema de controle, a construção e os testes realizados.

:::{admonition} Resultado central
:class: result-callout
A arquitetura integrou a controladora Pixhawk 6C, propulsão bidirecional, telemetria e estrutura flutuante em uma plataforma funcional para testes aquáticos.
:::

## Conteúdo do relatório

::::{grid} 2
:gutter: 3

:::{grid-item-card} 01 · Apresentação
:link: apresentacao
:link-type: doc
Contexto, objetivo geral e objetivos específicos.
:::

:::{grid-item-card} 02 · Materiais
:link: materiais
:link-type: doc
Estrutura, eletrônica, potência e software embarcado.
:::

:::{grid-item-card} 03 · Construção
:link: construcao
:link-type: doc
Montagem mecânica, integração e configuração do firmware.
:::

:::{grid-item-card} 04 · Testes e resultados
:link: testes
:link-type: doc
Validações de bancada e ensaios em ambiente aquático.
:::
::::

```{toctree}
:maxdepth: 2
:caption: Documentação
:hidden:

apresentacao
materiais
construcao
testes
conclusao
```
