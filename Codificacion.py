
def codificacion_calcula_subintervalo(Low, Hig, Lowj, Higj):
    Ln = Low + (Hig - Low)*Lowj
    Hn = Low + (Hig -Low)*Higj

    return [Ln, Hn]




