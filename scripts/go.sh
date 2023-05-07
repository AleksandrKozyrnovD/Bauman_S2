#!/bin/bash

sh build_apps.sh
sh update_data.sh
python3 make_preproc.py
sh make_postproc.sh