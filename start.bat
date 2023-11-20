@echo off

cd src

py -V && (
    py -m admon_parqueadero
) || (
    python -m admon_parqueadero
)
