








import plotly.express as px
import pandas as pd
from IPython.display import display
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np
import urllib.request as urlreq
from dash import Dash, html
import dash_bio as dashbio


# Pfad zur PHYLIP-Datei
fasta_file = "dataSources\TEM-1_Alignment_100_Homolgs.aln"

# Sequenzen aus der PHYLIP-Datei einlesen
sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

# DataFrame erstellen
df = pd.DataFrame.from_dict(sequences, orient="index")
df.reset_index(inplace=True)
display(df)

# show = px.df(indexed=True)
# fig = px.imshow(df, text_auto=True)
# fig.show()
app = Dash(__name__)

app.layout = html.Div([dashbio.AlignmentChart(id='alignment-viewer',data=df),])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

