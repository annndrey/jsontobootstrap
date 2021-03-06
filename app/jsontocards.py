#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from glob import glob


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


html_template = """<html>
  <head>
    <title>Results</title>
    <link href="http://netdna.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      {rows}
    </div>
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
"""

row_template = """<div class="row">
{columns}
</div>
"""

card_template = """<div class="col-sm-4">
    <div class="card">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">#{id} {LinkMainText}</h5>
          <h6 class="card-subtitle mb-2 text-muted">Keywords: {PrcoessingKeyword}</h6>
          <p class="card-text">{LinkSubText}</p>
          <a href="{LinkMainURLReal}" class="card-link">{LinkMainURLReal}</a>
          <a href="#" class="card-link">From site: {PrcoessingSite}</a>
        </div>
      </div>
    </div>
</div>
"""


for f in glob("*.json"):
    cards = []
    rows = []
    out_filename = os.path.splitext(f)[0] + '.html'

    with open(f) as j:
        data = json.load(j)
        cards_in_a_row = 0
        for card in data:
            bootstrap_card = card_template.format(**card)
            cards.append(bootstrap_card)
            
            
    splitted_cards = list(chunks(cards, 3))
    for row in splitted_cards:
            rows.append(row_template.format(columns="\n".join(row)))

    bootstrap_rows = "\n".join(rows)
    html_out = html_template.format(rows=bootstrap_rows)
    with open(out_filename, 'w') as outfile:
        outfile.write(html_out)
        outfile.close()
