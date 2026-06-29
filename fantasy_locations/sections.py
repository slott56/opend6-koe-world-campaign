from pathlib import Path

sections = """
    delmara
    kiselton
    inachon
    izmerlia
    typon
    gadata
    rhakotis
    nomad_camp
    morcades_hut
    halwyndale
    viking_village
    thalas
    utsmuul
    sala_colonia
    settlement_design
    settlement_design_sheet
""".splitlines()
for s in sections:
    path = (Path("Settlements") / s.strip()).with_suffix(".rst")
    path.write_text(s.strip( ))
