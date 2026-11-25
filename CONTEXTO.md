# CONTEXTO DO PROJETO — Banca Didática SENAI (Elétrica)

> Arquivo de contexto para qualquer pessoa ou ferramenta de IA (Claude, ChatGPT, Gemini, Copilot, Cursor etc.).
> Leia este arquivo primeiro: ele resume o objetivo, as decisões já tomadas e os arquivos do projeto.

## 1. Objetivo

Preparar a **aula demonstrativa (banca didática)** de um processo seletivo do **Sistema Fiep (SENAI-PR)**.

| Item | Valor |
|---|---|
| Vaga | Técnico de Ensino Jr (Mensalista), área Elétrica (RP 20801), Sistema Fiep (Fiep, Sesi, Senai, IEL) |
| Tema oficial | **Instalações Elétricas Industriais: Dimensionamento, Proteção e Segurança de Circuitos Elétricos** |
| Objetivo da banca | Avaliar o domínio técnico e a capacidade didático-pedagógica: dimensionamento, dispositivos de proteção, diagramas e normas |
| Orientação | Aula demonstrativa contextualizada com a indústria, para alunos de **curso técnico** |
| Duração | **20 minutos** (roteiro planejado para 18min30, com 1min30 de folga) |
| Enunciado original | `7760-tema-da-banca-didatica.docx` |

A vaga pede: planejar e ministrar aulas, elaborar planos e materiais **conforme a MSEP**, conduzir práticas de laboratório **com segurança**, avaliar e acompanhar os alunos.

## 2. Perfil do candidato
Nome completo: **Diego Souza Matos** (capa dos slides e do plano).
Pouca experiência docente; conhece **manutenção, automação e eletrônica**. O recorte usa isso (motor, placa, contator, partida direta, softstarter e inversor, manutenção). A aula é **teórica e prática**: o emulador nos slides faz o papel da bancada.

## 3. Recorte e situação de aprendizagem
**"Da placa do motor ao painel seguro"**: esteira nova da Linha 3, com motor trifásico de **7,5 cv, 380 V, IV polos, F~s~ = 1,15**, a **40 m** do QGBT, em **eletroduto aparente com mais 2 circuitos**, galpão a **40 °C** (estufas). A equipe de manutenção (os alunos) define cabo, proteção, ligação, melhorias, segurança e manutenção.

## 4. Material de apoio (uso interno): Mamede Filho (2007), 7ª edição
> ⚠️ **Regra do usuário: não citar o Mamede** em slides, plano ou narração. Citar **apenas NBR e NR** (NBR 5410, NBR 5462, NBR IEC 60947, NR-10, NR-12). Os PDFs servem só de apoio técnico interno.
PDFs digitalizados na raiz do projeto (capítulos do livro *Instalações elétricas industriais*, LTC). Eles foram lidos por OCR; o texto extraído não fica no projeto.

| Arquivo | Capítulo |
|---|---|
| `3.Dimensionamento de condutores eletricos.pdf` | Cap. 3 (p. 115 em diante) |
| `6.Motores eletricos.pdf` | Cap. 6 (p. 263 em diante) |
| `7.Partida de motores eletricos de inducao.pdf` | Cap. 7 |

Trechos usados (página impressa do livro):
- **p. 117:** circuito de um motor → **I~c~ = F~s~ × I~n~** ("quando não se especificar o fator de serviço […] considerá-lo igual a 1").
- **p. 119:** a queda de tensão na partida deve ser ≤ 10 %.
- **p. 120:** Tab. 3.12, FCT para PVC: 35 °C = 0,94; 40 °C = 0,87; 45 °C = 0,79.
- **p. 127:** Tab. 3.21, limites de queda (7 % a partir do transformador próprio). No cálculo da queda do motor, usar I~n~ × F~s~; na partida, usar FP = 0,30.
- **p. 128–129:** Eq. 3.17 e 3.18, queda de tensão trifásica; ρ do cobre = 1/56 Ω·mm²/m.
- **p. 274:** Eq. 6.6, I~n~ = 736·P / (√3·V·η·cosφ); definição de fator de serviço (citação longa no plano); o motor tolera ±10 % de tensão.
- **p. 275:** "uma elevação de temperatura de 10 °C na temperatura de isolação de um motor reduz a sua vida útil pela metade"; não julgar o aquecimento pela carcaça; desequilíbrio de tensão aquece o motor.
- **p. 276:** Eq. 6.7, temperatura pelo método da resistência: T = R₂/R₁·(235+T₁) − 235. Classes de isolamento: A 105, E 120, B 130, F 155, H 180 °C.
- **p. 280:** Exemplo 6.4: 0,240 Ω frio (40 °C) e 0,301 Ω quente → 109,8 °C.
- **p. 292:** Tab. 6.3, 7,5 cv, IV polos, 380 V: **I~n~ 11,9 A, FP 0,81, η 0,84, I~p~/I~n~ 7,0, rotor bloqueado 6 s**.
- **p. 315–316:** partida direta (só contatores e disjuntores) e as condições em que ela pode ser usada.

