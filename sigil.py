import os
import json
import cairosvg

pre = """
dozmarbinwansamlitsighidfidlissogdirwacsabwissib
rigsoldopmodfoglidhopdardorlorhodfolrintogsilmir
holpaslacrovlivdalsatlibtabhanticpidtorbolfosdot
losdilforpilramtirwintadbicdifrocwidbisdasmidlop
rilnardapmolsanlocnovsitnidtipsicropwitnatpanmin
ritpodmottamtolsavposnapnopsomfinfonbanmorworsip
ronnorbotwicsocwatdolmagpicdavbidbaltimtasmallig
sivtagpadsaldivdactansidfabtarmonranniswolmispal
lasdismaprabtobrollatlonnodnavfignomnibpagsopral
bilhaddocridmocpacravripfaltodtiltinhapmicfanpat
taclabmogsimsonpinlomrictapfirhasbosbatpochactid
havsaplindibhosdabbitbarracparloddosbortochilmac
tomdigfilfasmithobharmighinradmashalraglagfadtop
mophabnilnosmilfopfamdatnoldinhatnacrisfotribhoc
nimlarfitwalrapsarnalmoslandondanladdovrivbacpol
laptalpitnambonrostonfodponsovnocsorlavmatmipfip
""".replace('\n', '')

suf = """
zodnecbudwessevpersutletfulpensytdurwepserwylsun
rypsyxdyrnuphebpeglupdepdysputlughecryttyvsydnex
lunmeplutseppesdelsulpedtemledtulmetwenbynhexfeb
pyldulhetmevruttylwydtepbesdexsefwycburderneppur
rysrebdennutsubpetrulsynregtydsupsemwynrecmegnet
secmulnymtevwebsummutnyxrextebfushepbenmuswyxsym
selrucdecwexsyrwetdylmynmesdetbetbeltuxtugmyrpel
syptermebsetdutdegtexsurfeltudnuxruxrenwytnubmed
lytdusnebrumtynseglyxpunresredfunrevrefmectedrus
bexlebduxrynnumpyxrygryxfeptyrtustyclegnemfermer
tenlusnussyltecmexpubrymtucfyllepdebbermughuttun
bylsudpemdevlurdefbusbeprunmelpexdytbyttyplevmyl
wedducfurfexnulluclennerlexrupnedlecrydlydfenwel
nydhusrelrudneshesfetdesretdunlernyrsebhulryllud
remlysfynwerrycsugnysnyllyndyndemluxfedsedbecmun
lyrtesmudnytbyrsenwegfyrmurtelreptegpecnelnevfes
""".replace('\n', '')


with open(r'sigil.json') as f:
    all_data = json.load(f)


def replace_colors(s):
    s = s.replace("@BG", "#FFFFFF")
    s = s.replace("@FG", "#6184FF")
    return s


def json_to_svg(jso):
    name = jso["name"]
    attrs = " ".join([f"{k}=\"{replace_colors(v)}\"" for k, v in jso["attributes"].items()])
    return f"<{name} {attrs}></{name}>"


def syl_to_svg(syllable, filename):
    s = all_data[syllable]
    children = s["children"]
    svg_path = 'svg\\' + filename + '.svg'
    png_path = 'png\\' + filename + '.png'

    with open(svg_path, 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" width="150" height="150" version="1.1">')
        for c in children:
            f.write(json_to_svg(c))
        f.write("</svg>")

    cairosvg.svg2png(url=svg_path, write_to=png_path)


def render_all_syllables():
    os.makedirs('svg')
    os.makedirs('png')
    for i in range(0, 256):
        ii = i * 3
        h = f'{format(i, "02x")}'
        p = pre[ii] + pre[ii + 1] + pre[ii + 2]
        s = suf[ii] + suf[ii + 1] + suf[ii + 2]
        print(f'{h} {p} {s}')
        syl_to_svg(p, f"{h}.p.{p}")
        syl_to_svg(s, f"{h}.s.{s}")


render_all_syllables()
