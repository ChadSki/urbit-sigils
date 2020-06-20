toplefts = {
    'sog', 'fog', 'tog', 'tip', 'nap', 'fon', 'ron', 'wic',
    'mon', 'nis', 'mis', 'dis', 'map', 'rab', 'lon', 'lab',
    'mog', 'son', 'ris', 'don', 'lad', 'bon', 'ton', 'pon',
    'lav', 'mip'}

toprights = {
    'nec', 'bud', 'wyl', 'dys', 'hec', 'pyl', 'tyl', 'bes',
    'wyc', 'nep', 'rys', 'sub', 'rec', 'sec', 'fus', 'hep',
    'mus', 'ruc', 'dec', 'dyl', 'mes', 'tux', 'sur', 'tud',
    'nux', 'rux', 'nub', 'dus', 'mec', 'rus', 'fep', 'tus',
    'tyc', 'lus', 'nus', 'tec', 'pub', 'sud', 'lur', 'bus',
    'duc', 'luc', 'lec', 'rud', 'lud', 'lys', 'ryc', 'nys',
    'nyl', 'bec', 'mud'}

botlefts = {
    'wan', 'hid', 'dir', 'wac', 'sab', 'wis', 'lid', 'mir',
    'lac', 'sat', 'tab', 'tic', 'pid', 'los', 'tir', 'tad',
    'bic', 'dif', 'wid', 'bis', 'mid', 'dap', 'san', 'nid',
    'sic', 'nat', 'pan', 'pos', 'ban', 'bid', 'pad', 'dac',
    'tan', 'sid', 'fab', 'lat', 'nav', 'rid', 'pac', 'rav',
    'pat', 'tac', 'fir', 'bos', 'bat', 'hac', 'tid', 'hav',
    'sap', 'hos', 'dab', 'dos', 'mac', 'hab', 'nos', 'dat',
    'hat', 'nac', 'rap', 'mos', 'bac', 'lap', 'ros', 'mat'}

botrights = {
    'ryp', 'syx', 'byn', 'bur', 'pur', 'syn', 'wyn', 'nym',
    'sum', 'nyx', 'wyx', 'sym', 'myn', 'syp', 'rum', 'tyn',
    'lyx', 'dux', 'ryn', 'pyx', 'ryg', 'ryx', 'syl', 'rym',
    'fyl', 'byl', 'typ', 'myl', 'fur', 'fyn', 'lyn', 'dyn',
    'lux'}


full_circles = set()
almost_circles = set()

with open('sabten-planets.txt') as f:
    for line in f:
        name = line[:-1]
        topleft = line[1:4]
        topright = line[4:7]
        botleft = line[8:11]
        botright = line[11:14]

        score = \
            (topleft in toplefts) + \
            (topright in toprights) + \
            (botleft in botlefts) + \
            (botright in botrights)

        if score == 4:
            full_circles.add(name)
        elif score == 3:
            almost_circles.add(name)

for name in almost_circles:
    print(name)
