# Perguntas prováveis da banca (com respostas)

> Material de estudo do candidato, baseado nos slides (`slides/aula.html`) e nos valores do `CONTEXTO.md`.
> Perguntas 1 a 7: técnicas. Perguntas 8 a 10: pedagógicas.

---

## 1. Por que você dimensionou o cabo com 1,15 × I~n~ e não com 1,25 × I~n~?

O motor tem fator de serviço 1,15, e a NBR 5410 manda dimensionar o condutor de motor pela corrente nominal multiplicada pelo fator de serviço: 1,15 × 11,9 = **13,7 A**. O 1,25 vem da norma americana (NEC). Se o motor não tivesse fator de serviço na placa, eu usaria a própria corrente nominal.

## 2. Por que o cabo de 2,5 mm² não serve, se na tabela ele conduz 21 A?

Os 21 A valem para 30 °C e um único circuito. Na esteira são 40 °C (FCT 0,87) e três circuitos no mesmo eletroduto (FCA 0,70). O 2,5 mm² cai para cerca de **12,8 A**, abaixo dos 13,7 A necessários. O de 4 mm² dá cerca de **17,1 A** e atende. Depois confiro a queda de tensão (0,90 % em regime e 2,0 % na partida) e a seção mínima de 2,5 mm² para força, e fico com a maior seção entre os três critérios.

## 3. Por que disjuntor curva D e não curva C?

A partida direta puxa cerca de 7 × 11,9 ≈ **83 A**. A curva C dispara no magnético entre 5 e 10 vezes a corrente nominal, ou seja, a partir de 80 A num disjuntor de 16 A, perto demais da partida, e poderia desarmar ao ligar. A curva D dispara entre 10 e 20 vezes (160 a 320 A), bem acima da partida. E os 16 A ficam entre a corrente de projeto e a capacidade do cabo: **13,7 ≤ 16 ≤ 17,1 A**.

## 4. Se já tem o disjuntor, para que serve o relé térmico?

Cada um cuida de um problema:

- **DJ1 (disjuntor):** curto-circuito, que são milhares de ampères em milissegundos.
- **F1 (relé térmico):** sobrecarga, corrente um pouco acima do normal por muito tempo (esteira travada, falta de fase, rolamento ruim). Ajuste em 13,7 A, faixa de 12 a 18 A.
- **K1 (contator):** só manobra, não protege nada.

## 5. Por que o comando em 220 V e não em 380 V? E a NR-12?

Porque 220 V entre fase e neutro é o padrão de campo, com bobinas e botoeiras mais comuns e menos tensão no painel. A NBR 5410 permite esse arranjo com neutro, desde que o comando tenha proteção própria, que é o **DJ2**. A NR-12 prefere extrabaixa tensão nos comandos de partida e parada, ou outra proteção contra choque. Por isso apresento o **transformador de comando 380/24 V como melhoria**.

## 6. No simulador, o motor voltou a girar sozinho ao religar o DJ1. Isso não é um erro?

Não, é o comportamento real desse diagrama, e eu mostro de propósito. O comando vem do DJ2, independente do DJ1. No curto, o DJ1 abre a força, mas o K1 continua retido pelo contato 13-14. Se o técnico religar o DJ1 sem desligar no S0, o motor parte sem aviso. A lição de segurança é **desligar no S0 antes de religar o disjuntor**. Já no relé térmico isso não acontece: o 95-96 derruba a bobina, a retenção cai e é preciso apertar S1 de novo.

## 7. Por que a sequência da NR-10 não tem aterramento temporário?

Porque é uma intervenção em baixa tensão, num motor, a jusante do disjuntor. O foco está no seccionamento, no bloqueio com cadeado e etiqueta (LOTO), na constatação da ausência de tensão, na proteção das partes que continuam energizadas e na sinalização. Um detalhe importante: como o comando tem alimentação própria, o seccionamento precisa **desligar o DJ1 e o DJ2**.

## 8. Como você avalia se o aluno aprendeu? (pedagógica)

A avaliação é formativa e segue a MSEP, com critérios críticos e desejáveis. Durante a aula, observo as respostas às perguntas mediadoras ("o que vai acontecer?") e confronto o palpite inicial do cabo com o resultado. No fim, aplico o quiz com 4 perguntas, ligadas aos critérios críticos. Na atividade de continuidade, o aluno entrega um mini-memorial com outro motor (15 cv a 60 m) e monta a partida na bancada.

## 9. E o aluno que não acompanhar os cálculos? (pedagógica)

A aula parte de uma situação concreta, a esteira, e de um objeto que ele conhece, a placa do motor. Os cálculos aparecem passo a passo, com os números à vista na tela. Para quem tiver dificuldade, retomo com a régua **"carga ≤ proteção ≤ cabo"**, que é mais visual que a fórmula. Uso também o trabalho em grupo, juntando alunos com perfis diferentes, e a repetição prática na bancada.

## 10. Por que usar um simulador e não ir direto para a bancada? (pedagógica)

O simulador permite ver o que não se vê na bancada: a corrente circulando, o contato de retenção segurando a bobina e o relé atuando. E dá para provocar curto e sobrecarga sem risco nenhum. Ele **prepara o aluno para a bancada, não substitui**. Na aula seguinte, ele monta o mesmo circuito real aplicando o bloqueio antes de cada intervenção.