> ⚠️ Correção feita: a primeira versão usava "1,25 × In" (regra americana, NEC). O livro e a NBR 5410/2004 usam **F~s~ × I~n~**. Não voltar ao 1,25.

## 5. Valores de referência (manter iguais em slides, plano e falas)

**Regra do usuário:** a corrente de projeto é a **da placa** (11,9 A). A Eq. 6.6 só explica a origem do valor; não mostrar um "valor calculado" diferente da placa. Montagem **como na bancada e no diagrama de campo indicado pelo usuário** (imagem `maxresdefault.jpg`): **força** com bornes -X L1/L2/L3 → **-DJ1** (tripolar) → **-K1** → **-F1** (relé térmico) → **-M** (U1, V1, W1, PE). **Comando em 220 V derivado de L1 e N** (sistema 380/220 V com neutro; borne N no -X), protegido por **-DJ2** (bipolar F+N): **-S2 emergência (11-12, com trava)** → -S0 (11-12) → -S1 (13-14) ∥ retenção -K1 (13-14) → -F1 95-96 → bobina -K1 A1-A2 → retorno pelo neutro (polo 3-4 do DJ2). Decisão do usuário: comando em 220 V. Base: NBR 5410 (permite F-N com neutro); NBR IEC 60204-1 dispensa transformador para 1 partida com até 2 dispositivos de comando; NR-12 pede extrabaixa tensão nos comandos ou outra proteção, por isso o **transformador 380/24 V é citado como melhoria**. **Com S2 emergência (pedido do usuário); sem H1 ou H2.** Como o comando não depende do DJ1, ao religar o DJ1 depois de um curto o motor volta a girar se o K1 estava retido: o simulador mostra isso como gancho de segurança (desligar no S0 antes). O galpão está a **40 °C** (estufas), para o 2,5 mm² reprovar com folga.

| Item | Como chegar | Resultado |
|---|---|---|
| I~n~ | placa / Tab. 6.3 (380 V) | **11,9 A** · I~p~ = 7 × 11,9 ≈ **83 A** |
| I~b~ = I~c~ | 1,15 × 11,9 | **13,7 A** |
| Fatores | FCT 40 °C = 0,87 × FCA (3 circuitos) = 0,70 | 0,609 |
| 2,5 mm² | 21 × 0,609 | 12,8 A → **não atende** |
| 4 mm² | 28 × 0,609 | **17,1 A → atende** |
| Queda | regime (I = 13,7 A, FP 0,81) / partida (83 A, FP 0,30) | **0,90 %** (≤ 4 %) / **2,0 %** (≤ 10 %) |
| PE | igual à fase | 4 mm² |
| DJ1 disjuntor tripolar | I~b~ ≤ I~n~ ≤ I~z~ → 13,7 ≤ 16 ≤ 17,1; curva D (magnético 10–20 × I~n~ = 160–320 A > 83 A) | **16 A curva D** |
| F1 relé térmico | faixa contém F~s~ × I~n~; 95-96 NF (comando), 97-98 NA (H2) | **12–18 A, ajuste 13,7 A** |
| Coordenação (sobrecarga) | I~b~ ≤ ajuste do F1 ≤ I~z~ | 13,7 ≤ 13,7 ≤ 17,1 ✓ |
| K1 | AC-3, I~e~ ≥ 13,7 A | **18 A**, bobina 220 V |
| DJ2 comando | bipolar F+N, 220 V (L1–N), bobina < 1 A | 2 A |
| Cabo de comando | mínimo 0,5 mm² (NBR 5410 Tab. 47) | 1 mm² |
| Botoeiras | S2 emergência NF 11-12 com trava (1º no comando) · S0 NF 11-12 · S1 NA 13-14 (∥ retenção K1 13-14) | — |

