# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import requests
from urllib import quote

serverurl = "http://serv.cusp.nyu.edu/files/sonyc/annotation_exp/8/"

def get_sounds(group):
    # url = "https://api.mongolab.com/api/1/databases/sonyc/collections/audio-data/538a43f9e4b0d7a3741b7fe2?apiKey=eFdR9h45nm-AuciNuN6d4G1Pd7NM38NS"
    jsonurl = serverurl + "json/" + "clips.json"
    #payload = {'group':group}
    #res = requests.get(url, params=payload)
    res = requests.get(jsonurl)
    # print url
    data = res.json()
    for s in data['sounds']:
        #s['clip_url'] = serverurl + "audio/" + s['filename']
		s['mp3_url'] = serverurl + "mp3/" + s['filename'] + ".mp3"
		s['wav_url'] = serverurl + "audio/" + s['filename'] + ".wav"
		s['visual_url'] = serverurl + "waveforms/" + s['filename'] + ".png"
        # print clip_url
        # print spec_url
    return data['sounds']
