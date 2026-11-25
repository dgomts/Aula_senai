# Roteiro de narração da aula

Texto falado no vídeo `apresentacao-narrada.mp4`, slide a slide. [ação] indica o que clicar.

## Slide 1: Capa

Bom dia a todos. Hoje eu vou conduzir uma aula de instalações elétricas industriais a partir de uma pergunta bem prática: o que um técnico faz quando chega uma máquina nova na fábrica?
Nós vamos sair da placa do motor e chegar a um painel seguro: dimensionar, proteger, ligar e manter o circuito de um motor trifásico.
Essas três ondas são as três fases que alimentam o nosso motor, defasadas de cento e vinte graus.

## Slide 2: Situação-problema

Imaginem a situação. Segunda-feira, sete da manhã. A fábrica instalou uma esteira nova na Linha três, acionada por um motor trifásico de sete e meio cavalos, trezentos e oitenta volts, quatro polos, com fator de serviço de um vírgula quinze.
O quadro geral fica a quarenta metros. O cabo vai passar em eletroduto aparente, junto com mais dois circuitos, e o galpão chega a quarenta graus, por causa das estufas.
Vocês são a equipe de manutenção, e a esteira só liga depois que vocês derem o sinal verde. Então, primeira pergunta para a turma: que cabo vocês usariam?
*[ação no slide]*
Pois é. Quase sempre a resposta é dois e meio milímetros quadrados, o cabo de sempre. Eu vou registrar esse palpite, e no final da aula nós voltamos nele.
Reparem no brilho vermelho do cabo: um cabo subdimensionado esquenta, envelhece a isolação e pode provocar um incêndio. Para liberar a esteira, temos três perguntas: qual cabo, qual proteção, e como ligar e intervir com segurança.

## Slide 3: Roteiro

Para responder, vamos seguir seis decisões, as mesmas de qualquer projeto ou manutenção de motor: corrente, condutor, proteção, diagrama, segurança e manutenção.
O objetivo é que, ao final, cada um de vocês consiga dimensionar, proteger e manter esse circuito, aplicando a NBR cinquenta e quatro dez, a NR dez e a NR doze.

## Slide 4: Corrente

Tudo começa na placa do motor. Ela é a carteira de identidade da máquina, e tudo o que nós precisamos está aqui.
Os campos em amarelo entram no cálculo: potência, tensão, corrente, fator de serviço, a relação entre a corrente de partida e a nominal, o rendimento e o fator de potência.
A corrente nominal está na placa: onze vírgula nove ampères, em trezentos e oitenta volts. É esse o valor do projeto.
E a fórmula mostra de onde ele vem: setecentos e trinta e seis vezes a potência em cavalos, dividido por raiz de três, vezes a tensão, vezes o rendimento, vezes o fator de potência.
*[ação no slide]*
Se eu troco para um motor de dez cavalos, a placa muda junto, com os dados reais da tabela.
*[ação no slide]*
Voltando ao nosso motor. Na partida, a corrente sobe para sete vezes a nominal: cerca de oitenta e três ampères.
E o fator de serviço de um vírgula quinze significa que o motor pode trabalhar continuamente com quinze por cento a mais de carga. Por isso, o cabo do motor é dimensionado para o fator de serviço vezes a corrente nominal: um vírgula quinze vezes onze vírgula nove, treze vírgula sete ampères.

## Slide 5: Condutor

Agora, o condutor. O dois e meio aguenta? Depende do ambiente.
*[ação no slide]*
*[ação no slide]*
Se o cabo estivesse sozinho, a trinta graus, o dois e meio conduziria vinte e um ampères e passaria com folga. É por isso que todo mundo usa o dois e meio. Mas essa não é a realidade da nossa fábrica.
*[ação no slide]*
*[ação no slide]*
A quarenta graus, por causa das estufas, o fator de temperatura é zero vírgula oitenta e sete. Com três circuitos juntos no eletroduto, o fator de agrupamento é zero vírgula setenta.
O cabo não consegue trocar calor e perde capacidade: o dois e meio cai para doze vírgula oito ampères, menos que os treze vírgula sete que o motor precisa. Reprovado!
O cabo de quatro milímetros quadrados conduz dezessete vírgula um ampères e atende. E, embaixo, a queda de tensão: zero vírgula noventa por cento em regime, dentro do limite de quatro por cento, e dois por cento na partida, dentro do limite de dez.

## Slide 6: Proteção

