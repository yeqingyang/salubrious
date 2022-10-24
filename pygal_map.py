# import pygal_maps_world
import pygal
from pygal_maps_world import i18n
import csv

def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

def get_area_code(country_code):
    """根据国别码,返回区域名字"""
    if country_code in i18n.ASIA:
        return 'ASIA'
    if country_code in i18n.EUROPE:
        return 'EUROPE'
    if country_code in i18n.AFRICA:
        return 'AFRICA'
    if country_code in i18n.NORTH_AMERICA:
        return 'NORTH_AMERICA'
    if country_code in i18n.SOUTH_AMERICA:
        return 'SOUTH_AMERICA'
    if country_code in i18n.OCEANIA:
        return 'OCEANIA'
    if country_code in i18n.ANTARTICA:
        return 'ANTARTICA'
    # 如果没有找到指定的国家，就返回None
    return None

def p2f(x):
    return float(x.strip('%'))/100


wm = pygal.maps.world.World()
wm.title = '咖啡主要产地'
produces = {}
tasted = {}
with open('coffee_produce.csv') as f:
    f_csv = csv.reader(f)
    #获取headers
    headers = next(f_csv)

    for row in f_csv:
        country_code = get_country_code(row[1])
        #area = get_area_code(country_code)
        produces[country_code] = int(row[0])


with open('tasted.csv') as f:
    f_csv = csv.reader(f)
    #获取headers
    headers = next(f_csv)

    for row in f_csv:
        country_code = get_country_code(row[0])
        #area = get_area_code(country_code)
        # tasted.append(country_code)
        if (country_code in produces) :
            tasted[country_code] = produces[country_code]
            del produces[country_code]
print(produces)
wm.add('Top15', produces)
print(tasted)
wm.add('We tasted', tasted)

# wm.add('In 2022',{'ca':1, 'bz':1})
#
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#                          'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('coffee_produce.svg')
