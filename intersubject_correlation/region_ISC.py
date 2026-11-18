import os
import argparse

from pathlib import Path
import numpy as np
from scipy.spatial.distance import squareform

SUBJROOT = Path('/N/project/NimbleMRI/SNACK_Kretzel/derivatives/xcp_d_GSR_confounds/xcp_d')
PROJECTROOT = Path(__file__).resolve().parents[1]
REGION_LIST = np.loadtxt('/N/project/NimbleMRI/SNACK_Kretzel/code/level2/eTS/custom_parc/schaefer200_tian1_labels.txt', dtype=str)

def load_region(subjectlist, region_idx, verbose):

    zoobold = []
    shopbold = []

    for subject in subjectlist:
        
        zoo = SUBJROOT / subject / f'{subject}_pettingzoo_interpolated_ts_custom_parc.npy'
        shop = SUBJROOT / subject / f'{subject}_souvenirshop_interpolated_ts_custom_parc.npy'


        if verbose:
            print(f'pulling data for subject: {subject}')

        for data, container, arrlen in zip(
            (zoo, shop),
            (zoobold, shopbold),
            (233, 249)):
            
            fullarr = np.load(data)
            container.append(fullarr[:, region_idx][:arrlen])

            #nancheck
            if np.isnan(fullarr).any():
                print(subject)

    zoostack = np.column_stack(zoobold)
    shopstack = np.column_stack(shopbold)
    if verbose:
        print('Finished BOLD pull')

    return zoostack, shopstack


def main(region_idx, verbose):

    subjectlist = np.loadtxt(PROJECTROOT / 'sublist_goodsubs.txt', dtype=str)

    zoostack, shopstack = load_region(subjectlist, region_idx, verbose)
    fullstack = np.concatenate((zoostack, shopstack), axis=0)  

    region_label = REGION_LIST[region_idx]

    for stack, label in zip(
        (zoostack, shopstack, fullstack),
        ('zoo', 'shop', 'full')):

        region_isc = squareform(np.corrcoef(stack.T), checks=False)

        OUTPATH = PROJECTROOT / 'intersubject_correlation' / 'region_isc' / f'{label}_{region_label}.npy'
        os.makedirs(OUTPATH.parent, exist_ok = True)
        np.save(OUTPATH, region_isc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("region_idx", type=int)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    main(args.region_idx, args.verbose)
