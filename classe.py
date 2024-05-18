import googlemaps

class CordinateGetter:
    __base_url = 'https://do.diba.cat/data/ds/municipis/detall/'
    __gmaps = googlemaps.Client(key='AIzaSyDrS4cmFMnWHhamFFudv6VlBJWcmjLvGCk')
    # __gmaps = googlemaps.Client(key=Configuration.googlemaps_key)
    def get_coordinates(ine_code):
        url = f"{CordinateGetter.__base_url}{ine_code}?embed=True"
        import requests
        response = requests.get(url)
        if response.status_code == 200:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            dds = soup.find_all('dd')
            result = {}
            for dd in dds:
                title = dd.find_previous('dt').get_text(strip=True) if dd.find_previous('dt') else 'No Title'
                content = dd.get_text(strip=True)
                if len(content) != 0:
                    result[title] = content
            # return result
            inp = []
            if 'Nom del municipi' in result.keys():
                inp.append(f'Catalunya, Ajuntament {result["Nom del municipi"]}')
            if 'Codi postal' in result.keys():
                inp.append(f'{result["Codi postal"]}')
            if 'Nom de la comarca' in result.keys():
                inp.append(f'{result["Codi postal"]}')

            # o = CordinateGetter.__gmaps.geocode(f'')[0]['geometry']['location']
            if len(inp) == 0:
                raise Exception()
            o = CordinateGetter.__gmaps.geocode(', '.join(inp))
            try:
                o = o[0]['geometry']['location']
                return float(o['lat']), float(o['lng'])
            except:
                return result

        else:
            return None