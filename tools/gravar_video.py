"""Grava a apresentação slides/aula.html como vídeo narrado (voz pt-BR-AntonioNeural).

Etapas: 1) gera a narração de cada trecho com edge-tts; 2) monta a linha do tempo;
3) conduz o deck no Chrome (navegação e interações) no ritmo da narração, capturando
a tela via CDP; 4) junta vídeo, áudio e legendas em video/apresentacao-narrada.mp4.

Uso: python gravar_video.py [--so-roteiro]
Requer: edge-tts, playwright (python), ffmpeg e Google Chrome instalados.
"""
import asyncio, base64, hashlib, json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECK = os.path.join(ROOT, 'slides', 'aula.html')
OUTDIR = os.path.join(ROOT, 'video')
VOICE = 'pt-BR-AntonioNeural'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H, FPS = 1920, 1080, 30
GAP = 0.35          # pausa entre falas (s)

# ---------------------------------------------------------------- ações no deck
NEXT = "document.body.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}))"
def click(sel): return f"document.querySelector({json.dumps(sel)}).click()"
def press(sel): return (f"(()=>{{const b=document.querySelector({json.dumps(sel)});"
                        "b.dispatchEvent(new PointerEvent('pointerdown'));"
                        "setTimeout(()=>b.dispatchEvent(new PointerEvent('pointerup')),400);})()")
def slide_to(sel, v, ms=1600):
    return (f"(()=>{{const r=document.querySelector({json.dumps(sel)});const a=+r.value,b={v},t0=performance.now();"
            f"(function s(){{const k=Math.min(1,(performance.now()-t0)/{ms});r.value=(a+(b-a)*k).toFixed(3);"
            "r.dispatchEvent(new Event('input'));if(k<1)requestAnimationFrame(s);})();})()")

S = lambda t: ('say', t)
A = lambda js, w=0.8: ('act', js, w)
Wt = lambda s: ('wait', s)

