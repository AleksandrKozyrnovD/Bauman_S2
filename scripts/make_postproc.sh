#!/bin/bash

bash ./make_gnuplot_config.sh
for config in "./gnuplotconfigs/*"; do
    # echo $config
    gnuplot $config
done