import sys
sys.stdout.reconfigure(encoding='ascii')

from parse_args import parse_args
from parse_smf import parse_smf
from transform_vrc import world_to_vrc
from projection import project_vertices
from generate_ps import write_postscript


def main():
    cfg = parse_args()
    vertices_world, edges = parse_smf(cfg["smf_file"])
    vertices_vrc = world_to_vrc(vertices_world, cfg["VRP"], cfg["VPN"], cfg["VUP"])
    vertices_2d = project_vertices(vertices_vrc, cfg["PRPx"], cfg["PRPy"], cfg["PRPz"], cfg["parallel"])
    write_postscript(edges, vertices_2d, cfg, sys.stdout)

if __name__ == "__main__":
    main()