# ---------------------------------------------------------------- roteiro
ROTEIRO = [
 ('Capa', [
  S('Bom dia a todos. Hoje eu vou conduzir uma aula de instalações elétricas industriais a partir de uma pergunta bem prática: o que um técnico faz quando chega uma máquina nova na fábrica?'),
  S('Nós vamos sair da placa do motor e chegar a um painel seguro: dimensionar, proteger, ligar e manter o circuito de um motor trifásico.'),
  S('Essas três ondas são as três fases que alimentam o nosso motor, defasadas de cento e vinte graus.'),
 ]),
 ('Situação-problema', [
  S('Imaginem a situação. Segunda-feira, sete da manhã. A fábrica instalou uma esteira nova na Linha três, acionada por um motor trifásico de sete e meio cavalos, trezentos e oitenta volts, quatro polos, com fator de serviço de um vírgula quinze.'),
  S('O quadro geral fica a quarenta metros. O cabo vai passar em eletroduto aparente, junto com mais dois circuitos, e o galpão chega a quarenta graus, por causa das estufas.'),
  S('Vocês são a equipe de manutenção, e a esteira só liga depois que vocês derem o sinal verde. Então, primeira pergunta para a turma: que cabo vocês usariam?'),
  A(click('#poll button[data-v="2,5"]'), 1.0),
  S('Pois é. Quase sempre a resposta é dois e meio milímetros quadrados, o cabo de sempre. Eu vou registrar esse palpite, e no final da aula nós voltamos nele.'),
  S('Reparem no brilho vermelho do cabo: um cabo subdimensionado esquenta, envelhece a isolação e pode provocar um incêndio. Para liberar a esteira, temos três perguntas: qual cabo, qual proteção, e como ligar e intervir com segurança.'),
 ]),
 ('Roteiro', [
  S('Para responder, vamos seguir seis decisões, as mesmas de qualquer projeto ou manutenção de motor: corrente, condutor, proteção, diagrama, segurança e manutenção.'),
  S('O objetivo é que, ao final, cada um de vocês consiga dimensionar, proteger e manter esse circuito, aplicando a NBR cinquenta e quatro dez, a NR dez e a NR doze.'),
 ]),
 ('Corrente', [
  S('Tudo começa na placa do motor. Ela é a carteira de identidade da máquina, e tudo o que nós precisamos está aqui.'),
  S('Os campos em amarelo entram no cálculo: potência, tensão, corrente, fator de serviço, a relação entre a corrente de partida e a nominal, o rendimento e o fator de potência.'),
  S('A corrente nominal está na placa: onze vírgula nove ampères, em trezentos e oitenta volts. É esse o valor do projeto.'),
  S('E a fórmula mostra de onde ele vem: setecentos e trinta e seis vezes a potência em cavalos, dividido por raiz de três, vezes a tensão, vezes o rendimento, vezes o fator de potência.'),
  A(click('#i-cv button[data-v="10"]'), 1.2),
  S('Se eu troco para um motor de dez cavalos, a placa muda junto, com os dados reais da tabela.'),
  A(click('#i-cv button[data-v="7.5"]'), 1.0),
  S('Voltando ao nosso motor. Na partida, a corrente sobe para sete vezes a nominal: cerca de oitenta e três ampères.'),
  S('E o fator de serviço de um vírgula quinze significa que o motor pode trabalhar continuamente com quinze por cento a mais de carga. Por isso, o cabo do motor é dimensionado para o fator de serviço vezes a corrente nominal: um vírgula quinze vezes onze vírgula nove, treze vírgula sete ampères.'),
 ]),
 ('Condutor', [
  S('Agora, o condutor. O dois e meio aguenta? Depende do ambiente.'),
  A(click('#i-temp button[data-v="30"]'), 0.5), A(click('#i-grp button[data-v="1"]'), 1.0),
  S('Se o cabo estivesse sozinho, a trinta graus, o dois e meio conduziria vinte e um ampères e passaria com folga. É por isso que todo mundo usa o dois e meio. Mas essa não é a realidade da nossa fábrica.'),
  A(click('#i-temp button[data-v="40"]'), 0.6), A(click('#i-grp button[data-v="3"]'), 1.2),
  S('A quarenta graus, por causa das estufas, o fator de temperatura é zero vírgula oitenta e sete. Com três circuitos juntos no eletroduto, o fator de agrupamento é zero vírgula setenta.'),
  S('O cabo não consegue trocar calor e perde capacidade: o dois e meio cai para doze vírgula oito ampères, menos que os treze vírgula sete que o motor precisa. Reprovado!'),
  S('O cabo de quatro milímetros quadrados conduz dezessete vírgula um ampères e atende. E, embaixo, a queda de tensão: zero vírgula noventa por cento em regime, dentro do limite de quatro por cento, e dois por cento na partida, dentro do limite de dez.'),
 ]),
 ('Proteção', [
  S('Com o cabo definido, vem a proteção. São três problemas diferentes e três respostas diferentes, como na bancada: disjuntor, contator e relé térmico.'),
  S('O curto-circuito são milhares de ampères em milissegundos. Quem atua é o disjuntor D J um, de dezesseis ampères, curva D: abre na hora, mas não desarma na partida.'),
  A("document.querySelectorAll('[data-flip]')[1].click()", 1.0),
  S('A sobrecarga é a esteira travada, a falta de fase, o rolamento ruim. Quem atua é o relé térmico F um, ajustado em treze vírgula sete ampères. E se ele atuou, a regra é investigar a causa antes de rearmar.'),
  A("document.querySelectorAll('[data-flip]')[1].click()", 0.8),
  S('E a manobra é o contator. Atenção, porque esse é um erro comum: o contator não protege, ele só obedece ao comando.'),
  S('Na régua de baixo está a coordenação da NBR cinquenta e quatro dez: a corrente de projeto, treze vírgula sete, menor ou igual ao ajuste do relé, treze vírgula sete, menor ou igual à capacidade do cabo, dezessete vírgula um.'),
  S('E o disjuntor de dezesseis ampères também fica entre treze vírgula sete e dezessete vírgula um. Na curva D, ele só dispara acima de cento e sessenta ampères, bem acima dos oitenta e três da partida.'),
 ]),
 ('Componentes', [
  S('Agora, como chegar em cada componente da partida direta. Tudo parte de dois números da placa: a corrente nominal e o fator de serviço. A corrente de projeto é treze vírgula sete ampères.'),
  S('O disjuntor D J um protege contra curto: dezesseis ampères, entre a corrente de projeto e a capacidade do cabo, curva D, para não desarmar na partida.'),
  A(click('.bi[data-i="1"]'), 0.8),
  S('O contator: categoria AC três, para motor de gaiola, com corrente de emprego maior ou igual a treze vírgula sete. Uso o de dezoito ampères, com bobina de duzentos e vinte volts.'),
  A(click('.bi[data-i="2"]'), 0.8),
  S('O relé térmico protege contra sobrecarga: faixa de doze a dezoito ampères, ajustado em treze vírgula sete, acoplado direto no contator.'),
  A(click('.bi[data-i="3"]'), 0.6),
  S('O cabo de força, pelos três critérios: seção mínima, capacidade e queda de tensão. Vale o maior: quatro milímetros quadrados. E o condutor de proteção acompanha a fase.'),
  A(click('.bi[data-i="5"]'), 0.6),
  S('O comando é em duzentos e vinte volts, entre a fase L um e o neutro, protegido pelo disjuntor bipolar D J dois, de dois ampères. Cabo de um milímetro quadrado. Como melhoria, um transformador de comando de vinte e quatro volts atende à NR doze.'),
  A(click('.bi[data-i="7"]'), 0.6),
  S('E as botoeiras: S dois, a emergência tipo cogumelo, com trava, é a primeira do comando, como pede a NR doze. S zero desliga, contato fechado, vermelho. S um liga, contato aberto, verde, em paralelo com o contato de retenção do K um.'),
 ]),
 ('Diagrama', [
  S('Agora vamos ver o diagrama como encontramos em campo. No diagrama de força, as três fases entram pelos bornes, passam pelo disjuntor D J um, pelo contator K um e pelo relé térmico F um, até os terminais U um, V um e W um do motor.'),
  S('O diagrama de comando é derivado da fase L um e do neutro, em duzentos e vinte volts, protegido pelo D J dois. Passa pela emergência S dois, pelo S zero, pelo S um em paralelo com o contato de retenção do K um, pelo contato noventa e cinco, noventa e seis do relé térmico, e chega à bobina, A um e A dois. Antes de cada clique, eu pergunto para a turma: o que vai acontecer?'),
  A(press('[data-act="s1"]'), 1.2),
  S('Quando eu aperto o S um, a bobina do K um é energizada, os contatos de força fecham e o motor gira. E eu já soltei o botão: quem mantém é o contato de retenção, K um, treze, catorze.'),
  S('Agora, vamos simular a esteira travada.'),
  A(click('[data-act="ol"]'), 0.4),
  S('A corrente sobe, e o bimetal do relé térmico aquece...'),
  Wt(1.0),
  S('e o F um atua. O contato noventa e cinco, noventa e seis abre, a bobina cai e o motor para. Reparem que o disjuntor continua ligado: cada um cuida da sua proteção.'),
  A(click('[data-act="rst"]'), 0.8),
  S('Quando eu rearmo o relé, o motor não volta sozinho, porque a retenção caiu.'),
  A(press('[data-act="s1"]'), 1.2),
  S('Ligo de novo. E agora um curto-circuito.'),
  A(click('[data-act="sc"]'), 1.0),
  S('O D J um abre na hora. Mas atenção: o comando vem do D J dois, então o K um continua retido.'),
  A(click('[data-act="rst"]'), 1.0),
  S('E, ao religar o D J um, o motor volta a girar sozinho. Por isso, na prática, desligo no S zero antes de religar o disjuntor.'),
  A(press('[data-act="s1"]'), 1.0),
  S('E se alguém apertar a emergência...'),
  A(click('[data-act="s2"]'), 0.8),
  S('o contato onze, doze do S dois abre, o comando cai na hora e o botão fica travado. Para voltar, é preciso destravar e apertar o S um de novo.'),
  A(click('[data-act="s2"]'), 0.8),
 ]),
 ('Melhorias', [
  S('Funciona. Mas dá para melhorar? Imaginem que a esteira fosse de vocês.'),
  S('A partida direta é simples e barata, mas tem um pico de corrente de cerca de sete vezes a nominal e dá um tranco na correia.'),
  A(click('#mSel button[data-m="rff"]'), 0.8),
  S('O upgrade mais barato é o relé de falta de fase. Ele monitora as três fases e, se faltar uma, abre o comando. Mas atenção ao ajuste da simetria: mal ajustado, ele é enganado pela tensão que o próprio motor induz na fase que faltou.'),
  A(click('#mSel button[data-m="soft"]'), 0.8),
  S('A softstarter usa tiristores para aplicar uma rampa de tensão e limitar a corrente de partida. Acaba o tranco na esteira.'),
  A(click('#mSel button[data-m="inv"]'), 0.8),
  S('E o inversor de frequência controla a velocidade e parte com uma corrente próxima da nominal, mas é mais caro e exige parametrização.'),
  S('Para a nossa esteira, a partida direta atende, e o relé de falta de fase é o melhor custo-benefício. Os acionamentos eletrônicos ficam para as próximas unidades do curso.'),
 ]),
 ('Segurança NR-10', [
  S('Antes de colocar a mão no painel, segurança. A NR dez define a sequência de desenergização. Nesta atividade, em baixa tensão, o foco é o bloqueio. Vamos montar juntos.'),
  A(click('#pool .opt[data-i="0"]'), 0.5), S('Primeiro, o seccionamento: desligar os disjuntores D J um e D J dois, porque o comando tem alimentação própria.'),
  A(click('#pool .opt[data-i="1"]'), 0.5), S('Depois, impedir a reenergização, com cadeado e etiqueta pessoais. É o famoso LOTO, e só quem colocou pode retirar.'),
  A(click('#pool .opt[data-i="2"]'), 0.5), S('Então, constatar a ausência de tensão com um detector aferido. Esse é o passo mais crítico: só considero o circuito desenergizado depois de testar.'),
  A(click('#pool .opt[data-i="3"]'), 0.5), S('Proteger os elementos energizados que ficam na zona controlada, como os bornes de entrada.'),
  A(click('#pool .opt[data-i="4"]'), 0.6), S('E, por fim, a sinalização de impedimento de reenergização. Agora sim: circuito liberado para intervenção, sempre com os equipamentos de proteção individual.'),
 ]),
 ('Manutenção', [
  S('Depois que o motor está funcionando, é preciso mantê-lo. Na manutenção corretiva, nós agimos depois da falha. Na preventiva, por calendário: reaperto de bornes, contatos, teste do botão de emergência e ajuste do térmico. E na preditiva, pela condição do equipamento.'),
  S('Uma regra prática que todo técnico de manutenção deveria lembrar: cada dez graus acima do limite da isolação reduzem a vida útil do motor pela metade.'),
  S('E como medir essa temperatura? Não pela carcaça, que engana. Uso o método da resistência. Por exemplo, o enrolamento tem zero vírgula duzentos e quarenta ohms a frio, a quarenta graus, e zero vírgula trezentos e um ohms a quente. Isso dá cerca de cento e dez graus, dentro da classe B.'),
  A(slide_to('#i-r2', 0.330), 1.8),
  S('Se a resistência a quente subir para zero vírgula trezentos e trinta, a temperatura passa de cento e quarenta graus, e a vida útil cai para uma fração do normal.'),
  A(slide_to('#i-r2', 0.301), 1.6),
  S('Por fim, o método de diagnóstico, que vocês vão usar na bancada: sintoma, hipótese, bloquear, medir, corrigir e testar.'),
 ]),
 ('Memorial', [
  S('Então, vamos voltar à pergunta do início. Este é o memorial que libera a Linha três.'),
  S('Corrente de placa de onze vírgula nove ampères, cabo de quatro milímetros quadrados, condutor de proteção de quatro, queda de tensão de zero vírgula noventa por cento, disjuntor de dezesseis ampères curva D, relé térmico ajustado em treze vírgula sete, contator de dezoito ampères, partida direta e intervenção com NR dez e bloqueio.'),
  S('O palpite da turma era dois e meio. A solução técnica é quatro. Decisão técnica se justifica com norma e cálculo, não com costume.'),
 ]),
 ('Quiz', [
  S('Para verificar a aprendizagem, quatro perguntas rápidas. Primeira: a placa diz onze vírgula nove ampères e fator de serviço de um vírgula quinze. Qual a corrente mínima do cabo?'),
  A(click('#quiz .ans[data-q="0"][data-j="1"]'), 0.6), S('Treze vírgula sete: fator de serviço vezes a corrente nominal.'),
  S('Segunda: a esteira travou e o motor ficou em sobrecarga. Quem deve desligar?'),
  A(click('#quiz .ans[data-q="1"][data-j="1"]'), 0.6), S('O relé térmico F um. O contator só manobra.'),
  S('Terceira: a esteira só anda enquanto o operador segura o S um. Qual o defeito mais provável?'),
  A(click('#quiz .ans[data-q="2"][data-j="1"]'), 0.6), S('O selo do K um não fecha.'),
  S('E quarta: qual é o primeiro passo da desenergização?'),
  A(click('#quiz .ans[data-q="3"][data-j="2"]'), 0.6), S('O seccionamento.'),
 ]),
 ('Encerramento', [
  S('Para fechar, cinco ideias. A placa dá a corrente e o fator de serviço, e o cabo é dimensionado para o fator de serviço vezes a corrente nominal, já corrigido pelo ambiente.'),
  S('Temperatura e agrupamento reduzem a capacidade do cabo: o dois e meio de sempre nem sempre serve. A proteção fica entre a carga e o cabo, e o contator manobra, não protege.'),
  S('Sem desenergização e bloqueio, nenhuma intervenção. E manutenção tem método.'),
  S('Na próxima aula, no laboratório, vocês vão redimensionar o circuito para um motor de quinze cavalos a sessenta metros, montar a partida direta na bancada e diagnosticar defeitos reais, aplicando o bloqueio antes de cada medição.'),
  S('Muito obrigado. Fico à disposição para perguntas.'),
  Wt(2.0),
 ]),
]

