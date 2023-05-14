#!/bin/bash

bash ./make_gnuplot_config.sh
for config in ./gnuplotconfigs/*.gpi; do
    #А как по другому, чтобы shellcheck не ругался?
    gnuplot $config

done
