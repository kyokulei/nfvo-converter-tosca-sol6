#!/usr/bin/env bash

echo Creating build file...
if [ -d "dist" ]; then
  rm -r dist
fi
pyinstaller -F -p python/tailf_etsi_rel2_nfvo_tosca tosca.py
