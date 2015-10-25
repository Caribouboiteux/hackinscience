from __future__ import division
from __future__ import absolute_import, print_function, unicode_literals
import six
station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}
for k, v in six.iteritems(station):
    print(k, v)
