# thanks to https://gist.github.com/daFish/5990634
country_codes = {
    'ae': 'United Arab Emirates',
    'ag': 'Antigua and Barbuda',
    'ai': 'Anguilla',
    'al': 'Albania',
    'am': 'Armenia',
    'ao': 'Angola',
    'ar': 'Argentina',
    'at': 'Austria',
    'au': 'Australia',
    'az': 'Azerbaijan',
    'bb': 'Barbados',
    'be': 'Belgium',
    'bf': 'Burkina-Faso',
    'bg': 'Bulgaria',
    'bh': 'Bahrain',
    'bj': 'Benin',
    'bm': 'Bermuda',
    'bn': 'Brunei Darussalam',
    'bo': 'Bolivia',
    'br': 'Brazil',
    'bs': 'Bahamas',
    'bt': 'Bhutan',
    'bw': 'Botswana',
    'by': 'Belarus',
    'bz': 'Belize',
    'ca': 'Canada',
    'cg': 'Democratic Republic of the Congo',
    'ch': 'Switzerland',
    'cl': 'Chile',
    'cn': 'China',
    'co': 'Colombia',
    'cr': 'Costa Rica',
    'cv': 'Cape Verde',
    'cy': 'Cyprus',
    'cz': 'Czech Republic',
    'de': 'Germany',
    'dk': 'Denmark',
    'dm': 'Dominica',
    'do': 'Dominican Republic',
    'dz': 'Algeria',
    'ec': 'Ecuador',
    'ee': 'Estonia',
    'eg': 'Egypt',
    'es': 'Spain',
    'fi': 'Finland',
    'fj': 'Fiji',
    'fm': 'Federated States of Micronesia',
    'fr': 'France',
    'gb': 'Great Britain',
    'gd': 'Grenada',
    'gh': 'Ghana',
    'gm': 'Gambia',
    'gr': 'Greece',
    'gt': 'Guatemala',
    'gw': 'Guinea Bissau',
    'gy': 'Guyana',
    'hk': 'Hong Kong',
    'hn': 'Honduras',
    'hr': 'Croatia',
    'hu': 'Hungaria',
    'id': 'Indonesia',
    'ie': 'Ireland',
    'il': 'Israel',
    'in': 'India',
    'is': 'Iceland',
    'it': 'Italy',
    'jm': 'Jamaica',
    'jo': 'Jordan',
    'jp': 'Japan',
    'ke': 'Kenya',
    'kg': 'Krygyzstan',
    'kh': 'Cambodia',
    'kn': 'Saint Kitts and Nevis',
    'kr': 'South Korea',
    'kw': 'Kuwait',
    'ky': 'Cayman Islands',
    'kz': 'Kazakhstan',
    'la': 'Laos',
    'lb': 'Lebanon',
    'lc': 'Saint Lucia',
    'lk': 'Sri Lanka',
    'lr': 'Liberia',
    'lt': 'Lithuania',
    'lu': 'Luxembourg',
    'lv': 'Latvia',
    'md': 'Moldova',
    'mg': 'Madagascar',
    'mk': 'Macedonia',
    'ml': 'Mali',
    'mn': 'Mongolia',
    'mo': 'Macau',
    'mr': 'Mauritania',
    'ms': 'Montserrat',
    'mt': 'Malta',
    'mu': 'Mauritius',
    'mw': 'Malawi',
    'mx': 'Mexico',
    'my': 'Malaysia',
    'mz': 'Mozambique',
    'na': 'Namibia',
    'ne': 'Niger',
    'ng': 'Nigeria',
    'ni': 'Nicaragua',
    'nl': 'Netherlands',
    'np': 'Nepal',
    'no': 'Norway',
    'nz': 'New Zealand',
    'om': 'Oman',
    'pa': 'Panama',
    'pe': 'Peru',
    'pg': 'Papua New Guinea',
    'ph': 'Philippines',
    'pk': 'Pakistan',
    'pl': 'Poland',
    'pt': 'Portugal',
    'pw': 'Palau',
    'py': 'Paraguay',
    'qa': 'Qatar',
    'ro': 'Romania',
    'ru': 'Russia',
    'sa': 'Saudi Arabia',
    'sb': 'Soloman Islands',
    'sc': 'Seychelles',
    'se': 'Sweden',
    'sg': 'Singapore',
    'si': 'Slovenia',
    'sk': 'Slovakia',
    'sl': 'Sierra Leone',
    'sn': 'Senegal',
    'sr': 'Suriname',
    'st': 'Sao Tome e Principe',
    'sv': 'El Salvador',
    'sz': 'Swaziland',
    'tc': 'Turks and Caicos Islands',
    'td': 'Chad',
    'th': 'Thailand',
    'tj': 'Tajikistan',
    'tm': 'Turkmenistan',
    'tn': 'Tunisia',
    'tr': 'Turkey',
    'tt': 'Republic of Trinidad and Tobago',
    'tw': 'Taiwan',
    'tz': 'Tanzania',
    'ua': 'Ukraine',
    'ug': 'Uganda',
    'us': 'United States of America',
    'uy': 'Uruguay',
    'uz': 'Uzbekistan',
    'vc': 'Saint Vincent and the Grenadines',
    've': 'Venezuela',
    'vg': 'British Virgin Islands',
    'vn': 'Vietnam',
    'ye': 'Yemen',
    'za': 'South Africa',
    'zw': 'Zimbabwe'
}

code_choises = [key for key in country_codes.keys()]

VERBOSE = False