Com o cabo definido, vem a proteção. São três problemas diferentes e três respostas diferentes, como na bancada: disjuntor, contator e relé térmico.
O curto-circuito são milhares de ampères em milissegundos. Quem atua é o disjuntor D J um, de dezesseis ampères, curva D: abre na hora, mas não desarma na partida.
*[ação no slide]*
A sobrecarga é a esteira travada, a falta de fase, o rolamento ruim. Quem atua é o relé térmico F um, ajustado em treze vírgula sete ampères. E se ele atuou, a regra é investigar a causa antes de rearmar.
*[ação no slide]*
E a manobra é o contator. Atenção, porque esse é um erro comum: o contator não protege, ele só obedece ao comando.
Na régua de baixo está a coordenação da NBR cinquenta e quatro dez: a corrente de projeto, treze vírgula sete, menor ou igual ao ajuste do relé, treze vírgula sete, menor ou igual à capacidade do cabo, dezessete vírgula um.
E o disjuntor de dezesseis ampères também fica entre treze vírgula sete e dezessete vírgula um. Na curva D, ele só dispara acima de cento e sessenta ampères, bem acima dos oitenta e três da partida.

## Slide 7: Componentes

Agora, como chegar em cada componente da partida direta. Tudo parte de dois números da placa: a corrente nominal e o fator de serviço. A corrente de projeto é treze vírgula sete ampères.
O disjuntor D J um protege contra curto: dezesseis ampères, entre a corrente de projeto e a capacidade do cabo, curva D, para não desarmar na partida.
*[ação no slide]*
O contator: categoria AC três, para motor de gaiola, com corrente de emprego maior ou igual a treze vírgula sete. Uso o de dezoito ampères, com bobina de duzentos e vinte volts.
*[ação no slide]*
O relé térmico protege contra sobrecarga: faixa de doze a dezoito ampères, ajustado em treze vírgula sete, acoplado direto no contator.
*[ação no slide]*
O cabo de força, pelos três critérios: seção mínima, capacidade e queda de tensão. Vale o maior: quatro milímetros quadrados. E o condutor de proteção acompanha a fase.
*[ação no slide]*
O comando é em duzentos e vinte volts, entre a fase L um e o neutro, protegido pelo disjuntor bipolar D J dois, de dois ampères. Cabo de um milímetro quadrado. Como melhoria, um transformador de comando de vinte e quatro volts atende à NR doze.
*[ação no slide]*
E as botoeiras: S dois, a emergência tipo cogumelo, com trava, é a primeira do comando, como pede a NR doze. S zero desliga, contato fechado, vermelho. S um liga, contato aberto, verde, em paralelo com o contato de retenção do K um.

## Slide 8: Diagrama

Agora vamos ver o diagrama como encontramos em campo. No diagrama de força, as três fases entram pelos bornes, passam pelo disjuntor D J um, pelo contator K um e pelo relé térmico F um, até os terminais U um, V um e W um do motor.
O diagrama de comando é derivado da fase L um e do neutro, em duzentos e vinte volts, protegido pelo D J dois. Passa pela emergência S dois, pelo S zero, pelo S um em paralelo com o contato de retenção do K um, pelo contato noventa e cinco, noventa e seis do relé térmico, e chega à bobina, A um e A dois. Antes de cada clique, eu pergunto para a turma: o que vai acontecer?
*[ação no slide]*
Quando eu aperto o S um, a bobina do K um é energizada, os contatos de força fecham e o motor gira. E eu já soltei o botão: quem mantém é o contato de retenção, K um, treze, catorze.
Agora, vamos simular a esteira travada.
*[ação no slide]*
A corrente sobe, e o bimetal do relé térmico aquece...
e o F um atua. O contato noventa e cinco, noventa e seis abre, a bobina cai e o motor para. Reparem que o disjuntor continua ligado: cada um cuida da sua proteção.
*[ação no slide]*
Quando eu rearmo o relé, o motor não volta sozinho, porque a retenção caiu.
*[ação no slide]*
Ligo de novo. E agora um curto-circuito.
*[ação no slide]*
O D J um abre na hora. Mas atenção: o comando vem do D J dois, então o K um continua retido.
*[ação no slide]*
E, ao religar o D J um, o motor volta a girar sozinho. Por isso, na prática, desligo no S zero antes de religar o disjuntor.
*[ação no slide]*
E se alguém apertar a emergência...
*[ação no slide]*
o contato onze, doze do S dois abre, o comando cai na hora e o botão fica travado. Para voltar, é preciso destravar e apertar o S um de novo.
*[ação no slide]*

## Slide 9: Melhorias

