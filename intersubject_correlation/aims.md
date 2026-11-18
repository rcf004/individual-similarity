# ISC individal similarity aims

Extend work from SCAN ISC paper for dissertation

## hypothesis 3a
initial work to identify regions of interest before h3b, using pca on LOO maps
STATUS: SCRAPPED
    find other way to motivate specific regions, a-priori theoretical motivation?
        theory of mind regions, select parcels that overlap with meta analysis? neurosynth? schurz? is it public?
    data driven motivation
        find regions most associated with age differences? - could use age diff map? double dipping?
    
## hypothesis 3b
pairwise ISC - (using particular regions?)
for now could select all 456? 256? regions and run pairwise ISC
need to build pairwise ISC code
    instead parallelize by region - for all subjects load in activity only for region N
    correlate subject x subject for region N
    save output as csv -> regionN.csv
    repeat for all regions
    need to make sure input is viable -> use same thing as for neural/beh sim already known good

once built - then need to calculate similarity across regions - dimension reduction - build MDS mapping/or something