Capacidade (NBR 5410, B1, cobre/PVC, 3 condutores carregados): 1,5 → 15,5 · 2,5 → 21 · 4 → 28 · 6 → 36 · 10 → 50 · 16 → 68 A. FCT PVC: 30 °C 1,00 · 35 °C 0,94 · 40 °C 0,87 · 45 °C 0,79. FCA: 1 → 1,00 · 2 → 0,80 · 3 → 0,70 · 4 → 0,65 · 5 → 0,60 · 6 → 0,57.
Vídeos de referência indicados pelo usuário: Eletricity (partida direta fio a fio), Elétrica de A à Z (dimensionamento em 4 passos) e Engehall ("O motor pode queimar…": bancada com disjuntores → contator + relé térmico → motor e ajuste da simetria do relé de falta de fase).

## 6. Arquivos

| Arquivo | Conteúdo |
|---|---|
| `CONTEXTO.md` | Este arquivo, a fonte da verdade |
| `CLAUDE.md` / `AGENTS.md` | Ponteiros para este arquivo |
| `plano-de-aula.md` | **Fonte editável** do plano (MSEP), com cabeçalho YAML da capa |
| `perguntas-banca.md` | 10 perguntas prováveis da banca com respostas (estudo do candidato) |
| `pdf/` | PDFs para envio à banca: `Plano-de-aula_Diego-Souza-Matos.pdf` (ABNT, capa com Pato Branco – PR) e `Slides_Diego-Souza-Matos.pdf` (14 slides, estado inicial) |
| `tools/gerar_pdfs.py` | Gera os dois PDFs com o Chrome (requer `pip install playwright`): `python tools/gerar_pdfs.py` |
| `plano-de-aula.docx` | Plano em **formato ABNT**, gerado a partir do .md |
| `tools/gerar-plano-docx.js` | Gerador ABNT: `cd tools && npm install && node gerar-plano-docx.js` |
| `slides/aula.html` | Slides interativos e emulador (offline) |
| `*.pdf` | Capítulos 3, 6 e 7 do Mamede (2007) |
| `video/apresentacao-narrada.mp4` | Aula completa gravada com narração (voz pt-BR-AntonioNeural) e legendas embutidas, para estudo |
| `video/apresentacao-narrada.srt` | Legendas (texto falado com tempos) |
| `video/roteiro-narracao.md` | Texto da narração, slide a slide |
| `tools/gravar_video.py` | Gerador do vídeo: edge-tts → linha do tempo → Chrome (Playwright/CDP) → ffmpeg |

### Regras ABNT aplicadas pelo gerador
- **NBR 14724:** A4; margens de 3 cm (superior e esquerda) e 2 cm (inferior e direita); Arial 12; entrelinha 1,5; parágrafo com recuo de 1,25 cm, justificado; paginação no canto superior direito (a capa conta, mas não mostra número); quadros com título acima e "Fonte:" abaixo, em corpo 10.
- **NBR 6024:** seções numeradas ("1 TÍTULO" em caixa alta e negrito; "1.1 Título" em negrito). Alíneas a), b), c) terminam em ";" e a última em ".". REFERÊNCIAS sem número, centralizada.
- **NBR 10520:** citação curta entre aspas no texto; citação com mais de 3 linhas com recuo de 4 cm, corpo 10, entrelinha simples, sem aspas; chamada autor-data (MAMEDE FILHO, 2007, p. X).
- **NBR 6023:** referências alinhadas à esquerda, entrelinha simples, separadas por uma linha em branco, título em negrito.
- **Sintaxe do .md:** `## 1 TÍTULO`, `### 1.1 Título`, `- alínea;`, `> citação longa`, linha `Quadro N – título` antes da tabela, linha `Fonte: …` depois, `~sub~` para subscrito, `**negrito**`.

