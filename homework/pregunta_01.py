"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # <-- línea nueva
import matplotlib.pyplot as plt


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """


    plt.figure()

    colors ={
        "Television":"dimgray",
        "Radio":"lightgreen",
        "Internet":"tab:blue",
        "Newspaper":"gray"
    }

    zorder = {
        "Television": 1,
        "Radio": 1,
        "Internet": 2,
        "Newspaper": 1
    }

    linewidths= {
        "Television": 2,
        "Radio": 2,
        "Internet": 3,
        "Newspaper": 2,
    }


    df= pd.read_csv("files/input/news.csv", index_col=0)
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col)
    
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        fisrt_year = df.index[0]
        plt.scatter(
            x=fisrt_year,
            y=df[col][fisrt_year],
            color=colors[col],
            zorder=zorder[col],
        )
        plt.text(
            fisrt_year - 0.2,
            df[col][fisrt_year],
            col +  " " + str(df[col][fisrt_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )


        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )

        plt.text(
            fisrt_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha="center",
    )
    
    plt.tight_layout()
    Path("files/plots").mkdir(parents=True, exist_ok=True)
    plt.savefig("files/plots/news.png")
    
if __name__ == "__main__":
    pregunta_01()
