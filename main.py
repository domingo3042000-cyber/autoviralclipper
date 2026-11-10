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
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip install --upgrade pip
          pip install "Cython<3.0.0" buildozer

      - name: Compilar APK con Buildozer
        run: |
          buildozer -v android debug

      - name: Subir APK Generado como Artefacto
        uses: actions/upload-artifact@v4
        with:
          name: AutoViralClipper-APK
          path: bin/*.apk