## 7. Slides (`slides/aula.html`): 14 slides, cerca de 17min30

| Tempo | Slide | Conteúdo |
|---|---|---|
| 0:00–1:45 | 1–3 | Capa, situação de aprendizagem (palpite de cabo), roteiro de 6 etapas |
| 1:45–3:15 | 4 | Placa do motor (I~n~ = 11,9 A lido da placa) e I~c~ |
| 3:15–5:15 | 5 | Condutor: FCT, FCA e queda de tensão |
| 5:15–6:30 | 6 | Proteção (cartões que viram): Q1 curto, F1 sobrecarga, K1 manobra; coordenação |
| 6:30–8:30 | 7 | **Como chegar em cada componente**: lista de materiais interativa (DJ1, K1, F1, cabo, PE, DJ2, cabo de comando, botoeiras) |
| 8:30–10:30 | 8 | Emulador no padrão de campo (força + comando 220 V L1–N com DJ2). Botões: S1, S0, Emergência (S2, trava), Rearmar (DJ1 ou F1), Sobrecarga (atua F1), Curto (abre DJ1; K1 continua retido) |
| 10:30–11:45 | 9 | Melhorias (relé de falta de fase, softstarter, inversor) |
| 11:45–13:00 | 10 | NR-10: jogo da sequência, **5 passos, foco no bloqueio** (sem aterramento temporário, a pedido do usuário) |
| 13:00–14:30 | 11 | Manutenção e ensaio da Eq. 6.7 |
| 14:30–15:00 | 12 | Memorial e palpite |
| 15:00–16:30 | 13 | Quiz |
| 16:30–17:30 | 14 | Síntese |

Teclas: **F** tela cheia · **N** notas do apresentador · **T** cronômetro · **O** visão geral · `?static` desliga as animações.
**Removido a pedido do usuário:** o slide "Ordem de serviço: encontre o defeito" (diagnóstico no emulador). Não recriar.
Mamede, cap. 7, usado no slide 8: softstarter p. 318–323 (rampa de tensão, corrente limitada, proteções de rotor bloqueado e sequência de fase); inversor p. 344. O relé de falta de fase não está nos capítulos fornecidos (é prática de mercado).

### Vídeo
> `apresentacao-narrada.mp4` = **versão atual** (16 min, gravada em 16/11/2026: placa 11,9 A, 40 °C, DJ1 + K1 + relé térmico F1, comando 220 V L1–N com DJ2 e S2 emergência, NR-10 só com bloqueio, sem citar o Mamede). `apresentacao-narrada-v1.mp4` (+ `v1.srt`) = versão anterior (disjuntor-motor), guardada a pedido do usuário. **Não apagar versões antigas: renomear antes de regravar.**

### Como regravar o vídeo
Requer Python com `edge-tts` e `playwright`, além de ffmpeg e Google Chrome: `python tools/gravar_video.py` (`--teste` grava só os slides 7–8; `--so-roteiro` só atualiza o roteiro). O roteiro de fala e as ações (cliques) ficam na lista `ROTEIRO` do script. Se mudar os slides, ajustar os seletores das ações. Por privacidade, a narração não fala o nome do candidato, porque o texto passa pelo serviço de voz da Microsoft.

## 8. Pendências para o usuário
- Conferir os **anos** das referências da MSEP (2019) e da NR 12 (2010) na versão que a banca usa.
- Abrir o .docx no Word para conferir a paginação final. Aqui só foi possível pré-visualizar a capa.

## 9. Regras para quem for editar
- Usar sempre os valores da seção 5 e as páginas do Mamede da seção 4. Nunca inventar citação.
- Linguagem para aluno de curso técnico; teoria curta e ancorada em prática.
- MSEP: situação de aprendizagem → capacidades → conhecimentos → estratégias → avaliação (critérios críticos e desejáveis).
- Plano: editar o `.md` e gerar o `.docx` de novo; não editar o .docx à mão.
