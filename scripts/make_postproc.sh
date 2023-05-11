#!/bin/bash

bash ./make_gnuplot_config.sh
for config in ./gnuplotconfigs/*.gpi; do
    gnuplot $config
    # gnuplot config

done