Funciona. Mas dá para melhorar? Imaginem que a esteira fosse de vocês.
A partida direta é simples e barata, mas tem um pico de corrente de cerca de sete vezes a nominal e dá um tranco na correia.
*[ação no slide]*
O upgrade mais barato é o relé de falta de fase. Ele monitora as três fases e, se faltar uma, abre o comando. Mas atenção ao ajuste da simetria: mal ajustado, ele é enganado pela tensão que o próprio motor induz na fase que faltou.
*[ação no slide]*
A softstarter usa tiristores para aplicar uma rampa de tensão e limitar a corrente de partida. Acaba o tranco na esteira.
*[ação no slide]*
E o inversor de frequência controla a velocidade e parte com uma corrente próxima da nominal, mas é mais caro e exige parametrização.
Para a nossa esteira, a partida direta atende, e o relé de falta de fase é o melhor custo-benefício. Os acionamentos eletrônicos ficam para as próximas unidades do curso.

## Slide 10: Segurança NR-10

Antes de colocar a mão no painel, segurança. A NR dez define a sequência de desenergização. Nesta atividade, em baixa tensão, o foco é o bloqueio. Vamos montar juntos.
*[ação no slide]*
Primeiro, o seccionamento: desligar os disjuntores D J um e D J dois, porque o comando tem alimentação própria.
*[ação no slide]*
Depois, impedir a reenergização, com cadeado e etiqueta pessoais. É o famoso LOTO, e só quem colocou pode retirar.
*[ação no slide]*
Então, constatar a ausência de tensão com um detector aferido. Esse é o passo mais crítico: só considero o circuito desenergizado depois de testar.
*[ação no slide]*
Proteger os elementos energizados que ficam na zona controlada, como os bornes de entrada.
*[ação no slide]*
E, por fim, a sinalização de impedimento de reenergização. Agora sim: circuito liberado para intervenção, sempre com os equipamentos de proteção individual.

## Slide 11: Manutenção

Depois que o motor está funcionando, é preciso mantê-lo. Na manutenção corretiva, nós agimos depois da falha. Na preventiva, por calendário: reaperto de bornes, contatos, teste do botão de emergência e ajuste do térmico. E na preditiva, pela condição do equipamento.
Uma regra prática que todo técnico de manutenção deveria lembrar: cada dez graus acima do limite da isolação reduzem a vida útil do motor pela metade.
E como medir essa temperatura? Não pela carcaça, que engana. Uso o método da resistência. Por exemplo, o enrolamento tem zero vírgula duzentos e quarenta ohms a frio, a quarenta graus, e zero vírgula trezentos e um ohms a quente. Isso dá cerca de cento e dez graus, dentro da classe B.
*[ação no slide]*
Se a resistência a quente subir para zero vírgula trezentos e trinta, a temperatura passa de cento e quarenta graus, e a vida útil cai para uma fração do normal.
*[ação no slide]*
Por fim, o método de diagnóstico, que vocês vão usar na bancada: sintoma, hipótese, bloquear, medir, corrigir e testar.

## Slide 12: Memorial

Então, vamos voltar à pergunta do início. Este é o memorial que libera a Linha três.
Corrente de placa de onze vírgula nove ampères, cabo de quatro milímetros quadrados, condutor de proteção de quatro, queda de tensão de zero vírgula noventa por cento, disjuntor de dezesseis ampères curva D, relé térmico ajustado em treze vírgula sete, contator de dezoito ampères, partida direta e intervenção com NR dez e bloqueio.
O palpite da turma era dois e meio. A solução técnica é quatro. Decisão técnica se justifica com norma e cálculo, não com costume.

## Slide 13: Quiz

Para verificar a aprendizagem, quatro perguntas rápidas. Primeira: a placa diz onze vírgula nove ampères e fator de serviço de um vírgula quinze. Qual a corrente mínima do cabo?
*[ação no slide]*
Treze vírgula sete: fator de serviço vezes a corrente nominal.
Segunda: a esteira travou e o motor ficou em sobrecarga. Quem deve desligar?
*[ação no slide]*
O relé térmico F um. O contator só manobra.
Terceira: a esteira só anda enquanto o operador segura o S um. Qual o defeito mais provável?
*[ação no slide]*
O selo do K um não fecha.
E quarta: qual é o primeiro passo da desenergização?
*[ação no slide]*
O seccionamento.

## Slide 14: Encerramento

Para fechar, cinco ideias. A placa dá a corrente e o fator de serviço, e o cabo é dimensionado para o fator de serviço vezes a corrente nominal, já corrigido pelo ambiente.
Temperatura e agrupamento reduzem a capacidade do cabo: o dois e meio de sempre nem sempre serve. A proteção fica entre a carga e o cabo, e o contator manobra, não protege.
Sem desenergização e bloqueio, nenhuma intervenção. E manutenção tem método.
Na próxima aula, no laboratório, vocês vão redimensionar o circuito para um motor de quinze cavalos a sessenta metros, montar a partida direta na bancada e diagnosticar defeitos reais, aplicando o bloqueio antes de cada medição.
Muito obrigado. Fico à disposição para perguntas.