# ---------------------------------------------------------------- utilidades
def dur(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'csv=p=0', path]).decode().strip())

def srt_time(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

def escrever_roteiro_md():
    linhas = ['# Roteiro de narração da aula', '',
              'Texto falado no vídeo `apresentacao-narrada.mp4`, slide a slide. [ação] indica o que clicar.', '']
    for i, (nome, itens) in enumerate(ROTEIRO, 1):
        linhas += [f'## Slide {i}: {nome}', '']
        for it in itens:
            if it[0] == 'say': linhas.append(it[1])
            elif it[0] == 'act': linhas.append('*[ação no slide]*')
        linhas.append('')
    open(os.path.join(OUTDIR, 'roteiro-narracao.md'), 'w', encoding='utf-8').write('\n'.join(linhas))

async def gerar_tts(work):
    import edge_tts
    n = 0; arquivos = {}
    for si, (_, itens) in enumerate(ROTEIRO):
        for ii, it in enumerate(itens):
            if it[0] != 'say': continue
            f = os.path.join(work, 'tts_' + hashlib.md5((VOICE + it[1]).encode()).hexdigest()[:16] + '.mp3')
            if not os.path.exists(f) or os.path.getsize(f) == 0:
                for tent in range(4):
                    try:
                        await edge_tts.Communicate(it[1], VOICE, rate='+0%').save(f); break
                    except Exception as e:
                        print('  nova tentativa TTS', e); await asyncio.sleep(2 + tent * 2)
            arquivos[(si, ii)] = f; n += 1
    print(f'TTS: {n} trechos')
    return arquivos

def montar_linha_do_tempo(arquivos):
    t = 1.5; eventos = []; falas = []
    for si, (_, itens) in enumerate(ROTEIRO):
        if si > 0:
            eventos.append((t, NEXT)); t += 1.3
        for ii, it in enumerate(itens):
            if it[0] == 'say':
                d = dur(arquivos[(si, ii)]); falas.append((t, d, arquivos[(si, ii)], it[1])); t += d + GAP
            elif it[0] == 'act':
                eventos.append((t, it[1])); t += it[2]
            else:
                t += it[1]
        t += 0.6
    return eventos, falas, t + 1.0

def montar_audio(falas, total, work):
    wav = os.path.join(work, 'narracao.wav')
    inputs, filt = [], []
    for k, (t, d, f, _) in enumerate(falas):
        inputs += ['-i', f]
        ms = int(t * 1000); filt.append(f'[{k}:a]aresample=48000,adelay={ms}:all=1[a{k}]')
    mix = ''.join(f'[a{k}]' for k in range(len(falas))) + f'amix=inputs={len(falas)}:normalize=0,apad,atrim=0:{total:.3f}[out]'
    script = os.path.join(work, 'filtro.txt'); open(script, 'w').write(';'.join(filt + [mix]))
    subprocess.check_call(['ffmpeg', '-y', '-v', 'error', *inputs, '-/filter_complex', script,
                           '-map', '[out]', '-ac', '2', '-ar', '48000', wav])
    return wav

def escrever_srt(falas, path):
    with open(path, 'w', encoding='utf-8') as fh:
        for k, (t, d, _, txt) in enumerate(falas, 1):
            fh.write(f'{k}\n{srt_time(t)} --> {srt_time(t + d)}\n{txt}\n\n')

async def gravar(eventos, total, video_path):
    from playwright.async_api import async_playwright
    ff = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg',
                           '-i', '-', '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x080C11', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                           '-r', str(FPS), video_path], stdin=subprocess.PIPE)
    latest = {'jpg': None}
    async with async_playwright() as pw:
        br = await pw.chromium.launch(executable_path=CHROME, headless=True, args=['--hide-scrollbars', f'--window-size={W},{H}'])
        page = await br.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
        await page.goto('file://' + DECK + f'#{START + 1}')
        await page.add_style_tag(content='#hud,#help{display:none!important}')
        await page.wait_for_timeout(2500)
        cdp = await page.context.new_cdp_session(page)
        def on_frame(p):
            latest['jpg'] = base64.b64decode(p['data'])
            asyncio.ensure_future(cdp.send('Page.screencastFrameAck', {'sessionId': p['sessionId']}))
        cdp.on('Page.screencastFrame', on_frame)
        await cdp.send('Page.startScreencast', {'format': 'jpeg', 'quality': 92, 'maxWidth': W, 'maxHeight': H, 'everyNthFrame': 1})
        while latest['jpg'] is None: await asyncio.sleep(0.05)
        loop = asyncio.get_running_loop(); t0 = loop.time()

        async def sampler():
            k = 0; nframes = int(total * FPS)
            while k < nframes:
                alvo = t0 + k / FPS; agora = loop.time()
                if agora < alvo: await asyncio.sleep(alvo - agora)
                ff.stdin.write(latest['jpg']); k += 1
                if k % (FPS * 30) == 0: print(f'  gravando… {k / FPS / 60:.1f} de {total / 60:.1f} min', flush=True)

        async def roteiro():
            for t, js in eventos:
                espera = t0 + t - loop.time()
                if espera > 0: await asyncio.sleep(espera)
                try: await page.evaluate(js)
                except Exception as e: print('  ação falhou:', e)

        await asyncio.gather(sampler(), roteiro())
        await cdp.send('Page.stopScreencast'); await br.close()
    ff.stdin.close(); ff.wait()

