name: Compilar APK de Android

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Descargar Código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar Dependencias del Sistema
        run: |
          sudo dpkg --add-architecture i386
          sudo apt-get update
          sudo apt-get install -y build-essential ccache git libncurses5:i386 libstdc++6:i386 libz1:i386 openjdk-17-jdk unzip zlib1g-dev python3-pip autoconf libtool pkg-config cmake libffi-dev libssl-dev
          pip install --upgrade pip
          pip install "Cython<3.0.0" buildozer

      - name: Compilar APK con Buildozer
        run: |
          buildozer -v android debug

      - name: Subir APK Generado como Artefacto
        uses: actions/upload-artifact@v4
        with:
          name: app-debug
          path: bin/*.apk