START = 0
async def main():
    global ROTEIRO, START
    if '--teste' in sys.argv:
        ROTEIRO = ROTEIRO[6:8]; START = 6
    os.makedirs(OUTDIR, exist_ok=True)
    if '--teste' not in sys.argv: escrever_roteiro_md()
    if '--so-roteiro' in sys.argv: return
    work = os.path.join(tempfile.gettempdir(), 'aula_video_work'); os.makedirs(work, exist_ok=True)
    arquivos = await gerar_tts(work)
    eventos, falas, total = montar_linha_do_tempo(arquivos)
    print(f'Duração total: {total / 60:.1f} min')
    wav = montar_audio(falas, total, work)
    srt = os.path.join(work, 'teste.srt') if '--teste' in sys.argv else os.path.join(OUTDIR, 'apresentacao-narrada.srt')
    escrever_srt(falas, srt)
    raw = os.path.join(work, 'tela.mp4')
    await gravar(eventos, total, raw)
    out = os.path.join(OUTDIR, 'teste.mp4' if '--teste' in sys.argv else 'apresentacao-narrada.mp4')
    subprocess.check_call(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-i', wav, '-i', srt,
                           '-map', '0:v', '-map', '1:a', '-map', '2:s', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
                           '-c:s', 'mov_text', '-metadata:s:s:0', 'language=por', '-metadata:s:a:0', 'language=por',
                           '-shortest', '-movflags', '+faststart', out])
    print('Vídeo:', out)

if __name__ == '__main__':
    asyncio.run(main())
